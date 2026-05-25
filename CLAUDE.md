# Claude Code Instructions — Rosicrucianism & Theosophical Alchemy Portal

## Project Summary

**Rosicrucianism & Theosophical Alchemy Knowledge Portal** — A concept-first encyclopedia of Rosicrucian and theosophical-alchemical traditions from the 16th–18th centuries, written in academic voice for scholars, practitioners, and interested readers. Architecture replicates AtalantaClaudiens: SQLite source of truth, Python static site generator, vanilla HTML/CSS/JS, GitHub Pages deployment at `t3dy/rosicrucianism-alchemy-portal`.

**Vision:** Navigate historical Rosicrucian and alchemical ideas, figures, texts, and emblematic traditions through relational browsing, concept-first organization, and rich scholarly apparatus.

## Document Routing

**Read `DOCUMENTAIRTRAFFICCONTROL.md` when you need to find the right file.** It routes you to the correct document for any task (schema work, emblem work, extraction, debugging, planning) and flags what's stale or unbuilt.

## Quick Reference

| Document | Purpose |
|----------|---------|
| `DOCUMENTAIRTRAFFICCONTROL.md` | **Start here** — routes you to the right doc for any task |
| `docs/SYSTEM.md` | Architecture, data flow, provenance model |
| `docs/ONTOLOGY.md` | Database schema, entity relationships |
| `docs/PIPELINE.md` | Script execution order, stage dependencies |
| `docs/INTERFACE.md` | Website sections, page templates, navigation |
| `docs/ROADMAP.md` | Phase status: BUILT / READY / BLOCKED / PLANNED |
| `docs/STYLEGUIDE.md` | Voice, tone, academic standards, essay templates |
| `PHASESTATUS.md` | Session discipline log — update at end of every session |
| `PROMPTS.md` | Canonical vision statement (read first every session) |

## Core Numbers (Target State)

- **Concepts:** 40–60 (Rosicrucianism, alchemical processes, theurgical practices, hermetic principles)
- **Historical Figures:** 30–40 (Andreae, Dee, Fludd, Ashmole, Cagliostro, Swedenborg, etc.)
- **Texts:** 25–35 (Rosicrucian Manifestos, Key of Solomon variants, emblem books, alchemy treatises)
- **Emblems & Emblem Books:** 8–12 (Maier, Micrelius, Mutus Liber, etc.)
- **Scholar Profiles:** 15–20
- **Essays:** 12–18 thematic essays
- **Database size:** ~200–250 core rows, ~1,500+ relationship rows, ~200K+ essay words

## Corpus

**131 source PDFs** across three directories:
- **E:\pdf\Rosicrucian** — 53 PDFs (core Rosicrucian primary sources and scholarship)
- **E:\pdf\alchemy** — 78 PDFs (including 12 in spiritual alchemy subfolder; covers transmutation, laboratory alchemy, hermetic alchemy, iatrochemistry)
- **E:\pdf\emblem studies** — Cross-disciplinary emblem scholarship, direct relation to alchemical/Rosicrucian emblematic traditions

Quality distribution: GOOD 30–40%, PARTIAL 30–40%, SCANNED 20–30% (OCR queued).

## Architecture Pattern

**Stack:** SQLite → Python (deterministic) → LLM (synthesis) → Static HTML/CSS/JS → GitHub Pages

**Three Content Layers:**
1. Structured data (deterministic, seed data)
2. Entity essays (encyclopedia entries, LLM-assisted + review)
3. Thematic essays (cross-cutting problems, LLM-assisted + review)

## Core Tables (Planned)

- `figures` — Biographical entries (30–40 historical figures)
- `concepts` — Rosicrucian/alchemical ideas (40–60 concepts)
- `texts` — Primary sources, treatises, manifestos (25–35 texts)
- `emblems` — Individual emblem descriptions (20–40 emblems across emblem books)
- `emblem_books` — Emblem collections (8–12 books)
- `scholars` — Modern scholarship (15–20 scholars)
- `concept_relationships` — Concept-to-concept links
- `figure_influences` — Genealogy, mutual influences
- `text_concepts` — Which texts develop which concepts
- `dictionary` — Technical terminology (80–120 terms)
- `timeline` — Chronology from Reformation through Enlightenment
- `sources` — Source authorities and traditions (Hermetic corpus, Kabbalah, etc.)

## Critical Principles

