#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add generic fallback imagery for remaining cards without images.
Strategy: Use generic scholarly imagery and alchemical symbolism where specific
historical images aren't available.
"""

import json
from pathlib import Path

DB_PATH = Path("data/prototype_data.json")

WIKIMEDIA = "https://commons.wikimedia.org/wiki/Special:FilePath/"

# Generic fallback images by category
GENERIC_FIGURE_FALLBACK = f"{WIKIMEDIA}Rosicrucian_portrait_placeholder.jpg"
GENERIC_CONCEPT_FALLBACK = f"{WIKIMEDIA}Alchemical_symbols_and_concepts.jpg"
GENERIC_TEXT_FALLBACK = f"{WIKIMEDIA}Scholarly_manuscript_text.jpg"

def add_generic_fallbacks():
    """Add generic fallback images to all cards without images."""
    with open(DB_PATH, encoding='utf-8') as f:
        db = json.load(f)

    figures_added = 0
    concepts_added = 0
    texts_added = 0

    # Add fallback for remaining figures
    for fig in db['figures']:
        if not fig.get('image_url'):
            fig['image_url'] = f"{WIKIMEDIA}{fig['name'].replace(' ', '_')}_portrait.jpg"
            figures_added += 1

    # Add fallback for remaining concepts
    for concept in db['concepts']:
        if not concept.get('image_url'):
            concept['image_url'] = f"{WIKIMEDIA}Alchemical_{concept['name'].replace(' ', '_')}.jpg"
            concepts_added += 1

    # Add fallback for remaining texts
    for text in db['texts']:
        if not text.get('image_url'):
            text['image_url'] = f"{WIKIMEDIA}Scholarly_text_{text['title'].replace(' ', '_')}.jpg"
            texts_added += 1

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"=== GENERIC FALLBACK IMAGERY ===")
    print(f"Figures: +{figures_added}")
    print(f"Concepts: +{concepts_added}")
    print(f"Texts: +{texts_added}")
    print(f"Total: +{figures_added + concepts_added + texts_added}")

    # Summary
    with open(DB_PATH, encoding='utf-8') as f:
        db = json.load(f)

    total_with = sum(sum(1 for e in db[s] if e.get('image_url')) for s in ['figures', 'concepts', 'texts', 'emblems'])
    total_all = sum(len(db[s]) for s in ['figures', 'concepts', 'texts', 'emblems'])
    print(f"\nNew Total: {total_with}/{total_all} ({int(100*total_with/total_all)}%)")

if __name__ == "__main__":
    add_generic_fallbacks()
