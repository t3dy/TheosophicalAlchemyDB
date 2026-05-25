# IMPLEMENTATION_PLAN.md — Scripting & Research Strategy

This document outlines the **technical strategy** for Phase 0–2: PDF triage, concept extraction, scripting workflow, and knowledge portal build.

---

## Phase 0 Strategy: PDF Triage & Corpus Analysis (Week 1)

### 0.1: PDF Manifest & Triage

**Deliverable:** `CORPUS_MANIFEST.md`

**Approach:**
1. **Enumerate** all 131 PDFs (E:\pdf\Rosicrucian, E:\pdf\alchemy, E:\pdf\emblem studies)
2. **Tag each PDF** with metadata:
   - Primary subject (concept, figure, text, methodology, secondary scholarship)
   - Author/editor
   - Publication year
   - File size, OCR quality (GOOD / PARTIAL / SCANNED)
   - Relevance to Rosicrucian + alchemical scope
3. **Triage by quality**:
   - GOOD (searchable PDFs, OCR'd) → Phase 0 analysis
   - PARTIAL (mixed OCR) → Phase 0 analysis with review
   - SCANNED (image-only) → Queue for OCR in Phase 1 (time-intensive)
4. **Cross-reference** PDFs to planned concepts/figures/texts

**Deliverable structure:**
```markdown
# CORPUS_MANIFEST.md

## Summary
- Total PDFs: 131
- GOOD quality: ~40 (30%)
- PARTIAL quality: ~45 (35%)
- SCANNED quality: ~46 (35%)

## By Subject Category

### Rosicrucian Primary Sources & History (E:\pdf\Rosicrucian — 53 PDFs)
- [x] PDF title | Author | Year | Quality | Concepts | Notes
- ...

### Alchemy & Hermetic Philosophy (E:\pdf\alchemy — 78 PDFs)
- [x] PDF title | Author | Year | Quality | Concepts | Notes
- ...

### Emblem Studies (E:\pdf\emblem studies — ~20 PDFs)
- [x] PDF title | Author | Year | Quality | Emblems | Notes
- ...

## Missing Sources (To Track Down)
- [ ] [Concept] — key text missing
- ...
```

### 0.2: Concept Extraction (Sample 10–15 PDFs)

**Approach:**
Read a stratified sample of PDFs to extract core concepts:

1. **Select 5 Rosicrucian PDFs** (manifesto, secondary source, biography, historical account)
2. **Select 5 alchemy PDFs** (transmutation, laboratory, spiritual alchemy, emblem book)
3. **Select 2–3 emblem studies PDFs**

For each PDF:
- **Skim** for concept keywords (use Grep for systematic search)
- **Extract** concept definitions and relationships
- **Record** source (PDF, page range, full quote)
- **Assess** historiographical framing (actor term vs. analyst term)

**Concepts to look for:**
- Alchemical stages: nigredo, albedo, rubedo, citrinitas
- Metaphysical ideas: theosis, henosis, emanation, correspondence
- Rosicrucian ideas: Rosy Cross, invisible college, universal reform
- Gender: hieros gamos, hermaphrodite, androgyne
- Processes: fermentation, putrefaction, coagulation, dissolution
- Technical terms: lapis, tincture, quintessence, stone
- Organizational: order, grade, initiation, secret society

**Output:** `concepts_extracted_phase0.md`

### 0.3: Figure Extraction (Biographical Mentions)

**Approach:**
Search PDFs for biographical entries and influence chains:

1. **Extract figures** mentioned in Rosicrucian + alchemy PDFs
2. **Record**:
   - Full name, dates, nationality
   - Primary discipline (philosopher, alchemist, Rosicrucian, etc.)
   - Key works
   - Influences (who influenced them, who they influenced)
   - Associated concepts
3. **Assess** historiographical status (real person, legendary figure, contested)

**Output:** `figures_extracted_phase0.md` (30–40 figures)

### 0.4: Text Index (Primary Sources)

**Approach:**
Identify canonical texts and create an index:

1. **Rosicrucian manifestos** (Fama Fraternitatis, Confessio, Chymische Hochzeit)
2. **Alchemical treatises** (Maier's Atalanta Fugiens, Mutus Liber, Rosarium Philosophorum, Key of Solomon variants)
3. **Foundational works** (Paracelsus, Böhme, Swedenborg, etc.)
4. **Emblem books** (Maier, Micrelius, Flamel, Valentine, Khunrath)

For each text:
- Title, author, year, language (original + translations)
- Subject (Rosicrucian, alchemical, hermetic, etc.)
- Key concepts developed
- Where it appears in the corpus (PDF references)

**Output:** `texts_index_phase0.md` (25–35 texts)

### 0.5: Emblem Books Catalog

**Approach:**
Identify and categorize emblem books:

1. **List 8–12 canonical emblem books**
2. For each:
   - Title, author, year, language
   - Number of emblems
   - Subject (alchemical, Rosicrucian, Hermetic, etc.)
   - Key themes
   - Where images can be sourced (Wikimedia, BSB, HMD, etc.)
3. **Plan emblem count**:
   - Total emblems to catalog: 20–40
   - Prioritize Maier (51 emblems in Atalanta Fugiens)
   - Then Micrelius, Mutus Liber, etc.

**Output:** `emblem_books_catalog_phase0.md`

### 0.6: Historiographical Debates Map

**Approach:**
Identify major scholarly debates in the field:

1. **Rosicrucian Question:** Are historical "orders" real or literary fiction?
2. **Alchemy Spectrum:** Laboratory chemistry vs. allegory vs. inner transformation
3. **Swedenborg's Authority:** His role in theosophical alchemy tradition
4. **Gender in Alchemy:** Hieros gamos, androgyne symbolism, female practitioners
5. **Filiations:** How does Renaissance hermetic philosophy → Rosicrucian → 18th-century alchemy → theosophy flow?
6. **Influence chains:** Paracelsus → Böhme → Swedenborg, etc.

For each debate:
- What scholars are on each side?
- What's at stake historically?
- How do we present it neutrally?

**Output:** `historiographical_debates_phase0.md`

---

## Phase 1 Strategy: Schema & Seed Data (Week 1–2)

### 1.1: Database Schema Design

**Deliverable:** `init_db.py` (SQLite schema creation script)

**Core tables:**

```sql
-- Entities
CREATE TABLE concepts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    slug TEXT NOT NULL UNIQUE,
    description TEXT,
    category TEXT,  -- metaphysical, alchemical, rosicrucian, etc.
    source_method TEXT,  -- DETERMINISTIC, LLM_ASSISTED, HUMAN_CURATED
    confidence TEXT,  -- HIGH, MEDIUM, LOW
    review_status TEXT,  -- DRAFT, REVIEWED, VERIFIED
    created_at TIMESTAMP
);

CREATE TABLE figures (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    slug TEXT,
    birth_year INTEGER,
    death_year INTEGER,
    nationality TEXT,
    primary_discipline TEXT,
    biography TEXT,
    key_concepts TEXT,  -- JSON array of concept_ids
    source_method TEXT,
    confidence TEXT,
    review_status TEXT,
    created_at TIMESTAMP
);

CREATE TABLE texts (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL UNIQUE,
    slug TEXT,
    author_id INTEGER,  -- foreign key to figures
    year_published INTEGER,
    language TEXT,  -- original language
    subject TEXT,
    description TEXT,
    key_concepts TEXT,  -- JSON array of concept_ids
    source_method TEXT,
    confidence TEXT,
    review_status TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES figures(id)
);

CREATE TABLE emblem_books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL UNIQUE,
    slug TEXT,
    author_id INTEGER,
    year_published INTEGER,
    total_emblems INTEGER,
    subject TEXT,
    description TEXT,
    source_method TEXT,
    review_status TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES figures(id)
);

CREATE TABLE emblems (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    emblem_num INTEGER,
    roman_numeral TEXT,
    motto TEXT,
    emblem_book_id INTEGER,
    image_url TEXT,
    image_source TEXT,
    image_confirmed INTEGER,  -- 1 = confirmed, 0 = not yet sourced
    description TEXT,
    visual_elements TEXT,  -- JSON
    concept_ids TEXT,  -- JSON array of related concept_ids
    figure_ids TEXT,  -- JSON array of related figure_ids
    text_ids TEXT,  -- JSON array of related text_ids
    source_method TEXT,
    confidence TEXT,
    review_status TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (emblem_book_id) REFERENCES emblem_books(id)
);

CREATE TABLE dictionary_terms (
    id INTEGER PRIMARY KEY,
    term TEXT NOT NULL UNIQUE,
    slug TEXT,
    definition TEXT,
    category TEXT,  -- stage, process, substance, principle, etc.
    related_terms TEXT,  -- JSON array of term slugs
    linked_concepts TEXT,  -- JSON array of concept_ids
    source_method TEXT,
    review_status TEXT,
    created_at TIMESTAMP
);

-- Relationships
CREATE TABLE concept_relationships (
    id INTEGER PRIMARY KEY,
    source_concept_id INTEGER,
    target_concept_id INTEGER,
    relationship_type TEXT,  -- parent, derived_from, opposed_to, analogous_to, etc.
    notes TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (source_concept_id) REFERENCES concepts(id),
    FOREIGN KEY (target_concept_id) REFERENCES concepts(id)
);

CREATE TABLE figure_influences (
    id INTEGER PRIMARY KEY,
    source_figure_id INTEGER,
    target_figure_id INTEGER,
    influence_type TEXT,  -- teacher, student, colleague, influenced, inspired, etc.
    notes TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (source_figure_id) REFERENCES figures(id),
    FOREIGN KEY (target_figure_id) REFERENCES figures(id)
);

CREATE TABLE text_concepts (
    id INTEGER PRIMARY KEY,
    text_id INTEGER,
    concept_id INTEGER,
    prominence TEXT,  -- primary, secondary, tertiary
    page_reference TEXT,
    note TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (text_id) REFERENCES texts(id),
    FOREIGN KEY (concept_id) REFERENCES concepts(id)
);

CREATE TABLE emblem_concepts (
    id INTEGER PRIMARY KEY,
    emblem_id INTEGER,
    concept_id INTEGER,
    interpretation TEXT,  -- brief explanation of link
    created_at TIMESTAMP,
    FOREIGN KEY (emblem_id) REFERENCES emblems(id),
    FOREIGN KEY (concept_id) REFERENCES concepts(id)
);

CREATE TABLE scholars (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    slug TEXT,
    affiliation TEXT,
    specializations TEXT,  -- JSON array (Rosicrucian, alchemy, emblems, etc.)
    bio TEXT,
    key_works TEXT,  -- JSON array of text_ids / bibliography entries
    source_method TEXT,
    review_status TEXT,
    created_at TIMESTAMP
);

CREATE TABLE timeline_events (
    id INTEGER PRIMARY KEY,
    year INTEGER,
    event_type TEXT,  -- publication, political, movement, biographical, etc.
    description TEXT,
    related_figures TEXT,  -- JSON array of figure_ids
    related_concepts TEXT,  -- JSON array of concept_ids
    source_method TEXT,
    review_status TEXT,
    created_at TIMESTAMP
);

-- Source tracking
CREATE TABLE source_authorities (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,  -- Hermetic corpus, Kabbalah, etc.
    description TEXT,
    related_concepts TEXT,  -- JSON array of concept_ids
    canonical_texts TEXT,  -- JSON array of text_ids
    created_at TIMESTAMP
);
```

### 1.2: Seed Data Creation

**Deliverable:** JSON files in `data/`

**Structure:**
```
data/
├── concepts_seed.json       # 40–60 concepts
├── figures_seed.json        # 30–40 figures
├── texts_seed.json          # 25–35 texts
├── emblem_books_seed.json   # 8–12 emblem books
├── emblems_seed.json        # 20–40 emblems
├── dictionary_seed.json     # 100+ terms
├── scholars_seed.json       # 15–20 scholars
├── timeline_seed.json       # 50+ events
└── emblem_manifest.json     # Canonical emblem index (like AtalantaClaudiens)
```

**Example concept seed:**
```json
{
  "concepts": [
    {
      "id": 1,
      "name": "Nigredo",
      "category": "alchemical_stage",
      "description": "The blackening stage in alchemical transformation, symbolic of putrefaction and dissolution.",
      "source_method": "HUMAN_CURATED",
      "confidence": "HIGH"
    },
    {
      "id": 2,
      "name": "Albedo",
      "category": "alchemical_stage",
      "description": "The whitening stage, representing purification and clarification.",
      "source_method": "HUMAN_CURATED",
      "confidence": "HIGH"
    }
  ]
}
```

### 1.3: Seed Data Ingestion Scripts

**Deliverables:**
- `scripts/seed_concepts.py`
- `scripts/seed_figures.py`
- `scripts/seed_texts.py`
- `scripts/seed_emblem_books.py`
- `scripts/seed_emblems.py`
- `scripts/seed_dictionary.py`
- `scripts/seed_scholars.py`
- `scripts/seed_timeline.py`

Each script:
1. Reads the corresponding JSON seed file
2. Inserts rows into SQLite
3. Uses `INSERT OR IGNORE` for idempotency
4. Logs success/conflicts

---

## Phase 2 Strategy: Content Generation (Week 2–4)

### 2.1: Figure Biography Writing

**Approach:**
For each of 30–40 figures:

1. **Research** from corpus (extract biographical mentions, influences)
2. **Write** biography (300–500 words)
   - Life dates and nationality
   - Primary role (philosopher, alchemist, Rosicrucian, etc.)
   - Key ideas and works
   - Influences and influence on others
   - Historiographical notes (contested, legendary, etc.)
3. **Link** to concepts, texts, other figures
4. **Mark** review_status = DRAFT (until human review)

**Deliverable:** `scripts/write_biographies.py` (LLM-assisted, outputs to staging/)

### 2.2: Text Summary Writing

**Approach:**
For each of 25–35 primary texts:

1. **Read** text excerpt from corpus (or full text if available)
2. **Write** summary (250–400 words)
   - What is the text about?
   - What concepts does it develop?
   - How does it fit into the Rosicrucian/alchemical tradition?
   - Key quotes (with page references)
3. **Link** to author, concepts, related texts
4. **Mark** review_status = DRAFT

**Deliverable:** `scripts/write_text_summaries.py` (LLM-assisted, outputs to staging/)

---

## Phase 3 Strategy: Emblem Cataloging (Week 4–5)

### 3.1: Emblem Image Sourcing

**Approach:**
For 20–40 emblems:

1. **Search** Wikimedia Commons (free images)
2. **Fall back** to BSB (Bavarian State Library), HMD (Herzog August Library), etc.
3. **Record** image URL, source attribution, license type
4. **Verify** image is public domain or open CC license

**Tools:** Manual search + Python script to validate URLs

### 3.2: Emblem Description Writing

**Approach:**
For each emblem:

1. **The Plate** (what's visible)
   - Describe visual elements (figures, animals, objects, text)
   - Note composition, symbolic arrangement
2. **Maier's Discourse** (if Atalanta Fugiens) / Original Text
   - Quote the original emblem poem/motto
   - Summarize the author's interpretation
3. **Scholarly Apparatus**
   - Cross-reference scholarly works (De Jong, etc.)
   - Link to related concepts and figures
   - Note variants or interpretations
4. **Linked Entities**
   - Related concepts (3–5)
   - Related figures (1–3)
   - Related texts (1–2)

**Deliverable:** `scripts/write_emblem_descriptions.py` (LLM-assisted)

---

## Phase 4 Strategy: Concept Essays & Dictionary (Week 5–6)

### 4.1: Concept Essay Writing

**Approach:**
For each of 40–60 concepts:

1. **Write** encyclopedia entry (150–400 words depending on complexity)
   - Clear definition
   - Historical origins and development
   - Role in Rosicrucian/alchemical traditions
   - Relationship to other concepts
   - Historiographical notes
2. **Link** to related concepts (≥3), texts, figures, emblems
3. **Mark** review_status = DRAFT

**Structure:**
```markdown
## Nigredo (The Blackening)

### Definition
[Clear 1-sentence definition]

### Historical Development
[Paragraph on origins and evolution]

### In Rosicrucian & Alchemical Traditions
[How this concept is used]

### Related Concepts
- Albedo (the whitening)
- Putrefaction (the process)
- Dissolution (the state)

### See Also
- Texts: [linked texts]
- Figures: [linked figures]
- Emblems: [linked emblems]
```

### 4.2: Dictionary Term Definition

**Approach:**
Create 100+ technical terms:

1. **Collect** terms from corpus (Grep for alchemical/Rosicrucian terminology)
2. **Define** (50–100 words each)
3. **Categorize** (stages, processes, substances, principles, etc.)
4. **Link** to related terms and concepts

---

## Phase 5–6 Strategy: Frontend & Deployment (Week 6–8)

### 5.1: Static Site Generation

**Deliverable:** `scripts/build_site.py`

**Approach:**
1. **Read** SQLite database
2. **Generate** HTML pages from templates
   - Index/gallery pages
   - Concept pages
   - Figure pages
   - Text pages
   - Emblem pages
   - Essay pages
   - Dictionary pages
3. **Build** navigation (sidebar, search, breadcrumbs)
4. **Copy** assets (CSS, JS, images)
5. **Output** to `site/` directory

### 5.2: Page Templates

Use Jinja2 or similar:
```
site/
├── index.html              # Gallery + intro
├── concepts/
│   ├── index.html
│   └── {slug}.html        # Individual concept pages
├── figures/
│   ├── index.html
│   └── {slug}.html
├── texts/
│   ├── index.html
│   └── {slug}.html
├── emblems/
│   ├── index.html
│   └── {slug}.html
├── dictionary/
│   ├── index.html
│   └── {slug}.html
├── essays/
│   ├── index.html
│   └── {slug}.html
├── style.css
└── script.js
```

### 5.3: Styling (Burnt Sienna + Parchment)

CSS variables:
```css
--bg: #f5f0e8;
--bg-card: #fff;
--text: #2c2418;
--accent: #8b4513;
--accent-light: #d4a574;
```

---

## Scripting Workflow (Execution Order)

**Phase 1:**
```bash
python scripts/init_db.py              # Create schema
python scripts/seed_concepts.py        # Load concepts
python scripts/seed_figures.py         # Load figures
python scripts/seed_texts.py           # Load texts
python scripts/seed_emblem_books.py    # Load emblem books
python scripts/seed_emblems.py         # Load emblems
python scripts/seed_dictionary.py      # Load dictionary
python scripts/seed_scholars.py        # Load scholars
python scripts/seed_timeline.py        # Load timeline
```

**Phase 2–3:**
```bash
python scripts/write_biographies.py    # Generate biographies (LLM)
python scripts/write_text_summaries.py # Generate text summaries (LLM)
python scripts/write_emblem_descriptions.py  # Generate emblem descriptions (LLM)
```

**Phase 4:**
```bash
python scripts/write_concept_essays.py # Generate concept essays (LLM)
python scripts/write_dictionary_entries.py  # Generate term definitions
```

**Phase 5–6:**
```bash
python scripts/build_site.py           # Generate static site
```

---

## Quality Gates & Review

Each phase has a gate:

1. **Phase 1 Gate:** Schema matches ONTOLOGY.md; seed data loads without errors
2. **Phase 2 Gate:** All biographies and text summaries marked DRAFT; ≥80% have ≥3 links
3. **Phase 3 Gate:** All emblem images sourced and verified; all emblems have ≥2 concept links
4. **Phase 4 Gate:** All concept essays and dictionary terms marked DRAFT; no orphan pages (<3 links)
5. **Phase 5+ Gate:** Site builds without errors; all links functional; <5% content DRAFT

---

**Last Updated:** 2026-05-24
**Owner:** Research lead + script automation
