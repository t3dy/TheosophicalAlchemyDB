#!/usr/bin/env python3
"""
Fetch portrait images for figures using Wikipedia + Wikimedia Commons.
Uses direct URLs and known portrait links instead of API (more reliable).
"""

import json
import os
import requests
from pathlib import Path

# Known Wikimedia Commons portrait URLs for major figures
# Format: figure_name -> wikimedia_commons_direct_url
PORTRAIT_MAP = {
    "Johann Valentin Andreae": "https://commons.wikimedia.org/wiki/Special:FilePath/JVA_Kupferstich_1644.jpg",
    "John Dee": "https://commons.wikimedia.org/wiki/Special:FilePath/John_Dee_1527-1608.jpg",
    "Robert Fludd": "https://commons.wikimedia.org/wiki/Special:FilePath/Robert_Fludd.jpg",
    "Paracelsus": "https://commons.wikimedia.org/wiki/Special:FilePath/Paracelsus.jpg",
    "Jacob Böhme": "https://commons.wikimedia.org/wiki/Special:FilePath/Jakob_Bohme.jpg",
    "Elias Ashmole": "https://commons.wikimedia.org/wiki/Special:FilePath/Ashmole.jpg",
    "Emmanuel Swedenborg": "https://commons.wikimedia.org/wiki/Special:FilePath/Swedenborg.jpg",
    "Michael Maier": "https://commons.wikimedia.org/wiki/Special:FilePath/Michael_Maier_1568-1622.jpg",
    "Francis Bacon": "https://commons.wikimedia.org/wiki/Special:FilePath/Francis_Bacon_1561-1626.jpg",
    "Giordano Bruno": "https://commons.wikimedia.org/wiki/Special:FilePath/Giordano_Bruno.jpg",
    "Marsilio Ficino": "https://commons.wikimedia.org/wiki/Special:FilePath/Marsilio_Ficino.jpg",
    "Pico della Mirandola": "https://commons.wikimedia.org/wiki/Special:FilePath/Pico_della_Mirandola.jpg",
    "Thomas Aquinas": "https://commons.wikimedia.org/wiki/Special:FilePath/Thomas_Aquinas.jpg",
    "Roger Bacon": "https://commons.wikimedia.org/wiki/Special:FilePath/Roger_Bacon.jpg",
    "Jan Baptist van Helmont": "https://commons.wikimedia.org/wiki/Special:FilePath/Jan_Baptist_van_Helmont.jpg",
    "Tycho Brahe": "https://commons.wikimedia.org/wiki/Special:FilePath/Tycho_Brahe.jpg",
}

def download_image(url, figure_slug, output_dir="site/images/figures"):
    """Download image and save locally."""
    try:
        os.makedirs(output_dir, exist_ok=True)

        # Determine file extension
        if url.lower().endswith(".jpg"):
            ext = ".jpg"
        elif url.lower().endswith(".png"):
            ext = ".png"
        elif url.lower().endswith(".gif"):
            ext = ".gif"
        else:
            ext = ".jpg"

        filename = f"{figure_slug}{ext}"
        filepath = os.path.join(output_dir, filename)

        # Try to download
        response = requests.get(url, timeout=10, allow_redirects=True)
        response.raise_for_status()

        # Save file
        with open(filepath, "wb") as f:
            f.write(response.content)

        return f"images/figures/{filename}"
    except Exception as e:
        return None

def main():
    print("=" * 70)
    print("FETCHING PORTRAIT IMAGES FOR FIGURES")
    print("=" * 70)
    print()

    db_path = "data/prototype_data.json"
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    figures = db.get("figures", [])
    total = len(figures)
    found = 0
    downloaded = 0

    for i, figure in enumerate(figures, 1):
        name = figure.get("name", "Unknown")
        slug = figure.get("slug", "")

        # Skip if already has image
        if figure.get("image_url"):
            found += 1
            continue

        print(f"[{i:3d}/{total}] {name}...", end=" ")

        # Check if we have a known URL for this figure
        if name in PORTRAIT_MAP:
            img_url = PORTRAIT_MAP[name]
            print(f"found", end=" ")

            # Try to download
            local_path = download_image(img_url, slug)

            if local_path:
                figure["image_url"] = local_path
                print("✓")
                downloaded += 1
                found += 1
            else:
                print("(download failed)")
        else:
            print("(no known source)")

    print()
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"Figures with images: {found} / {total} ({100*found//total}%)")
    print(f"Successfully downloaded: {downloaded}")
    print()

    # Save updated database
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"[SAVED] Updated database with image URLs")
    print()

if __name__ == "__main__":
    main()
