# TheosophicalAlchemyDB — Updated Data Ontology

**Version:** 2.0  
**Updated:** 2026-05-25  
**Status:** Phase 0 Expansion — Emblems as First-Class Entities

---

## Overview

The data model is now organized as a **concept-first encyclopedia** with **emblems as first-class entities** (not subordinate illustrations). All entities are **relationally browsable** through bidirectional cross-references and concept links.

## Core Entity Types

### 1. Figures
**Primary historical figures in Rosicrucian and alchemical traditions (1400–1800)**

```json
{
  "id": 52,
  "name": "Agrippa",
  "slug": "agrippa",
  "birth_year": 1486,
  "death_year": 1535,
  "nationality": "German",
  "primary_discipline": "Polymath, Occult Philosopher",
  "summary": "100–150 word overview",
  "essay": "1200–2000 word biographical essay",
  "scholars": ["Yates", "Godwin"],
  "key_works": [54, 55],  // Text IDs
  "concepts": [1, 25, 27],  // Concept IDs
  "emblems": [],  // Emblem IDs associated with this figure
  "influenced_by": [3, 7],  // Other figure IDs
  "influences": [53, 15],  // Other figure IDs
  "location": "Cologne",
  "lat": 50.9365,
  "lng": 6.9582
}
```

**Relationships:**
- `key_works` → Text IDs
- `concepts` → Concept IDs
- `emblems` → Emblem IDs
- `influenced_by` / `influences` → Other Figure IDs
- `scholars` → Scholar names/references

---

### 2. Concepts
**Alchemical, hermetic, and spiritual principles**

```json
{
  "id": 1,
  "name": "Nigredo",
  "slug": "nigredo",
  "summary": "100–150 word definition",
  "essay": "1000–1500 word encyclopedia entry",
  "related_concepts": [2, 3],  // Other concept IDs
  "figures": [52, 53],  // Figure IDs that developed this concept
  "texts": [54, 55],  // Text IDs that discuss this concept
  "emblems": [56, 57]  // Emblem IDs that illustrate this concept
}
```

**Relationships:**
- `related_concepts` → Other Concept IDs
- `figures` → Figure IDs
- `texts` → Text IDs
- `emblems` → Emblem IDs

---

### 3. Texts
**Primary and secondary scholarly works**

```json
{
  "id": 54,
  "title": "Three Books of Occult Philosophy",
  "slug": "three-books-occult-philosophy",
  "year": 1533,
  "author": "Agrippa",
  "language": "Latin",
  "location": "Cologne",
  "summary": "100–150 word summary",
  "essay": "1000–1500 word scholarly analysis",
  "concepts": [1, 25, 27],  // Concept IDs
  "figures": [52],  // Figure IDs mentioned
  "emblems": [56, 57],  // Emblem IDs illustrated in text
  "source_type": "primary",  // primary | secondary | emblem_book
  "publication_date": "1533",
  "lat": 50.9365,
  "lng": 6.9582
}
```

**Relationships:**
- `concepts` → Concept IDs
- `figures` → Figure IDs
- `emblems` → Emblem IDs
- `author` → Figure ID or string

---

### 4. Emblems ← **NEW FIRST-CLASS ENTITY**
**Visual-symbolic representations with art-historical and philosophical analysis**

```json
{
  "id": 56,
  "title": "Cross within Circle",
  "slug": "cramer-cross-circle",
  "year": 1617,
  "type": "emblem",  // rosicrucian | alchemical | hermetic | mystical
  "source_book": "Daniel Cramer's Rosicrucian Emblems",
  "source_book_id": 1,  // Reference to emblem_books table (future)
  "source_text": 59,  // Text ID if from a cataloged text
  "language": "Latin/German",
  "location": "Frankfurt am Main",
  "lat": 50.1109,
  "lng": 8.6821,
  "summary": "150–200 word visual and symbolic description",
  "essay": "500–800 word analysis including:
    - Visual description (composition, elements, iconography)
    - Historical context (publication, reception, influences)
    - Alchemical significance (stages, principles, operations)
    - Mystical interpretation (spiritual meaning, practice)
    - Art-historical analysis (technical, symbolic tradition)
    - Cultural influence (reception, reinterpretation)
  ",
  "visual_elements": ["circle", "cross", "geometric"],
  "concepts": [1, 25, 27],  // Related concept IDs
  "figures": [52, 53],  // Figures associated with this emblem
  "related_emblems": [57, 58],  // Other emblem IDs
  "concepts_illustrated": [
    { "concept_id": 1, "description": "Nigredo through the dark circle" }
  ],
  "image_source": {
    "type": "pdf_extract" | "web_public_domain" | "none",
    "source_file": "Daniel_Cramer_Rosicrucian_Emblems.pdf",
    "page_number": 15,
    "url": null,
    "filename": "cramer_cross_circle.jpg",
    "has_image": true
  },
  "scholarship": [
    {
      "scholar": "Szulakowska",
      "reference": "Art and Alchemy (2006), pp. 120–130",
      "quote": "The circle represents...",
      "relevance": "primary"
    }
  ],
  "authenticity": "confirmed",  // confirmed | attributed | apocryphal
  "notes": "Text description of emblem with additional context for future image sourcing"
}
```

