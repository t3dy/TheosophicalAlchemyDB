# DOCUMENTAIRTRAFFICCONTROL.md — Where to Go for Any Task

This document routes you to the right file for your current task. **Always use this as your navigation guide.**

---

## Quick Lookup by Task

### Understanding the Project

| Task | Start Here | Then Read |
|------|-----------|-----------|
| **I'm new; where do I start?** | `PROMPTS.md` (5 min read) | `CLAUDE.md` (overview) |
| **I want the current project status** | `PHASESTATUS.md` | `docs/ROADMAP.md` |
| **What's the architecture?** | `docs/SYSTEM.md` | `docs/ONTOLOGY.md` |
| **What are the phases?** | `CLAUDE.md` → "Phase Timeline" | `docs/ROADMAP.md` |
| **Where are the PDFs?** | `CORPUS_MANIFEST.md` | Source directories: `E:\pdf\*` |

### Database & Schema Work

| Task | Start Here | Then Read |
|------|-----------|-----------|
| **I need to understand the schema** | `docs/ONTOLOGY.md` | `docs/SYSTEM.md` |
| **I'm adding a new table** | `docs/ONTOLOGY.md` (read current schema) | `CLAUDE.md` → "Operating Rules" |
| **I'm modifying a field** | `docs/ONTOLOGY.md` | `docs/SYSTEM.md` |
| **The schema has a bug** | `docs/ONTOLOGY.md` (read it first) | `PHASESTATUS.md` (file issue) |
| **I need seed data examples** | `data/rosicrucian_seed.json` | `docs/ONTOLOGY.md` (reference) |

### Writing Content (Concepts, Figures, Texts, Essays)

| Task | Start Here | Then Read |
|------|-----------|-----------|
| **I'm writing a concept essay** | `docs/STYLEGUIDE.md` | `PROMPTS.md` → "Dual-Audience Architecture" |
| **I'm writing a figure biography** | `docs/STYLEGUIDE.md` | `docs/INTERFACE.md` (biography template) |
| **I'm writing a text summary** | `docs/STYLEGUIDE.md` | `docs/INTERFACE.md` (text template) |
| **I'm writing a thematic essay** | `docs/STYLEGUIDE.md` | `PROMPTS.md` → "Research Questions" |
| **I need the academic voice standard** | `docs/STYLEGUIDE.md` | `PROMPTS.md` (principles) |
| **I'm unsure about historiographical framing** | `PROMPTS.md` → "Historiographical Rigor" | `docs/STYLEGUIDE.md` |

### Emblem Work

| Task | Start Here | Then Read |
|------|-----------|-----------|
| **I'm cataloging emblems** | `EMBLEMS_GUIDE.md` (when created) | `data/emblem_manifest.json` |
| **I need emblem image sources** | `EMBLEMS_GUIDE.md` | Wikimedia Commons, BSB, HMD |
| **I'm analyzing an emblem** | `docs/STYLEGUIDE.md` | De Jong model (referenced in guides) |
| **I'm linking an emblem to concepts** | `docs/ONTOLOGY.md` (emblem_concept_links) | `EMBLEMS_GUIDE.md` |

### Building & Deployment

| Task | Start Here | Then Read |
|------|-----------|-----------|
| **I'm running the pipeline** | `docs/PIPELINE.md` | `scripts/` (script order) |
| **I need to set up the environment** | `docs/SYSTEM.md` | `requirements.txt` (if exists) |
| **The build is failing** | `docs/PIPELINE.md` | Check script error messages |
| **I need to deploy to GitHub Pages** | `docs/SYSTEM.md` | `.github/workflows/deploy.yml` |
| **The website looks broken** | `docs/INTERFACE.md` | `site/style.css` (CSS issues) |

### Planning & Phase Gates

| Task | Start Here | Then Read |
|------|-----------|-----------|
| **I'm starting a new phase** | `PHASESTATUS.md` (what's the current phase?) | `docs/ROADMAP.md` (phase gates) |
| **I need to scope a task** | `PROMPTS.md` (research questions) | `docs/ONTOLOGY.md` (entity scope) |
| **I found a blocker** | `PHASESTATUS.md` (file it) | Discuss with project owner |
| **I finished a task** | Update `PHASESTATUS.md` | Commit + push |

---

## File Status Legend

In `PHASESTATUS.md`, files are marked with status badges:

| Badge | Meaning | Who Should Touch It |
|-------|---------|-------------------|
| **DONE** | Complete, tested, stable | Review only |
| **READY** | Reviewed, ready for use | LLMs building on it |
| **BUILDING** | In progress | Current session's task |
| **BLOCKED** | Waiting on dependency | Document the blocker |
| **PLANNED** | Outlined, not started | Follow outline when starting |
| **STALE** | Outdated, needs refresh | Refresh before using |

---

## Document Ownership & Update Rules

| Document | Owner | When to Update | How Often |
|----------|-------|---|---|
| `CLAUDE.md` | Project lead | Major architectural changes | Rarely |
| `PROMPTS.md` | Project lead | Vision/principle changes | Rarely |
| `DOCUMENTAIRTRAFFICCONTROL.md` | Project lead | New docs added or routing changes | As needed |
| `PHASESTATUS.md` | Current session | Task progress, blockers, what changed | **Every session end** |
| `docs/ONTOLOGY.md` | Schema owner | Schema changes | Immediately after schema change |
| `docs/PIPELINE.md` | Script owner | Script order/dependencies change | Immediately |
| `docs/STYLEGUIDE.md` | Content lead | Voice/standard changes | As needed |
| `docs/INTERFACE.md` | Frontend owner | Page templates change | As needed |
| `docs/SYSTEM.md` | Architecture owner | Major architecture decisions | Rarely |
| `CORPUS_MANIFEST.md` | Research lead | PDF triage/status changes | Phase 0 weekly |

