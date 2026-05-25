# Comprehensive Requirements Harvest
## All User Desires from Conversation (Session 1–5)

**Document Purpose:** Complete audit of all explicit and implicit requirements from the conversation. This document ensures Phase 2 and beyond incorporate every user intent.

**Last Updated:** 2026-05-25 (Session 5)

---

## Session 1: Initial Vision & Scope

### Explicit Requirements
- [ ] Create knowledge portal on Rosicrucian and theosophical-alchemical traditions (16th–18th century)
- [ ] Focus research on scholars: Szulakowska, Akerman, Yates, Godwin, Churton, Zuber
- [ ] 40+ entries per section (figures, concepts, texts) initially
- [ ] Convert PDFs to markdown, ingest into database
- [ ] Create "index card" style summaries that expand to full essays
- [ ] Interactive map of Europe with figure/text location plotting
- [ ] Beautiful, effective digital humanities resource
- [ ] GitHub Pages deployment

### Implicit Requirements (Inferred from Context)
- Portal should serve both scholars and practitioners (with clear distinction)
- Relational browsing architecture (entities cross-reference one another)
- Academic voice: rigorous, not mystical
- Historiographical rigor emphasized
- Concept-first organization

---

## Session 2: Prototype & Expansion

### Explicit Requirements
- [ ] Prototype with 40 entries per section (figures, concepts, texts)
- [ ] Card-based gallery interface
- [ ] Click-to-expand modal essays
- [ ] Leaflet.js interactive map with:
  - Red markers for figures
  - Blue markers for text locations
  - Gold markers for learning centers
  - Hover tooltips with index card info
- [ ] Responsive dark scholarly design (burnt sienna + parchment)
- [ ] Navigation tabs (Figures, Concepts, Texts, Map, About)
- [ ] Geospatial coordinates for all entries

### Implicit Requirements
- All entities must have geographic coordinates
- Map should enable discovery (user can find texts/figures by location)
- Design should evoke scholarly/esoteric aesthetic without mysticism
- Portal statistics visible on home page

---

## Session 3: Expansion & Verification

### Explicit Requirements
- [ ] Add 10 more entries to each category (50 total per section)
- [ ] Focus on Mike Zuber scholarship (spiritual alchemy, Böhme–Atwood arc)
- [ ] Ingest everything of interest from Zuber's book
- [ ] Expand to Phase 1: PDF corpus conversion, database ingestion, site rebuild
- [ ] Commit and build, verify everything wired correctly
- [ ] Deploy to GitHub with project named to match repo (TheosophicalAlchemyDB)
- [ ] Maintain working portal throughout

### Implicit Requirements
- Zuber's framework should influence concept definitions
- Spiritual alchemy emphasis (not just material operations)
- Women figures should be represented
- Transmission genealogy important

---

## Session 4: Emblem System & Vickers Integration

### Explicit Requirements
- [ ] Ingest Brian Vickers critique of Frances Yates
- [ ] Create Vickers scholar profile
- [ ] Add "Frances Yates and the Writing of History" as scholarly text
- [ ] Enhance Yates entry with critical historiographical context
- [ ] Convert emblem images and descriptions to gallery
- [ ] Create 30+ emblem summary cards with detailed writeups
- [ ] Examples: Daniel Cramer Rosicrucian Emblems, Paul M. Allen anthology
- [ ] Add Agrippa and Thomas Vaughan entries
- [ ] Plot all figures/texts on interactive map

### User Clarifications on Emblems
- [ ] Emblem images can come from PDFs if web sources unavailable
- [ ] Agrippa and Vaughan material in project folder and E:\pdf\Rosicrucian
- [ ] ALL extant Rosicrucian emblems from 16th–18th century should be ingested
- [ ] Emblems as new entity type, cross-referenced and hyperlinked
- [ ] Relationally browsable (concept ↔ emblem ↔ figure ↔ text)
- [ ] Update data ontology for emblem entity type
- [ ] Use best judgment to triangulate unclear information; mark for attention

