#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch portraits from PICRYL (Public Domain Image Archive) - more reliable than Wikimedia direct.
"""

import json
import os
import requests
import time

# PICRYL and Archive.org URLs (alternative to Wikimedia direct)
PORTRAIT_SOURCES = {
    "Jan Baptist van Helmont": "https://picryl.com/media/jan-baptista-van-helmont-line-engraving-1666-wellcome-v0002677-schnitt-8aa814",
    "Jacob Böhme": "https://picryl.com/topics/jakob+bohme",
    "Giordano Bruno": "https://picryl.com/media/bruno-giordano-e72150",
}

def fetch_picryl_image(figure_name, picryl_url):
    """Extract actual image URL from PICRYL page."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(picryl_url, timeout=10, headers=headers)
        resp.raise_for_status()

        # PICRYL pages contain image URLs in the HTML
        # Look for download link or image src
        if 'download' in resp.text.lower():
            # Extract download URL from page
            import re
            urls = re.findall(r'https?://[^\s"<>]+\.(?:jpg|png|jpeg)', resp.text)
            if urls:
                return urls[0]
        return None
    except Exception as e:
        print(f"Error fetching {figure_name} from PICRYL: {e}")
        return None

def download_from_url(url, figure_slug, output_dir="site/images/figures"):
    """Download image from URL."""
    try:
        if not url:
            return None

        os.makedirs(output_dir, exist_ok=True)

        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, timeout=15, allow_redirects=True, headers=headers)
        resp.raise_for_status()

        # Detect format
        ext = ".jpg"
        if 'png' in resp.headers.get("content-type", "").lower():
            ext = ".png"
        elif 'gif' in resp.headers.get("content-type", "").lower():
            ext = ".gif"

        filename = f"{figure_slug}{ext}"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "wb") as f:
            f.write(resp.content)

        print(f"  [OK] {filename} ({len(resp.content) / 1024:.1f} KB)")
        return f"images/figures/{filename}"
    except Exception as e:
        print(f"  [ERROR] {e}")
        return None

# Alternative: Use archive.org which often has portraits
ARCHIVE_ORG_URLS = {
    "Emmanuel Swedenborg": "https://archive.org/download/swedenborg_archive/Swedenborg_Portrait.jpg",
}

print("=" * 70)
print("PORTRAIT IMAGE INTEGRATION STATUS")
print("=" * 70)
print()
print("The goal: Download real public-domain portraits for 100 figures")
print()
print("STATUS: Technical blockers encountered")
print("- Wikimedia Commons: Rate limiting (429), URL resolution issues")
print("- API approaches: All failed (HTTPError, 404s, connectivity)")
print("- Direct downloads: Getting stuck/hanging")
print()
print("WORKAROUND STRATEGY:")
print("1. Use alternative sources (PICRYL, Archive.org)")
print("2. Focus on getting Tier 1 figures first (7 priority figures)")
print("3. Manual batch download process documented")
print()
print("NEXT STEPS:")
print("1. Manually source portraits from:")
print("   - Wikipedia (find portrait, download directly)")
print("   - PICRYL (public-domain-image-archive.org)")
print("   - Wellcome Collection (wellcomecollection.org)")
print("2. Save to site/images/figures/[slug].jpg")
print("3. Update database with image_url field")
print("4. Deploy to GitHub Pages")
print()
print("=" * 70)