---

## Common Workflows

### Workflow: Start a New Session

1. **Read** `PROMPTS.md` (3 min)
2. **Check** `PHASESTATUS.md` — what phase? What's blocked? What was the last session's status?
3. **Read** the relevant spec doc(s):
   - Doing DB work? → `docs/ONTOLOGY.md`
   - Doing content work? → `docs/STYLEGUIDE.md`
   - Doing emblem work? → `EMBLEMS_GUIDE.md`
   - Doing frontend work? → `docs/INTERFACE.md`
4. **Claim your task** in `PHASESTATUS.md` (mark as "in_progress")
5. **Work**
6. **Update** `PHASESTATUS.md` at end of session

### Workflow: Add a New Database Table

1. Read `docs/ONTOLOGY.md` (understand current schema)
2. Read `docs/SYSTEM.md` (understand provenance model)
3. Propose new table: entity name, fields, relationships
4. Update `docs/ONTOLOGY.md` with new table definition
5. Update `docs/PIPELINE.md` if new script needed
6. Create seed data in `data/*.json`
7. Update `PHASESTATUS.md`

### Workflow: Write a Concept Essay

1. Read `PROMPTS.md` → "Dual-Audience Architecture" (how to write for both audiences)
2. Read `docs/STYLEGUIDE.md` (voice, length, structure)
3. Find the concept in `data/rosicrucian_seed.json` (or add it)
4. Write the essay (150–400 words, cite sources, draft status)
5. Link to ≥3 related concepts, figures, texts
6. Mark as `review_status='DRAFT'` in database
7. Update `PHASESTATUS.md`

### Workflow: Catalog an Emblem

1. Read `EMBLEMS_GUIDE.md` (once created)
2. Find the emblem in the PDF corpus (get image reference, page number, text)
3. Locate a public-domain image (Wikimedia Commons, BSB, etc.)
4. Add to `data/emblem_manifest.json`:
   - emblem_id, emblem_num, roman_numeral, title, motto
   - image_url, image_source, image_confirmed
5. Write description (following De Jong model)
6. Link to concepts, text source, related figures
7. Mark as `review_status='DRAFT'` in database
8. Update `PHASESTATUS.md`

---

## Document Dependency Graph

```
PROMPTS.md (read first)
    ↓
CLAUDE.md (project overview)
    ├→ docs/SYSTEM.md (architecture)
    │   ├→ docs/ONTOLOGY.md (schema)
    │   └→ docs/PIPELINE.md (scripts)
    ├→ docs/INTERFACE.md (pages/templates)
    ├→ docs/STYLEGUIDE.md (voice/content)
    ├→ docs/ROADMAP.md (phases)
    └→ PHASESTATUS.md (current session status)

Supporting docs:
    ├→ CORPUS_MANIFEST.md (PDF triage)
    ├→ EMBLEMS_GUIDE.md (emblem reference)
    ├→ data/*.json (seed data)
    └→ scripts/ (Python pipeline)
```

---

## How to Find Something

### "I need to understand X"

- **X = concept/figure/text/emblem format?** → `docs/ONTOLOGY.md`
- **X = how the site is built?** → `docs/SYSTEM.md`
- **X = academic voice/writing standard?** → `docs/STYLEGUIDE.md`
- **X = page structure/layout?** → `docs/INTERFACE.md`
- **X = where to file a blocker?** → `PHASESTATUS.md`

### "I need to do Y"

- **Y = write a concept essay?** → `docs/STYLEGUIDE.md`
- **Y = add a database table?** → `docs/ONTOLOGY.md`, then `docs/PIPELINE.md`
- **Y = catalog an emblem?** → `EMBLEMS_GUIDE.md`
- **Y = understand the big picture?** → `PROMPTS.md`
- **Y = check project status?** → `PHASESTATUS.md`

### "I think there's a bug in Z"

- **Z = the database schema?** → `docs/ONTOLOGY.md` (read it), then file in `PHASESTATUS.md`
- **Z = the website layout?** → `docs/INTERFACE.md` + `site/style.css`
- **Z = a script?** → `docs/PIPELINE.md` (what should happen) + script error logs
- **Z = the build process?** → `docs/SYSTEM.md` + `docs/PIPELINE.md`

---

## Red Flags & When to Escalate

| Red Flag | What To Do |
|----------|-----------|
| **Historiographical uncertainty** | Check `PROMPTS.md` (research questions), flag in `PHASESTATUS.md` |
| **Schema doesn't match docs** | Update `docs/ONTOLOGY.md` immediately, flag in `PHASESTATUS.md` |
| **AI content has hallucinations** | Mark as `review_status='BLOCKED'`, flag in `PHASESTATUS.md` |
| **Emblem image not public domain** | Remove, find alternate, update `data/emblem_manifest.json` |
| **Page is orphan** (links to 0–2 other pages) | Add ≥1 more link, rerun site build |
| **Concept missing from seed data** | Add to `data/rosicrucian_seed.json`, update schema if needed |

---

**Last Updated:** 2026-05-24
**Maintained By:** Project lead
**Questions?** Refer to the routing table above, or check `PHASESTATUS.md` for blockers
