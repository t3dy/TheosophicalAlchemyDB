# TheosophicalAlchemyDB — Quick Start Guide

**For agents and new contributors orienting to the project.**

---

## What Is This Project?

A **concept-first knowledge portal** on Rosicrucian and theosophical-alchemy traditions (16th–18th century), with:
- **206+ entities**: 63 figures, 60 concepts, 83 texts, 30+ emblems (expanding to 100+)
- **Interactive map**: Leaflet.js showing 106+ geographic locations
- **Gallery cards**: Click-to-expand essays with scholarly apparatus
- **Relational browsing**: Every entity links to ≥3 others; navigate by idea, not chronology

**Live:** https://t3dy.github.io/TheosophicalAlchemyDB/  
**Repository:** https://github.com/t3dy/TheosophicalAlchemyDB

---

## The Four Core Entity Types

### 1. **Figures** (63 total)
Historical people: alchemists, mystics, scholars, women practitioners.

**Example:** Jacob Böhme (1575–1624)
- **Summary:** 100-150 word index card
- **Essay:** 500-1500 word biography covering life, contributions, scholarship, transmission
- **Geographic:** Coordinates where they lived/worked
- **Links:** Related figures, concepts they developed, texts they wrote

**Standards:** Historiographical rigor, not hagiography. State what sources document; distinguish facts from legend.

---

### 2. **Concepts** (60 total)
Philosophical and practical principles: Nigredo, Sublimation, Thesis, Correspondentia, etc.

**Example:** Sublimation (Lat. *sublimare*, to elevate)
- **Summary:** 100-150 word definition
- **Essay:** 500-800 words covering:
  - Laboratory meaning (what practitioners actually do)
  - Philosophical meaning (what principle it represents)
  - Historical development (how understanding evolved)
  - Practical application (how to work with this concept)
  - Related concepts and modern relevance
- **Links:** Related concepts, figures who developed it, texts that explain it, emblems that illustrate it

**Standards:** Dual-level analysis (operational + philosophical). Etymologically grounded. No reductionism.

---

### 3. **Texts** (83 total)
Primary and secondary sources: Rosicrucian manifestos, alchemical treatises, scholarly monographs.

**Example:** The *Chymical Wedding of Christian Rosencreutz* (1616)
- **Summary:** 100-150 word overview
- **Essay:** 500-1500 words covering:
  - Historical context (when, who, why)
  - Content summary (what does it actually say?)
  - Argument or practice (what is it teaching?)
  - Historical influence (how did it shape subsequent thinking?)
  - Scholarly interpretation (how do modern scholars understand it?)
  - Limitations or debates (what controversies exist?)
- **Links:** Related texts, figures, concepts

**Standards:** Primary source priority. Secondary source integration. Historiographical honesty. Transmission tracking.

---

### 4. **Emblems** (30+, expanding to 100+)
Visual-philosophical instruments from emblem books (Cramer, Maier, Stolcius, etc.).

**Example:** Cramer's "Cross Within Circle" (1617)
- **Visual description:** 200-300 word technical description of image composition
- **Essay:** 500-800 words covering:
  - Visual primacy (describe before interpreting)
  - Historical context (when created, for whom, why)
  - Alchemical significance (what stage/principle?)
  - Mystical interpretation (spiritual meaning)
  - Art-historical analysis (how does it fit emblem tradition?)
  - Contemporary influence (how did later thinkers use this?)
  - Scholarly apparatus (references, debates)
- **Image:** Extracted from PDF or public-domain digitization
- **Links:** Related concepts (what does it illustrate?), figures (who created/influenced it?), related emblems

**Standards:** Visual epistemology. Szulakowska art-historical framework. Layered reading (emblems encode multiple meanings).

---

## The Data Structure

**File:** `C:\Dev\TheosophicalAlchemyDB\data\prototype_data.json`

Simple, flat JSON with arrays:

```json
{
  "figures": [
    {
      "id": 1,
      "name": "Jacob Böhme",
      "slug": "jacob-bohme",
      "birth_year": 1575,
      "death_year": 1624,
      "nationality": "German",
      "location": "Görlitz",
      "lat": 51.1537,
      "lng": 14.9633,
      "primary_discipline": "Mysticism",
      "summary": "100-150 word summary...",
      "essay": "500-1500 word essay...",
      "scholars": ["Zuber", "Godwin", "Szulakowska"],
      "key_works": [1, 5, 12],
      "concepts": [3, 7, 15],
      "related_figures": [2, 4, 8]
    }
  ],
  "concepts": [...],
  "texts": [...],
  "emblems": [...]
}
```

