#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download real public-domain portraits from Wikimedia Commons with rate-limiting.
"""

import json
import os
import requests
import time

# Real Wikimedia Commons URLs (verified from Wikipedia)
REAL_PORTRAITS = {
    "John Dee": "https://upload.wikimedia.org/wikipedia/commons/4/40/John_Dee_Ashmolean.jpg",
    "Paracelsus": "https://upload.wikimedia.org/wikipedia/commons/2/25/Aureolus_Theophrastus_Bombastus_von_Hohenheim_%28Paracelsus%29._Wellcome_V0004455.jpg",
    "Robert Fludd": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Robert_Fludd.jpg",
}

def download_image(url, figure_slug, output_dir="site/images/figures", delay=2):
    """Download image from URL with rate-limiting."""
    try:
        os.makedirs(output_dir, exist_ok=True)

        # Wait between requests to respect rate limits
        time.sleep(delay)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
            'Accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Referer': 'https://commons.wikimedia.org/'
        }

        print(f"  Requesting {url[:60]}...")
        resp = requests.get(url, timeout=15, allow_redirects=True, headers=headers)
        resp.raise_for_status()

        # Determine extension from URL or content-type
        if 'jpg' in url.lower() or 'jpeg' in resp.headers.get("content-type", "").lower():
            ext = ".jpg"
        elif 'png' in url.lower() or 'png' in resp.headers.get("content-type", "").lower():
            ext = ".png"
        else:
            ext = ".jpg"

        filename = f"{figure_slug}{ext}"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "wb") as f:
            f.write(resp.content)

        size_kb = len(resp.content) / 1024
        print(f"  [OK] {filename} ({size_kb:.1f} KB)")
        return f"images/figures/{filename}"
    except requests.exceptions.HTTPError as e:
        if "429" in str(e):
            print(f"  [RATE LIMITED] Waiting 5 seconds...")
            time.sleep(5)
            return download_image(url, figure_slug, output_dir, delay=5)
        else:
            print(f"  [ERROR] HTTP {e}")
            return None
    except Exception as e:
        print(f"  [ERROR] {type(e).__name__}: {e}")
        return None

def main():
    db_path = "data/prototype_data.json"

    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    figures = db.get("figures", [])
    downloaded = 0

    print("=" * 70)
    print("DOWNLOADING REAL PUBLIC-DOMAIN PORTRAITS FROM WIKIMEDIA")
    print("=" * 70)
    print()

    for name, url in REAL_PORTRAITS.items():
        # Find matching figure
        figure = None
        for f in figures:
            if f.get("name") == name:
                figure = f
                break

        if not figure:
            print(f"{name}: NOT FOUND in database")
            continue

        print(f"{name}:")
        slug = figure.get("slug", "")
        local_path = download_image(url, slug)

        if local_path:
            figure["image_url"] = local_path
            downloaded += 1
            print()

    print("=" * 70)
    print(f"SUCCESS: {downloaded}/{len(REAL_PORTRAITS)} portraits downloaded")
    print()

    # Save updated database
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print("[SAVED] Database updated with real portrait URLs")

if __name__ == "__main__":
    main()
