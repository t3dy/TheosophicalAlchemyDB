#!/usr/bin/env python3
"""
Merge all patch files into prototype_data.json.
Applies: scholars, debates, reading_paths, confessional_affiliations, dictionary.
"""
import json
from pathlib import Path

ROOT  = Path(__file__).parent.parent
DATA  = ROOT / "data" / "prototype_data.json"
SCRI  = ROOT / "scripts"

with open(DATA, encoding='utf-8') as f:
    db = json.load(f)

# ── 1. Scholars ───────────────────────────────────────────────────────────────
patch_file = SCRI / "scholars_major_patch.json"
if patch_file.exists():
    with open(patch_file, encoding='utf-8') as f:
        new_scholars = json.load(f)
    existing_ids = {s['id'] for s in db.get('scholars', [])}
    added = 0
    for s in new_scholars:
        if s['id'] not in existing_ids:
            db.setdefault('scholars', []).append(s)
            existing_ids.add(s['id'])
            added += 1
        else:
            # Update in place (richer data wins)
            for i, es in enumerate(db['scholars']):
                if es['id'] == s['id']:
                    db['scholars'][i] = s
                    break
    print(f"[scholars] {added} added, {len(new_scholars)-added} updated → {len(db['scholars'])} total")

# ── 2. Debates ────────────────────────────────────────────────────────────────
patch_file = SCRI / "debates_patch.json"
if patch_file.exists():
    with open(patch_file, encoding='utf-8') as f:
        raw = json.load(f)
    debates = raw.get('debates', raw) if isinstance(raw, dict) else raw
    db['debates'] = debates
    print(f"[debates] {len(debates)} entries loaded")

# ── 3. Reading paths ──────────────────────────────────────────────────────────
patch_file = SCRI / "reading_paths_patch.json"
if patch_file.exists():
    with open(patch_file, encoding='utf-8') as f:
        raw = json.load(f)
    paths = raw.get('reading_paths', raw) if isinstance(raw, dict) else raw
    db['reading_paths'] = paths
    print(f"[reading_paths] {len(paths)} paths loaded")

# ── 4. Confessional affiliations ──────────────────────────────────────────────
patch_file = SCRI / "confessional_affiliations_patch.json"
if patch_file.exists():
    with open(patch_file, encoding='utf-8') as f:
        raw = json.load(f)
    affiliations = raw.get('confessional_affiliations', raw) if isinstance(raw, dict) else raw
    updated = 0
    for fig in db.get('figures', []):
        fid = str(fig['id'])
        if fid in affiliations:
            fig['confessional_affiliation'] = affiliations[fid].get('confessional_affiliation', '')
            fig['secondary_affiliation']    = affiliations[fid].get('secondary_affiliation', '')
            updated += 1
    print(f"[confessional] {updated} figures updated with confessional data")

# ── 5. Glossary (dictionary) ─────────────────────────────────────────────────
patch_file = SCRI / "glossary_patch.json"
if patch_file.exists():
    with open(patch_file, encoding='utf-8') as f:
        raw = json.load(f)
    glossary = raw.get('dictionary', raw) if isinstance(raw, dict) else raw
    db['dictionary'] = glossary
    print(f"[dictionary] {len(glossary)} terms loaded")
else:
    print("[dictionary] No glossary_patch.json found — skipping")

# ── Save ──────────────────────────────────────────────────────────────────────
with open(DATA, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)
print(f"\nSaved {DATA}")
print(f"  figures:       {len(db.get('figures', []))}")
print(f"  concepts:      {len(db.get('concepts', []))}")
print(f"  texts:         {len(db.get('texts', []))}")
print(f"  emblems:       {len(db.get('emblems', []))}")
print(f"  scholars:      {len(db.get('scholars', []))}")
print(f"  debates:       {len(db.get('debates', []))}")
print(f"  reading_paths: {len(db.get('reading_paths', []))}")
print(f"  dictionary:    {len(db.get('dictionary', []))}")
