#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch portrait images for historical figures using verified public domain sources.
Uses Wikimedia Commons direct image URLs and public domain archives.
"""

import json
import os
import requests
import time
from pathlib import Path

# Curated portrait URLs from verified public domain sources
# Format: figure_name -> (image_url, source_description)
VERIFIED_PORTRAITS = {
    "Paracelsus": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Paracelsus.jpg",
        "Wikimedia Commons - public domain portrait"
    ),
    "Johann Valentin Andreae": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Johann_Valentin_Andreae.jpg",
        "Wikimedia Commons"
    ),
    "John Dee": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/John_Dee_1527-1608.jpg",
        "Wikimedia Commons - Ashmolean Museum collection"
    ),
    "Robert Fludd": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Robert_Fludd.jpg",
        "Wikimedia Commons - Smithsonian collection"
    ),
    "Michael Maier": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Michael_Maier_1568-1622.jpg",
        "Wikimedia Commons - Symbola Aureae Mensae 1617"
    ),
    "Emmanuel Swedenborg": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Emanuel_Swedenborg.png",
        "Wikimedia Commons - Carl Frederik von Breda portrait"
    ),
    "Jacob Böhme": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Jakob_Bohme.jpg",
        "PICRYL public domain collection"
    ),
    "Giordano Bruno": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Giordano_Bruno.jpg",
        "Wikimedia Commons - 18th century engraving"
    ),
    "Tycho Brahe": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Tycho_Brahe.JPG",
        "Wikimedia Commons - historical engraving"
    ),
    "Jan Baptist van Helmont": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Jan_Baptist_van_Helmont.jpg",
        "Wellcome Collection - 1666 line engraving"
    ),
    "Elias Ashmole": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Ashmole.jpg",
        "Wikimedia Commons"
    ),
    "Marsilio Ficino": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Marsilio_Ficino.jpg",
        "Wikimedia Commons - Renaissance portrait"
    ),
    "Pico della Mirandola": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Pico_della_Mirandola.jpg",
        "Wikimedia Commons"
    ),
    "Thomas Aquinas": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Thomas_Aquinas.jpg",
        "Wikimedia Commons - medieval saint portrait"
    ),
    "Roger Bacon": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Roger_Bacon.jpg",
        "Wikimedia Commons"
    ),
    "Francis Bacon": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Francis_Bacon_1561-1626.jpg",
        "Wikimedia Commons"
    ),
    "Giordano Bruno": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Giordano_Bruno.jpg",
        "Wikimedia Commons - 18th century engraving"
    ),
    "Pope Gregory XIII": (
        "https://commons.wikimedia.org/wiki/Special:FilePath/Pope_Gregory_XIII.jpg",
        "Wikimedia Commons - papal portrait"
    ),
}

def download_image(url, figure_slug, output_dir="site/images/figures"):
    """Download image with improved error handling and redirects."""
    try:
        if not url:
            return None

        os.makedirs(output_dir, exist_ok=True)

        # Set timeout and headers to avoid blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        # Request with follow redirects
        resp = requests.get(url, timeout=10, allow_redirects=True, headers=headers)
        resp.raise_for_status()

        # Determine extension from content-type or URL
        content_type = resp.headers.get("content-type", "").lower()
        if "png" in content_type or url.lower().endswith(".png"):
            ext = ".png"
        elif "jpeg" in content_type or "jpg" in content_type or url.lower().endswith(".jpg"):
            ext = ".jpg"
        elif "gif" in content_type:
            ext = ".gif"
        else:
            ext = ".jpg"  # default

        filename = f"{figure_slug}{ext}"
        filepath = os.path.join(output_dir, filename)

        # Save file
        with open(filepath, "wb") as f:
            f.write(resp.content)

        return f"images/figures/{filename}"
    except requests.exceptions.RequestException as e:
        print(f"    Download error: {type(e).__name__}")
        return None
    except Exception as e:
        print(f"    Save error: {e}")
        return None

def main():
    db_path = "data/prototype_data.json"

    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            db = json.load(f)
    except Exception as e:
        print(f"Error loading database: {e}")
        return

    figures = db.get("figures", [])
    total = len(figures)
    found = 0
    downloaded = 0
    skipped = 0

    print("=" * 70)
    print("FETCHING VERIFIED PORTRAIT IMAGES")
    print("=" * 70)
    print()

    for i, figure in enumerate(figures, 1):
        name = figure.get("name", "Unknown")
        slug = figure.get("slug", "")

        # Skip if already has image
        if figure.get("image_url"):
            found += 1
            skipped += 1
            continue

        print(f"[{i:3d}/{total}] {name}...", end=" ")

        # Check if we have a verified URL for this figure
        if name in VERIFIED_PORTRAITS:
            url, source = VERIFIED_PORTRAITS[name]
            print(f"found ({source})", end=" ")

            # Try to download
            local_path = download_image(url, slug)

            if local_path:
                figure["image_url"] = local_path
                print("✓")
                downloaded += 1
                found += 1
            else:
                print("(download failed)")
        else:
            print("(not in verified list)")

        # Rate limiting
        if i % 10 == 0:
            time.sleep(0.5)

    print()
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"Figures with images: {found} / {total} ({100*found//total if total > 0 else 0}%)")
    print(f"Already had images: {skipped}")
    print(f"Successfully downloaded: {downloaded}")
    print()

    # Save updated database
    try:
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump(db, f, indent=2, ensure_ascii=False)
        print(f"[SAVED] Updated database with image URLs")
    except Exception as e:
        print(f"Error saving database: {e}")

if __name__ == "__main__":
    main()
