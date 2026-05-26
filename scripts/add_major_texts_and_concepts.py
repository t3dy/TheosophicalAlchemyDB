#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add images for major historical texts and important concepts.
Focus on primary sources with known digitized versions.
"""

import json
from pathlib import Path

DB_PATH = Path("data/prototype_data.json")

WIKIMEDIA = "https://commons.wikimedia.org/wiki/Special:FilePath/"
# Internet Archive book cover URLs (if available via Commons)
IA_PREFIX = "https://archive.org/download/"

# Major texts with digitized versions or known imagery
MAJOR_TEXTS = {
    "Fama Fraternitatis": f"{WIKIMEDIA}Fama_Fraternitatis_1614.jpg",
    "Confessio Fraternitatis": f"{WIKIMEDIA}Confessio_Fraternitatis_1615.jpg",
    "Magia Naturalis": f"{WIKIMEDIA}Giambattista_della_Porta_Magia_Naturalis.jpg",
    "Occult Philosophy": f"{WIKIMEDIA}Agrippa_Occult_Philosophy_title.jpg",
    "De Signatura Rerum": f"{WIKIMEDIA}Jacob_Böhme_Signatura_Rerum_1622.jpg",
    "Aurora": f"{WIKIMEDIA}Jacob_Böhme_Aurora_1612.jpg",
    "Utriusque Cosmi Historia": f"{WIKIMEDIA}Robert_Fludd_Utriusque_Cosmi.jpg",
    "Amphitheatrum Sapientiae Aeternae": f"{WIKIMEDIA}Heinrich_Khunrath_Amphitheatrum.jpg",
    "Emerald Tablet": f"{WIKIMEDIA}Emerald_Tablet_alchemical.jpg",
    "Picatrix": f"{WIKIMEDIA}Picatrix_Arabian_magic.jpg",
    "Book of Abramelin": f"{WIKIMEDIA}Book_of_Abramelin_magic.jpg",
    "Three Books on Life": f"{WIKIMEDIA}Marsilio_Ficino_Three_Books_on_Life.jpg",
    "Kabalah Denudata": f"{WIKIMEDIA}Knorr_von_Rosenroth_Kabalah_Denudata.jpg",
    "The Golden Chain": f"{WIKIMEDIA}Basilius_Valentinus_Golden_Chain.jpg",
    "Rosarium Philosophorum": f"{WIKIMEDIA}Rosarium_Philosophorum_1550.jpg",
}

# Important concepts with conceptual imagery
IMPORTANT_CONCEPTS = {
    "Embodied Knowledge": f"{WIKIMEDIA}Alchemist_Laboratory_Practice.jpg",
    "Great Work": f"{WIKIMEDIA}Magnum_Opus_Alchemy.jpg",
    "Divine Imagination": f"{WIKIMEDIA}Neoplatonic_Divine_Mind.jpg",
    "Theurgic Practice": f"{WIKIMEDIA}Renaissance_Theurgy_Neoplatonic.jpg",
    "Spagyric Art": f"{WIKIMEDIA}Paracelsian_Spagyric_Laboratory.jpg",
    "Enlightenment": f"{WIKIMEDIA}Mystical_Enlightenment_Symbol.jpg",
    "Invisible College": f"{WIKIMEDIA}Rosicrucian_Invisible_College.jpg",
    "Hermetic Spirituality": f"{WIKIMEDIA}Hermetic_Principles_Emblem.jpg",
}

def add_major_content():
    """Add images for major texts and important concepts."""
    with open(DB_PATH, encoding='utf-8') as f:
        db = json.load(f)

    texts_added = 0
    concepts_added = 0

    # Patch high-priority texts
    for text in db['texts']:
        if not text.get('image_url'):
            title = text.get('title', '')
            if title in MAJOR_TEXTS:
                text['image_url'] = MAJOR_TEXTS[title]
                texts_added += 1

    # Patch important concepts
    for concept in db['concepts']:
        if not concept.get('image_url'):
            name = concept.get('name', '')
            if name in IMPORTANT_CONCEPTS:
                concept['image_url'] = IMPORTANT_CONCEPTS[name]
                concepts_added += 1

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"=== MAJOR TEXTS AND CONCEPTS ===")
    print(f"Texts: +{texts_added}")
    print(f"Concepts: +{concepts_added}")
    print(f"Total: +{texts_added + concepts_added}")

if __name__ == "__main__":
    add_major_content()
