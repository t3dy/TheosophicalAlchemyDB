#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a test portrait image to verify image display in the portal.
"""

import json
from PIL import Image, ImageDraw, ImageFont

def create_test_portrait(figure_slug, figure_name, output_path="site/images/figures"):
    """Create a simple test portrait image."""
    # Create image with scholarly colors
    img = Image.new('RGB', (300, 400), color=(245, 240, 232))  # parchment
    draw = ImageDraw.Draw(img)

    # Draw a simple portrait-like circle (head)
    head_color = (139, 69, 19)  # burnt sienna
    draw.ellipse([75, 60, 225, 210], fill=head_color, outline=(210, 180, 140), width=2)

    # Draw text
    try:
        # Try to use a serif font
        font = ImageFont.truetype("C:\\Windows\\Fonts\\GeorgiaB.ttf", 16)
        font_small = ImageFont.truetype("C:\\Windows\\Fonts\\georgia.ttf", 12)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
        font_small = font

    # Name
    draw.text((150, 230), figure_name, fill=(44, 36, 24), font=font, anchor="mm")

    # Attribution
    draw.text((150, 300), "Public Domain Portrait", fill=(107, 93, 77), font=font_small, anchor="mm")
    draw.text((150, 325), "[Test Image]", fill=(212, 165, 116), font=font_small, anchor="mm")

    # Save
    filepath = f"{output_path}/{figure_slug}.png"
    img.save(filepath)
    print(f"Created test portrait: {filepath}")
    return f"images/figures/{figure_slug}.png"

def main():
    import os
    os.makedirs("site/images/figures", exist_ok=True)

    # Create test portraits for a few figures
    test_figures = [
        ("john-dee", "John Dee"),
        ("paracelsus", "Paracelsus"),
        ("robert-fludd", "Robert Fludd"),
    ]

    db_path = "data/prototype_data.json"
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    for slug, name in test_figures:
        image_url = create_test_portrait(slug, name)

        # Update database
        for figure in db["figures"]:
            if figure.get("slug") == slug:
                figure["image_url"] = image_url
                print(f"Updated database: {name} -> {image_url}")
                break

    # Save database
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print("\nTest portraits created and database updated.")

if __name__ == "__main__":
    main()
