# Claude Code Instructions — TheosophicalAlchemyDB

## Project Summary

**TheosophicalAlchemyDB** — A concept-first knowledge portal on Rosicrucian and theosophical-alchemical traditions (16th–18th century). Built with 206+ entities (63 figures, 60 concepts, 83 texts, 30+ emblems), interactive Leaflet.js map, card-based gallery interface, dark scholarly design (burnt sienna + parchment), GitHub Pages deployment at https://t3dy.github.io/TheosophicalAlchemyDB/

**Phase 1 Status:** ✅ COMPLETE (Figures, concepts, texts, initial emblem gallery)  
**Phase 2 Status:** 🚀 IN PROGRESS (Emblem expansion, concept-emblem mapping, scholarly apparatus enrichment)

**Vision:** Navigate Rosicrucian and alchemical ideas through concept-first organization, relational browsing, and scholarly rigor. All entities geographic-mapped; historiographical debates presented fairly; gender awareness throughout; embodied knowledge emphasized.

## Critical Documents (Read in This Order)

**First Session?** Start here:
1. `QUICK_START.md` — 5-minute orientation (what is this, how does it work, key files)
2. `CONVERSATION_REQUIREMENTS_HARVEST.md` — What the user wants (read entire document)
3. `STYLEGUIDE_UPDATED.md` — Writing standards for all entries
4. `ONTOLOGY_UPDATED.md` — Data structure specification

**Continuing Session?** Start here:
1. `RESUMPTION_PROMPT.md` — Quick re-orientation for this session
2. `PHASE_2_HANDOVER.md` — What to work on (detailed roadmap with 7 workstreams)
3. `PHASESTATUS.md` — What's been done, what's blocked, what's next

**Deep Dives:**
- `AGENTIC_CONTEXT_ENGINEERING.md` — Best practices for multi-session LLM projects
- `EMBLEM_SYSTEM_PLAN.md` — Detailed emblem sourcing strategy (400+ sources identified)
- `VICKERS_CRITIQUE_INGESTION.md` — Historiographical methodology documentation

## Current State (Phase 1 Complete)

**Entities Created:**
- **Figures:** 63 (Phase 1 target: 40–50; exceeded with Zuber scholarship focus)
- **Concepts:** 60 (Phase 1 target: 40–50; complete with dual-level analysis)
- **Texts:** 83 (Phase 1 target: 25–35; expanded with scholarly sources)
- **Emblems:** 30 (Phase 0.5 completion; expanding to 100+ in Phase 2)
- **Geographic Coordinates:** 106+ mapped locations
- **Essay Words:** 80,000+ (all entries meet 300+ word minimum)
- **Scholarly Sources Cited:** 500+

**Phase 2 Targets (In Progress):**
- **Emblems:** 30 → 100+ (Cramer 40, Maier 51, Stolcius 40-60 focus)
- **Concept-Emblem Links:** 60 concepts × 2-3 emblems each = 120+ links
- **Figure-Emblem Attribution:** All figures connected to emblem creation/influence
- **Scholarly Apparatus:** Direct quotes, page citations, historiographical debates
- **Emblem Images Sourced:** 40-50 (PDF extraction + public-domain)
- **Emblem Gallery UI:** Full card/modal/search/filter/map integration

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

## Critical Principles (Discovered in Phase 1)

1. **Historiographical Rigor** — Present scholarly debates fairly (Yates/Vickers model), not false certainty
2. **Concept-First Organization** — Users navigate by philosophical principle, not chronology
3. **Emblems as Philosophical Instruments** — Not illustrations; first-class entities with full scholarly apparatus (Szulakowska framework)
4. **Relational Browsing** — Every entity links to ≥3 others; enables serendipitous discovery
5. **Geographic Grounding** — All entities mapped to real places (lat/lng coordinates)
6. **Gender Awareness** — Explicit note of women's participation and obstacles in transmission
7. **Embodied Knowledge** — Ground concepts in actual practice/operations, not abstract theory (Zuber emphasis)
8. **Transmission Genealogy** — How ideas spread across cultures/centuries; show lineages explicitly
9. **Academic Voice** — Learned but not pedantic; rigorous but not defensive; respectful but not reverent
10. **Live Portal Throughout** — Portal remains functional during all development phases (Friday deployments)

