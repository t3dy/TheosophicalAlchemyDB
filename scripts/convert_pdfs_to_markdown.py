#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Systematic PDF to Markdown conversion with chapter chunking.
Converts PDFs to markdown files organized by chapter/section.
Includes metadata (source, page range, figure/concept mentions).
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime
import pdfplumber

# Load our database to extract figure and concept names
def load_database():
    """Load prototype_data.json to get figure and concept names."""
    db_path = Path("data/prototype_data.json")
    if db_path.exists():
        with open(db_path, 'r', encoding='utf-8') as f:
            db = json.load(f)
        return db
    return {"figures": [], "concepts": []}

# Define PDF source directories
PDF_DIRS = [
    ("Rosicrucian", "E:\\pdf\\Rosicrucian"),
    ("Alchemy", "E:\\pdf\\alchemy"),
    ("Western Esotericism", "E:\\pdf\\western esotericism religious studies"),
    ("Emblem Studies", "E:\\pdf\\emblem studies"),
]

# Output directory
OUTPUT_DIR = Path("data/markdown_sources")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_figures_and_concepts(db):
    """Extract figure names and concept names from database."""
    figures = {fig["name"] for fig in db.get("figures", [])}
    concepts = {concept["name"] for concept in db.get("concepts", [])}
    return figures, concepts

def detect_sections(text):
    """Detect chapter/section breaks in text.
    Returns list of tuples: (section_title, text_content, page_start, page_end)
    """
    # Common patterns for chapter/section headers
    patterns = [
        (r'^CHAPTER\s+([IVX]+|[\d]+)[\s:](.+?)$', 'Chapter'),
        (r'^§\s*(.+?)$', 'Section'),
        (r'^Introduction', 'Introduction'),
        (r'^Preface', 'Preface'),
        (r'^Conclusion', 'Conclusion'),
    ]

    sections = []
    lines = text.split('\n')
    current_section = None
    section_start = 0
    section_text = []

    for i, line in enumerate(lines):
        for pattern, section_type in patterns:
            if re.match(pattern, line, re.IGNORECASE):
                # Save previous section
                if current_section:
                    sections.append({
                        'title': current_section,
                        'text': '\n'.join(section_text),
                        'start_line': section_start
                    })

                # Start new section
                current_section = line.strip()[:80]  # Truncate long titles
                section_start = i
                section_text = [line]
                break
        else:
            if current_section:
                section_text.append(line)

    # Save last section
    if current_section:
        sections.append({
            'title': current_section,
            'text': '\n'.join(section_text),
            'start_line': section_start
        })

    return sections if sections else [{'title': 'Full Text', 'text': text, 'start_line': 0}]

def extract_pdf_metadata(pdf_path):
    """Extract metadata from PDF."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            metadata = pdf.metadata or {}
            return {
                'title': metadata.get('Title', Path(pdf_path).stem),
                'author': metadata.get('Author', 'Unknown'),
                'pages': len(pdf.pages),
                'created': metadata.get('CreationDate', 'Unknown'),
            }
    except Exception as e:
        return {
            'title': Path(pdf_path).stem,
            'author': 'Unknown',
            'pages': 0,
            'created': 'Unknown',
        }

def extract_pdf_text(pdf_path):
    """Extract full text from PDF using pdfplumber."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    full_text += f"\n\n[Page {page_num + 1}]\n{text}"
        return full_text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ""

def find_mentions(text, figures, concepts):
    """Find mentions of figures and concepts in text."""
    mentioned_figures = set()
    mentioned_concepts = set()

    for figure in figures:
        if re.search(r'\b' + re.escape(figure) + r'\b', text, re.IGNORECASE):
            mentioned_figures.add(figure)

    for concept in concepts:
        if re.search(r'\b' + re.escape(concept) + r'\b', text, re.IGNORECASE):
            mentioned_concepts.add(concept)

    return list(mentioned_figures), list(mentioned_concepts)

def sanitize_filename(filename):
    """Convert title to safe filename."""
    return re.sub(r'[^a-z0-9_-]', '_', filename.lower())[:60]

def convert_pdf_to_markdown(pdf_path, source_category, db, figures, concepts):
    """Convert single PDF to markdown chapters."""
    print(f"Processing: {Path(pdf_path).name}")

    # Extract metadata and text
    metadata = extract_pdf_metadata(pdf_path)
    full_text = extract_pdf_text(pdf_path)

    if not full_text:
        print("  [NO TEXT EXTRACTED]")
        return 0

    # Detect sections
    sections = detect_sections(full_text)

    # Find mentions
    mentioned_figures, mentioned_concepts = find_mentions(full_text, figures, concepts)

    # Create source directory
    source_dir = OUTPUT_DIR / source_category.replace(" ", "_")
    pdf_dir = source_dir / sanitize_filename(metadata['title'])
    pdf_dir.mkdir(parents=True, exist_ok=True)

    # Write markdown files for each section
    section_count = 0
    for i, section in enumerate(sections, 1):
        filename = f"{i:02d}_{sanitize_filename(section['title'])}.md"
        filepath = pdf_dir / filename

        # Create markdown frontmatter
        markdown = f"""---
source: {metadata['title']}
source_category: {source_category}
author: {metadata['author']}
total_pages: {metadata['pages']}
section: {section['title']}
section_number: {i}
date_processed: {datetime.now().isoformat()}
figures_mentioned: {', '.join(mentioned_figures) if mentioned_figures else 'None'}
concepts_mentioned: {', '.join(mentioned_concepts) if mentioned_concepts else 'None'}
---

# {metadata['title']}

## Section: {section['title']}

{section['text']}

---

*Extracted from: {metadata['title']} ({metadata['pages']} pages)*
*Figures mentioned: {', '.join(mentioned_figures) if mentioned_figures else 'None'}*
*Concepts mentioned: {', '.join(mentioned_concepts) if mentioned_concepts else 'None'}*
"""

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)
            section_count += 1
        except Exception as e:
            print(f"  Error writing {filename}: {e}")

    print(f"  [CREATED {section_count} sections]")
    return section_count

def main():
    print("=" * 70)
    print("PDF TO MARKDOWN CONVERSION")
    print("=" * 70)
    print()

    # Load database
    db = load_database()
    figures, concepts = extract_figures_and_concepts(db)

    print(f"Database loaded: {len(figures)} figures, {len(concepts)} concepts")
    print()

    total_pdfs = 0
    total_sections = 0

    # Process each directory
    for source_category, pdf_dir in PDF_DIRS:
        if not os.path.exists(pdf_dir):
            print(f"Skipping {source_category} (directory not found)")
            continue

        print(f"\n{source_category}:")
        print("-" * 70)

        pdf_files = sorted(Path(pdf_dir).glob("*.pdf"))
        print(f"Found {len(pdf_files)} PDFs")

        for pdf_path in pdf_files:
            sections = convert_pdf_to_markdown(
                str(pdf_path), source_category, db, figures, concepts
            )
            total_sections += sections
            if sections > 0:
                total_pdfs += 1

    print()
    print("=" * 70)
    print("CONVERSION COMPLETE")
    print("=" * 70)
    print(f"PDFs processed: {total_pdfs}")
    print(f"Markdown sections created: {total_sections}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    print("Next steps:")
    print("  1. Review markdown files in data/markdown_sources/")
    print("  2. Run ingestion script to extract relevant content")
    print("  3. Add source citations to figure/concept entries")

if __name__ == "__main__":
    main()
