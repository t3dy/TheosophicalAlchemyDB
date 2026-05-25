#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aggregate all markdown citations from all directories.
Creates master citation index linking figures and concepts to sources.
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

def aggregate_all_citations():
    """Scan all markdown directories and create master citation index."""
    print("=" * 70)
    print("MASTER CITATION AGGREGATION")
    print("=" * 70)
    print()

    db = load_database()
    figures, concepts = extract_figures_and_concepts(db)

    sources_dir = Path("data/markdown_sources")
    if not sources_dir.exists():
        print("No markdown_sources directory found")
        return

    # Track all mentions
    figure_citations = defaultdict(list)
    concept_citations = defaultdict(list)
    category_stats = {}

    total_files = 0
    total_mentions = 0

    # Walk through markdown files
    for markdown_file in sorted(sources_dir.rglob("*.md")):
        total_files += 1
        relative_path = markdown_file.relative_to(sources_dir)
        category = relative_path.parts[0] if relative_path.parts else "Unknown"

        if category not in category_stats:
            category_stats[category] = {'files': 0, 'mentions': 0}
        category_stats[category]['files'] += 1

        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {markdown_file}: {e}")
            continue

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
                    'fig_id': fig_id,
                    'category': category
                })
                total_mentions += 1
                category_stats[category]['mentions'] += 1

        # Find concept mentions
        for concept_name, concept_id in concepts.items():
            if re.search(r'\b' + re.escape(concept_name) + r'\b', text, re.IGNORECASE):
                concept_citations[concept_name].append({
                    'source': source_title,
                    'section': section_title,
                    'file': str(relative_path),
                    'concept_id': concept_id,
                    'category': category
                })
                total_mentions += 1
                category_stats[category]['mentions'] += 1

    # Report findings
    print(f"Scanned {total_files} total markdown files")
    print(f"Found {total_mentions} total mentions across all categories")
    print()

    print("Citations by Category:")
    print("-" * 70)
    for category in sorted(category_stats.keys()):
        stats = category_stats[category]
        print(f"{category}: {stats['files']} files, {stats['mentions']} mentions")

    print()
    print("Top Figures (by mention count):")
    print("-" * 70)
    sorted_figures = sorted(figure_citations.items(), key=lambda x: len(x[1]), reverse=True)
    for i, (figure, citations) in enumerate(sorted_figures[:20], 1):
        print(f"{i:2d}. {figure}: {len(citations)} mentions")

    print()
    print("Top Concepts (by mention count):")
    print("-" * 70)
    sorted_concepts = sorted(concept_citations.items(), key=lambda x: len(x[1]), reverse=True)
    for i, (concept, citations) in enumerate(sorted_concepts[:20], 1):
        print(f"{i:2d}. {concept}: {len(citations)} mentions")

    # Save master citation index
    citation_index = {
        'metadata': {
            'total_files': total_files,
            'total_mentions': total_mentions,
            'categories': category_stats,
            'generated_at': str(Path('data/markdown_sources').stat().st_mtime if Path('data/markdown_sources').exists() else 'unknown')
        },
        'figures': dict(figure_citations),
        'concepts': dict(concept_citations)
    }

    with open("data/master_citation_index.json", 'w', encoding='utf-8') as f:
        json.dump(citation_index, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print(f"Master citation index saved to data/master_citation_index.json")
    print()
    print("Summary Statistics:")
    print(f"  - Total figures cited: {len(figure_citations)}")
    print(f"  - Total concepts cited: {len(concept_citations)}")
    print(f"  - Total mentions: {total_mentions}")
    print(f"  - Average mentions per figure: {total_mentions / max(len(figure_citations), 1):.1f}")
    print(f"  - Average mentions per concept: {total_mentions / max(len(concept_citations), 1):.1f}")

if __name__ == "__main__":
    aggregate_all_citations()
