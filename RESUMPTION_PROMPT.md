# Quick Resumption Prompt for New Session

**Use this prompt when starting a new session to quickly orient the agent.**

---

**Session Start Prompt:**

```
You are resuming work on TheosophicalAlchemyDB — a Rosicrucian and theosophical-alchemy 
knowledge portal with 63 figures, 60 concepts, 83 texts, and 30+ emblem entries.

## Critical: Read These First (in order)
1. C:\Dev\TheosophicalAlchemyDB\CONVERSATION_REQUIREMENTS_HARVEST.md
2. C:\Dev\TheosophicalAlchemyDB\PHASE_2_HANDOVER.md
3. C:\Dev\TheosophicalAlchemyDB\docs\STYLEGUIDE_UPDATED.md
4. C:\Dev\TheosophicalAlchemyDB\docs\ONTOLOGY_UPDATED.md

## Current Status
- Phase 1 COMPLETE (63 figures, 60 concepts, 83 texts)
- Phase 2 IN PROGRESS: Expand emblems from 30 → 100+, create concept-emblem mappings, 
  enrich scholarly apparatus, refine ontology

## Current Task
Focus on these 7 workstreams (in priority order):
1. Emblem sourcing & image acquisition (30 → 100+) — Tier 1: Cramer, Maier, Stolcius
2. Concept-emblem comprehensive mapping (60 concepts × 2-3 emblems each)
3. Figure-emblem genealogy (who created/influenced emblems)
4. Scholarly apparatus enrichment (direct quotes, page citations, debates)
5. Data ontology refinement (emblem-book entity, authenticity field)
6. Emblem gallery UI/UX (card/modal/search/filter/map integration)
7. PDF corpus systematic ingestion (131 sources, extract text/images/metadata)

## Key Constraints
- Portal must remain live and functional throughout
- All writing must meet STYLEGUIDE_UPDATED.md standards
- Every emblem must have: visual_description + essay + ≥2 concept links + sourcing metadata
- Every concept must link to ≥2 emblems (concept-emblem mapping)
- Historiographical rigor (Yates/Vickers model): present scholarly debates, not false certainty
- Gender awareness & transmission genealogy in all entries
- Image sourcing priority: PDF extraction → public-domain → text-only fallback

## File Locations
- **Data:** C:\Dev\TheosophicalAlchemyDB\data\prototype_data.json
- **Build script:** C:\Dev\TheosophicalAlchemyDB\scripts\build_site.py
- **Frontend:** C:\Dev\TheosophicalAlchemyDB\site/ (index.html, app.js, style.css)
- **Deployment:** https://github.com/t3dy/TheosophicalAlchemyDB (GitHub Pages)

## Quick Links
- E:\pdf\Rosicrucian\ → 53 PDFs (manifestos, Cramer, Maier, scholarship)
- E:\pdf\alchemy\ → 78 PDFs (general alchemy, emblem collections, operations)
- E:\pdf\emblem\ → emblem scholarship resources

## User Communication Style
- User prefers terse responses with no trailing summaries ("I can read the diff")
- User appreciates action over clarifying questions (feedback: "sheesh" when over-questioning)
- User wants text-only summaries when asking for them; don't call tools unless explicitly instructed
- User values historiographical rigor, art-historical analysis, and embodied knowledge emphasis

## Success Looks Like
- 100+ emblem entries with images and scholarly apparatus
- 60 concepts each linked to 2-3+ emblems
- All figures attributed to emblem creation/influence
- Portal live, functional, all features tested
- GitHub deployment successful

**Ready? Begin with CONVERSATION_REQUIREMENTS_HARVEST.md.**
```

---

**If User Asks for Detailed Guidance:**

Respond with: "See PHASE_2_HANDOVER.md for complete Phase 2 roadmap, workstream breakdown, timeline, and success criteria."

**If User Asks About Writing Standards:**

Respond with: "See STYLEGUIDE_UPDATED.md. All entries must follow: historiographical rigor, art-historical analysis (Szulakowska), gender awareness, transmission tracking, embodied knowledge emphasis."

**If User Asks About Data Structure:**

Respond with: "See ONTOLOGY_UPDATED.md for current schema. Phase 2 adds emblem-book entity, authenticity field, enhanced scholarship array."

---

