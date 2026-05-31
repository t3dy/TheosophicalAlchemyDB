#!/usr/bin/env python3
"""
Batch 3 biography updates — 36 remaining short figures.
Loads data from the three data modules, applies updates to prototype_data.json,
and reports before/after character counts.
"""

import json
import sys
import os

# Add scripts dir to path so we can import the data modules
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

# Import the three data modules
from update_bios_batch3_data1 import UPDATES as UPDATES1
from update_bios_batch3_data2 import UPDATES as UPDATES2
from update_bios_batch3_data3 import UPDATES as UPDATES3
from update_bios_batch3_data4 import UPDATES as UPDATES4

# Merge all updates
ALL_UPDATES = {}
ALL_UPDATES.update(UPDATES1)
ALL_UPDATES.update(UPDATES2)
ALL_UPDATES.update(UPDATES3)
ALL_UPDATES.update(UPDATES4)

DATA_PATH = os.path.join(os.path.dirname(script_dir), "data", "prototype_data.json")

def main():
    print(f"Loading data from {DATA_PATH}")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    figures = data.get("figures", [])
    id_to_figure = {fig["id"]: fig for fig in figures}

    print(f"\nTotal updates to apply: {len(ALL_UPDATES)}")
    print(f"Total figures in database: {len(figures)}\n")
    print(f"{'ID':<6} {'Name':<50} {'Before':>8} {'After':>8} {'Delta':>8}")
    print("-" * 84)

    total_before = 0
    total_after = 0
    updated_count = 0

    for fig_id, update in sorted(ALL_UPDATES.items()):
        if fig_id not in id_to_figure:
            print(f"  WARNING: id={fig_id} not found in database!")
            continue

        fig = id_to_figure[fig_id]
        before_len = len(fig.get("essay", ""))

        # Apply updates
        if "essay" in update:
            fig["essay"] = update["essay"]
        if "key_works" in update:
            fig["key_works"] = update["key_works"]

        after_len = len(fig.get("essay", ""))
        delta = after_len - before_len
        total_before += before_len
        total_after += after_len
        updated_count += 1

        name = fig.get("name", "Unknown")[:48]
        print(f"  {fig_id:<6} {name:<50} {before_len:>8,} {after_len:>8,} {delta:>+8,}")

    print("-" * 84)
    print(f"  {'TOTAL':<56} {total_before:>8,} {total_after:>8,} {total_after - total_before:>+8,}")
    print(f"\nUpdated {updated_count} figures.")

    # Save back
    print(f"\nSaving to {DATA_PATH}...")
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Saved successfully.")

    # Verify JSON validity
    print("\nVerifying JSON validity...")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        verify = json.load(f)
    print(f"JSON valid. Figures count: {len(verify.get('figures', []))}")

if __name__ == "__main__":
    main()
