#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch portrait images using a curated list of verified URLs from Wikimedia Commons.
Falls back to Wikipedia API for figures not in the curated list.
"""

import json
import os
import requests
import time
from pathlib import Path
import sys

# Ensure UTF-8 output
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'

# Known working portrait URLs from Wikimedia Commons
# Extracted from verified sources during research phase
CURATED_PORTRAITS = {
    "John Dee": "https://upload.wikimedia.org/wikipedia/commons/5/58/John_Dee_1527-1608.jpg",
    "Tycho Brahe": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Tycho_Brahe.JPG",
    "Paracelsus": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Paracelsus.jpg/440px-Paracelsus.jpg",
    "Emmanuel Swedenborg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Emanuel_Swedenborg.png/300px-Emanuel_Swedenborg.png",
    "Robert Fludd": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Robert_Fludd.jpg/300px-Robert_Fludd.jpg",
    "Michael Maier": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Michael_Maier_1568-1622.jpg/300px-Michael_Maier_1568-1622.jpg",
    "Giordano Bruno": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Giordano_Bruno.jpg/300px-Giordano_Bruno.jpg",
    "Jan Baptist van Helmont": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Jan_Baptist_van_Helmont.jpg/300px-Jan_Baptist_van_Helmont.jpg",
    "Isaac Newton": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/GodfreyKneller-IsaacNewton-1689.jpg/440px-GodfreyKneller-IsaacNewton-1689.jpg",
    "Marsilio Ficino": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Marsilio_Ficino.jpg/300px-Marsilio_Ficino.jpg",
    "Jacob Böhme": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Jakob_Bohme.jpg/300px-Jakob_Bohme.jpg",
    "Francis Bacon": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Francis_Bacon_1561-1626.jpg/300px-Francis_Bacon_1561-1626.jpg",
    "Roger Bacon": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Roger_Bacon.jpg/300px-Roger_Bacon.jpg",
    "Thomas Aquinas": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Thomas_Aquinas_%28Bartolome_Bermejo%29.jpg/300px-Thomas_Aquinas_%28Bartolome_Bermejo%29.jpg",
    "Pico della Mirandola": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Pico_della_Mirandola.jpg/300px-Pico_della_Mirandola.jpg",
}

def get_wikipedia_portrait(figure_name):
    """Try to get portrait from Wikipedia REST API."""
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{figure_name.replace(' ', '_')}"
        resp = requests.get(url, timeout=5)

        if resp.status_code == 200:
            data = resp.json()
            if "originalimage" in data:
                return data["originalimage"]["source"]
            elif "thumbnail" in data:
                return data["thumbnail"]["source"]

        return None
    except Exception as e:
        return None

def download_image(url, figure_slug, output_dir="site/images/figures"):
    """Download image and save locally."""
    try:
        if not url:
            return None

        os.makedirs(output_dir, exist_ok=True)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        resp = requests.get(url, timeout=10, allow_redirects=True, headers=headers)
        resp.raise_for_status()

        # Determine extension
        content_type = resp.headers.get("content-type", "").lower()
        if "png" in content_type:
            ext = ".png"
        else:
            ext = ".jpg"

        filename = f"{figure_slug}{ext}"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "wb") as f:
            f.write(resp.content)

        return f"images/figures/{filename}"
    except Exception as e:
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
    print("FETCHING PORTRAIT IMAGES (CURATED + WIKIPEDIA FALLBACK)")
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

        status_line = f"[{i:3d}/{total}] {name[:50]:<50}"
        print(status_line, end=" ", flush=True)

        img_url = None

        # First try curated list
        if name in CURATED_PORTRAITS:
            img_url = CURATED_PORTRAITS[name]
            print("curated", end=" ", flush=True)
        else:
            # Fall back to Wikipedia
            img_url = get_wikipedia_portrait(name)
            if img_url:
                print("wikipedia", end=" ", flush=True)

        if img_url:
            local_path = download_image(img_url, slug)
            if local_path:
                figure["image_url"] = local_path
                print("✓")
                downloaded += 1
                found += 1
            else:
                print("(dl failed)")
        else:
            print("(not found)")

        # Rate limiting
        if i % 5 == 0:
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