**Key fields:** id, name/title, slug, coordinates (lat/lng), summary, essay, links (arrays of IDs), scholars (name list), sourcing metadata.

**Simple rule:** Every entity links to ≥3 others. No orphans.

---

## How to Build & Deploy

### 1. **Edit Data** (If adding entries)
Edit `prototype_data.json` directly. Add to appropriate array (figures, concepts, texts, emblems).

**For new entry, follow template:**
```json
{
  "id": [next_id],
  "name": "...",
  "slug": "...",
  "[all required fields]",
  "summary": "[100-150 words]",
  "essay": "[500-1500 words, meeting style guide]",
  "scholars": ["..."],
  "[links to other entities]": [ids]
}
```

### 2. **Rebuild Portal** (After editing data)
```bash
cd C:\Dev\TheosophicalAlchemyDB
python scripts/build_site.py
```

Output: Updates `site/index.html` with latest data.

### 3. **Test Locally** (Before deployment)
```bash
cd site/
python -m http.server 8000
# Visit http://localhost:8000 in browser
# Test: cards, modals, map, navigation
```

### 4. **Deploy to GitHub** (When ready)
```bash
git add -A
git commit -m "Phase 2: [descriptive message]"
git push origin main
```

Site updates automatically at: https://t3dy.github.io/TheosophicalAlchemyDB/

**Important:** Commit frequently (daily). Portal should remain live throughout development.

---

## Key Files & Their Purpose

| File | Purpose |
|------|---------|
| `prototype_data.json` | **LIVE DATABASE** — All 206+ entities |
| `scripts/build_site.py` | Reads JSON, generates `site/index.html` |
| `site/app.js` | Frontend logic (cards, modals, map, search) |
| `site/style.css` | Design system (burnt sienna + parchment) |
| `CONVERSATION_REQUIREMENTS_HARVEST.md` | **Master requirements** from all sessions |
| `PHASE_2_HANDOVER.md` | **Detailed Phase 2 roadmap** |
| `STYLEGUIDE_UPDATED.md` | **Writing standards** for all entries |
| `ONTOLOGY_UPDATED.md` | **Data schema** documentation |
| `EMBLEM_SYSTEM_PLAN.md` | **Emblem sourcing strategy** (400+ sources) |
| `PHASESTATUS.md` | **Phase tracking** — what's done, what's next |

---

## Writing Standards (TL;DR)

**For Figures (Biographies):**
- Historiographical rigor: facts vs. inference vs. speculation
- 500-1500 words; structure: birth → education → contributions → context → scholarship → transmission → closing
- Gender awareness: note obstacles, participation, transmission patterns
- ✅ "Böhme described interior alchemical work in rich visionary language" (factual, grounded)
- ❌ "The great master Böhme achieved enlightenment" (hagiography)

**For Concepts (Definitions):**
- Dual-level analysis: operational (what practitioners do) + philosophical (what principle it represents)
- 300-800 words; structure: etymology → lab meaning → philosophy → history → practice → relations → modern relevance
- Etymological grounding: show where word comes from
- ✅ "Sublimation (from Lat. *sublimare*, elevate) is both operation and principle..." (grounded)
- ❌ "Sublimation is just heating" (reductionist)

**For Texts (Summaries):**
- Primary source priority; secondary source integration
- 500-1500 words; structure: context → content → argument → influence → scholarship → debates
- Historiographical honesty: acknowledge when sources are ambiguous, legendary, or disputed
- ✅ "The *Chymical Wedding* remains controversial: was it Andreae's or collaborative?" (honest)
- ❌ "The *Chymical Wedding* definitely describes the seven stages" (overconfident)

**For Emblems (Art-Historical Essays):**
- Szulakowska framework: visual description → historical context → alchemical significance → art-historical analysis
- 500-800 words; emphasize visual primacy (describe what you see before interpreting)
- Sourcing metadata: which book, page, edition; scholarly references
- ✅ "Cramer's cross-within-circle presents geometric precision, indicating mathematical theology" (visual + analysis)
- ❌ "This emblem means divine unity" (interpretation without description)

**Common Pitfalls to Avoid:**
- ❌ Orientalism (treating non-Western esotericism as exotic)
- ❌ Anachronism (using modern vocabulary for historical thinkers)
- ❌ Retroactive validation ("alchemy anticipated modern chemistry")
- ❌ Gender erasure (invisibilizing women through pronouns, narratives)
- ❌ Overstating certainty (presenting debates as settled)
- ❌ Reductionism ("it's really just psychology" or "chemistry")
- ❌ Mystification (vague, reverent language)
- ❌ Intellectualism (ignoring that practice matters)

