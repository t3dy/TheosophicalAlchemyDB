#!/usr/bin/env python3
"""
Final consolidation script. Run after ALL background agents complete.
Applies emblem patches and restores any text/concept changes potentially
overwritten by concurrent agent writes.
"""
import subprocess
import sys
import json

SCRIPTS_DIR = '/home/user/TheosophicalAlchemyDB/scripts'
DATA_FILE = '/home/user/TheosophicalAlchemyDB/data/prototype_data.json'


def run(script, label):
    print(f"\n=== Running: {label} ===")
    result = subprocess.run([sys.executable, f'{SCRIPTS_DIR}/{script}'],
                            capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}")
    return result.returncode == 0


def audit():
    with open(DATA_FILE) as f:
        data = json.load(f)

    stubs = sum(1 for e in data.get('emblems', []) if (e.get('essay', '') or '').startswith('['))
    empty = sum(1 for e in data.get('emblems', []) if not (e.get('essay', '') or '').startswith('[') and len(e.get('essay', '') or '') < 100)
    short_texts = sum(1 for t in data.get('texts', []) if len(t.get('essay', '') or '') < 1500 and not str(t.get('id', '')) == '20')
    short_concepts = sum(1 for c in data.get('concepts', []) if len(c.get('essay', '') or '') < 1500)
    coords = sum(1 for c in data.get('concepts', []) if c.get('lat'))

    print(f"\n=== AUDIT SUMMARY ===")
    print(f"Emblem stubs: {stubs}")
    print(f"Emblem empty: {empty}")
    print(f"Short texts (<1500 chars, excl ID 20): {short_texts}")
    print(f"Short concepts (<1500 chars): {short_concepts}")
    print(f"Concepts with coordinates: {coords}/67")


# Step 1: Apply emblem patches (for 178-190, string IDs)
run('apply_emblem_patches.py', 'Apply emblem patches (178-190, Maier string IDs)')

# Step 2: Re-run text expansion scripts (idempotent — restores any overwritten text changes)
run('expand_short_texts.py', 'Restore text expansions (43-50)')
run('expand_text_emblems.py', 'Restore text-array emblem expansions (63-83)')

# Step 3: Run group 2 text expansions (if agent created a script)
import os
if os.path.exists(f'{SCRIPTS_DIR}/expand_texts_group2.py'):
    run('expand_texts_group2.py', 'Apply text group 2 expansions (52, 53, 84-92, Paracelsus)')
else:
    print("\nNOTE: expand_texts_group2.py not found — text group 2 agent may still be running")

# Step 4: Restore concept essay expansions
run('expand_short_concepts.py', 'Restore concept essay expansions')

# Step 5: Restore concept coordinates
run('restore_concept_coords.py', 'Restore concept coordinates')

# Audit
audit()

print("\n=== Consolidation complete ===")
