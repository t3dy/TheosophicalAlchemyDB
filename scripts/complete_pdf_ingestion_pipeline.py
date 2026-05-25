#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete PDF ingestion pipeline: Convert, aggregate, and integrate.
Run this after all PDF conversions are complete.
"""

import json
import re
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def load_database():
    """Load main database."""
    db_path = Path("data/prototype_data.json")
    with open(db_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_figures_and_concepts(db):
    """Extract figure and concept names."""
    figures = {fig["name"]: fig.get("id", "") for fig in db.get("figures", [])}
    concepts = {concept["name"]: concept.get("id", "") for concept in db.get("concepts", [])}
    return figures, concepts

def aggregate_citations():
    """Aggregate all markdown citations."""
    print("\n[STEP 2] AGGREGATING CITATIONS")
    print("=" * 70)

    db = load_database()
    figures, concepts = extract_figures_and_concepts(db)

    sources_dir = Path("data/markdown_sources")
    if not sources_dir.exists():
        print("No markdown_sources directory found")
        return {}, {}

    figure_citations = defaultdict(list)
    concept_citations = defaultdict(list)
    category_stats = {}

    total_files = 0
    total_mentions = 0

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
            continue

        frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        frontmatter = {}
        if frontmatter_match:
            for line in frontmatter_match.group(1).split('\n'):
                if ':' in line:
                    key, val = line.split(':', 1)
                    frontmatter[key.strip()] = val.strip()

        source_title = frontmatter.get('source', str(relative_path))
        section_title = frontmatter.get('section', 'Unknown')

        text_match = re.search(r'^---\n.*?\n---\n(.*?)---', content, re.DOTALL)
        text = text_match.group(1) if text_match else content

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

    print(f"Scanned {total_files} markdown files")
    print(f"Found {total_mentions} total mentions")
    print(f"Categories: {', '.join(sorted(category_stats.keys()))}")

    # Save master citation index
    citation_index = {
        'metadata': {
            'total_files': total_files,
            'total_mentions': total_mentions,
            'categories': category_stats,
            'generated_at': datetime.now().isoformat()
        },
        'figures': dict(figure_citations),
        'concepts': dict(concept_citations)
    }

    with open("data/master_citation_index.json", 'w', encoding='utf-8') as f:
        json.dump(citation_index, f, indent=2, ensure_ascii=False)

    print(f"Master citation index saved")
    return dict(figure_citations), dict(concept_citations)

def update_database_with_sources(figure_citations, concept_citations):
    """Update database with source citations."""
    print("\n[STEP 3] UPDATING DATABASE")
    print("=" * 70)

    db_path = Path("data/prototype_data.json")
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    figures_updated = 0
    concepts_updated = 0

    for figure in db.get('figures', []):
        figure_name = figure.get('name')
        if figure_name in figure_citations:
            citations_list = figure_citations[figure_name]
            sources = defaultdict(list)
            for citation in citations_list:
                category = citation.get('category', 'Unknown')
                sources[category].append(citation.get('source', 'Unknown'))

            unique_sources = set()
            for source_list in sources.values():
                unique_sources.update(source_list[:2])

            if unique_sources:
                figure['markdown_sources_found'] = list(unique_sources)[:10]
                figure['source_citations_count'] = len(citations_list)
                figures_updated += 1

    for concept in db.get('concepts', []):
        concept_name = concept.get('name')
        if concept_name in concept_citations:
            citations_list = concept_citations[concept_name]
            sources = defaultdict(list)
            for citation in citations_list:
                category = citation.get('category', 'Unknown')
                sources[category].append(citation.get('source', 'Unknown'))

            unique_sources = set()
            for source_list in sources.values():
                unique_sources.update(source_list[:2])

            if unique_sources:
                concept['markdown_sources_found'] = list(unique_sources)[:10]
                concept['source_citations_count'] = len(citations_list)
                concepts_updated += 1

    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Updated {figures_updated} figures with sources")
    print(f"Updated {concepts_updated} concepts with sources")

def print_summary():
    """Print final summary."""
    print("\n[STEP 4] FINAL SUMMARY")
    print("=" * 70)

    # Load master citation index
    with open("data/master_citation_index.json", 'r', encoding='utf-8') as f:
        citations = json.load(f)

    metadata = citations['metadata']
    figures = citations['figures']
    concepts = citations['concepts']

    print(f"Total markdown files: {metadata['total_files']}")
    print(f"Total mentions: {metadata['total_mentions']}")
    print(f"Unique figures cited: {len(figures)}")
    print(f"Unique concepts cited: {len(concepts)}")

    print("\nCategories:")
    for cat, stats in metadata['categories'].items():
        print(f"  {cat}: {stats['files']} files, {stats['mentions']} mentions")

    sorted_figures = sorted(figures.items(), key=lambda x: len(x[1]), reverse=True)
    sorted_concepts = sorted(concepts.items(), key=lambda x: len(x[1]), reverse=True)

    print("\nTop 10 Figures:")
    for i, (name, citations) in enumerate(sorted_figures[:10], 1):
        print(f"  {i:2d}. {name}: {len(citations)} mentions")

    print("\nTop 10 Concepts:")
    for i, (name, citations) in enumerate(sorted_concepts[:10], 1):
        print(f"  {i:2d}. {name}: {len(citations)} mentions")

def main():
    print("=" * 70)
    print("COMPLETE PDF INGESTION PIPELINE")
    print("=" * 70)
    print(f"Started: {datetime.now().isoformat()}")

    print("\n[STEP 1] VERIFYING MARKDOWN SOURCES")
    print("=" * 70)

    sources_dir = Path("data/markdown_sources")
    if not sources_dir.exists():
        print("ERROR: No markdown_sources directory found")
        print("Run PDF conversion scripts first")
        return

    file_count = len(list(sources_dir.rglob("*.md")))
    print(f"Found {file_count} markdown files")

    # Aggregate citations
    figure_citations, concept_citations = aggregate_citations()

    # Update database
    update_database_with_sources(figure_citations, concept_citations)

    # Print summary
    print_summary()

    print("\n" + "=" * 70)
    print("PIPELINE COMPLETE")
    print(f"Finished: {datetime.now().isoformat()}")
    print()
    print("Next steps:")
    print("  1. Review master_citation_index.json for accuracy")
    print("  2. Test portal with updated sources")
    print("  3. Deploy to GitHub Pages")

if __name__ == "__main__":
    main()