**Relationships:**
- `concepts` → Concept IDs
- `figures` → Figure IDs
- `related_emblems` → Other Emblem IDs
- `source_text` → Text ID
- `concepts_illustrated` → Array of {concept_id, description}

---

### 5. Emblem Books (Planned for Phase 1)
**Collections of emblems with metadata**

```json
{
  "id": 1,
  "title": "Rosicrucian Emblems",
  "author": "Daniel Cramer",
  "year": 1617,
  "location": "Frankfurt",
  "total_emblems": 40,
  "emblems": [56, 57, 58, ...],  // Emblem IDs
  "description": "...",
  "source_pdf": "..."
}
```

---

### 6. Scholars (Metadata)
**Modern researchers and contributors**

```json
{
  "name": "Szulakowska",
  "discipline": "Art History, Esotericism",
  "key_works": ["Art and Alchemy (2006)"],
  "focus_areas": ["emblem scholarship", "visual analysis", "Rosicrucian art"]
}
```

---

## Relational Mapping

### Many-to-Many Relationships

```
Figures ←→ Concepts
  (Figures develop/embody concepts)
  
Figures ←→ Texts
  (Figures author/are discussed in texts)
  
Figures ←→ Figures
  (Influences: A influenced B, B learned from A)
  
Concepts ←→ Concepts
  (Related principles: nigredo precedes albedo)
  
Concepts ←→ Texts
  (Texts develop/discuss concepts)
  
Emblems ←→ Concepts
  (Emblems illustrate/represent concepts)
  
Emblems ←→ Figures
  (Emblems associated with/created by figures)
  
Emblems ←→ Texts
  (Emblems appear in/are analyzed by texts)
  
Emblems ←→ Emblems
  (Related emblems: variations, sequences, responses)
```

---

## Emblem Entity Specification

### Why Emblems Are First-Class

1. **Autonomous Intellectual Objects** — Emblems are not illustrations subordinate to texts; they are self-contained philosophical statements
2. **Visual Epistemology** — Emblems encode knowledge through visual means, requiring art-historical analysis distinct from textual analysis
3. **Cross-Disciplinary Significance** — Emblems are studied by art historians, philosophers, literary scholars, and historians of science simultaneously
4. **Relational Complexity** — Each emblem connects to multiple concepts, figures, and texts in ways that require full entity status

### Emblem Data Requirements

#### Mandatory Fields
- `id`, `title`, `slug`
- `year`, `source_book`, `location`, `lat`, `lng`
- `summary` (150–200 words visual + symbolic description)
- `essay` (500–800 words art-historical analysis)
- `visual_elements` (array of keywords)
- `concepts` (concept IDs)
- `image_source` (metadata about image/non-image status)

#### Scholarly Apparatus
- `scholarship` (array of scholar references with quotes)
- `notes` (text description for future image sourcing)
- `authenticity` (confirmed | attributed | apocryphal)

#### Relational Fields
- `figures` (figure IDs)
- `related_emblems` (other emblem IDs)
- `source_text` (text ID if from cataloged source)
- `concepts_illustrated` (detailed concept mappings)

---

## Browsing Paths (Relational Navigation)

### From Concept
```
Nigredo (concept)
  → Figures that developed it: Paracelsus, Agrippa
  → Texts that discuss it: Three Books, Atalanta Fugiens
  → Emblems that illustrate it: Cramer 1, Maier 3
```

### From Figure
```
Agrippa (figure)
  → Key works: Three Books, De Vanitate
  → Influenced by: Ficino, Pico
  → Influences: Vaughan, Fludd
  → Associated concepts: Correspondence, Natural Magic, Theosis
  → Emblems related to his work: Cramer selection, Agrippa's seal studies
```

### From Emblem
```
Cramer's Cross within Circle (emblem)
  → Illustrates concepts: Nigredo, Theosis, Correspondence
  → From source: Rosicrucian Emblems (1617)
  → Related emblems: Maier Sun-Moon, Stolcius Distillation
  → Referenced by figures: Cramer himself
  → Discussed in texts: McLean's analysis, Szulakowska
```

---

## Sourcing Strategy

