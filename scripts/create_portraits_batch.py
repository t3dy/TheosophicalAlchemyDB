#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create portrait images for key historical figures.
Fast, direct approach - generate images immediately.
"""

from PIL import Image, ImageDraw, ImageFont
import json
import os

os.makedirs("site/images/figures", exist_ok=True)

# 7 key figures - Tier 1 priority
FIGURES = [
    ("john-dee", "John Dee", 1527, 1608),
    ("paracelsus", "Paracelsus", 1493, 1541),
    ("robert-fludd", "Robert Fludd", 1574, 1637),
    ("jacob-bohme", "Jacob Bohme", 1575, 1624),
    ("michael-maier", "Michael Maier", 1568, 1622),
    ("emmanuel-swedenborg", "Emanuel Swedenborg", 1688, 1772),
    ("jan-baptist-van-helmont", "Jan Baptist van Helmont", 1580, 1644),
]

print("=" * 70)
print("CREATING PORTRAIT IMAGES FOR KEY FIGURES")
print("=" * 70)

for slug, name, birth, death in FIGURES:
    # Create 300x400 image
    img = Image.new('RGB', (300, 400), color=(245, 240, 232))
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("C:\\Windows\\Fonts\\GeorgiaB.ttf", 16)
        text_font = ImageFont.truetype("C:\\Windows\\Fonts\\Georgia.ttf", 12)
    except:
        title_font = ImageFont.load_default()
        text_font = title_font

    # Draw head (burnt sienna circle)
    head_color = (139, 69, 19)
    draw.ellipse([50, 40, 250, 240], fill=head_color, outline=(212, 165, 116), width=3)

    # Draw name banner
    draw.rectangle([60, 250, 240, 280], outline=(212, 165, 116), width=2)

    # Text
    draw.text((150, 300), name, fill=(44, 36, 24), font=title_font, anchor="mm")
    draw.text((150, 330), f"{birth}-{death}", fill=(107, 93, 77), font=text_font, anchor="mm")

    # Save JPEG
    filepath = f"site/images/figures/{slug}.jpg"
    img.save(filepath, 'JPEG', quality=90)

    size_kb = os.path.getsize(filepath) / 1024
    print(f"  {slug:30s} {size_kb:6.1f} KB")

print()

# Now update database
db_path = "data/prototype_data.json"
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

figures = db.get("figures", [])
updated = 0

print("UPDATING DATABASE WITH IMAGE URLS")
print("=" * 70)

# Map database names to slugs
slug_map = {f[1]: f[0] for f in FIGURES}

for figure in figures:
    name = figure.get("name", "")
    if name in slug_map:
        slug = slug_map[name]
        figure["image_url"] = f"images/figures/{slug}.jpg"
        updated += 1
        print(f"  {name:35s} -> images/figures/{slug}.jpg")

print()
print(f"Updated {updated}/{len(FIGURES)} figures in database")

# Save database
with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print()
print("=" * 70)
print("DONE: 7 figures now have portrait images")
print("=" * 70)
