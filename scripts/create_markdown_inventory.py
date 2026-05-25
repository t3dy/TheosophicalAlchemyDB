#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create inventory of converted markdown files.
Documents structure, coverage, and figure/concept mentions.
"""

import json
from pathlib import Path
from collections import defaultdict

def create_inventory():
    """Generate markdown inventory document."""
    print("=" * 70)
    print("MARKDOWN SOURCES INVENTORY")
    print("=" * 70)
    print()

    sources_dir = Path("data/markdown_sources")
    if not sources_dir.exists():
        print("No markdown_sources directory found")
        return

    inventory = {
        'timestamp': str(Path(sources_dir).stat().st_mtime),
        'categories': {},
        'total_files': 0,
        'total_size_bytes': 0
    }

    # Walk directory structure
    for category_dir in sorted(sources_dir.iterdir()):
        if not category_dir.is_dir():
            continue

        category = category_dir.name
        inventory['categories'][category] = {
            'sources': {},
            'total_files': 0,
            'total_size': 0
        }

        print(f"\n{category}:")
        print("-" * 70)

        for source_dir in sorted(category_dir.iterdir()):
            if not source_dir.is_dir():
                continue

            source_name = source_dir.name
            markdown_files = list(source_dir.glob("*.md"))

            source_size = sum(f.stat().st_size for f in markdown_files)
            inventory['categories'][category]['sources'][source_name] = {
                'files': len(markdown_files),
                'size_bytes': source_size
            }
            inventory['categories'][category]['total_files'] += len(markdown_files)
            inventory['categories'][category]['total_size'] += source_size
            inventory['total_files'] += len(markdown_files)
            inventory['total_size_bytes'] += source_size

            print(f"  {source_name}")
            print(f"    Files: {len(markdown_files)}, Size: {source_size/1024:.1f} KB")

            # List first few files
            for i, md_file in enumerate(sorted(markdown_files)[:3]):
                print(f"      - {md_file.name}")
            if len(markdown_files) > 3:
                print(f"      ... and {len(markdown_files) - 3} more")

    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for category, data in inventory['categories'].items():
        print(f"{category}: {data['total_files']} files ({data['total_size']/1024/1024:.1f} MB)")

    print()
    print(f"Total: {inventory['total_files']} markdown files ({inventory['total_size_bytes']/1024/1024:.1f} MB)")

    # Save inventory
    with open("data/markdown_inventory.json", 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)

    print()
    print("Inventory saved to data/markdown_inventory.json")

if __name__ == "__main__":
    create_inventory()
