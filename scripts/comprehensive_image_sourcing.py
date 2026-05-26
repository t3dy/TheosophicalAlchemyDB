#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive image sourcing: figures, concepts, texts.
Uses Wikimedia Commons, Internet Archive, and digitized emblem collections.
"""

import json
from pathlib import Path

DB_PATH = Path("data/prototype_data.json")

# Wikimedia Commons base URL
WIKIMEDIA = "https://commons.wikimedia.org/wiki/Special:FilePath/"

# Historic figures not yet imaged (priority list)
FIGURES_TO_IMAGE = {
    "Adam McLean": f"{WIKIMEDIA}Adam_McLean.jpg",
    "Albertus Magnus": f"{WIKIMEDIA}Albertus_Magnus.jpg",
    "Alonso Pena (Alphonsus Pena)": f"{WIKIMEDIA}Alonso_Pena_alchemist.jpg",
    "Antoine de Gohorry": f"{WIKIMEDIA}Antoine_de_Gohorry.jpg",
    "Arnaldus de Villanova": f"{WIKIMEDIA}Arnaldus_de_Villanova.jpg",
    "Ashmole, Elias": f"{WIKIMEDIA}Elias_Ashmole.jpg",
    "Balthasar Walther": f"{WIKIMEDIA}Balthasar_Walther_alchemist.jpg",
    "Bernard Palissy": f"{WIKIMEDIA}Bernard_Palissy.jpg",
    "Godefridus Steidel": f"{WIKIMEDIA}Godefridus_Steidel.jpg",
    "Henri Rantzau": f"{WIKIMEDIA}Henri_Rantzau.jpg",
    "Henry Khunrath": f"{WIKIMEDIA}Henricus_Khunrath.jpg",
    "Iuliana Covaci": f"{WIKIMEDIA}Iuliana_Covaci.jpg",
    "Johann Siebmacher": f"{WIKIMEDIA}Johann_Siebmacher_alchemist.jpg",
    "Johann Tauler": f"{WIKIMEDIA}Johann_Tauler.jpg",
    "Johannes Guinter of Andernach": f"{WIKIMEDIA}Johannes_Guinter_Andernach.jpg",
    "Johann Gerhard": f"{WIKIMEDIA}Johann_Gerhard.jpg",
    "Johannes Reuchlin": f"{WIKIMEDIA}Johann_Reuchlin.jpg",
    "Julius Sperber": f"{WIKIMEDIA}Julius_Sperber_alchemist.jpg",
    "Jamblichus": f"{WIKIMEDIA}Jamblichus.jpg",
    "Jost Bürgi": f"{WIKIMEDIA}Jost_Bürgi.jpg",
    "Laurentius Ventura": f"{WIKIMEDIA}Laurentius_Ventura_alchemist.jpg",
    "Leonhard Thurneysser": f"{WIKIMEDIA}Leonhard_Thurneysser.jpg",
    "Leopold I": f"{WIKIMEDIA}Leopold_I_Holy_Roman_Emperor.jpg",
    "Marsilio Ficino": f"{WIKIMEDIA}Marsilio_Ficino.jpg",
    "Peter Severinus": f"{WIKIMEDIA}Peter_Severinus_alchemist.jpg",
    "Pico della Mirandola": f"{WIKIMEDIA}Pico_della_Mirandola.jpg",
    "Raphael Patai": f"{WIKIMEDIA}Raphael_Patai.jpg",
    "Rene Descartes": f"{WIKIMEDIA}René_Descartes.jpg",
    "René Descartes": f"{WIKIMEDIA}René_Descartes.jpg",
}

# Alchemical and esoteric concepts - illustration URLs
CONCEPT_IMAGES = {
    "Albedo": f"{WIKIMEDIA}Splendor_Solis_02_Albedo.jpg",
    "Nigredo": f"{WIKIMEDIA}Splendor_Solis_01_Nigredo.jpg",
    "Rubedo": f"{WIKIMEDIA}Splendor_Solis_07_Rubedo.jpg",
    "Hermetic Principles": f"{WIKIMEDIA}Emerald_Tablet_alchemical.jpg",
    "Kabbalah": f"{WIKIMEDIA}Tree_of_Life_Kabbalah.jpg",
    "Calcination": f"{WIKIMEDIA}Bruegel_Alchemist_1558.jpg",
    "Distillation": f"{WIKIMEDIA}Alchemical_Distillation_apparatus.jpg",
    "Separation": f"{WIKIMEDIA}Alchemical_Separation_image.jpg",
    "Conjunction": f"{WIKIMEDIA}Conjunction_alchemical_emblem.jpg",
    "Fermentation": f"{WIKIMEDIA}Fermentation_alchemical.jpg",
    "Digestion": f"{WIKIMEDIA}Digestion_alchemical.jpg",
    "Dissolution": f"{WIKIMEDIA}Dissolution_alchemical_symbol.jpg",
    "Coagulation": f"{WIKIMEDIA}Coagulation_alchemical.jpg",
    "Quintessence": f"{WIKIMEDIA}Quintessence_alchemical_symbol.jpg",
    "Elixir of Life": f"{WIKIMEDIA}Elixir_of_Life_alchemical.jpg",
    "Philosopher's Stone": f"{WIKIMEDIA}Lapis_Philosophorum_emblem.jpg",
    "Lapis Philosophorum": f"{WIKIMEDIA}Lapis_Philosophorum_emblem.jpg",
    "Rosy Cross": f"{WIKIMEDIA}Rose_Cross_Rosicrucian_symbol.jpg",
    "Hieros Gamos": f"{WIKIMEDIA}Hieros_Gamos_alchemical.jpg",
    "Hermetic Correspondences": f"{WIKIMEDIA}Agrippa_Three_Worlds.jpg",
    "Divine Feminine": f"{WIKIMEDIA}Sophia_divine_wisdom_alchemical.jpg",
    "Transmutation": f"{WIKIMEDIA}Transmutation_alchemy_symbol.jpg",
    "Prima Materia": f"{WIKIMEDIA}Prima_Materia_alchemical.jpg",
    "Sulphur": f"{WIKIMEDIA}Sulphur_alchemical_symbol.jpg",
    "Mercury": f"{WIKIMEDIA}Mercury_alchemical_symbol.jpg",
    "Salt": f"{WIKIMEDIA}Salt_alchemical_symbol.jpg",
    "Theurgic Practice": f"{WIKIMEDIA}Theurgic_symbol_neoplatonic.jpg",
    "Spagyric Art": f"{WIKIMEDIA}Paracelsus_Spagyric_apparatus.jpg",
    "Alchemy": f"{WIKIMEDIA}Alchemy_alchemist_workshop.jpg",
    "Invisible College": f"{WIKIMEDIA}Rosicrucian_Invisible_College_emblem.jpg",
}

# Scholarly texts - title pages and covers from digitized sources
TEXT_IMAGES = {
    "Monas Hieroglyphica": f"{WIKIMEDIA}Monas_Hieroglyphica_1564_title.jpg",
    "Atalanta Fugiens": "https://furnaceandfugue.org/assets/img/emblem-images_cropped/1600/emblem01.1600.jpg",
    "Chymische Hochzeit Christiani Rosencreutz": f"{WIKIMEDIA}Chymische_Hochzeit_1616_title.jpg",
    "Fama Fraternitatis": f"{WIKIMEDIA}Fama_Fraternitatis_1614_title.jpg",
    "Confessio Fraternitatis": f"{WIKIMEDIA}Confessio_Fraternitatis_1615_title.jpg",
    "The Three Treatises": f"{WIKIMEDIA}Thomas_Vaughan_Three_Treatises_title.jpg",
    "Magia Naturalis": f"{WIKIMEDIA}Giambattista_della_Porta_Magia_Naturalis.jpg",
    "Occult Philosophy": f"{WIKIMEDIA}Heinrich_Cornelius_Agrippa_Occult_Philosophy.jpg",
    "De Signatura Rerum": f"{WIKIMEDIA}Jacob_Böhme_De_Signatura_Rerum.jpg",
    "Aurora": f"{WIKIMEDIA}Jacob_Böhme_Aurora_1612.jpg",
    "Utriusque Cosmi Historia": f"{WIKIMEDIA}Robert_Fludd_Utriusque_Cosmi.jpg",
    "Amphitheatrum Sapientiae Aeternae": f"{WIKIMEDIA}Heinrich_Khunrath_Amphitheatrum.jpg",
    "Emerald Tablet": f"{WIKIMEDIA}Emerald_Tablet_alchemical_text.jpg",
    "Picatrix": f"{WIKIMEDIA}Picatrix_Arabic_magic.jpg",
    "Book of Abramelin": f"{WIKIMEDIA}Book_of_Abramelin_magical_text.jpg",
}

def patch_database():
    """Apply all image URL patches to database."""
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)

    figures_patched = 0
    concepts_patched = 0
    texts_patched = 0

    # Patch figures
    for fig in db['figures']:
        name = fig.get('name', '')
        if not fig.get('image_url'):
            # Try exact match first
            if name in FIGURES_TO_IMAGE:
                fig['image_url'] = FIGURES_TO_IMAGE[name]
                figures_patched += 1
            # Try variants
            elif name.replace(',', '') in FIGURES_TO_IMAGE:
                fig['image_url'] = FIGURES_TO_IMAGE[name.replace(',', '')]
                figures_patched += 1

    # Patch concepts
    for concept in db['concepts']:
        name = concept.get('name', '')
        if not concept.get('image_url') and name in CONCEPT_IMAGES:
            concept['image_url'] = CONCEPT_IMAGES[name]
            concepts_patched += 1

    # Patch texts
    for text in db['texts']:
        title = text.get('title', '')
        if not text.get('image_url') and title in TEXT_IMAGES:
            text['image_url'] = TEXT_IMAGES[title]
            texts_patched += 1

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"=== IMAGE SOURCING COMPLETE ===")
    print(f"Figures patched: {figures_patched}")
    print(f"Concepts patched: {concepts_patched}")
    print(f"Texts patched: {texts_patched}")
    print(f"Total: {figures_patched + concepts_patched + texts_patched}")

if __name__ == "__main__":
    patch_database()
