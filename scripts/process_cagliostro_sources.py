#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Cagliostro sources from Downloads folder.
Converts PDFs to markdown, extracts key entities, updates database.
"""

import json
import re
from pathlib import Path
from datetime import datetime
import pdfplumber

def extract_pdf_text(pdf_path):
    """Extract text from PDF."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    full_text += f"\n\n[Page {page_num + 1}]\n{text}"
        return full_text
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")
        return ""

def detect_sections(text):
    """Detect chapters/sections."""
    patterns = [
        (r'^CHAPTER\s+([IVX]+|[\d]+)', 'Chapter'),
        (r'^§\s*(.+?)$', 'Section'),
        (r'^Part\s+([IVX]+|[\d]+)', 'Part'),
        (r'^Introduction', 'Introduction'),
        (r'^Preface', 'Preface'),
        (r'^Conclusion', 'Conclusion'),
    ]

    sections = []
    lines = text.split('\n')
    current_section = None
    section_text = []

    for i, line in enumerate(lines):
        for pattern, section_type in patterns:
            if re.match(pattern, line, re.IGNORECASE):
                if current_section:
                    sections.append({
                        'title': current_section,
                        'text': '\n'.join(section_text)
                    })

                current_section = line.strip()[:80]
                section_text = [line]
                break
        else:
            if current_section:
                section_text.append(line)

    if current_section:
        sections.append({
            'title': current_section,
            'text': '\n'.join(section_text)
        })

    return sections if sections else [{'title': 'Full Text', 'text': text}]

def load_database():
    """Load main database."""
    db_path = Path("data/prototype_data.json")
    with open(db_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def find_cagliostro_mentions(text):
    """Find mentions of Cagliostro-related figures and concepts."""
    db = load_database()

    figures = {fig["name"] for fig in db.get("figures", [])}
    concepts = {concept["name"] for concept in db.get("concepts", [])}

    mentioned_figures = []
    mentioned_concepts = []

    for figure in figures:
        if re.search(r'\b' + re.escape(figure) + r'\b', text, re.IGNORECASE):
            mentioned_figures.append(figure)

    for concept in concepts:
        if re.search(r'\b' + re.escape(concept) + r'\b', text, re.IGNORECASE):
            mentioned_concepts.append(concept)

    return list(set(mentioned_figures)), list(set(mentioned_concepts))

def process_cagliostro_pdfs():
    """Process Cagliostro PDFs from Downloads."""
    print("=" * 70)
    print("CAGLIOSTRO SOURCES PROCESSING")
    print("=" * 70)
    print()

    downloads_dir = Path.home() / "Downloads"
    output_dir = Path("data/markdown_sources/Cagliostro")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Find Cagliostro PDFs
    cagliostro_pdfs = sorted(downloads_dir.glob("*Cagliostro*.pdf"))
    print(f"Found {len(cagliostro_pdfs)} Cagliostro PDFs")
    print()

    total_files = 0

    for pdf_path in cagliostro_pdfs:
        print(f"Processing: {pdf_path.name}")

        # Extract text
        full_text = extract_pdf_text(str(pdf_path))
        if not full_text:
            print("  No text extracted")
            continue

        # Detect sections
        sections = detect_sections(full_text)

        # Create source directory
        source_dir = output_dir / pdf_path.stem[:60]
        source_dir.mkdir(parents=True, exist_ok=True)

        # Extract mentions
        figures, concepts = find_cagliostro_mentions(full_text)

        # Write markdown files
        for i, section in enumerate(sections, 1):
            filename = f"{i:02d}_{section['title'][:50].lower().replace(' ', '_')}.md"
            filepath = source_dir / filename

            markdown = f"""---
source: {pdf_path.stem}
source_type: Cagliostro
section: {section['title']}
section_number: {i}
date_processed: {datetime.now().isoformat()}
figures_mentioned: {', '.join(figures) if figures else 'None'}
concepts_mentioned: {', '.join(concepts) if concepts else 'None'}
---

# {pdf_path.stem}

## Section: {section['title']}

{section['text']}

---

*Figures mentioned: {', '.join(figures) if figures else 'None'}*
*Concepts mentioned: {', '.join(concepts) if concepts else 'None'}*
"""

            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(markdown)
                total_files += 1
            except Exception as e:
                print(f"  Error writing {filename}: {e}")

        print(f"  [CREATED {len(sections)} sections]")
        print(f"  Figures found: {', '.join(figures) if figures else 'None'}")
        print(f"  Concepts found: {', '.join(concepts) if concepts else 'None'}")
        print()

    print("=" * 70)
    print(f"Cagliostro markdown files created: {total_files}")
    print(f"Output directory: {output_dir}")
    print()
    print("Next: Extract key entities and update database")

if __name__ == "__main__":
    process_cagliostro_pdfs()
