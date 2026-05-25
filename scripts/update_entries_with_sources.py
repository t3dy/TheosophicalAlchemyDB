#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update database entries with markdown source citations.
Links figures and concepts to scholarly sources found in converted PDFs.
"""

import json
from pathlib import Path
from collections import defaultdict

def main():
    print("=" * 70)
    print("UPDATE ENTRIES WITH SOURCE CITATIONS")
    print("=" * 70)
    print()

    # Load database and citations
    db_path = Path("data/prototype_data.json")
    citations_path = Path("data/master_citation_index.json")

    if not citations_path.exists():
        print("Master citation index not found. Run aggregate_all_citations.py first.")
        return

    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    with open(citations_path, 'r', encoding='utf-8') as f:
        citations = json.load(f)

    # Track updates
    figures_updated = 0
    concepts_updated = 0

    # Update figures with sources
    figure_citations = citations.get('figures', {})
    for figure in db.get('figures', []):
        figure_name = figure.get('name')
        if figure_name in figure_citations:
            citations_list = figure_citations[figure_name]
            # Add source references (top 5 by category diversity)
            sources = defaultdict(list)
            for citation in citations_list:
                category = citation.get('category', 'Unknown')
                sources[category].append(citation.get('source', 'Unknown'))

            # Create source summary
            unique_sources = set()
            for source_list in sources.values():
                unique_sources.update(source_list[:2])  # Top 2 per category

            if unique_sources:
                figure['markdown_sources_found'] = list(unique_sources)[:10]
                figure['source_citations_count'] = len(citations_list)
                figures_updated += 1

    # Update concepts with sources
    concept_citations = citations.get('concepts', {})
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

    # Save updated database
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print("Updates Applied:")
    print(f"  - {figures_updated} figures updated with source citations")
    print(f"  - {concepts_updated} concepts updated with source citations")
    print()
    print(f"Updated database saved to {db_path}")
    print()
    print("Sample updated entries:")

    # Show examples
    count = 0
    for fig in db.get('figures', []):
        if fig.get('markdown_sources_found'):
            print(f"\n{fig['name']}:")
            print(f"  Sources found: {fig['source_citations_count']} mentions")
            for src in fig.get('markdown_sources_found', [])[:3]:
                print(f"    - {src[:60]}")
            count += 1
            if count >= 3:
                break

if __name__ == "__main__":
    main()
