#!/usr/bin/env python3
"""Apply all emblem patch files to the main data file safely (sequential merge)."""
import json
import os
import glob

DATA_FILE = '/home/user/TheosophicalAlchemyDB/data/prototype_data.json'
SCRIPTS_DIR = '/home/user/TheosophicalAlchemyDB/scripts'

# Load main data
with open(DATA_FILE) as f:
    data = json.load(f)

# Build lookup by string and int ID
emblems_by_str_id = {str(e['id']): e for e in data['emblems']}

# Load and apply all patch files
patch_files = sorted(glob.glob(os.path.join(SCRIPTS_DIR, 'emblem_patch_*.json')))
print(f"Found {len(patch_files)} patch files: {[os.path.basename(p) for p in patch_files]}")

total_updated = 0
for patch_file in patch_files:
    with open(patch_file) as f:
        patch_data = json.load(f)

    # Handle both formats: direct dict OR metadata wrapper with 'essays' key
    if 'essays' in patch_data and isinstance(patch_data['essays'], dict):
        patches = patch_data['essays']
        print(f"  {os.path.basename(patch_file)}: using 'essays' wrapper ({len(patches)} entries)")
    else:
        # Filter out non-essay metadata keys
        patches = {k: v for k, v in patch_data.items()
                   if isinstance(v, str) and len(v) > 100}
        print(f"  {os.path.basename(patch_file)}: direct dict ({len(patches)} entries)")

    updated_in_batch = 0
    for emblem_id_str, essay in patches.items():
        # Try string key first, then integer key
        emblem = emblems_by_str_id.get(emblem_id_str)
        if emblem is None and emblem_id_str.isdigit():
            emblem = emblems_by_str_id.get(int(emblem_id_str))

        if emblem is not None:
            old_essay = emblem.get('essay', '') or ''
            if old_essay.startswith('[') or len(old_essay) < 500:
                emblem['essay'] = essay
                updated_in_batch += 1
            else:
                pass  # Already has a real essay, skip
        else:
            print(f"    WARNING: Emblem ID '{emblem_id_str}' not found in data")

    print(f"    Updated {updated_in_batch} emblems from this patch")
    total_updated += updated_in_batch

# Save
with open(DATA_FILE, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nTotal emblems updated from patches: {total_updated}")

# Final audit
stubs = [e['id'] for e in data['emblems'] if (e.get('essay', '') or '').startswith('[')]
short = [e['id'] for e in data['emblems']
         if not (e.get('essay', '') or '').startswith('[') and len(e.get('essay', '') or '') < 1000]
print(f"Remaining placeholder stubs: {len(stubs)}")
if stubs:
    print(f"  IDs: {stubs[:20]}")
print(f"Remaining short (<1000 chars): {len(short)}")
if short:
    print(f"  IDs: {short[:20]}")
print("Done.")
