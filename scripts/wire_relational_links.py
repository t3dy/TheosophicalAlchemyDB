#!/usr/bin/env python3
"""
Wire relational links: scan figure/text essays for concept name mentions,
add concept IDs to figures and texts that are missing them.
"""
import json, re
from pathlib import Path

DB = Path("site/data/prototype_data.json")

def find_mentions(text, concepts):
    """Return list of concept IDs whose name appears in text."""
    if not text:
        return []
    hits = []
    for c in concepts:
        # Match whole word (allow hyphens inside the name)
        pattern = r'\b' + re.escape(c['name']) + r'\b'
        if re.search(pattern, text, re.IGNORECASE):
            hits.append(c['id'])
    return hits

def merge_ids(existing, new_ids):
    combined = list(existing or [])
    for i in new_ids:
        if i not in combined:
            combined.append(i)
    return combined

with open(DB, encoding='utf-8') as f:
    db = json.load(f)

concepts = db['concepts']

figures_updated = 0
texts_updated = 0

# --- Figures ---
for fig in db['figures']:
    essay = (fig.get('essay') or '') + ' ' + (fig.get('summary') or '')
    found = find_mentions(essay, concepts)
    before = len(fig.get('concepts') or [])
    fig['concepts'] = merge_ids(fig.get('concepts'), found)
    if len(fig['concepts']) > before:
        figures_updated += 1

# --- Texts ---
for text in db['texts']:
    essay = (text.get('essay') or '') + ' ' + (text.get('summary') or '')
    found = find_mentions(essay, concepts)
    before = len(text.get('concepts') or [])
    text['concepts'] = merge_ids(text.get('concepts'), found)
    if len(text['concepts']) > before:
        texts_updated += 1

# --- Concepts: wire related_concepts by mention ---
concept_updated = 0
for c in concepts:
    essay = (c.get('essay') or '') + ' ' + (c.get('summary') or '')
    found = find_mentions(essay, concepts)
    # Exclude self
    found = [i for i in found if i != c['id']]
    before = len(c.get('related_concepts') or [])
    c['related_concepts'] = merge_ids(c.get('related_concepts'), found)
    if len(c['related_concepts']) > before:
        concept_updated += 1

with open(DB, 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"Figures with new concept links: {figures_updated}")
print(f"Texts with new concept links:   {texts_updated}")
print(f"Concepts with new related:      {concept_updated}")

# Stats
fig_with = sum(1 for f in db['figures'] if f.get('concepts'))
con_with = sum(1 for c in concepts if c.get('related_concepts'))
txt_with = sum(1 for t in db['texts'] if t.get('concepts'))
print(f"\nFigures with concepts: {fig_with}/{len(db['figures'])}")
print(f"Concepts with related: {con_with}/{len(concepts)}")
print(f"Texts with concepts:   {txt_with}/{len(db['texts'])}")
