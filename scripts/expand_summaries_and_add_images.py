#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expand card summaries to 2-4 sentences (40-80 words minimum) and add image URLs.
Targets figures (portraits), emblems (from emblem books), and concepts (thematic illustrations).
"""

import json
from pathlib import Path

DB_PATH = Path("data/prototype_data.json")

# ─── Summary expansion: longer, richer 2-4 sentence descriptions ───────────────

EXPANDED_FIGURES = {
    # High-priority figures with documented portraits
    "John Dee": {
        "summary": "English mathematician, astronomer, astrologer, and mystical philosopher (1527–1609). Dee's Monas Hieroglyphica (1564) integrated Neoplatonic and Kabbalistic doctrine with mathematical symbolism; his private library at Mortlake became the intellectual capital of Elizabethan England. As advisor to Queen Elizabeth I on scientific and arcane matters, he embodied the Renaissance ideal of the learned magus drawing cosmic wisdom into political counsel.",
        "image_url": "https://commons.wikimedia.org/wiki/Special:FilePath/John_Dee_1527-1609.jpg"
    },
    "Robert Fludd": {
        "summary": "English physician, astrologer, and mystical philosopher (1574–1637). Fludd's vast encyclopedic works, particularly the Utriusque Cosmi Historia, married alchemical, hermetic, and Rosicrucian doctrine into a unified cosmological system. His integration of Paracelsian medicine with Kabbalistic symbolism and his enthusiastic defence of the Rosicrucian fraternity made him the most sophisticated apologist for Christian Hermeticism in the early seventeenth century.",
        "image_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Robert_Fludd.jpg"
    },
    "Paracelsus": {
        "summary": "Swiss physician, alchemist, and reformer (c. 1493–1541). Paracelsus revolutionized medicine and pharmacy by insisting that chemistry, not Galenic humoralism, held the secrets of healing — that the arcana of nature could be extracted through spagyric art and deployed therapeutically. His doctrine that 'the art heals, experience confirms, reasoning enlightens, and practice teaches' became the foundation of Paracelsian medicine and iatrochemistry.",
        "image_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Paracelsus_1493-1541.png"
    },
    "Michael Maier": {
        "summary": "German alchemist, physician, and polymath (1568–1622). Maier's luminous emblem books, particularly the Atalanta Fugiens (1617), united alchemical laboratory practice with classical mythology and hermetic doctrine in images and prose that remain unsurpassed for philosophical depth. His work as imperial physician to Rudolf II and his prolific output established him as the most eloquent interpreter of alchemy's spiritual dimensions.",
        "image_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Michael_Maier_1568-1622.jpg"
    },
    "Jacob Böhme": {
        "summary": "German cobbler-mystic and theosophical writer (1575–1624). Böhme's visionary theology, expressed in works like the Aurora and De Signatura Rerum, integrated alchemical symbolism, mystical doctrine, and a radical theology of divine self-manifestation that profoundly influenced Rosicrucian and later theosophical thought. His teaching that God's inner darkness must produce light through conflict and union became foundational to spiritual alchemy.",
        "image_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Jacob_Böhme_1575-1624.jpg"
    },
    "Johann Valentin Andreae": {
        "summary": "German theologian and mystical writer (1586–1654). Andreae authored the Chymische Hochzeit Christiani Rosencreutz (1616), the cryptic allegorical narrative that launched the Rosicrucian manifestos and defined the movement's image and intellectual project. His fusion of Christian theology, alchemical symbolism, and utopian social reform established a template for esoteric Christianity that endured for centuries.",
        "image_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Johann_Valentin_Andreae.jpg"
    },
    "Giordano Bruno": {
        "summary": "Italian philosopher and hermeticist (1548–1600). Bruno's passionate defence of Copernican astronomy, infinite worlds, and the hermetic philosophy cost him his life when Rome burned him as a heretic in 1600. His integration of Neoplatonic, hermetic, and kabbalistic doctrine with an early heliocentric universe articulated a cosmology in which divine infinity was distributed throughout creation.",
        "image_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Giordano_Bruno_1548-1600.jpg"
    },
}

EXPANDED_CONCEPTS = {
    "Fermentation": {
        "summary": "In laboratory alchemy, fermentation (fermentatio) designated the operation by which organic matter decomposed and transformed, releasing active volatile principles — the process by which wine ferments into vinegar, or grain mash transforms into alcohol. Philosophically, fermentation represented the inner working of nature upon itself, the hidden agency that transformed materials from within rather than through external force. Spiritually, fermentation figured the inner fermentation of the soul, the slow transformation of consciousness through the agency of grace.",
    },
    "Dissolution": {
        "summary": "Dissolution (solutio) named the alchemical operation by which a solid substance was reduced to liquid — through heat, solvent action, or chemical reaction — returning it to a primal, undifferentiated state. Philosophically, it represented the stripping away of particular form to reveal prime matter, the preparatory dissolving essential before a new, perfected form could be impressed. Spiritually, dissolution corresponded to the breaking-down of the rigid ego-structures necessary before genuine mystical union could occur.",
    },
}

EXPANDED_EMBLEMS = {
    # Sample expansions for key emblems
    # Most emblems should be 40-80 words describing the visual scene, alchemical meaning, and spiritual significance
}

EXPANDED_TEXTS = {
    # Key texts needing summary expansion
    "Monas Hieroglyphica": {
        "summary": "John Dee's mystical symbol-treatise (1564) presenting a single unified glyph integrating astronomical, astrological, and kabbalistic doctrine — the monad as a mathematical and mystical principle encompassing all knowledge. The work launched a tradition of hermetic-mathematical symbolism in which the structure of the cosmos could be expressed through geometric and alphanumeric correspondences. Dee's monad became influential among later Rosicrucian and alchemical thinkers seeking to visualise the unity underlying apparent multiplicity.",
    },
    "Chymische Hochzeit Christiani Rosencreutz": {
        "summary": "Johann Valentin Andreae's allegorical narrative (1616) of the seven-day initiation of Christian Rosencreutz into mystical wisdom, culminating in a royal wedding ceremony uniting opposed principles. The work established the symbolic vocabulary of Rosicrucian allegory — the castle, the wedding feast, the sacred vessel — while encoding alchemical operations and spiritual transformation in elaborate symbolic action. Its cryptic narrative launched the Rosicrucian manifestos and became the canonical text of the movement.",
    },
}


def expand_database():
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # Expand figure summaries
    figures_expanded = 0
    for fig in db['figures']:
        name = fig.get('name', '')
        if name in EXPANDED_FIGURES:
            patch = EXPANDED_FIGURES[name]
            fig.update(patch)
            figures_expanded += 1
            print(f"  Expanded figure: {name}")

    # Expand concept summaries
    concepts_expanded = 0
    for concept in db['concepts']:
        name = concept.get('name', '')
        if name in EXPANDED_CONCEPTS:
            patch = EXPANDED_CONCEPTS[name]
            concept.update(patch)
            concepts_expanded += 1
            print(f"  Expanded concept: {name}")

    # Expand text summaries
    texts_expanded = 0
    for text in db['texts']:
        title = text.get('title', '')
        if title in EXPANDED_TEXTS:
            patch = EXPANDED_TEXTS[title]
            text.update(patch)
            texts_expanded += 1
            print(f"  Expanded text: {title}")

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"\nExpanded summaries: {figures_expanded} figures, {concepts_expanded} concepts, {texts_expanded} texts")
    print("Next: add image URLs and expand remaining summaries")


if __name__ == "__main__":
    expand_database()
