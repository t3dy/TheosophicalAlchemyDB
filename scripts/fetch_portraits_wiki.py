#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch portrait images using Wikipedia REST API.
Queries Wikipedia for figure pages and extracts thumbnail images.
"""

import json
import os
import requests
from pathlib import Path

def get_wikipedia_image(figure_name):
    """
    Get the main image from a Wikipedia article using REST API.
    Returns the image URL if found.
    """
    try:
        # Query Wikipedia REST API
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{figure_name.replace(' ', '_')}"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            if "originalimage" in data:
                return data["originalimage"]["source"]
            elif "thumbnail" in data:
                return data["thumbnail"]["source"]
        return None
    except:
        return None

def download_image(url, figure_slug, output_dir="site/images/figures"):
    """Download and save image locally."""
    try:
        os.makedirs(output_dir, exist_ok=True)

        # Determine extension
        if ".jpg" in url.lower():
            ext = ".jpg"
        elif ".png" in url.lower():
            ext = ".png"
        else:
            ext = ".jpg"

        filename = f"{figure_slug}{ext}"
        filepath = os.path.join(output_dir, filename)

        # Download
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Save
        with open(filepath, "wb") as f:
            f.write(response.content)

        return f"images/figures/{filename}"
    except:
        return None

def main():
    db_path = "data/prototype_data.json"
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    figures = db.get("figures", [])
    total = len(figures)
    found = 0

    print("FETCHING WIKIPEDIA PORTRAITS")
    print("=" * 70)
    print()

    for i, figure in enumerate(figures, 1):
        name = figure.get("name", "Unknown")
        slug = figure.get("slug", "")

        if figure.get("image_url"):
            found += 1
            continue

        # Try to get Wikipedia image
        img_url = get_wikipedia_image(name)

        if img_url:
            local_path = download_image(img_url, slug)
            if local_path:
                figure["image_url"] = local_path
                found += 1
                status = "✓"
            else:
                status = "failed"
        else:
            status = "not found"

        if i % 10 == 0:
            print(f"[{i}/{total}] {found} found so far... ({100*found//total}%)")

    print()
    print("=" * 70)
    print(f"Total: {found}/{total} figures have images ({100*found//total}%)")
    print()

    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Saved database with images")

if __name__ == "__main__":
    main()
