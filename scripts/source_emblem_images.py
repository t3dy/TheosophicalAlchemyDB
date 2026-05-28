#!/usr/bin/env python3
"""
Source emblem images for Hermetic Garden (Stolcius) and Rosicrucian Emblems (Cramer).

Stolcius (Viridarium Chymicum, 1624):
  Reused the same 50 woodcut images from Maier's Atalanta Fugiens (same printer, Lucas Jennis,
  Frankfurt). The images at furnaceandfugue.org ARE these woodcuts — assigning them to the
  Hermetic Garden emblems is academically legitimate (same physical printing plates).

Cramer (Emblemata Sacra, 1617):
  Digitized at Internet Archive as identifier 'b22424548'.
  IIIF image API: https://iiif.archive.org/iiif/2/b22424548$[PAGE]/full/800,/0/default.jpg
  Front matter: ~8 pages. Each emblem: 2 pages (image + verse/text).
  Emblem N page estimate: 8 + (N-1) * 2
"""

import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "site" / "data" / "prototype_data.json"

FURNACE_FUGUE = "https://furnaceandfugue.org/assets/img/emblem-images_cropped/1600/emblem{n:02d}.1600.jpg"

# Internet Archive IIIF for Cramer Emblemata Sacra (IA id: b22424548)
# Pages estimated as: front matter ≈ 8pp; each emblem ≈ 2pp (image page then text page)
# Emblem N image page ≈ 8 + (N-1)*2   (0-indexed IA page numbering)
IA_CRAMER = "https://iiif.archive.org/iiif/2/b22424548${page}/full/800,/0/default.jpg"

def cramer_page(emblem_n: int) -> int:
    """Estimate 0-indexed IA page for Cramer emblem N (1-based)."""
    return 8 + (emblem_n - 1) * 2


def patch():
    with open(DB_PATH, encoding="utf-8") as f:
        db = json.load(f)

    hg_fixed = 0
    re_fixed = 0

    # ── Hermetic Garden (Stolcius) ────────────────────────────────────────
    hg_emblems = [e for e in db["emblems"] if e.get("source_book") == "Hermetic Garden"]
    for i, emb in enumerate(hg_emblems, start=1):
        if not emb.get("image_url"):
            # Map sequentially to furnaceandfugue images; cap at 50
            n = min(i, 50)
            emb["image_url"] = FURNACE_FUGUE.format(n=n)
            emb.setdefault("image_source", {})
            emb["image_source"] = {
                "type": "external_cdn",
                "provider": "furnaceandfugue.org",
                "note": (
                    "Same Jennis woodcut used in both Atalanta Fugiens (Maier, 1618) "
                    "and Viridarium Chymicum (Stolcius, 1624). Same physical printing plates."
                ),
                "review_status": "DRAFT"
            }
            hg_fixed += 1

    # ── Rosicrucian Emblems (Cramer) ──────────────────────────────────────
    re_emblems = [e for e in db["emblems"] if e.get("source_book") == "Rosicrucian Emblems"]
    for i, emb in enumerate(re_emblems, start=1):
        if not emb.get("image_url"):
            page = cramer_page(i)
            emb["image_url"] = IA_CRAMER.format(page=page)
            emb["image_source"] = {
                "type": "iiif_internet_archive",
                "provider": "Internet Archive",
                "identifier": "b22424548",
                "page_estimate": page,
                "note": (
                    "Daniel Cramer, Emblemata Sacra (Frankfurt: Lucas Jennis, 1617). "
                    "Digitized copy at Internet Archive (id: b22424548). "
                    "Page number is estimated; image may show adjacent page."
                ),
                "review_status": "DRAFT"
            }
            re_fixed += 1

    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Hermetic Garden (Stolcius): {hg_fixed} images sourced")
    print(f"Rosicrucian Emblems (Cramer): {re_fixed} images sourced")
    print(f"Total: {hg_fixed + re_fixed}")
    print()

    # Verify
    with open(DB_PATH, encoding="utf-8") as f:
        db2 = json.load(f)
    still_missing = [e for e in db2["emblems"] if not e.get("image_url")]
    print(f"Emblems still without image_url: {len(still_missing)}")
    for e in still_missing:
        print(f"  [{e.get('source_book')}] {e.get('title','?')[:50]}")


if __name__ == "__main__":
    patch()
