# PROMPTS.md — Canonical Vision & North Star

**Read this file at the START of every session.** It articulates the non-negotiable vision and the research questions that guide all decisions.

---

## One-Sentence Vision

A **concept-first, scholarly encyclopedia of Rosicrucian and theosophical-alchemical traditions (16th–18th c.)** that serves scholars, interested readers, and practitioners with relational browsing, rich provenance, and rigorous historiographical discipline.

---

## The Problem We're Solving

Rosicrucian and theosophical-alchemical scholarship is scattered across:
- Scattered PDF corpora (no unified reference)
- Mixed historiographical frames (legendary vs. historical; mystical vs. scientific)
- No concept-first organization (texts and biographies exist, but concepts don't navigate)
- Missing emblem scholarship (emblem books are illustrations, not entities)
- Inaccessible to non-specialists (jargon overload)

**This portal fixes it.** A single, navigable, rigorously sourced reference that organizes knowledge by *idea*, not *author*.

---

## Core Principles (Non-Negotiable)

### 1. Concept-First Organization
Users navigate by **philosophical/alchemical idea**, not chronology or author:
- "What is *nigredo*?" → nigredo page → linked concepts, texts, figures, emblems
- "What is *theosis*?" → theosis page with Rosicrucian interpretations
- "What is *hieros gamos*?" → alchemy + Kabbalah + Rosicrucian contextualization

### 2. Strict Historiographical Rigor
- **Actor/Analyst distinction:** What Rosicrucians called themselves ≠ what modern scholars call them
- **No anachronism:** Renaissance hermetic philosophy is NOT medieval Kabbalah (they're related, but distinct)
- **No speculative content:** All claims are source-trackable; draft status visible
- **Debates are explicit:** When scholars disagree (Rosicrucian "orders" as real vs. legendary), both frames are presented

### 3. Dual-Audience Architecture (No Conflation)
- **For scholars:** Full apparatus, historiographical nuance, debate mapping, comprehensive bibliography
- **For practitioners:** Accessible language, relational navigation, emblem interpretation without mysticism
- **Never conflate:** A scholar page is not a practitioner guide; an essay can't blur the two

### 4. Emblems as First-Class Entities
Each emblem is a **navigable entity** with:
- High-resolution image + source
- Textual description (what Maier/Micrelius/etc. said)
- Scholarly apparatus (De Jong-style source analysis)
- Links to concepts, texts, figures
- Visual element analysis (if applicable)

This is **not** an illustration gallery; it's an emblem *research infrastructure*.

### 5. Deterministic First, LLM Second
- **Python extracts** what's provable (dates, names, hierarchies, explicit relationships)
- **LLM synthesizes** what requires judgment (concept summaries, thematic essays, connections)
- **Humans review** all LLM output before publication
- **Provenance on every datum:** source_method, confidence, review_status always recorded

### 6. Academic Voice
- No mysticism, no channeled content, no false authority
- Clear, accessible language (complex ideas, simple words)
- Explain jargon on first use; link to dictionary
- Cite sources consistently
- Visible AI attribution on generated content

### 7. Relational Browsing
Every entity links to ≥3 others:
- A figure biography links to influenced figures, key concepts, major texts
- A concept page links to related concepts, texts, figures, emblems
- A text summary links to author, concepts developed, related works
- Sidebar previews show related items without leaving the page

---

## Research Questions Driving Phase 0 Triage

These questions guide our corpus analysis and seed data design:

1. **Concepts:** What are the 40–60 most important philosophical/alchemical ideas in Rosicrucianism and theosophical alchemy? (e.g., *nigredo, albedo, rubedo, theosis, hieros gamos, quaternio, lapis, etc.*)

2. **Genealogy:** How does Renaissance hermetic philosophy → Rosicrucian movements → 18th-century alchemy → Swedenborgianism form a coherent tradition?

3. **The Rosicrucian Question:** Were historical Rosicrucian "orders" real organizations or literary fictions? What does modern scholarship say? How do we present both frames fairly?

4. **Alchemy's Range:** What's the spectrum from laboratory alchemy → alchemical allegory → inner-world theurgy? Which traditions are included here?

5. **Emblems:** Which 8–12 emblem books are canonical? (Maier, Micrelius, Mutus Liber, Khunrath, Flamel, Valentine, etc.) How many individual emblems should we catalog?

6. **Figures:** Who are the 30–40 figures we must include? (Andreae, Dee, Fludd, Ashmole, Cagliostro, Swedenborg, Böhme, Paracelsus, etc.)

7. **Historiographical Debates:** What are the big scholarly disagreements? (e.g., Swedenborg's authority, gender in alchemy, alchemy as chemistry vs. metaphor)

8. **Dual Audience:** How do we write for both scholars and practitioners without conflating the two?

---

## What Success Looks Like (Phase 8 End State)

✓ **50–70 concept encyclopedia pages** organized hierarchically (core → derived → niche concepts)
✓ **30–40 figure biographies** with genealogy links
✓ **25–35 text summaries** with quotations and concept maps
✓ **20–40 emblem entries** with images, provenance, scholarly apparatus
✓ **100+ dictionary terms** cross-linked to concepts and texts
✓ **12–18 thematic essays** on historiographical debates and cross-cutting problems
✓ **Concept network visualization** (D3.js or similar) showing links between ideas
✓ **Full-text search** across all content
✓ **<5% content DRAFT** (rest REVIEWED or VERIFIED)
✓ **Zero historiographical errors** (every claim source-trackable)
✓ **Complete provenance** (source_method, confidence, review_status on every datum)
✓ **Academic disclosure** visible (what's human-written vs. AI-drafted)
✓ **Live at GitHub Pages** (t3dy/rosicrucianism-alchemy-portal)

---

## Anti-Patterns (What We Will NOT Do)

❌ Mystical language or New Age framing
❌ Speculative content without source attribution
❌ Conflating scholar voice with practitioner voice
❌ Treating legendary Rosicrucian "orders" as historical fact
❌ Alchemy as purely chemical or purely symbolic (present the spectrum)
❌ Hallucinated scholarship or fictional citations
❌ AI-generated content without review or draft-status marking
❌ Orphan pages (every page links to ≥3 others)
❌ Anachronistic terminology (use period-appropriate language)

---

## The Emblem Scholar's North Star

For emblem work specifically:

- **Emblems are NOT illustrations**; they are *researched entities*
- Every emblem has: image, provenance, Maier/Micrelius text, scholarly interpretation, linked concepts
- De Jong's *Atalanta Fugiens* scholarship is our anchor; other emblem book traditions supplement
- Visual analysis is rigorous, not intuitive (describe what's *visible* in the plate, not what it *means*)
- Every emblem links to ≥2 concepts, ≥1 text, ≥1 figure
- All emblem images must be public domain or openly licensed (no rights-restricted images)

---

## Session Discipline

**At the start of each session:**
1. Read this file (PROMPTS.md)
2. Check `PHASESTATUS.md` for current phase and blockers
3. Read the routing guide (`DOCUMENTAIRTRAFFICCONTROL.md`)
4. Review the relevant spec doc (e.g., `docs/ONTOLOGY.md` for DB work)

**At the end of each session:**
1. Update `PHASESTATUS.md` with: what changed, what's blocked, next steps
2. Commit your work with clear message
3. Leave the repo in a state where another session can pick up immediately

---

## How to Use This File

- **Planning phase:** Refer to **Concepts** and **Research Questions** sections to scope new work
- **Writing content:** Refer to **Core Principles** (especially Dual-Audience Architecture and Academic Voice)
- **Emblem work:** Refer to **The Emblem Scholar's North Star** section
- **Data integrity:** Refer to **Anti-Patterns** to catch mistakes
- **End of session:** Update `PHASESTATUS.md` with reference to **Session Discipline**

---

**Last Updated:** 2026-05-24
**Canonical Vision Owner:** t3dy
