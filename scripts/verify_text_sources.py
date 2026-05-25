#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verify text sources: ensure all texts are properly cited from real, extant publications.
Checks citations against known scholarly works and provides verification report.
"""

import json
from pathlib import Path
from collections import defaultdict

# Known authoritative academic sources for verification
VERIFIED_SOURCES = {
    # Renaissance & Early Modern
    "Yates": ["The Rosicrucian Enlightenment", "The Art of Memory", "Giordano Bruno and the Hermetic Tradition"],
    "Godwin": ["The Theosophical Enlightenment", "The Golden Thread"],
    "Churton": ["The Golden Builders", "Gnostic Philosophy"],
    "Hanegraaff": ["New Age Religion and Western Culture", "Esotericism and the Academy"],
    "Coudert": ["The Impact of the Kabbalah in the Seventeenth Century", "Alchemy in the Sixteenth and Seventeenth Centuries"],
    "Newman": ["Atoms and Alchemy", "Promethean Ambitions"],
    "Szulakowska": ["The Alchemy of Light"],

    # Alchemical/Chemical
    "Debus": ["The English Paracelsians", "The History of Chemistry"],
    "Moran": ["Distilling Knowledge", "The Alchemical World of the German Renaissance"],
    "Nummedal": ["Alchemy and Authority in the Holy Roman Empire"],
    "Weeks": ["Paracelsus: The Man and His Reputation"],
    "Pagel": ["Paracelsus: An Introduction to Philosophical Medicine"],

    # Hermetic & Kabbalah
    "Walker": ["Spiritual and Demonic Magic from Ficino to Campanella"],
    "Copenhaver": ["Hermetica: The Greek Corpus Hermeticum"],

    # Masonic & Rosicrucian
    "McCalman": ["The Last Alchemist"],
    "Rijnhart": ["A Blazing Star"],
}

# Known primary sources (historical texts)
PRIMARY_SOURCES = {
    "Paracelsus": ["Archidoxies", "Paragranum", "Labyrinthus Medicorum", "Seven Defensiones"],
    "John Dee": ["Monas Hieroglyphica", "Preface to Euclid"],
    "Robert Fludd": ["Utriusque Cosmi Historia", "Mosaical Philosophy"],
    "Jacob Böhme": ["Aurora", "The Way to Christ", "De Signatura Rerum"],
    "Michael Maier": ["Atalanta Fugiens", "Symbola Aureae Mensae"],
    "Johann Valentin Andreae": ["Chymische Hochzeit", "Fama Fraternitatis", "Confessio Fraternitatis"],
    "Thomas Vaughan": ["Anthroposophia Theomagica", "Magia Adamica"],
    "Roger Bacon": ["Opus Majus", "De Mirabili Potestate Artis et Naturae"],
    "Athanasius Kircher": ["Oedipus Aegyptiacus", "Mundus Subterraneus"],
}

def verify_text_sources():
    """Analyze all texts and verify their sources."""
    print("=" * 70)
    print("TEXT SOURCE VERIFICATION REPORT")
    print("=" * 70)
    print()

    db_path = Path("data/prototype_data.json")
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    texts = db.get("texts", [])

    # Categorize texts by source quality
    verified = []
    partial = []
    unverified = []
    issues = defaultdict(list)

    for text in texts:
        title = text.get("title", "Unknown")
        author = text.get("author", "Unknown")
        year = text.get("year", "Unknown")

        # Check for required fields
        has_title = bool(text.get("title"))
        has_author = bool(text.get("author"))
        has_year = bool(text.get("year"))
        has_citation = bool(text.get("scholarship") and len(text.get("scholarship", [])) > 0)
        has_summary = bool(text.get("summary"))

        completeness_score = sum([has_title, has_author, has_year, has_citation, has_summary])

        # Verify against known sources
        is_known_primary = False
        is_known_secondary = False

        for author_key, works in PRIMARY_SOURCES.items():
            if any(work.lower() in title.lower() for work in works):
                is_known_primary = True
                break

        for scholar, works in VERIFIED_SOURCES.items():
            if text.get("scholarship"):
                for scholarship in text.get("scholarship", []):
                    if scholar in scholarship.get("scholar", "") or any(
                        work.lower() in scholarship.get("reference", "").lower()
                        for work in works
                    ):
                        is_known_secondary = True
                        break

        # Categorize
        if completeness_score >= 4 and (is_known_primary or is_known_secondary):
            verified.append({
                'title': title,
                'author': author,
                'year': year,
                'completeness': completeness_score
            })
        elif completeness_score >= 3:
            partial.append({
                'title': title,
                'author': author,
                'year': year,
                'completeness': completeness_score,
                'missing': [
                    'title' if not has_title else None,
                    'author' if not has_author else None,
                    'year' if not has_year else None,
                    'citation' if not has_citation else None,
                    'summary' if not has_summary else None
                ]
            })
        else:
            unverified.append({
                'title': title,
                'author': author,
                'year': year,
                'completeness': completeness_score,
                'missing': [
                    'title' if not has_title else None,
                    'author' if not has_author else None,
                    'year' if not has_year else None,
                    'citation' if not has_citation else None,
                    'summary' if not has_summary else None
                ]
            })

    # Report
    print(f"Total texts: {len(texts)}")
    print(f"Verified (known sources + complete metadata): {len(verified)}")
    print(f"Partial (substantial but missing some fields): {len(partial)}")
    print(f"Unverified/Incomplete (needs attention): {len(unverified)}")
    print()

    if unverified:
        print("TEXTS NEEDING VERIFICATION:")
        print("-" * 70)
        for text in unverified[:15]:
            missing = [m for m in text['missing'] if m]
            print(f"\n{text['title']}")
            print(f"  Author: {text['author']}, Year: {text['year']}")
            print(f"  Completeness: {text['completeness']}/5")
            print(f"  Missing: {', '.join(missing) if missing else 'None'}")

    if partial:
        print("\n\nPARTIALLY VERIFIED TEXTS (Can be completed):")
        print("-" * 70)
        for text in partial[:10]:
            missing = [m for m in text['missing'] if m]
            print(f"\n{text['title']}")
            print(f"  Missing: {', '.join(missing) if missing else 'Complete!'}")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Quality metric: {len(verified)}/{len(texts)} texts ({100*len(verified)//len(texts)}%) verified")
    print(f"Action items: {len(unverified)} texts need field completion or source verification")
    print()

    # Recommendations
    print("RECOMMENDATIONS:")
    print("  1. Add missing citations to unverified texts")
    print("  2. Expand summaries for texts with minimal descriptions")
    print("  3. Cross-reference against academic databases for authority")
    print("  4. Link primary sources to secondary scholarship")

if __name__ == "__main__":
    verify_text_sources()
