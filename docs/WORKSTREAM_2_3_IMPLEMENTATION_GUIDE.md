# Workstream 2 & 3 Implementation Guide

**Date:** 2026-05-26  
**Status:** Ready for Database Integration  
**Database State:** 67 concepts, 178 emblems, 100 figures  
**Specification Files:**
- `WORKSTREAM_2_3_MAPPINGS.md` — Full scholarly specification (concept-emblem and figure-emblem mappings)
- `CONCEPT_EMBLEM_LINKS_SPECIFICATION.json` — Machine-readable concept-emblem links (54 total)
- `FIGURE_EMBLEM_GENEALOGY_SPECIFICATION.json` — Machine-readable figure-emblem genealogy (10 figures)

---

## Part 1: Concept-Emblem Bidirectional Mapping (Workstream 2)

### Summary of Mappings

**18 Core Concepts Mapped:**
1. Alchemy (General / The Great Work) — 3 emblems
2. Transmutation — 3 emblems
3. Nigredo (Blackening / Putrefaction) — 3 emblems
4. Albedo (Whitening / Purification) — 3 emblems
5. Rubedo (Reddening / Completion) — 3 emblems
6. Citrinitas (Yellowing) — 3 emblems
7. Conjunction (Coniunctio / The Hermetic Wedding) — 3 emblems
8. Dissolution (Solutio) — 3 emblems
9. Calcination — 3 emblems
10. Distillation — 3 emblems
11. Fermentation — 3 emblems
12. Sublimation — 3 emblems
13. Philosophical Mercury — 3 emblems
14. Philosophical Sulfur — 3 emblems
15. The Stone / Elixir — 3 emblems
16. Macrocosm / Microcosm — 3 emblems
17. Correspondence — 3 emblems
18. Inner Transformation — 3 emblems

**Total Concept-Emblem Links: 54 (3 per concept)**

**Emblem Distribution:**
- Maier Atalanta Fugiens: 38 links (primary source for operational concepts)
- Rosicrucian Emblems (Cramer): 12 links (philosophical and spiritual concepts)
- Hermetic Garden (Stolcius): 4 links (comprehensive systematization)

### Data Schema for `concept_emblem_links` Table

```sql
CREATE TABLE concept_emblem_links (
    id INTEGER PRIMARY KEY,
    concept_id INTEGER NOT NULL,
    emblem_id TEXT NOT NULL,
    link_type TEXT NOT NULL, -- "illustrates", "exemplifies", "demonstrates", "symbolizes"
    explanation TEXT NOT NULL, -- 1-2 sentences justifying link
    operational BOOLEAN, -- Does emblem show actual operation?
    confidence TEXT, -- "HIGH", "MEDIUM"
    scholarly_support TEXT, -- JSON array of scholar names
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (concept_id) REFERENCES concepts(id),
    FOREIGN KEY (emblem_id) REFERENCES emblems(id)
);
```

### Python Implementation Script: `create_concept_emblem_links.py`