## Phase Timeline (Actual Progress)

**Phase 0: Project Setup & Prototype** ✅ COMPLETE (2026-05-24 to 2026-05-25)
- Created project structure, documentation, CLAUDE.md, PROMPTS.md
- Built interactive prototype with 40 entries per section
- Implemented Leaflet.js map, card gallery, modal essays
- Published to GitHub Pages

**Phase 1: Seed Data & Emblem Foundation** ✅ COMPLETE (2026-05-25)
- Added 23 new figures (40 → 63 total), 10 new concepts (50 → 60), 9 new texts (74 → 83)
- Integrated Brian Vickers scholarship and historiographical rigor
- Created 30 emblem entries with art-historical analysis
- Updated STYLEGUIDE_UPDATED.md with Szulakowska/Zuber/De Jong frameworks
- Updated ONTOLOGY_UPDATED.md with emblem-as-entity specification
- Live deployment with all features tested

**Phase 2: Emblem Expansion & Scholarly Enrichment** 🚀 IN PROGRESS (2026-05-25 to 2026-06-21)
- **Workstream 1:** Emblem sourcing (30 → 100+) with image acquisition
- **Workstream 2:** Concept-emblem comprehensive mapping
- **Workstream 3:** Figure-emblem genealogy
- **Workstream 4:** Scholarly apparatus enrichment
- **Workstream 5:** Data ontology refinement
- **Workstream 6:** Emblem gallery UI/UX implementation
- **Workstream 7:** PDF corpus systematic ingestion (131 sources)
- **See PHASE_2_HANDOVER.md for detailed roadmap**

**Phase 3 (Planned):** SQLite backend, full-text search, advanced features

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
1. **First session?** Read `QUICK_START.md` (5 min), then `CONVERSATION_REQUIREMENTS_HARVEST.md` (full context)
2. **Continuing session?** Read `RESUMPTION_PROMPT.md`, then `PHASE_2_HANDOVER.md`
3. Always check `PHASESTATUS.md` for current phase status and blockers
4. Read `STYLEGUIDE_UPDATED.md` if writing any entries
5. Read `ONTOLOGY_UPDATED.md` if modifying data structure

### During Work
- Test on live site after each major change (no dark launches)
- Commit frequently (ideally daily) with descriptive messages
- Update `PHASESTATUS.md` when status changes
- If schema evolves, update `ONTOLOGY_UPDATED.md` immediately
- If user provides feedback, document in PHASESTATUS.md "Notes" section
- If you discover a pattern, update `STYLEGUIDE_UPDATED.md` or `AGENTIC_CONTEXT_ENGINEERING.md`

### At End of Session
- Update `PHASESTATUS.md` with:
  - Phase status (what changed?)
  - Completed items (with checkmarks)
  - Blockers (if any)
  - Next steps (specific, actionable)
  - Session log entry (duration, tasks, blockers, notes)
- Commit all changes with clear message
- Update `CONVERSATION_REQUIREMENTS_HARVEST.md` if new learnings

## Data Integrity Rules

- Never overwrite data with `review_status='VERIFIED'` — log discrepancies instead
- LLM-extracted data starts as `review_status='DRAFT'`, `confidence='MEDIUM'`
- Deterministic data starts as `confidence='HIGH'`
- All AI-generated content marked with source_method, review_status, confidence
- Academic claims must cite source (PDF page, text section, scholar reference)

## File Structure

