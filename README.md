# Rosicrucianism & Theosophical Alchemy Knowledge Portal

**[🔮 Live Portal → https://t3dy.github.io/TheosophicalAlchemyDB/](https://t3dy.github.io/TheosophicalAlchemyDB/)**

A concept-first, scholarly encyclopedia of Rosicrucian and theosophical-alchemical traditions from the 16th–18th centuries, created for scholars, practitioners, and interested readers.

## Vision

Navigate historical Rosicrucian and alchemical ideas, figures, texts, and emblematic traditions through **concept-first organization**, **relational browsing**, and **rigorous scholarly apparatus**.

## Quick Start

**New to the project?** Read in this order:
1. `PROMPTS.md` — Canonical vision (5 min)
2. `CLAUDE.md` — Project overview (10 min)
3. `DOCUMENTAIRTRAFFICCONTROL.md` — Navigation guide (reference as needed)

**Want to work on the project?** Start with your task:
- Adding a concept → `docs/STYLEGUIDE.md`
- Writing a biography → `docs/STYLEGUIDE.md`
- Cataloging an emblem → `IMPLEMENTATION_PLAN.md`
- Understanding the schema → `docs/ONTOLOGY.md`

## Core Numbers

- **Concepts:** 40–60 (Rosicrucian, alchemical, hermetic, theurgical)
- **Historical Figures:** 30–40 (Andreae, Dee, Fludd, Ashmole, Swedenborg, etc.)
- **Texts:** 25–35 (Rosicrucian Manifestos, alchemy treatises, emblem books)
- **Emblems:** 20–40 (across 8–12 emblem books)
- **Dictionary:** 100+ technical terms
- **Essays:** 12–18 thematic
- **Scholars:** 15–20 modern researchers

## Architecture

```
SQLite (source of truth)
    ↓
Python (deterministic extraction)
    ↓
LLM (synthesis, always marked DRAFT)
    ↓
Human Review
    ↓
Static HTML/CSS/JS (GitHub Pages)
```

## Key Design Principles

1. **Concept-first:** Navigate by idea, not chronology or author
2. **Historiographical rigor:** Actor/Analyst distinction; debates presented fairly
3. **Dual audience:** Serve scholars and practitioners without conflation
4. **Emblems as entities:** Each emblem is researched, linked, visualized
5. **Deterministic + LLM:** Python validates; LLM synthesizes; humans review
6. **Academic voice:** Rigorous, accessible, no mysticism
7. **Relational:** Every entity links to ≥3 others

## Corpus

**131 source PDFs:**
- **E:\pdf\Rosicrucian** — 53 PDFs (primary + secondary scholarship)
- **E:\pdf\alchemy** — 78 PDFs (transmutation, laboratory, hermetic, spiritual alchemy)
- **E:\pdf\emblem studies** — Cross-disciplinary emblem scholarship

Quality: ~30% GOOD (OCR'd), ~35% PARTIAL, ~35% SCANNED (OCR queued)

## Project Phases (10 weeks target)

| Phase | Timeline | Deliverable |
|-------|----------|-------------|
| **0** | Week 1 | PDF triage, concept extraction, seed data design |
| **1** | Week 1–2 | SQLite schema, seed data ingestion |
| **2** | Week 2–4 | Figure biographies, text summaries (LLM-assisted) |
| **3** | Week 4–5 | Emblem cataloging, image sourcing |
| **4** | Week 5–6 | Concept essays, dictionary (100+ terms) |
| **5** | Week 6–7 | Thematic essays, relationship enrichment |
| **6** | Week 7–8 | Frontend build, static site generation |
| **7** | Week 8–9 | Styling, dark scholarly design |
| **8** | Week 9–10 | Testing, deployment to GitHub Pages |

## Website Sections (Planned)

- **Home** — Emblem gallery, conceptual navigation, intro
- **Concepts** — 40–60 encyclopedia pages (nigredo, albedo, rubedo, theosis, etc.)
- **Figures** — 30–40 biographies (genealogy links, influence chains)
- **Texts** — 25–35 primary source summaries (with quotations)
- **Emblems** — Emblem book catalog + individual emblem pages (Maier, Micrelius, Mutus Liber, etc.)
- **Dictionary** — 100+ technical terms with cross-links
- **Timeline** — 1550–1800+ chronology, major events
- **Essays** — 12–18 thematic essays (historiographical debates, cross-cutting problems)
- **Scholars** — 15–20 modern researcher profiles
- **Bibliography** — Curated sources, relevance badges
- **About** — Methodology, provenance, AI disclosure, academic standards

## Design System

**Dark scholarly aesthetic** (burnt sienna + parchment):

```css
Background: #f5f0e8 (warm parchment)
Text: #2c2418 (dark brown)
Accent: #8b4513 (burnt sienna)
Accent-light: #d4a574 (tan/gold)
```

## File Structure

```
C:\Dev\Rosicrucianism/
├── CLAUDE.md                      # Project entry point
├── PROMPTS.md                     # Canonical vision
├── DOCUMENTAIRTRAFFICCONTROL.md   # Navigation guide
├── PHASESTATUS.md                 # Session log
├── IMPLEMENTATION_PLAN.md         # Technical strategy
├── README.md                      # This file
├── docs/
│   ├── SYSTEM.md                  # Architecture
│   ├── ONTOLOGY.md                # Schema
│   ├── PIPELINE.md                # Scripts
│   ├── INTERFACE.md               # Page templates
│   ├── STYLEGUIDE.md              # Voice & standards
│   └── ROADMAP.md                 # Phase tracking
├── data/
│   ├── rosicrucian_seed.json      # Seed data
│   ├── concepts_seed.json
│   ├── figures_seed.json
│   ├── texts_seed.json
│   ├── emblem_books_seed.json
│   ├── emblems_seed.json
│   ├── dictionary_seed.json
│   └── emblem_manifest.json
├── scripts/
│   ├── init_db.py
│   ├── seed_*.py
│   ├── write_*.py
│   └── build_site.py
├── site/                          # Generated static site
│   ├── index.html
│   ├── concepts/
│   ├── figures/
│   ├── texts/
│   ├── emblems/
│   ├── dictionary/
│   ├── essays/
│   ├── style.css
│   └── script.js
├── staging/                       # LLM outputs before merge
├── db/
│   └── rosicrucianism.db          # SQLite database
└── .claude/
    └── settings.local.json
```

## For Scholars

This portal is **rigorous and peer-friendly**:
- Historiographical debates presented fairly
- All claims source-trackable
- Academic voice and vocabulary
- Rich apparatus (genealogy maps, concept networks, full bibliography)
- AI-generated content marked and reviewable

## For Practitioners

This portal is **accessible and relational**:
- Concepts explained without jargon
- Easy navigation (concept → figures → texts → emblems)
- Practical interpretations
- Emblem scholarship at your fingertips
- No false authority or speculative content

## Critical Principles

✓ **Concept-first navigation** (not text-first, not author-first)  
✓ **Historiographical rigor** (actor ≠ analyst; debates explicit)  
✓ **Dual-audience architecture** (scholars + practitioners, no conflation)  
✓ **Emblems as entities** (not illustrations; researched, linked, visualized)  
✓ **Deterministic + LLM** (Python validates; LLM synthesizes; humans review)  
✓ **Academic voice** (clear, rigorous, no mysticism)  
✓ **Relational browsing** (every page links to ≥3 others)  

## Success Criteria (Phase 8)

- [ ] Live at GitHub Pages
- [ ] 40–60 concept pages
- [ ] 30–40 figure biographies
- [ ] 25–35 text summaries
- [ ] 20–40 emblem entries
- [ ] 100+ dictionary terms
- [ ] 12–18 essays
- [ ] <5% content DRAFT
- [ ] Zero historiographical errors
- [ ] Full-text search functional
- [ ] Complete documentation

## Getting Help

- **New to the project?** → Read `PROMPTS.md`
- **Looking for a specific file?** → Check `DOCUMENTAIRTRAFFICCONTROL.md`
- **Current project status?** → Check `PHASESTATUS.md`
- **Want to understand architecture?** → Read `docs/SYSTEM.md`
- **Need writing guidance?** → Read `docs/STYLEGUIDE.md`

## Contributing

All work follows the **Session Discipline** in `PHASESTATUS.md`:

1. Start session: Read `PROMPTS.md` + `PHASESTATUS.md`
2. Work on assigned phase
3. End session: Update `PHASESTATUS.md` with progress, blockers, next steps

## Academic Disclosure

This knowledge portal uses **AI assistance** for content generation:
- LLM-generated content is marked `review_status='DRAFT'` until human review
- All sources are tracked: `source_method`, `confidence`, `review_status`
- Generated content is clearly labeled in the frontend

## License & Attribution

*[To be determined when portal goes live]*

**Project Lead:** t3dy  
**Created:** 2026-05-24  
**Status:** Phase 0 (Project Setup)  
**Next Release Target:** 2026-08-16