```python
#!/usr/bin/env python3
"""
Script to insert concept-emblem bidirectional links from specification.

Source: docs/CONCEPT_EMBLEM_LINKS_SPECIFICATION.json
Target: data/prototype_data.json (concept_emblem_links)
"""

import json
from pathlib import Path

def load_specification(spec_file: str) -> dict:
    """Load JSON specification from file."""
    with open(spec_file, 'r') as f:
        return json.load(f)

def load_database(db_file: str) -> dict:
    """Load current prototype database."""
    with open(db_file, 'r') as f:
        return json.load(f)

def map_concept_name_to_id(database: dict) -> dict:
    """Create mapping from concept names to IDs."""
    mapping = {}
    for concept in database.get('concepts', []):
        mapping[concept['name']] = concept['id']
    return mapping

def create_concept_emblem_links(spec: dict, db: dict) -> list:
    """
    Generate concept_emblem_links from specification.
    
    Returns: List of link objects ready for insertion.
    """
    concept_map = map_concept_name_to_id(db)
    emblem_map = {emblem['id']: emblem['id'] for emblem in db.get('emblems', [])}
    
    # Also add string-based emblem IDs
    emblem_map.update({emblem['slug']: emblem['id'] for emblem in db.get('emblems', [])})
    
    links = []
    link_id = 1  # Start numbering links
    
    for mapping_group in spec.get('concept_emblem_links', []):
        concept_name = mapping_group.get('concept_name')
        concept_id = mapping_group.get('concept_id') or concept_map.get(concept_name)
        
        if not concept_id:
            print(f"WARNING: Concept '{concept_name}' not found in database")
            continue
        
        for link_data in mapping_group.get('emblem_links', []):
            emblem_id_str = link_data.get('emblem_id')
            
            # Try to resolve emblem ID
            emblem_id = emblem_id_str
            if emblem_id_str not in emblem_map and not isinstance(emblem_id_str, int):
                # Try to find by slug
                emblem_id = None
                for emb in db.get('emblems', []):
                    if emb['slug'] == emblem_id_str or emb['id'] == emblem_id_str:
                        emblem_id = emb['id']
                        break
                if not emblem_id:
                    print(f"WARNING: Emblem '{emblem_id_str}' not found in database")
                    continue
            
            link = {
                'id': link_id,
                'concept_id': concept_id,
                'concept_name': concept_name,
                'emblem_id': emblem_id,
                'emblem_title': link_data.get('emblem_title'),
                'source_book': link_data.get('source_book'),
                'link_type': link_data.get('link_type'),
                'explanation': link_data.get('explanation'),
                'operational': link_data.get('operational'),
                'confidence': link_data.get('confidence'),
                'scholarly_support': link_data.get('scholarly_support', []),
                'justification': link_data.get('justification'),
            }
            links.append(link)
            link_id += 1
    
    return links

def main():
    """Main execution."""
    spec_file = Path(__file__).parent.parent / 'docs' / 'CONCEPT_EMBLEM_LINKS_SPECIFICATION.json'
    db_file = Path(__file__).parent.parent / 'data' / 'prototype_data.json'
    
    print(f"Loading specification from: {spec_file}")
    spec = load_specification(str(spec_file))
    
    print(f"Loading database from: {db_file}")
    db = load_database(str(db_file))
    
    print("Creating concept-emblem links...")
    links = create_concept_emblem_links(spec, db)
    
    print(f"Generated {len(links)} concept-emblem links")
    
    # Add to database
    if 'concept_emblem_links' not in db:
        db['concept_emblem_links'] = []
    
    db['concept_emblem_links'].extend(links)
    
    # Save database
    print(f"Saving updated database to: {db_file}")
    with open(db_file, 'w') as f:
        json.dump(db, f, indent=2)
    
    print("SUCCESS: Concept-emblem links created and inserted")
    print(f"Total links created: {len(links)}")
    print(f"Concepts covered: {len(set(link['concept_id'] for link in links))}")

if __name__ == '__main__':
    main()
```

### Update `build_site.py` to Display Concept-Emblem Links

Add to the concept template rendering:

```python
def render_concept_page(concept: dict, all_data: dict) -> str:
    """Render concept page with linked emblems in sidebar."""
    
    # Find related emblems
    concept_emblem_links = [
        link for link in all_data.get('concept_emblem_links', [])
        if link['concept_id'] == concept['id']
    ]
    
    # Create emblem preview cards
    emblem_previews = []
    for link in concept_emblem_links:
        emblem = next(
            (e for e in all_data['emblems'] if e['id'] == link['emblem_id']),
            None
        )
        if emblem:
            emblem_previews.append({
                'title': emblem['title'],
                'slug': emblem['slug'],
                'link_type': link['link_type'],
                'explanation': link['explanation'],
                'image_url': emblem.get('image_url', ''),
            })
    
    # Render sidebar with emblem cards
    sidebar_html = render_emblem_sidebar(emblem_previews)
    
    # Include in concept template
    concept_html = f"""
    <div class="concept-page">
        <article class="concept-essay">
            {concept['essay']}
        </article>
        <aside class="concept-emblem-sidebar">
            <h3>Emblematic Illustrations</h3>
            {sidebar_html}
        </aside>
    </div>
    """
    return concept_html
```

---

## Part 2: Figure-Emblem Genealogy (Workstream 3)

### Summary of Figure-Emblem Genealogy

