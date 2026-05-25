#!/usr/bin/env python3
"""
Fetch portrait images for historical figures from Wikimedia Commons.
Focuses on public domain images of Renaissance/early modern alchemists, theologians, etc.
"""

import json
import os
import requests
from urllib.parse import quote
from pathlib import Path

def search_wikimedia_commons(figure_name, birth_year=None):
    """
    Search Wikimedia Commons for a portrait of a figure.
    Returns the best matching image URL if found.
    """
    try:
        # Search for images of this person on Wikimedia Commons
        search_query = f'"{figure_name}" portrait'
        if birth_year:
            search_query += f" {birth_year}"

        # Wikimedia Commons API
        url = "https://commons.wikimedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": search_query,
            "srnamespace": "6",  # File namespace
            "srlimit": "5",
            "format": "json"
        }

        response = requests.get(url, params=params, timeout=5)
        results = response.json().get("query", {}).get("search", [])

        if not results:
            return None

        # Get the first result's file page
        file_title = results[0]["title"]

        # Get file info including URL
        file_params = {
            "action": "query",
            "titles": file_title,
            "prop": "imageinfo",
            "iiprop": "url|extmetadata",
            "format": "json"
        }

        file_response = requests.get(url, params=file_params, timeout=5)
        pages = file_response.json().get("query", {}).get("pages", {})

        for page_id, page_data in pages.items():
            if "imageinfo" in page_data:
                img_info = page_data["imageinfo"][0]
                img_url = img_info.get("url")

                # Check if it's public domain or freely licensed
                metadata = img_info.get("extmetadata", {})
                license_info = metadata.get("License", {}).get("value", "").lower()

                # Accept public domain and permissive licenses
                if "public domain" in license_info or "cc" in license_info or "free" in license_info:
                    return img_url

        return None
    except Exception as e:
        print(f"  Error searching for {figure_name}: {e}")
        return None

def download_image(url, figure_slug, output_dir="site/images/figures"):
    """
    Download an image from URL and save it locally.
    Returns the relative path for use in database.
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Download image
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Determine file extension from URL or content-type
        content_type = response.headers.get("content-type", "").lower()
        if "jpeg" in content_type or "jpg" in url.lower():
            ext = ".jpg"
        elif "png" in content_type or "png" in url.lower():
            ext = ".png"
        elif "gif" in content_type:
            ext = ".gif"
        else:
            ext = ".jpg"  # default

        filename = f"{figure_slug}{ext}"
        filepath = os.path.join(output_dir, filename)

        # Save file
        with open(filepath, "wb") as f:
            f.write(response.content)

        # Return relative path for web
        return f"images/figures/{filename}"
    except Exception as e:
        print(f"  Error downloading {url}: {e}")
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
            print(f"[{i:3d}/{total}] {name}: already has image")
            found += 1
            continue

        print(f"[{i:3d}/{total}] {name}...", end=" ")

        # Search for image
        img_url = search_wikimedia_commons(name, figure.get("birth_year"))

        if img_url:
            print(f"found", end=" ")

            # Download image
            local_path = download_image(img_url, slug)

            if local_path:
                figure["image_url"] = local_path
                print(f"downloaded ✓")
                downloaded += 1
                found += 1
            else:
                print(f"download failed")
        else:
            print("not found")

    print()
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"Figures with images: {found} / {total}")
    print(f"Successfully downloaded: {downloaded}")
    print()

    # Save updated database
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"[SAVED] Updated database with image URLs")
    print()

if __name__ == "__main__":
    main()
