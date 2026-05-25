#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ingest markdown sources: extract figure/concept mentions with source attribution.
Cross-references back to main database with page citations.
"""

import json
import re
from pathlib import Path
from collections import defaultdict

def load_database():
    """Load main database."""
    db_path = Path("data/prototype_data.json")
    with open(db_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_figures_and_concepts(db):
    """Extract figure names and concept names with IDs."""
    figures = {fig["name"]: fig.get("id", "") for fig in db.get("figures", [])}
    concepts = {concept["name"]: concept.get("id", "") for concept in db.get("concepts", [])}
    return figures, concepts

def ingest_markdown_sources():
    """Scan markdown_sources directory and extract citations."""
    print("=" * 70)
    print("MARKDOWN SOURCE INGESTION")
    print("=" * 70)
    print()

    db = load_database()
    figures, concepts = extract_figures_and_concepts(db)

    sources_dir = Path("data/markdown_sources")
    if not sources_dir.exists():
        print("No markdown_sources directory found. Run convert_pdfs_to_markdown.py first.")
        return

    # Track all mentions
    figure_citations = defaultdict(list)
    concept_citations = defaultdict(list)

    total_files = 0
    total_mentions = 0

    # Walk through markdown files
    for markdown_file in sorted(sources_dir.rglob("*.md")):
        total_files += 1
        relative_path = markdown_file.relative_to(sources_dir)

        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        frontmatter = {}
        if frontmatter_match:
            for line in frontmatter_match.group(1).split('\n'):
                if ':' in line:
                    key, val = line.split(':', 1)
                    frontmatter[key.strip()] = val.strip()

        source_title = frontmatter.get('source', str(relative_path))
        section_title = frontmatter.get('section', 'Unknown')

        # Extract text content
        text_match = re.search(r'^---\n.*?\n---\n(.*?)---', content, re.DOTALL)
        text = text_match.group(1) if text_match else content

        # Find figure mentions
        for figure_name, fig_id in figures.items():
            if re.search(r'\b' + re.escape(figure_name) + r'\b', text, re.IGNORECASE):
                figure_citations[figure_name].append({
                    'source': source_title,
                    'section': section_title,
                    'file': str(relative_path),
                    'fig_id': fig_id
                })
                total_mentions += 1

        # Find concept mentions
        for concept_name, concept_id in concepts.items():
            if re.search(r'\b' + re.escape(concept_name) + r'\b', text, re.IGNORECASE):
                concept_citations[concept_name].append({
                    'source': source_title,
                    'section': section_title,
                    'file': str(relative_path),
                    'concept_id': concept_id
                })
                total_mentions += 1

    # Report findings
    print(f"Scanned {total_files} markdown files")
    print(f"Found {total_mentions} total mentions")
    print()
    print("Figure citations:")
    print("-" * 70)
    for figure, citations in sorted(figure_citations.items()):
        print(f"{figure}: {len(citations)} mentions")
        for citation in citations[:2]:  # Show first 2
            print(f"  - {citation['source']} / {citation['section'][:40]}")

    print()
    print("Concept citations:")
    print("-" * 70)
    for concept, citations in sorted(concept_citations.items()):
        print(f"{concept}: {len(citations)} mentions")
        for citation in citations[:2]:  # Show first 2
            print(f"  - {citation['source']} / {citation['section'][:40]}")

    # Save citation index
    citation_index = {
        'figures': dict(figure_citations),
        'concepts': dict(concept_citations),
        'timestamp': str(Path('data/markdown_sources').stat().st_mtime if Path('data/markdown_sources').exists() else 'unknown'),
        'total_mentions': total_mentions
    }

    with open("data/markdown_citations.json", 'w', encoding='utf-8') as f:
        json.dump(citation_index, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print(f"Citation index saved to data/markdown_citations.json")
    print()
    print("Next steps:")
    print("  1. Review citations to verify relevance")
    print("  2. Add source fields to figure/concept entries")
    print("  3. Create scholarly_sources_ingested field in entries")

if __name__ == "__main__":
    ingest_markdown_sources()