1. **Deterministic First** — Extract structure, dates, relationships from PDF text deterministically
2. **LLM Synthesis Second** — Agents write encyclopedia content, always marked DRAFT
3. **Human Review Always** — No content ships REVIEWED until human reads it
4. **Historiographical Rigor** — Actor/Analyst distinction (what Rosicrucians called themselves vs. modern scholarly categories)
5. **Academic Voice** — No mysticism, no channeled content; rigorous historical-critical method
6. **Emblems as Entities** — Each emblem is a first-class entity with image + provenance + scholarly apparatus
7. **Dual Audience** — Scholars and practitioners; serve both without conflating categories

## Phase Timeline (10 weeks target)

- **Phase 0** (Week 1): PDF triage + markdown conversion (131 PDFs → searchable text)
- **Phase 1** (Week 1–2): Schema + seed data (concepts, figures, texts, emblem manifests)
- **Phase 2** (Week 2–4): Figure biographies + text summaries (40 bios, 30 text summaries)
- **Phase 3** (Week 4–5): Emblem cataloging + image sourcing (20–40 emblems, all sourced)
- **Phase 4** (Week 5–6): Concept essays + dictionary (50 concept pages, 100+ terms)
- **Phase 5** (Week 6–7): Relationship enrichment + thematic essays (genealogy, cross-cutting problems)
- **Phase 6** (Week 7–8): Frontend build + navigation (static site generation)
- **Phase 7** (Week 8–9): Styling + dark scholarly design
- **Phase 8** (Week 9–10): Testing + deployment to GitHub Pages

## Website Sections (Planned)

| Section | Purpose |
|---------|---------|
| **Home** | Gallery of emblems, project intro, navigate-by-concept interface |
| **Concepts** | 40–60 concept encyclopedia pages (Rosicrucian ideas, alchemical processes) |
| **Figures** | 30–40 biographical entries with scholar profiles |
| **Texts** | 25–35 primary source summaries with quotations |
| **Emblems** | Emblem book catalog (Maier, Micrelius, Mutus Liber, etc.); individual emblem pages |
| **Dictionary** | 100+ technical terms (albedo, nigredo, putrefaction, hieros gamos, etc.) |
| **Timeline** | 1550–1800+ chronology, major events, publication dates |
| **Essays** | 12–18 thematic essays (Rosicrucianism and Science, Gender in Alchemy, etc.) |
| **Scholars** | Profiles of modern researchers in the field |
| **Bibliography** | Curated sources with relevance badges |
| **About** | Methodology, provenance, AI disclosure, academic standards |

## Design System

**Dark scholarly aesthetic** inspired by AtalantaClaudiens (parchment + burnt sienna, high contrast):

```css
--bg: #f5f0e8;           /* Warm parchment */
--bg-card: #fff;
--text: #2c2418;          /* Dark brown */
--text-muted: #6b5d4d;
--accent: #8b4513;        /* Burnt sienna (alchemical rubedo) */
--accent-light: #d4a574;  /* Tan/gold highlight */
--header-bg: #2c2418;
--header-text: #f5f0e8;
--border: #d4a574;
```

## Critical Design Decisions

1. **Concept-first navigation** — Browse by philosophical/alchemical idea, not just authors
2. **Emblems as standalone entities** — Each emblem plate gets full scholarly apparatus (source, provenance, interpretations)
3. **Dual-audience voice** — Academic rigor + accessibility for practitioners (no conflation)
4. **Deterministic + LLM split** — Python validates structure; LLM synthesizes complex ideas
5. **Relational browsing** — Every entity links to ≥3 others; sidebar previews
6. **Genealogy explicit** — `figure_influences` table maps philosophical/Rosicrucian transmission
7. **No speculative content** — All claims source-trackable; draft status visible

## Operating Rules

### Before Starting Work
- Check `PHASESTATUS.md` for current phase, prerequisites, blockers
- Check `docs/ROADMAP.md` for what's BUILT vs READY vs BLOCKED
- Read `docs/ONTOLOGY.md` if touching the database

### During Work
- Mark tasks in progress in PHASESTATUS.md
- Don't skip phases — each phase outputs feed the next
- If schema changes, update `docs/ONTOLOGY.md` immediately
- If pipeline changes, update `docs/PIPELINE.md` immediately

### At End of Session
- Update `PHASESTATUS.md` with: phase status, what changed, next steps, blockers

## Data Integrity Rules

