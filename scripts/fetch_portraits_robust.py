#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch portrait images by querying Wikimedia Commons directly with proper API.
"""

import json
import os
import requests
import time

def search_commons_api(figure_name):
    """Search Wikimedia Commons API for portrait images."""
    try:
        # Try with "portrait" keyword
        search_terms = [
            f'"{figure_name}"',
            f'"{figure_name}" portrait',
        ]

        for search_term in search_terms:
            url = "https://commons.wikimedia.org/w/api.php"
            params = {
                "action": "query",
                "list": "allimages",
                "aisort": "timestamp",
                "aidir": "descending",
                "aiprop": "url|dimensions",
                "aifrom": figure_name[:3],  # Start search near the name
                "ailimit": "100",
                "format": "json"
            }

            try:
                resp = requests.get(url, params=params, timeout=3)
                if resp.status_code == 200:
                    data = resp.json()
                    images = data.get("query", {}).get("allimages", [])

                    # Look for portrait-like images
                    for img in images:
                        title = img.get("name", "").lower()
                        # Skip non-image formats
                        if ".jpg" in title or ".png" in title or ".jpeg" in title:
                            # Simple heuristic: portrait usually has square or portrait dimensions
                            w = img.get("width", 0)
                            h = img.get("height", 0)
                            if h > w * 0.7:  # Taller than wide (portrait orientation)
                                return img.get("url")
            except:
                pass

        return None
    except:
        return None

def download_image_simple(url, figure_slug, output_dir="site/images/figures"):
    """Download and save image."""
    try:
        if not url:
            return None

        os.makedirs(output_dir, exist_ok=True)

        # Determine extension from URL
        if ".jpg" in url.lower():
            ext = ".jpg"
        elif ".png" in url.lower():
            ext = ".png"
        elif ".gif" in url.lower():
            ext = ".gif"
        else:
            # Try to get from content-type
            resp = requests.head(url, timeout=3, allow_redirects=True)
            content_type = resp.headers.get("content-type", "").lower()
            if "png" in content_type:
                ext = ".png"
            else:
                ext = ".jpg"

        filename = f"{figure_slug}{ext}"
        filepath = os.path.join(output_dir, filename)

        resp = requests.get(url, timeout=5, allow_redirects=True)
        if resp.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(resp.content)
            return f"images/figures/{filename}"

        return None
    except:
        return None

def main():
    db_path = "data/prototype_data.json"
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    figures = db.get("figures", [])
    found = 0
    downloaded = 0

    print("FETCHING PORTRAITS FROM WIKIMEDIA COMMONS")
    print("=" * 70)

    for i, figure in enumerate(figures, 1):
        name = figure.get("name", "Unknown")
        slug = figure.get("slug", "")

        if figure.get("image_url"):
            found += 1
            continue

        # Search for image
        img_url = search_commons_api(name)

        if img_url:
            # Try to download
            local_path = download_image_simple(img_url, slug)
            if local_path:
                figure["image_url"] = local_path
                found += 1
                downloaded += 1

        # Show progress every 10
        if i % 10 == 0:
            print(f"[{i:3d}/100] Progress: {found} images found, {downloaded} downloaded")
            time.sleep(0.5)  # Rate limiting

    print()
    print("=" * 70)
    print(f"RESULTS: {found}/{len(figures)} figures have images ({100*found//len(figures)}%)")
    print(f"Successfully downloaded: {downloaded}")
    print()

    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print("Database saved with image URLs")

if __name__ == "__main__":
    main()