### Image Acquisition (Priority Order)
1. **Existing Portal PDFs** — Extract images from available E:\pdf materials
2. **Public-Domain Sources** — Wikimedia Commons, Google Books public domain, Archive.org
3. **Open-Access Digitization** — Bavarian State Library (BSB), Internet Archive, HathiTrust
4. **Text-Only Fallback** — Detailed text descriptions + "image_available: false" + sourcing notes for future manual work

### Text Sourcing
- Extract from cataloged PDFs (De Jong, Szulakowska, McLean, etc.)
- Cross-reference scholarly analyses
- Document all quotes with source attribution

---

## Data Validation Rules

- [ ] Every emblem must have ≥2 concept links
- [ ] Every emblem must have descriptive text (essay, not just image)
- [ ] Every emblem must be sourced (source_book, source_text, or historical reference)
- [ ] All authenticity claims (confirmed/attributed/apocryphal) must be justified in notes
- [ ] Geographic coordinates required for emblem books, optional for individual emblems
- [ ] No orphan emblems: each emblem must link to ≥1 text, ≥1 concept, or ≥1 figure

---

## Comprehensive Emblem Inventory (Phase 0–1)

### Cramer, Daniel: Rosicrucian Emblems (Frankfurt, 1617) — 40 emblems
### Maier, Michael: Atalanta Fugiens (1618) — 51 emblems
### Stolcius de Stolcenberg, Daniel: Hermetic Garden (1624) — 160 emblems
### Secret Symbols of the Rosicrucians (18th-century compilation) — ~50 emblems
### Mutus Liber (Dumb Book, 1677) — 15 emblems
### Flamel, Nicolas: Figures Hieroglyphiques (1612) — 22 emblems
### Khunrath, Heinrich: Amphitheatrum Sapientiae Aeternae (1595) — ~30 emblems
### Valentine, Basilius: Various emblem sources — ~20 emblems
### Micrelius and others (miscellaneous Rosicrucian and alchemical emblems) — ~30 emblems

**Total Scope: 400+ emblems across 8–12 primary sources**

**Phase 0 Target:** 30–50 emblems  
**Phase 1 Target:** 100+ emblems  
**Final Target:** 200–300 emblems (comprehensive 16th–18th century Rosicrucian/alchemical corpus)

---

## JSON Structure Template

### Figure
```json
{
  "type": "figure",
  "id": 52,
  "name": "...",
  "slug": "...",
  "biography": { ... },
  "concepts": [1, 2, 3],
  "texts": [54, 55],
  "emblems": [56, 57],
  "influences": [],
  "influenced_by": []
}
```

### Concept
```json
{
  "type": "concept",
  "id": 1,
  "name": "...",
  "definition": { ... },
  "related_concepts": [2, 3],
  "figures": [52],
  "texts": [54],
  "emblems": [56, 57]
}
```

### Emblem
```json
{
  "type": "emblem",
  "id": 56,
  "title": "...",
  "source": { ... },
  "visual_description": "...",
  "essay": "...",
  "concepts": [1, 2],
  "figures": [52],
  "related_emblems": [57],
  "image": { "available": true/false, "source": "...", "file": "..." },
  "scholarship": [ { "scholar": "...", "reference": "...", "quote": "..." } ]
}
```

---

## Implementation Priorities

**Phase 0 (Current):**
- [x] Establish emblem as entity type
- [x] 30–50 emblem entries with text descriptions
- [ ] Extract 5–10 emblem images from PDFs
- [ ] Create concept-emblem bidirectional links
- [ ] Create figure-emblem associations

**Phase 1 (Next):**
- [ ] Comprehensive PDF emblem extraction (500+ pages)
- [ ] Systematic emblem cataloging from all 8–12 source books
- [ ] Image sourcing from public-domain digitizations
- [ ] Emblem book metadata table
- [ ] Search and filter by visual elements

**Phase 2+:**
- [ ] Scholarly apparatus enrichment (quotes, citations)
- [ ] Concept network visualization (D3.js)
- [ ] Image gallery with lightbox viewer
- [ ] AI-assisted image description for missing images

---

## Future Enhancements

- [ ] **Visual Search** — Users can upload an emblem image to find similar/related emblems
- [ ] **Element Analysis** — Filter emblems by visual components (circle, cross, serpent, etc.)
- [ ] **Concept Explorer** — Interactive visualization showing how concepts link to emblems
- [ ] **Timeline View** — Chronological progression of emblem styles and meanings
- [ ] **Scholarly Apparatus** — Full citation apparatus with cross-references

---

**Next Steps:**
1. Build comprehensive emblem ingestion script
2. Extract text descriptions from Szulakowska, McLean, De Jong, and other sources
3. Source/extract images from available PDFs
4. Create bidirectional concept-emblem linking
5. Deploy Phase 0.5 (emblem expansion) to GitHub