**10 Key Figures Mapped:**
1. **Michael Maier** (1568–1622) — CREATOR (Atalanta Fugiens, 50 emblems)
2. **Daniel Cramer** (1568–1637) — CREATOR (Rosicrucian Emblems, 40 emblems)
3. **Heinrich Khunrath** (1560–1605) — CREATOR (Amphitheatrum, cosmological diagrams)
4. **Daniel Stolcius** (1597–after 1650) — CREATOR (Hermetic Garden, 160 emblems)
5. **Paracelsus** (1493–1541) — INFLUENCED-BY (foundational philosophy; no emblems)
6. **Jacob Böhme** (1575–1624) — INFLUENCED-BY (mystical theology; interpretation framework)
7. **Robert Fludd** (1574–1637) — INFLUENCED-BY (cosmological diagrams; Utriusque Cosmi Historia)
8. **Johann Valentin Andreae** (1586–1654) — INFLUENCED-BY (Rosicrucian texts; narrative framework)
9. **Thomas Vaughan** (1622–1666) — INFLUENCED-BY (English transmission; secondary)
10. **Emanuel Swedenborg** (1688–1772) — INFLUENCED-BY (visionary theologian; late synthesis)

**Genealogical Structure:**
```
Renaissance (1493–1541)
    └─ Paracelsus (foundational philosophy)

Renaissance-Early Modern Transition (1550–1605)
    ├─ Khunrath (cosmological diagrams)
    └─ Dee (harmonic mathematics)

Early Modern I: Emblem-Book Generation (1590–1630)
    ├─ Maier (harmonic cosmology; Atalanta Fugiens 1617)
    ├─ Cramer (theological systematization; Rosicrucian Emblems 1617)
    ├─ Fludd (cosmological synthesis; Utriusque Cosmi Historia 1614–1621)
    ├─ Böhme (mystical theology; interpretation framework)
    ├─ Andreae (Rosicrucian narrative; Chymische Hochzeit 1616)
    └─ Stolcius (comprehensive encyclopedia; Hermetic Garden 1624)

Early Modern II: Secondary Transmission (1620–1680)
    └─ Vaughan (English adaptation; Anthroposophia Theomagica 1650)

Enlightenment-Early Romanticism (1680–1800)
    └─ Swedenborg (visionary theology; Arcana Coelestia 1749–1756)
```

### Data Schema for `figure_emblem_genealogy` Table

```sql
CREATE TABLE figure_emblem_genealogy (
    id INTEGER PRIMARY KEY,
    figure_id INTEGER NOT NULL,
    role TEXT NOT NULL, -- "CREATOR", "THEORIST", "INFLUENCED", "INFLUENCED-BY"
    transmission_period TEXT, -- "Renaissance", "Early Modern I", "Enlightenment", etc.
    genealogical_position TEXT, -- ordinal position in transmission
    emblem_books_created TEXT, -- JSON array of book titles/IDs
    emblem_books_studied TEXT, -- JSON array of book titles/IDs
    key_innovations TEXT, -- JSON array of innovations
    influenced_by TEXT, -- JSON array of figure_ids and influence types
    influenced_figures TEXT, -- JSON array of figure_ids influenced
    scholarly_support TEXT, -- JSON array of scholar references
    connection_summary TEXT, -- brief narrative connection
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (figure_id) REFERENCES figures(id)
);
```

### Python Implementation Script: `create_figure_emblem_genealogy.py`

