# Agrippa 1510 Extraction Pipeline

A reproducible, **deterministic-first** workflow for extracting structured
scholarly metadata about the **1510 Würzburg draft** of Heinrich Cornelius
Agrippa's *De occulta philosophia libri tres*, from **Vittoria Perrone
Compagni's critical edition** (Brill).

The target manuscript is **MS Würzburg, Universitätsbibliothek M.ch.q.50**.

## What this does (and does not) produce

**Produces:** structured metadata — variant analysis, chapter correspondence
(1510 ↔ 1533), apparatus entries citing the Würzburg witness, thematic
classification, page/line references, and analytical reports.

**Does NOT produce:** a continuous transcription of Perrone Compagni's
copyrighted edited text. Raw excerpts are truncated to the minimum needed for
verification (≈120–280 chars), and reports paraphrase rather than reproduce.

## Copyright & fair use

- The edition PDF is treated as **local source material** and is `.gitignore`d
  (`data/raw/*.pdf`) — it is never committed.
- Derived full text (`data/ocr/`), chunks, and the SQLite DB are also ignored.
- Only short, fair-use excerpts for verification are retained in tables.

## Install

```bash
pip install -r requirements.txt
# Optional OCR fallback (only if the edition is scanned):
#   apt-get install tesseract-ocr tesseract-ocr-lat tesseract-ocr-grc tesseract-ocr-heb
```

## Place the edition

Copy Perrone Compagni's edition PDF into `data/raw/`, **or** pass `--pdf` to
each script. (On the author's machine it lives at roughly
`E:\pdf\Renaissance magic\agrippa\...`.)

## Run the pipeline

| Phase | Script | Output |
|------:|--------|--------|
| 1 | `00_inspect_pdf.py` | `outputs/reports/pdf_inspection.md` (page count, embedded-text check, **siglum hunt**, comparison-table & apparatus locations) |
| 2 | `01_extract_text.py` | `data/ocr/pages.jsonl`, `data/ocr/full_text.txt`, `logs/extraction_warnings.md` |
| 3 | `02_detect_structure.py` | `data/indices/edition_structure.json` |
| 4 | `03_extract_table_of_comparison.py` | `outputs/tables/table_of_comparison.{csv,json}` + summary |
| 5 | `04_extract_apparatus.py` | `outputs/tables/wurzburg_apparatus_entries.{csv,json}` + method report |
| 6 | `06_build_passage_database.py` | `db/agrippa_1510.sqlite` |
| 7 | `05_chunk_for_llm.py` | `data/chunks/*.json` (prioritised, schema-bound prompts) |
| 9 | `07_generate_reports.py` | `outputs/reports/*.md`, `outputs/tables/chapter_status_matrix.csv` |

```bash
cd agrippa_1510_extraction
python scripts/00_inspect_pdf.py --pdf data/raw/EDITION.pdf
python scripts/01_extract_text.py --pdf data/raw/EDITION.pdf      # add --ocr auto if scanned
python scripts/02_detect_structure.py
# --- read outputs/reports/pdf_inspection.md, confirm the Würzburg siglum ---
python scripts/03_extract_table_of_comparison.py --pages 18,19,20 # use pages from the report
python scripts/04_extract_apparatus.py --siglum W                 # use the CONFIRMED siglum
python scripts/06_build_passage_database.py
python scripts/05_chunk_for_llm.py
python scripts/07_generate_reports.py
```

## Critical workflow rule: confirm the siglum

**Do not assume the Würzburg siglum is `W`.** Phase 1 hunts for the shelfmark
(`M.ch.q.50`) and Latin place names (`Wirceburgensis`, `Herbipolitanus`) and
reports candidate siglum assignments from the *conspectus siglorum*. Confirm it,
then pass `--siglum <X>` to Phase 5 (or set `WUERZBURG_SIGLUM` in
`04_extract_apparatus.py`). Until confirmed, Phase 5 runs in **discovery mode**
(matches anchors, not a guessed letter).

## Status of each phase

- **Phases 1–3, 6:** fully implemented (deterministic).
- **Phases 4, 5, 7, 9:** runnable scaffolds whose row/segment parsing is
  intentionally conservative until the *real* column layout and siglum are
  read off the edition (heuristics are flagged low-confidence and queued for
  manual review).

## Data integrity / validation (Phase 10 intent)

- Every `passage_assessment` must carry ≥1 evidence reference.
- `absent_from_1510` requires comparison-table or explicit editorial evidence,
  else it must be marked `inferred`.
- Apparatus entries always preserve a page reference.
- LLM outputs must be valid JSON (schema in `05_chunk_for_llm.py`).
- No report contains long verbatim copyrighted passages.

## Manual review queue

Low-confidence rows, discovery-mode apparatus hits, and ambiguous chapter
mappings are surfaced in `outputs/reports/uncertainties_and_manual_review.md`
and via the `confidence` columns in the CSV/JSON tables.
