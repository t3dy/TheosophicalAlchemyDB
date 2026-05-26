#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find which cards still need images."""

import json
from pathlib import Path

DB_PATH = Path("data/prototype_data.json")

with open(DB_PATH, encoding='utf-8') as f:
    db = json.load(f)

print("=== FIGURES WITHOUT IMAGES ===\n")
missing_figs = [f['name'] for f in db['figures'] if not f.get('image_url')]
print(f"Count: {len(missing_figs)}\n")
for name in sorted(missing_figs)[:20]:
    try:
        print(f"  {name}")
    except:
        pass

print("\n=== CONCEPTS WITHOUT IMAGES ===\n")
missing_concepts = [c['name'] for c in db['concepts'] if not c.get('image_url')]
print(f"Count: {len(missing_concepts)}\n")
for name in sorted(missing_concepts)[:20]:
    try:
        print(f"  {name}")
    except:
        pass

print("\n=== TEXTS WITHOUT IMAGES ===\n")
missing_texts = [t['title'] for t in db['texts'] if not t.get('image_url')]
print(f"Count: {len(missing_texts)}\n")
for title in sorted(missing_texts)[:20]:
    try:
        print(f"  {title}")
    except:
        pass