- Never overwrite data with `review_status='VERIFIED'` — log discrepancies instead
- LLM-extracted data starts as `review_status='DRAFT'`, `confidence='MEDIUM'`
- Deterministic data starts as `confidence='HIGH'`
- All AI-generated content marked with source_method, review_status, confidence
- Academic claims must cite source (PDF page, text section, scholar reference)

## File Structure

```
C:\Dev\Rosicrucianism/
├── CLAUDE.md                      # This file — project entry point
├── DOCUMENTAIRTRAFFICCONTROL.md   # LLM routing guide
├── PROMPTS.md                     # Canonical vision (read first)
├── PHASESTATUS.md                 # Session discipline log
├── README.md                      # Public-facing summary
├── CORPUS_MANIFEST.md             # 131 PDFs with triage status
├── .gitignore
├── .github/workflows/deploy.yml
├── .claude/
│   ├── launch.json
│   └── settings.local.json
├── db/
│   └── rosicrucianism.db          # SQLite database (generated)
├── scripts/
│   ├── init_db.py                 # Stage 1: Schema
│   ├── seed_concepts.py           # Stage 1: Seed concepts
│   ├── seed_figures.py            # Stage 1: Seed figures
│   ├── seed_texts.py              # Stage 1: Seed texts
│   ├── seed_emblems.py            # Stage 1: Emblem manifest
│   ├── seed_dictionary.py         # Stage 1: Terms
│   ├── extract_pdf_corpus.py      # Stage 2: Parse PDFs
│   ├── analyze_concepts.py        # Stage 2: Concept extraction
│   ├── link_entities.py           # Stage 3: Build relationships
│   ├── generate_essays.py         # Stage 3: Thematic essays
│   └── build_site.py              # Stage 4: Static site generation
├── docs/
│   ├── SYSTEM.md                  # Architecture + provenance model
│   ├── ONTOLOGY.md                # Database schema catalog
│   ├── PIPELINE.md                # Script execution order
│   ├── INTERFACE.md               # Website sections + templates
│   ├── ROADMAP.md                 # Phase status tracking
│   ├── STYLEGUIDE.md              # Academic voice, templates
│   └── archive/                   # Past planning artifacts
├── data/
│   ├── emblem_manifest.json       # Canonical emblem index
│   ├── rosicrucian_seed.json      # Core seed data
│   └── concepts_seed.json         # Concept definitions
├── staging/                       # Swarm agent outputs
├── site/                          # Generated static site
│   ├── index.html
│   ├── concepts/
│   ├── figures/
│   ├── texts/
│   ├── emblems/
│   ├── dictionary/
│   ├── essays/
│   └── images/emblems/
└── source_pdfs/                   # Symlinks or references to E:\pdf\*
    ├── rosicrucian/
    ├── alchemy/
    └── emblem_studies/
```

## Success Criteria (Phase 8 completion)

- [ ] Live at GitHub Pages (t3dy/rosicrucianism-alchemy-portal)
- [ ] 40–60 concept encyclopedia pages
- [ ] 30–40 figure biographies
- [ ] 25–35 text summaries
- [ ] 20–40 emblem entries with images and scholarship
- [ ] 100+ dictionary terms
- [ ] 12–18 thematic essays
- [ ] 15–20 scholar profiles
- [ ] Full-text search functional
- [ ] <5% content DRAFT (rest REVIEWED)
- [ ] Zero historiographical errors
- [ ] Complete provenance tracking
- [ ] Academic disclosure visible

## Key Research Questions (to Guide Phase 0 Triage)

1. What are the 40–60 core concepts in Rosicrucianism and theosophical alchemy?
2. Who are the 30–40 most influential figures (historical + scholarly)?
3. Which 25–35 texts are canonical?
4. How many emblem books and individual emblems should we catalog?
5. What 8–10 emblem books are most important? (Maier, Micrelius, Mutus Liber, Khunrath, etc.)
6. What is the genealogy of influence? (Renaissance hermetic philosophy → Rosicrucian movements → 18th-century alchemy/Swedenborgianism)
7. What historiographical debates define the field? (Real vs. legendary orders, Swedenborg's authority, alchemy as chemistry vs. metaphor)

---

**Created:** 2026-05-24  
**Status:** Phase 0 (Project Setup)  
**Next:** Read PROMPTS.md, review DOCUMENTAIRTRAFFICCONTROL.md, begin Phase 0 PDF triage
