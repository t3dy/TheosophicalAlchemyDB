# Markdown Sources Directory

This directory contains systematically converted PDFs from our scholarly corpus, chunked by chapter/section and cross-indexed with our main database of figures and concepts.

## Structure

```
markdown_sources/
├── Rosicrucian/              # 43 Rosicrucian PDFs (233 markdown files)
│   ├── [source_name]/
│   │   ├── 01_[chapter_title].md
│   │   ├── 02_[chapter_title].md
│   │   └── ...
│   └── [more sources]
│
├── Alchemy/                  # 55 Alchemy PDFs (389+ markdown files)
│   ├── [source_name]/
│   │   └── [chapter files]
│   └── [more sources]
│
├── Western_Esotericism/      # 54 Western Esotericism PDFs (in progress)
│   ├── [source_name]/
│   │   └── [chapter files]
│   └── [more sources]
│
└── Emblem_Studies/           # 5 Emblem Studies PDFs (in progress)
    ├── [source_name]/
    │   └── [chapter files]
    └── [more sources]
```

## Metadata

Each markdown file includes YAML frontmatter with:
- `source`: Original PDF title
- `source_category`: Rosicrucian/Alchemy/Western_Esotericism/Emblem_Studies
- `author`: Extracted from PDF metadata
- `total_pages`: Page count of source PDF
- `section`: Chapter/section title
- `section_number`: Sequential numbering
- `figures_mentioned`: Figures from our database found in this section
- `concepts_mentioned`: Concepts from our database found in this section

## Example Frontmatter

```yaml
---
source: The Rosicrucian Enlightenment
source_category: Rosicrucian
author: Frances A. Yates
total_pages: 454
section: Chapter 4 The Rosicrucian Enlightenment
section_number: 1
figures_mentioned: John Dee, Giordano Bruno, Marsilio Ficino
concepts_mentioned: Hermetic Philosophy, Rosy Cross, Enlightenment
---
```

## Citation Index

Two JSON files cross-reference the markdown sources:

1. **`data/markdown_citations.json`** (per-category)
   - Figure citations for Rosicrucian PDFs
   - Concept citations for Rosicrucian PDFs
   - Useful for checking individual category coverage

2. **`data/master_citation_index.json`** (all categories)
   - All figures found across all 4 categories
   - All concepts found across all 4 categories
   - Summary statistics (mention counts, top figures/concepts)
   - Category-wise breakdown

## Statistics (Updated 2026-05-25)

| Metric | Value |
|--------|-------|
| Total PDFs Converted | 98+ / 131 |
| Markdown Files Created | 622+ |
| Total Markdown Size | ~25 MB |
| Unique Figures Cited | 70+ |
| Unique Concepts Cited | 46+ |
| Total Mentions | 2,815+ |
| Categories Complete | Rosicrucian, Alchemy |
| Categories In Progress | Western Esotericism, Emblem Studies |

## Top Cited Figures

1. Paracelsus (150 mentions)
2. John Dee (98 mentions)
3. Robert Fludd (89 mentions)
4. Hermes Trismegistus (79 mentions)
5. Roger Bacon (78 mentions)

## Top Cited Concepts

1. Enlightenment (164 mentions)
2. Correspondence (96 mentions)
3. Initiation (83 mentions)
4. Distillation (75 mentions)
5. Dissolution (69 mentions)

## Usage

### Finding Mentions of a Specific Figure

```bash
# Search all markdown files for mentions of Robert Fludd
grep -r "Robert Fludd" markdown_sources/ | head -20
```

### Extracting Concepts from a Category

```bash
# Find all concept citations in Alchemy PDFs
grep "concepts_mentioned:" markdown_sources/Alchemy/*/*.md | sort | uniq
```

### Analyzing a Specific Source

```bash
# List all sections of a particular work
ls -la markdown_sources/Rosicrucian/the_rosicrucian_enlightenment/
```

## Database Integration

The main database (`data/prototype_data.json`) has been updated with:
- `markdown_sources_found`: List of source PDFs mentioning this figure/concept
- `source_citations_count`: Number of mentions in converted PDFs

Example:
```json
{
  "name": "John Dee",
  "markdown_sources_found": [
    "33326_SP_BOG_FM_00i-xii",
    "A Christian Rosenkreutz Anthology",
    "Alchemy, Jung, and Remedios Varo"
  ],
  "source_citations_count": 98
}
```

## Processing Scripts

- `scripts/convert_pdfs_to_markdown.py` — Initial conversion (Rosicrucian)
- `scripts/convert_all_pdfs_batch.py` — Batch conversion (Alchemy + remaining)
- `scripts/create_markdown_inventory.py` — Directory inventory
- `scripts/ingest_markdown_sources.py` — Extract citations (single category)
- `scripts/aggregate_all_citations.py` — Master citation index (all categories)
- `scripts/update_entries_with_sources.py` — Update database with references

## Quality Notes

- All text preserved with page markers (`[Page N]`)
- UTF-8 encoding throughout
- Corrupt PDFs skipped with warnings
- No data loss — all sections preserved even if extraction imperfect
- Section detection automatic; manual review available for edge cases

## Next Steps

1. Complete Western Esotericism and Emblem Studies conversion
2. Run master aggregation on full corpus
3. Identify and verify false positives (name collisions)
4. Create portal UI to display source citations
5. Add excerpt views linking sections to figure/concept pages

---

**Last Updated:** 2026-05-25  
**Format Version:** 1.0  
**Status:** IN PROGRESS