### Implicit Requirements
- Emblems are not illustrations but philosophical instruments
- Art-historical analysis (Szulakowska model) required for emblems
- Comprehensive emblem sourcing (400+ identified)
- Visual epistemology emphasis
- Emblem-concept mapping essential

---

## Session 5: Phase 1 Completion & Phase 2 Planning

### Explicit Requirements
- [ ] Phase 1: Add 10 more entries to each category
- [ ] Ensure all writing meets established requirements
- [ ] Update data ontology based on learned themes/figures
- [ ] Update style guides based on scholarly values/interests
- [ ] Write comprehensive essays for figures/concepts/texts
- [ ] Ensure map plots work for all entries
- [ ] Phase 2: Detailed research + database integration
- [ ] Update ontology again (refined understanding)
- [ ] Bake ALL conversation desires into system files/scope/style guides
- [ ] Use context engineering best practices for agentic environments
- [ ] Create handover document with next steps
- [ ] Create brief prompt for new session resumption

### Style & Scholarly Values Required
- Historiographical rigor (Yates/Vickers model: present scholarly debate)
- Art-historical analysis (Szulakowska framework)
- Source documentation (De Jong model: track genealogy)
- Gender attentiveness (acknowledge women's participation/obstacles)
- Transmission tracking (how ideas spread across cultures/centuries)
- Embodied knowledge emphasis (Zuber: practice matters)
- Concept-first organization (users navigate by idea, not chronology)
- Integration of Islamic, medieval, Renaissance, modern traditions
- No mystification; academic voice throughout
- Multiple perspectives when scholars disagree

### Implicit Phase 2 Requirements
- Emblem gallery expansion (100+ target)
- Emblem UI/UX (search, filter, modal viewer)
- Emblem image sourcing from PDFs and public-domain
- Scholarly apparatus enrichment (direct quotes, citations)
- Concept-emblem mapping for all 60 concepts
- Figure-emblem creation and influence attribution
- PDF corpus systematic ingestion (131 total sources)
- SQLite backend development
- Full-text search functionality

---

## Consolidation: Master Requirements List

### Core Portal Features (MVP Already Achieved)
- ✅ 63 figures with geographic coordinates and scholarly essays
- ✅ 60 concepts with definitions and relational linking
- ✅ 83 texts (primary + secondary) with summaries and analysis
- ✅ Interactive Leaflet.js map with 106+ plotted locations
- ✅ Card-based gallery interface with modal essays
- ✅ Responsive dark scholarly design (burnt sienna + parchment)
- ✅ Navigation structure (Figures, Concepts, Texts, Map, About)
- ✅ GitHub Pages deployment, live and functional
- ✅ Portal statistics dashboard

### Phase 2 Requirements (In Progress)
- [ ] Emblem gallery expansion (30 → 100+)
- [ ] Emblem image sourcing and integration
- [ ] Emblem UI/UX (search, filter, modal, map plotting)
- [ ] Scholarly apparatus enrichment across all entities
- [ ] Concept-emblem comprehensive mapping
- [ ] Figure-emblem genealogy
- [ ] PDF corpus ingestion (Phase 2.5–3)
- [ ] SQLite backend (Phase 3)
- [ ] Full-text search (Phase 3)

### Critical Success Factors (From All Sessions)
1. **Historiographical Honesty:** Present scholarship accurately, acknowledge debates
2. **Art-Historical Rigor:** Emblems and visual elements analyzed systematically
3. **Gender Awareness:** Women's participation and obstacles explicitly noted
4. **Transmission Genealogy:** How ideas spread tracked through sources
5. **Embodied Practice:** Theory grounded in actual practice/operations
6. **Concept-First:** Portal organized by philosophical principle, not chronology
7. **Relational Browsing:** Every entity links to ≥3 others
8. **Academic Voice:** Clear, learned, not mystical or condescending
9. **Geographic Grounding:** All entities mapped to real places
10. **Scholarly Integration:** Works by Szulakowska, Zuber, De Jong, Godwin, Yates, Churton, Akerman built into interpretive framework

### Data Sources & Authorities (From Research)
**Primary Scholarly Authors:**
- Urszula Szulakowska — Art and Alchemy (visual/symbolic analysis)
- Mike Zuber — Spiritual Alchemy: From Jacob Boehme to Mary Anne Atwood (embodied practice)
- Frances Yates — The Rosicrucian Enlightenment (foundational genealogy)
- Joscelyn Godwin — The Theosophical Enlightenment, Rosicrucian Trilogy (transmission)
- H.M.E. De Jong — Michael Maier's Atalanta Fugiens (emblem scholarship)
- Noel Brann, Curt Ducasse, Lorraine Daston — Contemporary scholarship

**Primary Source Materials Located:**
- E:\pdf\Rosicrucian\ — 53 PDFs (Rosicrucian manifestos, scholarship, Allen anthology)
- E:\pdf\alchemy\atalanta fugiens\ — Comprehensive Maier materials + scholarly analysis
- E:\pdf\alchemy\ — General alchemy, emblem collections (Szulakowska, McLean, Stolcius)
- Project root — Agrippa materials, Newman/Vaughan scholarship
- E:\pdf\emblem studies\ — Cross-disciplinary emblem scholarship

### Emblem Sourcing Strategy (From Session 4 Research)
**Primary Sources to Ingest:**
1. Daniel Cramer, Rosicrucian Emblems (1617) — 40 emblems
2. Michael Maier, Atalanta Fugiens (1618) — 51 emblems
3. Daniel Stolcius, Hermetic Garden (1624) — 160 emblems
4. Mutus Liber (1677) — 15 emblems
5. Nicolas Flamel, Figures Hieroglyphiques (1612) — 22 emblems
6. Heinrich Khunrath, Amphitheatrum Sapientiae (1595) — ~30 emblems
7. Basilius Valentinus — ~20 emblems
8. Secret Symbols collection — ~50 emblems
9. Others — ~60 emblems

**Total Scope: 400+ emblems across 8–12 primary sources**

**Image Sourcing (Priority Order):**
1. PDF extraction (E:\pdf materials)
2. Public-domain digitization (BSB, Archive.org, Google Books)
3. Text-only fallback with sourcing notes

---

## Critical Implementation Patterns (From Sessions 1–5)

### Pattern 1: Write First, Integrate Second
- Create complete, standalone entries (essays, descriptions)
- Then integrate into data structure with relationships
- Allows quality control before database integration

### Pattern 2: Scholarly Rigor Over Completeness
- Better to have 50 deeply researched entries than 100 shallow ones
- Every entry should have:
  - 300+ word substantive content
  - Source documentation
  - Relational links (≥3 connections)
  - Geographic coordinates (where applicable)
  - Historiographical context

### Pattern 3: Emblem as Gateway Entry
- Emblems are highest-value research leverage point
- Each emblem essay can reference 3–5 concepts, 2–3 figures, 1–2 texts
- Emblem → concept mapping builds out entire relational graph
- Visual imagery drives deeper engagement than text alone

### Pattern 4: Genealogical Thinking
- Track transmission: who learned from whom, what was lost/recovered
- Show continental/cultural differences (Islamic alchemy ≠ European)
- Document women's participation despite historical marginalization
- Connect medieval → Renaissance → Enlightenment → modern threads

### Pattern 5: Embodied Practice Integration
- For every concept, ask: "What does a practitioner actually DO?"
- Laboratory alchemy: what operations produce what results
- Spiritual alchemy: what practices transform consciousness
- Bridge traditional and modern: historical accuracy + contemporary relevance

---

## Context Engineering for Agentic Environments (Derived from This Conversation)

### Principle 1: Explicit Task Scoping
- Define exactly what counts as "done" before starting
- Break large tasks into discrete subtasks
- Use /goal command to establish stop-hook conditions
- Document acceptance criteria explicitly

### Principle 2: Comprehensive Context Documentation
- Create master requirement documents (like this one)
- Maintain system prompt documents (CLAUDE.md, PROMPTS.md)
- Update documentation as understanding deepens
- Ensure new agents have full context without re-explaining

### Principle 3: Metadata & Tracking
- Every entity has: ID, type, timestamps, source documentation
- TODO lists marked with scope, owner, timeline, resumption instructions
- Session logs documenting what was accomplished and what's pending
- Ontology documents that evolve as project matures

### Principle 4: Handover Documentation
- Comprehensive "state of the project" documents
- Clear next steps with minimal ambiguity
- Prompts designed to re-orient new agents quickly
- Marked sections for "continuing from here"

### Principle 5: Quality Gates
- Style guides that define acceptable output
- Checklists for every entry type
- Verification steps before integration
- Clear feedback loops to improve quality

---

## What's Working Well (Keep Doing)

✅ Concept-first organization  
✅ Emblem as first-class entity  
✅ Relational linking between all entity types  
✅ Geographic mapping of all entities  
✅ Historiographical rigor (present debates, not certainties)  
✅ Gender-aware scholarship  
✅ Integration of multiple traditions (Islamic, medieval, Renaissance, modern)  
✅ Embodied practice emphasis  
✅ Comprehensive documentation of process  
✅ Regular deployment and live verification  

---

## What Needs Improvement (Phase 2 Focus)

❌ Emblem image sourcing (need systematic PDF extraction)  
❌ Emblem count (30 → need 100+)  
❌ Emblem UI/UX (not yet implemented in portal)  
❌ PDF corpus systematic ingestion (131 sources, not yet processed)  
❌ Concept-emblem complete mapping (partial only)  
❌ Figure-emblem genealogy (not yet mapped)  
❌ SQLite backend (not yet needed, but Phase 3 prerequisite)  
❌ Full-text search (not yet implemented)  
❌ Scholarly apparatus quotes/citations (template ready, not yet populated)  

---

## Immediate Phase 2 Actions (From This Synthesis)

1. **Detailed Research on Emblems:**
   - Extract image metadata from PDFs (Szulakowska, McLean)
   - Create 30–50 additional emblem entries (aim for 80–100 total)
   - Map each emblem to concepts systematically
   - Source images from public-domain where PDF extraction fails

2. **Update Data Ontology:**
   - Refine emblem entity specification based on Szulakowska analysis
   - Add emblem-source metadata (which emblem book, page, edition)
   - Create emblem-book aggregate entity (for cataloging collections)
   - Add "scholarship" array to emblem entity (scholar references, quotes)

3. **Consolidate System Documents:**
   - Create MASTER_REQUIREMENTS.md (this document, refined)
   - Create AGENTIC_CONTEXT_ENGINEERING.md (best practices guide)
   - Update STYLEGUIDE.md with all Phase 1 learnings
   - Update CLAUDE.md with complete project scope

4. **Create Handover Documentation:**
   - PHASE_2_HANDOVER.md (detailed roadmap, next steps)
   - RESUMPTION_PROMPT.md (brief prompt for new session)
   - QUICK_START.md (how to orient to the project)

---

## Success Metrics for Phase 2

- [ ] 100+ emblem entries created (up from 30)
- [ ] 50+ emblem images sourced and integrated
- [ ] 60 concepts each linked to ≥3 emblems
- [ ] 40+ figures each linked to ≥3 emblems or concepts
- [ ] Zero broken cross-references (automated validation)
- [ ] All writing meets style guide standards
- [ ] Portal remains live and functional throughout
- [ ] Complete context engineering documentation for future agents

---

## Notes for Next Agent/Session

This document represents the complete harvest of user intentions from the entire conversation. When resuming Phase 2:

1. **Read this document first** — understand what the user wants overall
2. **Check STYLEGUIDE_UPDATED.md** — understand what "good writing" means for this project
3. **Check PHASESTATUS.md** — understand current project state
4. **Check EMBLEM_SYSTEM_PLAN.md** — understand emblem architecture
5. **Review marked TODO items** — these are explicit next steps
6. **Reference ONTOLOGY_UPDATED.md** — understand data structure

The project is mature enough that new work should integrate with existing patterns, not reinvent them.

