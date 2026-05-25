#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulk expand card summaries to 2-4 sentences and add image URLs.
- Generate summaries from essays where needed
- Add image URLs from public domain sources (Wikimedia, Furnace and Fugue, Internet Archive)
"""

import json
import re
from pathlib import Path

DB_PATH = Path("data/prototype_data.json")

# Furnace and Fugue emblem image URLs for Atalanta Fugiens
FURNACE_FUGUE_BASE = "https://furnaceandfugue.org/assets/img/emblem-images_cropped/1600/emblem{:02d}.1600.jpg"

# Wikimedia Commons file URL template
WIKIMEDIA_BASE = "https://commons.wikimedia.org/wiki/Special:FilePath/"

def extract_summary_from_essay(essay_text, min_words=40, max_words=80):
    """Extract 2-4 sentence summary from essay, targeting 40-80 words."""
    if not essay_text:
        return None

    # Split on sentence boundaries (period + space + capital)
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', essay_text)

    summary = ""
    word_count = 0
    sentence_count = 0

    for sent in sentences:
        words = len(sent.split())
        if word_count + words <= max_words and sentence_count < 4:
            summary += sent + " "
            word_count += words
            sentence_count += 1
        elif word_count >= min_words:
            break

    return summary.strip() if word_count >= min_words else None

def build_emblem_image_url(emblem):
    """Build image URL for emblem based on source book."""
    source_book = emblem.get('source_book', '')
    title = emblem.get('title', '')

    if source_book == 'Atalanta Fugiens':
        # For Atalanta, we need to map to emblem numbers 0-50
        # For now, use a placeholder; actual mapping requires title correlation
        # emblems are ordered, so we can estimate position
        pass

    return None

def get_figure_wikimedia_url(figure_name):
    """Generate likely Wikimedia Commons URL for historical figure portrait."""
    # Common format: "FirstName LastName.jpg" or with dates
    # Try: "Paracelsus.jpg", "John Dee 1527-1609.jpg", etc.
    variants = [
        f"{figure_name}.jpg",
        f"{figure_name}.png",
        f"{figure_name.replace(' ', '_')}.jpg",
    ]

    # Return the most likely; user would need to verify
    return f"{WIKIMEDIA_BASE}{variants[0]}"

def enrich_database():
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)

    print("=== EXPANDING CARD SUMMARIES ===\n")

    # Expand figure summaries
    figures_expanded = 0
    for fig in db['figures']:
        current_summary = fig.get('summary', '')
        current_words = len((current_summary or '').split())

        if current_words < 40 and fig.get('essay'):
            # Try to extract from essay
            new_summary = extract_summary_from_essay(fig['essay'])
            if new_summary:
                fig['summary'] = new_summary
                figures_expanded += 1
                print(f"[OK] {fig['name']}: {len(new_summary.split())} words")

    # Expand concept summaries
    concepts_expanded = 0
    for concept in db['concepts']:
        current_summary = concept.get('summary', '')
        current_words = len((current_summary or '').split())

        if current_words < 40 and concept.get('essay'):
            new_summary = extract_summary_from_essay(concept['essay'])
            if new_summary:
                concept['summary'] = new_summary
                concepts_expanded += 1
                print(f"[OK] {concept['name']}: {len(new_summary.split())} words")

    # Expand text summaries
    texts_expanded = 0
    for text in db['texts']:
        current_summary = text.get('summary', '')
        current_words = len((current_summary or '').split())

        if current_words < 40 and text.get('essay'):
            new_summary = extract_summary_from_essay(text['essay'])
            if new_summary:
                text['summary'] = new_summary
                texts_expanded += 1
                print(f"[OK] {text['title']}: {len(new_summary.split())} words")

    # Expand emblem summaries
    emblems_expanded = 0
    for emblem in db['emblems']:
        current_summary = emblem.get('summary', '')
        current_words = len((current_summary or '').split())

        if current_words < 40 and emblem.get('essay'):
            new_summary = extract_summary_from_essay(emblem['essay'])
            if new_summary:
                emblem['summary'] = new_summary
                emblems_expanded += 1
                if emblems_expanded <= 5:  # Show first 5
                    print(f"[OK] {emblem['title']}: {len(new_summary.split())} words")

    print(f"\nTotal summaries expanded: {figures_expanded} figures, {concepts_expanded} concepts, "
          f"{texts_expanded} texts, {emblems_expanded} emblems")

    # Save expanded data
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print("\nDatabase updated with expanded summaries.")
    print("\nNext steps:")
    print("  1. Add image URLs for figures from Wikimedia Commons")
    print("  2. Add emblem images from Furnace and Fugue (Atalanta Fugiens)")
    print("  3. Research images for Stolcius and Cramer emblems")
    print("  4. Add concept illustration URLs from emblem books/manuscripts")


if __name__ == "__main__":
    enrich_database()