**See `STYLEGUIDE_UPDATED.md` for detailed standards and examples.**

---

## Current Phase Status

**Phase 1: COMPLETE** ✅
- 63 figures, 60 concepts, 83 texts created
- 30 emblem entries created
- Interactive map functional
- Portal live and deployed

**Phase 2: IN PROGRESS** 🚀
- Goal: 100+ emblems (expand from 30)
- Goal: Concept-emblem comprehensive mapping
- Goal: Figure-emblem genealogy
- Goal: Scholarly apparatus enrichment
- Goal: Emblem gallery UI/UX
- **Timeline:** 2026-05-25 to 2026-06-21

**Phases 3+:**
- Phase 3: SQLite backend, full-text search
- Phase 4: PDF corpus systematic ingestion
- Phase 5+: Advanced features (network visualization, etc.)

---

## Scholarly Authorities (Your Interpretive Framework)

These scholars shape how the portal interprets esotericism:

| Scholar | Works | Focus |
|---------|-------|-------|
| **Urszula Szulakowska** | *Art and Alchemy* | Visual-symbolic analysis; emblems as philosophical instruments |
| **Mike Zuber** | *Spiritual Alchemy* | Embodied practice; Böhme→Atwood genealogy; transmission |
| **Joscelyn Godwin** | *The Theosophical Enlightenment*, *Rosicrucian Trilogy* | Genealogical thinking; transmission across cultures |
| **H.M.E. De Jong** | *Michael Maier's Atalanta Fugiens* | Scholarly apparatus; emblem scholarship; technical knowledge |
| **Frances Yates** | *The Rosicrucian Enlightenment* | Foundational genealogy; historiographical methodology |
| **Brian Vickers** | "Frances Yates and the Writing of History" | Historiographical critique; rigorous documentary evidence |
| **Noel Brann, David Kuntz, Nicholas Goodrick-Clarke** | Contemporary scholarship | Social history; gender awareness; occultism in intellectual history |

**Your job:** Integrate these frameworks into entries, present scholarly debates fairly (Yates vs. Vickers model), and maintain historiographical rigor.

---

## Quick Orientation Checklist

- [ ] Read CONVERSATION_REQUIREMENTS_HARVEST.md (understand ALL user desires)
- [ ] Read PHASE_2_HANDOVER.md (understand current roadmap)
- [ ] Read STYLEGUIDE_UPDATED.md (understand writing standards)
- [ ] Read ONTOLOGY_UPDATED.md (understand data structure)
- [ ] Skim EMBLEM_SYSTEM_PLAN.md (understand emblem sourcing strategy)
- [ ] Check PHASESTATUS.md (see current phase and what's blocked)
- [ ] Verify `site/index.html` loads locally (test build process)
- [ ] Check E:\pdf\Rosicrucian and E:\pdf\alchemy exist (source materials)

**Once these are done, you're ready to work.**

---

## When You Get Stuck

**If you don't know how to do something:**

1. Check `STYLEGUIDE_UPDATED.md` (standards question)
2. Check `ONTOLOGY_UPDATED.md` (data structure question)
3. Check `PHASE_2_HANDOVER.md` (what's the current task?)
4. Check `EMBLEM_SYSTEM_PLAN.md` (emblem sourcing strategy)
5. Look at Phase 1 examples in `prototype_data.json` (how were existing entries done?)

**If you find an error or inconsistency:**
- Flag it in comments
- Update `PHASESTATUS.md` "Blocked/Issues" section
- Ask user for clarification if needed

**If you run out of context:**
- Save your work (commit to git)
- Update `PHASESTATUS.md` with what you accomplished
- Refer new agent to `RESUMPTION_PROMPT.md`

---

## Success Looks Like

By end of Phase 2:
- ✅ 100+ emblem entries (up from 30)
- ✅ 50+ emblem images sourced (extracted/public-domain)
- ✅ All 60 concepts linked to 2-3+ emblems
- ✅ All figures linked to emblem creation/influence
- ✅ Scholarly apparatus enriched (quotes, page citations, debates)
- ✅ Emblem gallery UI/UX functional (cards, modals, search, filters, map)
- ✅ Data ontology refined (emblem-book entity, authenticity field)
- ✅ Portal live, functional, all features tested
- ✅ All writing meets style guide standards
- ✅ GitHub deployment successful

**You'll know you're done when all 7 Phase 2 workstreams are complete and the portal is live with 100+ emblems fully integrated.**

---

**Ready to start? Begin with CONVERSATION_REQUIREMENTS_HARVEST.md. Good luck!**

