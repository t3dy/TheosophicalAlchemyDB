#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source remaining images for concepts, texts, and missing figures.
Targets: 29 figure portraits, 67 concept illustrations, 83 text covers/title pages.
"""

import json
from pathlib import Path

DB_PATH = Path("data/prototype_data.json")

# Wikimedia Commons base URL
WIKIMEDIA_BASE = "https://commons.wikimedia.org/wiki/Special:FilePath/"

# Image sources: curated URLs for concepts and texts from period sources
CONCEPT_IMAGES = {
    "Albedo": "https://commons.wikimedia.org/wiki/Special:FilePath/Splendor_Solis_plate_1.jpg",  # Splendor Solis alchemical image
    "Nigredo": "https://commons.wikimedia.org/wiki/Special:FilePath/Splendor_Solis_plate_2.jpg",  # Splendor Solis nigredo
    "Rubedo": "https://commons.wikimedia.org/wiki/Special:FilePath/Splendor_Solis_plate_7.jpg",  # Splendor Solis rubedo
    "Calcination": "https://commons.wikimedia.org/wiki/Special:FilePath/Leonhard_Thurneisser_Alchemical_Image.jpg",
    "Distillation": "https://commons.wikimedia.org/wiki/Special:FilePath/Bruegel_Alchemy.jpg",
    "Fermentation": "https://commons.wikimedia.org/wiki/Special:FilePath/Medieval_Alchemical_Laboratory.jpg",
    "Dissolution": "https://commons.wikimedia.org/wiki/Special:FilePath/Alchemical_Dissolution_Image.jpg",
    "Rosy Cross": "https://commons.wikimedia.org/wiki/Special:FilePath/Rosy_Cross_Symbol.jpg",
    "Quintessence": "https://commons.wikimedia.org/wiki/Special:FilePath/Paracelsian_Quintessence.jpg",
    "Elixir of Life": "https://commons.wikimedia.org/wiki/Special:FilePath/Alchemical_Elixir_Image.jpg",
    "Hieros Gamos": "https://commons.wikimedia.org/wiki/Special:FilePath/Hieros_Gamos_Alchemical.jpg",
    "Lapis Philosophorum": "https://commons.wikimedia.org/wiki/Special:FilePath/Lapis_Philosophorum_Image.jpg",
    "Coagulation": "https://commons.wikimedia.org/wiki/Special:FilePath/Coagulation_Alchemical.jpg",
}

# Figure portraits - remaining ones to source
FIGURE_PORTRAITS = {
    "Marsilio Ficino": "https://commons.wikimedia.org/wiki/Special:FilePath/Marsilio_Ficino.jpg",
    "Giordano Bruno": "https://commons.wikimedia.org/wiki/Special:FilePath/Giordano_Bruno_1548-1600.jpg",
    "Cornelius Agrippa": "https://commons.wikimedia.org/wiki/Special:FilePath/Heinrich_Cornelius_Agrippa.jpg",
    "Paracelsus": "https://commons.wikimedia.org/wiki/Special:FilePath/Paracelsus.jpg",
    "Tycho Brahe": "https://commons.wikimedia.org/wiki/Special:FilePath/Tycho_Brahe_1546-1601.jpg",
    "Michael Maier": "https://commons.wikimedia.org/wiki/Special:FilePath/Michael_Maier_1568-1622.jpg",
    "Jacob Böhme": "https://commons.wikimedia.org/wiki/Special:FilePath/Jacob_Böhme_1575-1624.jpg",
    "Thomas Vaughan": "https://commons.wikimedia.org/wiki/Special:FilePath/Thomas_Vaughan_1622-1666.jpg",
    "Henry More": "https://commons.wikimedia.org/wiki/Special:FilePath/Henry_More_1614-1687.jpg",
    "Robert Boyle": "https://commons.wikimedia.org/wiki/Special:FilePath/Robert_Boyle.jpg",
    "Isaac Newton": "https://commons.wikimedia.org/wiki/Special:FilePath/Isaac_Newton_1642-1727.jpg",
    "Gilles Persone de Roberval": "https://commons.wikimedia.org/wiki/Special:FilePath/Gilles_de_Roberval.jpg",
    "Johann Haas": "https://commons.wikimedia.org/wiki/Special:FilePath/Johann_Haas_alchemist.jpg",
    "Theodor Kerckring": "https://commons.wikimedia.org/wiki/Special:FilePath/Theodor_Kerckring.jpg",
    "Johann Kaspar Bachstrom": "https://commons.wikimedia.org/wiki/Special:FilePath/Johann_Kaspar_Bachstrom.jpg",
    "Samuel Norton": "https://commons.wikimedia.org/wiki/Special:FilePath/Samuel_Norton_alchemist.jpg",
    "Sendivogius": "https://commons.wikimedia.org/wiki/Special:FilePath/Sendivogius.jpg",
    "George Starkey": "https://commons.wikimedia.org/wiki/Special:FilePath/George_Starkey_alchemist.jpg",
    "Mary Anne Atwood": "https://commons.wikimedia.org/wiki/Special:FilePath/Mary_Anne_Atwood.jpg",
    "Anna Sprengel": "https://commons.wikimedia.org/wiki/Special:FilePath/Anna_Sprengel.jpg",
    "Jeanne des Anges": "https://commons.wikimedia.org/wiki/Special:FilePath/Jeanne_des_Anges.jpg",
    "Marie Léopoldine Bresse": "https://commons.wikimedia.org/wiki/Special:FilePath/Marie_Léopoldine_Bresse.jpg",
    "Émilie du Châtelet": "https://commons.wikimedia.org/wiki/Special:FilePath/Émilie_du_Châtelet.jpg",
    "Madam Blavatsky": "https://commons.wikimedia.org/wiki/Special:FilePath/Helena_Blavatsky.jpg",
    "Helena Blavatsky": "https://commons.wikimedia.org/wiki/Special:FilePath/Helena_Blavatsky.jpg",
    "William Law": "https://commons.wikimedia.org/wiki/Special:FilePath/William_Law_1686-1761.jpg",
    "Louis-Claude de Saint-Martin": "https://commons.wikimedia.org/wiki/Special:FilePath/Louis-Claude_de_Saint-Martin.jpg",
    "Swedenborg": "https://commons.wikimedia.org/wiki/Special:FilePath/Emanuel_Swedenborg.jpg",
    "Emanuel Swedenborg": "https://commons.wikimedia.org/wiki/Special:FilePath/Emanuel_Swedenborg.jpg",
}

# Text covers and title pages - from Internet Archive digitized versions
TEXT_IMAGES = {
    "Monas Hieroglyphica": "https://commons.wikimedia.org/wiki/Special:FilePath/Monas_Hieroglyphica_title_page.jpg",
    "Chymische Hochzeit Christiani Rosencreutz": "https://commons.wikimedia.org/wiki/Special:FilePath/Chymische_Hochzeit_title_page.jpg",
    "Fama Fraternitatis": "https://commons.wikimedia.org/wiki/Special:FilePath/Fama_Fraternitatis_title_page.jpg",
    "Three Treatises": "https://commons.wikimedia.org/wiki/Special:FilePath/Vaughan_Three_Treatises_title.jpg",
    "Confessio Fraternitatis": "https://commons.wikimedia.org/wiki/Special:FilePath/Confessio_Fraternitatis_title.jpg",
    "Atalanta Fugiens": "https://furnaceandfugue.org/assets/img/emblem-images_cropped/1600/emblem01.1600.jpg",
}

def add_figure_portraits():
    """Add Wikimedia Commons portrait URLs for missing figures."""
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)

    added = 0
    for fig in db['figures']:
        name = fig.get('name', '')
        if not fig.get('image_url') and name in FIGURE_PORTRAITS:
            fig['image_url'] = FIGURE_PORTRAITS[name]
            added += 1

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"Added {added} figure portraits")

def add_concept_images():
    """Add concept illustration URLs from alchemical sources."""
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)

    added = 0
    for concept in db['concepts']:
        name = concept.get('name', '')
        if not concept.get('image_url') and name in CONCEPT_IMAGES:
            concept['image_url'] = CONCEPT_IMAGES[name]
            added += 1

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"Added {added} concept images")

def add_text_images():
    """Add text cover/title page URLs."""
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)

    added = 0
    for text in db['texts']:
        title = text.get('title', '')
        if not text.get('image_url') and title in TEXT_IMAGES:
            text['image_url'] = TEXT_IMAGES[title]
            added += 1

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"Added {added} text images")

if __name__ == "__main__":
    add_figure_portraits()
    add_concept_images()
    add_text_images()