```
C:\Dev\TheosophicalAlchemyDB/
├── CLAUDE.md                              # This file — project entry point
├── PROMPTS.md                             # Canonical vision statement
├── QUICK_START.md                         # ✨ 5-min orientation guide
├── RESUMPTION_PROMPT.md                   # ✨ Copy-paste for new sessions
├── PHASESTATUS.md                         # Session discipline log (update after each session)
├── CONVERSATION_REQUIREMENTS_HARVEST.md   # ✨ Master requirements (read first!)
├── AGENTIC_CONTEXT_ENGINEERING.md         # ✨ Best practices for LLM projects
├── PHASE_2_HANDOVER.md                    # ✨ Detailed Phase 2 roadmap (7 workstreams)
├── README.md                              # Public-facing summary
├── .gitignore
├── .github/workflows/deploy.yml
├── .claude/
│   └── launch.json                        # Preview server config
├── scripts/
│   ├── build_site.py                      # Main: rebuild portal from data
│   ├── phase_1_expansion.py               # Phase 1: batch entry creation
│   ├── add_vickers.py                     # Session 4: Vickers integration
│   ├── add_emblems_and_figures.py         # Session 4: Agrippa/Vaughan/emblems
│   ├── add_more_emblems.py                # Session 4: 15 more emblems
│   ├── add_final_emblem.py                # Session 4: final emblem
│   ├── ingest_comprehensive_emblems.py    # Phase 2: emblem sourcing framework
│   └── [Phase 2 scripts to be created]    # extract_emblem_images, enrich_apparatus, etc.
├── docs/
│   ├── STYLEGUIDE_UPDATED.md              # ✨ Writing standards (Phase 1 version)
│   ├── ONTOLOGY_UPDATED.md                # ✨ Data schema specification (Phase 1 version)
│   ├── EMBLEM_SYSTEM_PLAN.md              # ✨ Emblem sourcing strategy (detailed)
│   ├── VICKERS_CRITIQUE_INGESTION.md      # Phase 4: Historiographical rigor doc
│   ├── DOCUMENTAIRTRAFFICCONTROL.md       # LLM routing guide (may be stale)
│   └── archive/                           # Old planning docs
├── data/
│   └── prototype_data.json                # ✨ LIVE DATABASE (206+ entities)
├── staging/
│   └── emblem_images/                     # Phase 2: extracted emblem images
├── site/                                  # Generated static site
│   ├── index.html                         # Portal homepage (regenerated by build_site.py)
│   ├── app.js                             # Frontend logic (cards, modals, map)
│   ├── style.css                          # Design system (burnt sienna + parchment)
│   └── images/                            # Emblem images go here
├── docs/                                  # GitHub Pages source (synced to site/)
└── SESSION_5_COMPREHENSIVE_SUMMARY.md     # Context from Sessions 4-5 (reference)
```

**Key:** ✨ = Critical files for orientation and execution

## Phase 2 Success Criteria (Target: 2026-06-21)

- [ ] 100+ emblem entries created (up from 30)
- [ ] 50+ emblem images sourced (extracted from PDFs or public-domain)
- [ ] 60 concepts × 2-3 emblems each = 120+ concept-emblem links
- [ ] All figures (63) linked to emblem creation/influence
- [ ] Scholarly apparatus enriched (direct quotes, page citations, debates)
- [ ] Data ontology refined (emblem-book entity, authenticity field)
- [ ] Emblem gallery UI/UX functional (cards, modals, search, filters, map)
- [ ] Portal remains live and functional throughout (Friday deployments)
- [ ] All writing meets STYLEGUIDE_UPDATED.md standards
- [ ] GitHub deployment successful at https://t3dy.github.io/TheosophicalAlchemyDB/

**See PHASE_2_HANDOVER.md for detailed workstream breakdown, timeline, and metrics.**

---

## How to Contribute / Continue

1. **New to the project?**
   - Read `QUICK_START.md` (5 minutes)
   - Read `CONVERSATION_REQUIREMENTS_HARVEST.md` (full context)
   - Read `STYLEGUIDE_UPDATED.md` (standards)

2. **Resuming from prior session?**
   - Read `RESUMPTION_PROMPT.md`
   - Read `PHASE_2_HANDOVER.md` (current workstreams)
   - Check `PHASESTATUS.md` (what's done, what's blocked)

3. **Questions about approach?**
   - See `AGENTIC_CONTEXT_ENGINEERING.md` (how we work)
   - See `EMBLEM_SYSTEM_PLAN.md` (emblem sourcing)
   - See `VICKERS_CRITIQUE_INGESTION.md` (historiographical methodology)

---

**Project Owner:** t3dy  
**Last Updated:** 2026-05-25 (Phase 1 Complete, Phase 2 Handover)  
**Current Phase:** Phase 2 (Emblem Expansion & Scholarly Enrichment)  
**Next Phase:** Phase 3 (SQLite Backend, Full-Text Search)
