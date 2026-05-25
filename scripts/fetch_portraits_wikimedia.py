#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch portrait images using Wikimedia Commons API.
Searches for each figure by name and downloads available portraits.
"""

import json
import os
import requests
import time

def search_wikimedia_image(figure_name):
    """
    Search Wikimedia Commons for a portrait of a figure and return the download URL.
    """
    try:
        # Search Wikimedia Commons for files matching the figure name + "portrait"
        url = "https://commons.wikimedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": f"{figure_name} portrait",
            "srnamespace": 6,  # File namespace only
            "srlimit": 10,
            "format": "json"
        }

        resp = requests.get(url, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        results = data.get("query", {}).get("search", [])

        if not results:
            # Try without "portrait"
            params["srsearch"] = figure_name
            resp = requests.get(url, params=params, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            results = data.get("query", {}).get("search", [])

        if not results:
            return None

        # Get image info for the first result
        file_title = results[0]["title"]

        # Query to get actual download URL
        file_params = {
            "action": "query",
            "titles": file_title,
            "prop": "imageinfo",
            "iiprop": "url",
            "format": "json"
        }

        file_resp = requests.get(url, params=file_params, timeout=5)
        file_resp.raise_for_status()
        pages = file_resp.json().get("query", {}).get("pages", {})

        for page_id, page_data in pages.items():
            if "imageinfo" in page_data:
                img_url = page_data["imageinfo"][0].get("url")
                if img_url:
                    return img_url

        return None
    except Exception as e:
        print(f"    API error: {type(e).__name__}")
        return None

def download_image(url, figure_slug, output_dir="site/images/figures"):
    """Download image from URL and save locally."""
    try:
        if not url:
            return None

        os.makedirs(output_dir, exist_ok=True)

        # Request with proper headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        resp = requests.get(url, timeout=10, allow_redirects=True, headers=headers)
        resp.raise_for_status()

        # Determine extension
        content_type = resp.headers.get("content-type", "").lower()
        if "png" in content_type or url.lower().endswith(".png"):
            ext = ".png"
        elif "jpeg" in content_type or "jpg" in content_type or url.lower().endswith((".jpg", ".jpeg")):
            ext = ".jpg"
        elif "gif" in content_type:
            ext = ".gif"
        else:
            ext = ".jpg"

        filename = f"{figure_slug}{ext}"
        filepath = os.path.join(output_dir, filename)

        # Save file
        with open(filepath, "wb") as f:
            f.write(resp.content)

        return f"images/figures/{filename}"
    except Exception as e:
        print(f"    Download error: {type(e).__name__}")
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
    print("FETCHING PORTRAITS FROM WIKIMEDIA COMMONS API")
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

        # Search for image via API
        img_url = search_wikimedia_image(name)

        if img_url:
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
            print("(not found)")

        # Rate limiting to avoid API throttling
        if i % 5 == 0:
            time.sleep(1)

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