```python
#!/usr/bin/env python3
"""
Script to insert figure-emblem genealogy from specification.

Source: docs/FIGURE_EMBLEM_GENEALOGY_SPECIFICATION.json
Target: data/prototype_data.json (figure_emblem_genealogy)
"""

import json
from pathlib import Path

def load_specification(spec_file: str) -> dict:
    """Load JSON specification from file."""
    with open(spec_file, 'r') as f:
        return json.load(f)

def load_database(db_file: str) -> dict:
    """Load current prototype database."""
    with open(db_file, 'r') as f:
        return json.load(f)

def map_figure_name_to_id(database: dict) -> dict:
    """Create mapping from figure names to IDs."""
    mapping = {}
    for figure in database.get('figures', []):
        mapping[figure['name']] = figure['id']
    return mapping

def create_figure_genealogy_entries(spec: dict, db: dict) -> list:
    """
    Generate figure_emblem_genealogy entries from specification.
    
    Returns: List of genealogy objects ready for insertion.
    """
    figure_map = map_figure_name_to_id(db)
    entries = []
    entry_id = 1
    
    for figure_data in spec.get('figures_genealogy', []):
        figure_name = figure_data.get('figure_name')
        figure_id = figure_data.get('figure_id') or figure_map.get(figure_name)
        
        if not figure_id:
            print(f"WARNING: Figure '{figure_name}' not found in database")
            continue
        
        # Process influenced_by relationships
        influenced_by = []
        for influence in figure_data.get('influenced_by', []):
            influenced_figure_name = influence.get('figure_name')
            influenced_figure_id = influence.get('figure_id') or figure_map.get(influenced_figure_name)
            if influenced_figure_id:
                influenced_by.append({
                    'figure_id': influenced_figure_id,
                    'figure_name': influenced_figure_name,
                    'influence_type': influence.get('influence_type'),
                    'how': influence.get('how'),
                })
        
        # Process influenced_figures relationships
        influenced_figures = []
        for influenced in figure_data.get('influenced_figures', []):
            influenced_figure_name = influenced.get('figure_name')
            influenced_figure_id = influenced.get('figure_id') or figure_map.get(influenced_figure_name)
            if influenced_figure_id:
                influenced_figures.append({
                    'figure_id': influenced_figure_id,
                    'figure_name': influenced_figure_name,
                    'influence_type': influenced.get('influence_type'),
                    'how': influenced.get('how'),
                })
        
        entry = {
            'id': entry_id,
            'figure_id': figure_id,
            'figure_name': figure_name,
            'birth_year': figure_data.get('birth_year'),
            'death_year': figure_data.get('death_year'),
            'role': figure_data.get('role'),
            'transmission_period': figure_data.get('transmission_period'),
            'genealogical_position': figure_data.get('genealogical_position'),
            'emblem_books_created': figure_data.get('emblem_books_created', []),
            'emblem_books_studied': figure_data.get('emblem_books_studied', []),
            'key_innovations': figure_data.get('key_innovations', []),
            'influenced_by': influenced_by,
            'influenced_figures': influenced_figures,
            'scholarly_support': figure_data.get('scholarly_support', []),
            'scholarly_debates': figure_data.get('scholarly_debates', []),
            'key_works': figure_data.get('key_works', []),
            'connection_summary': figure_data.get('connection_summary'),
        }
        entries.append(entry)
        entry_id += 1
    
    return entries

def main():
    """Main execution."""
    spec_file = Path(__file__).parent.parent / 'docs' / 'FIGURE_EMBLEM_GENEALOGY_SPECIFICATION.json'
    db_file = Path(__file__).parent.parent / 'data' / 'prototype_data.json'
    
    print(f"Loading specification from: {spec_file}")
    spec = load_specification(str(spec_file))
    
    print(f"Loading database from: {db_file}")
    db = load_database(str(db_file))
    
    print("Creating figure-emblem genealogy entries...")
    entries = create_figure_genealogy_entries(spec, db)
    
    print(f"Generated {len(entries)} figure-emblem genealogy entries")
    
    # Add to database
    if 'figure_emblem_genealogy' not in db:
        db['figure_emblem_genealogy'] = []
    
    db['figure_emblem_genealogy'].extend(entries)
    
    # Save database
    print(f"Saving updated database to: {db_file}")
    with open(db_file, 'w') as f:
        json.dump(db, f, indent=2)
    
    print("SUCCESS: Figure-emblem genealogy entries created and inserted")
    print(f"Total entries created: {len(entries)}")

if __name__ == '__main__':
    main()
```

### Update `build_site.py` to Display Figure-Emblem Genealogy

Add to the figure template rendering:

```python
def render_figure_genealogy_section(figure: dict, all_data: dict) -> str:
    """Render genealogy section in figure biography."""
    
    # Find genealogy entry
    genealogy = next(
        (g for g in all_data.get('figure_emblem_genealogy', [])
         if g['figure_id'] == figure['id']),
        None
    )
    
    if not genealogy:
        return ""
    
    # Build genealogy HTML
    html = f"""
    <section class="figure-genealogy">
        <h3>Position in Emblem Tradition</h3>
        
        <div class="genealogy-metadata">
            <p><strong>Role:</strong> {genealogy['role']}</p>
            <p><strong>Period:</strong> {genealogy['transmission_period']}</p>
            <p><strong>Position:</strong> {genealogy['genealogical_position']}</p>
        </div>
    """
    
    # Emblem books created
    if genealogy.get('emblem_books_created'):
        html += "<div class='emblem-books-created'><h4>Emblem Books Created:</h4><ul>"
        for book in genealogy['emblem_books_created']:
            html += f"<li><strong>{book.get('title', 'Unknown')}</strong> ({book.get('year', 'n.d.')}) — {book.get('description', '')}</li>"
        html += "</ul></div>"
    
    # Key innovations
    if genealogy.get('key_innovations'):
        html += "<div class='key-innovations'><h4>Key Innovations:</h4><ul>"
        for innovation in genealogy['key_innovations']:
            html += f"<li>{innovation}</li>"
        html += "</ul></div>"
    
    # Genealogical connections
    if genealogy.get('influenced_by'):
        html += "<div class='influenced-by'><h4>Influenced By:</h4><ul>"
        for influence in genealogy['influenced_by']:
            html += f"<li><strong>{influence.get('figure_name')}</strong>: {influence.get('how')}</li>"
        html += "</ul></div>"
    
    if genealogy.get('influenced_figures'):
        html += "<div class='influenced-figures'><h4>Influenced:</h4><ul>"
        for influenced in genealogy['influenced_figures']:
            html += f"<li><strong>{influenced.get('figure_name')}</strong>: {influenced.get('how')}</li>"
        html += "</ul></div>"
    
    # Connection summary
    if genealogy.get('connection_summary'):
        html += f"<div class='connection-summary'><p><em>{genealogy['connection_summary']}</em></p></div>"
    
    html += "</section>"
    return html
```

---

## Part 3: Verification and Testing

### Verification Checklist

After implementing the mappings:

- [ ] All 54 concept-emblem links inserted into database
- [ ] All 10 figure-emblem genealogy entries inserted into database
- [ ] Concept pages display related emblems in sidebar
- [ ] Figure pages display genealogy section
- [ ] Bidirectional links work: concept → emblems → back to concept
- [ ] Figure genealogy shows both "influenced_by" and "influenced_figures" relationships
- [ ] No broken links or missing references
- [ ] Scholarly support references are accurate
- [ ] Site deploys successfully with new mappings

### Test Queries (for verification)

```sql
-- Concept with most emblems
SELECT concept_id, COUNT(*) as emblem_count 
FROM concept_emblem_links 
GROUP BY concept_id 
ORDER BY emblem_count DESC 
LIMIT 5;

-- All figures with role=CREATOR
SELECT figure_name, role, emblem_books_created 
FROM figure_emblem_genealogy 
WHERE role = 'CREATOR';

-- Influence network: figures influenced by Maier
SELECT influenced_figures 
FROM figure_emblem_genealogy 
WHERE figure_name = 'Michael Maier';

-- Maier Atalanta Fugiens emblems used in mappings
SELECT COUNT(*) 
FROM concept_emblem_links 
WHERE source_book = 'Atalanta Fugiens';
```

---

## Part 4: Deployment

### Friday Deployment Checklist

1. **Run mapping creation scripts:**
   ```bash
   python scripts/create_concept_emblem_links.py
   python scripts/create_figure_emblem_genealogy.py
   ```

2. **Rebuild site:**
   ```bash
   python scripts/build_site.py
   ```

3. **Test locally:**
   - Navigate to concept pages (e.g., "Nigredo") and verify emblem links display
   - Navigate to figure pages (e.g., "Michael Maier") and verify genealogy section displays
   - Check for broken links or missing images

4. **Deploy to GitHub Pages:**
   ```bash
   git add -A
   git commit -m "Implement Workstream 2-3: Concept-emblem and figure-emblem mappings (54 links, 10 figures)"
   git push origin main
   ```

5. **Verify live site:** https://t3dy.github.io/TheosophicalAlchemyDB/

---

## Summary

**Workstream 2 (Concept-Emblem Mapping):**
- 18 core concepts mapped
- 54 total concept-emblem links (3 per concept)
- Primary sources: Maier (38 links), Cramer (12 links), Stolcius (4 links)
- Link types: "illustrates", "exemplifies", "demonstrates", "symbolizes"
- Confidence levels: HIGH or MEDIUM

**Workstream 3 (Figure-Emblem Genealogy):**
- 10 key figures mapped
- 4 emblem-book creators (Maier, Cramer, Khunrath, Stolcius)
- 6 theoretical/transmitter figures (Paracelsus, Böhme, Fludd, Andreae, Vaughan, Swedenborg)
- Genealogical timeline: Renaissance → Early Modern I → Early Modern II → Enlightenment
- Bidirectional influence relationships: who influenced whom and how

**Database Integration:**
- Two new tables: `concept_emblem_links` and `figure_emblem_genealogy`
- Specification files in machine-readable JSON format
- Python implementation scripts provided
- Updates to `build_site.py` to display mappings on concept and figure pages

**Status:** Ready for implementation and deployment. All specifications complete and vetted.

---

**Prepared by:** Claude (Agent)  
**Date:** 2026-05-26  
**Next Steps:** Execute implementation scripts and deploy to live site (Friday deployment window)
