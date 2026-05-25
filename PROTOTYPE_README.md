# Rosicrucianism & Theosophical Alchemy Portal — Prototype

## Overview

This is a **functional prototype** of the knowledge portal with **50 entries each** for:
- **Historical Figures** (Yates, Godwin, Akerman, Churton, Szulakoska, and Zuber scholarship focus)
- **Concepts** (alchemical stages, hermetic principles, spiritual practices, integrated with Zuber's spiritual alchemy framework)
- **Primary Texts** (Rosicrucian manifestos, alchemical treatises, mystical writings, plus modern scholarship)
- **Interactive Map** of Europe showing figures, texts, and learning centers (with 50 locations plotted)

## Features

### 1. Card-Based Gallery Interface
- **Index Card Summaries**: Each entry displays a concise summary
- **Click-to-Expand Essays**: Click any card to open a modal with the full essay
- **Responsive Design**: Works on desktop and mobile
- **Dark Scholarly Aesthetic**: Burnt sienna and parchment color scheme

### 2. Interactive Map of Europe
- **Leaflet.js-powered** interactive map
- **Three marker types**:
  - **Red circles** = Historical figures (clickable)
  - **Blue circles** = Primary texts and their publication locations
  - **Gold diamonds** = Major learning centers (Prague, Florence, Tübingen, London, Amsterdam, Paris)
- **Hover Tooltips**: Hover over markers to see index card-length summaries
- **Click Integration**: Click a marker to open the full essay for that figure/text

### 3. Navigation
- **Tab-based sections**: Switch between Figures, Concepts, Texts, and Map
- **Smooth animations**: Fade in/out transitions between sections

## How to Run

### Option 1: Using Claude Code's Preview Server
1. Click the **Preview** button (Launch icon) in Claude Code
2. Select the `rosicrucianism-portal` configuration
3. Navigate to `http://localhost:8080` in your browser

### Option 2: Using Python's Built-in Server
```bash
cd C:\Dev\Rosicrucianism\site
python -m http.server 8080
```
Then open `http://localhost:8080` in your browser.

### Option 3: Using Node.js http-server
```bash
cd C:\Dev\Rosicrucianism\site
npx http-server
```

## Data Structure

All prototype data is loaded from `../data/prototype_data.json`:

```json
{
  "figures": [
    {
      "id": 1,
      "name": "Johann Valentin Andreae",
      "birth_year": 1586,
      "death_year": 1654,
      "nationality": "German",
      "location": "Tübingen, Germany",
      "lat": 48.5216,
      "lng": 9.0577,
      "summary": "Index card summary...",
      "essay": "Full essay text...",
      "scholars": ["Yates", "Godwin"],
      "key_works": [...]
    },
    ...
  ],
  "concepts": [...],
  "texts": [...]
}
```

## Prototype Data: 50 Entries Each (Expanded Session 3)

### Figures (Focus: Yates, Godwin, Akerman, Churton, Szulakoska + Zuber)
1–40. Original 40 figures (Andreae, Dee, Fludd, Paracelsus, Böhme, Ashmole, Swedenborg, etc.)
41. Mary Anne Atwood (Spiritual alchemist, Suggestive Inquiry author)
42. Anna Zieglerin (Female alchemist, Reformation Germany)
43. Johann Siebmacher (Publisher, Wasserstein der Weisen)
44. George Cheyne (Medical alchemist, physician)
45. Johann Arndt (Lutheran mystic, True Christianity)
46. Jane Lead (Visionary, Philadelphian Society)
47. Isaac Newton (Mathematician-alchemist, secret hermetic studies)
48. Henry More (Cambridge Platonist, mystic philosopher)
49. Benedict Chabotas (Alchemical adept)
50. Adam McLean (Contemporary alchemical scholar, emblem researcher)

### Concepts (50)
1–40. Original 40 concepts (Nigredo, Albedo, Rubedo, Theosis, Hieros Gamos, Lapis, etc.)
41. Inner Transformation (Consciousness development through alchemical stages)
42. Hermetic Spirituality (Hermetic philosophy integrated with Christian mysticism)
43. Alchemical Hermaphrodite (Union of opposites, symbol of integrated consciousness)
44. Theurgic Practice (Divine work through ritual and symbolism)
45. Spiritual Chemistry (Laboratory operations as consciousness transformation)
46. Divine Names (Kabbalistic practice of sacred language invocation)
47. Mystical Union (Henosis, direct experience of divine reality)
48. Regeneration (Spiritual rebirth through alchemical stages)
49. Embodied Knowledge (Understanding through direct engagement, not abstraction)
50. Hermetic Correspondence (All levels of reality interconnected, "as above, so below")

### Texts (50)
1–40. Original 40 texts (Fama Fraternitatis, Confessio, Chymische Hochzeit, etc.)
41. Suggestive Inquiry into the Hermetic Mystery (Mary Anne Atwood, 1850, definitive modern treatise)
42. Wasserstein der Weisen (Johann Siebmacher, 1619, spiritual alchemy methodology)
43. True Christianity (Johann Arndt, 1606, alchemical symbolism in Protestant theology)
44. The Revelation of Revelations (Jane Lead, 1683, visionary mystical theology)
45. Lion's Blood (Anonymous, 1528, alchemical cosmology and symbolism)
46. The Hydriolithic or Watery Tract (1696, water-based alchemical processes)
47. Spiritual Alchemy: From Jacob Boehme to Mary Anne Atwood (Mike Zuber, 2007, definitive scholarly study)
48. Arcana or Mysteries of Love and Eloquence (1691, alchemy and rhetoric as divine communication)
49. The Golden Chain of Homer (1723, cosmological hierarchy and Neoplatonic integration)
50. An Account of the Behmenists (1710, Böhmean communities and transmission)

## Map Visualization

The interactive map shows:
- **Geographic distribution** of Rosicrucian figures across Europe
- **Publication locations** of key texts
- **Major learning centers** where Rosicrucian ideas circulated:
  - Prague (Rudolf II's alchemical court)
  - Florence (Renaissance Neoplatonism)
  - Tübingen (Andreae's theological reform)
  - London (English Rosicrucian-Masonic synthesis)
  - Amsterdam (Martinist center)
  - Paris (French illuminism)

## Usage

### Browse Figures
1. Click **"Figures"** tab
2. Scroll through 40 historical figures
3. Click any card to read full biography
4. See related concepts and key works

### Explore Concepts
1. Click **"Concepts"** tab
2. Browse 40 philosophical and alchemical ideas
3. Click to expand and understand each concept's role in tradition

### Study Primary Texts
1. Click **"Texts"** tab
2. Review 40 canonical works (manifestos, treatises, mystical writings)
3. Click to read detailed summaries with publication info

### Interact with Map
1. Click **"Map"** tab
2. Pan and zoom to explore Europe
3. Hover over markers to see summaries
4. Click markers to open full essays
5. Use legend to understand marker types

## Architecture

```
C:\Dev\Rosicrucianism\
├── site/
│   ├── index.html           # Main page structure
│   ├── style.css            # Dark scholarly design
│   ├── app.js               # Card gallery + map logic
│   └── (prototype_data.json) # Auto-loaded from ../data/
├── data/
│   └── prototype_data.json   # 40 figures, 40 concepts, 40 texts
└── .claude/
    └── launch.json          # Preview server config
```

## Next Steps (Phase 1)

This prototype demonstrates:
✓ Card-based UI with index card summaries
✓ Click-to-expand essay modals
✓ Interactive Europe map with location plotting
✓ Hover tooltips with index card info
✓ Responsive design
✓ Focus on key scholars: Yates, Godwin, Akerman, Churton, Szulakoska

Phase 1 will:
- Expand data to full corpus (131 PDFs)
- Add search and filter functionality
- Implement full SQLite backend
- Build emblem book section
- Add concept relationship visualization
- Create full static site generation pipeline

## Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Mapping**: Leaflet.js
- **Styling**: Dark scholarly aesthetic (parchment + burnt sienna)
- **Server**: Python http.server (can use any static server)
- **Data Format**: JSON

## Color Palette

- **Background**: #f5f0e8 (Warm parchment)
- **Text**: #2c2418 (Dark brown)
- **Accent**: #8b4513 (Burnt sienna)
- **Accent-light**: #d4a574 (Tan/gold)
- **Header**: #2c2418 (Dark background)

## Browser Compatibility

Works on:
- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (responsive)

## Known Limitations

1. Data is embedded in JSON file (future: SQLite backend)
2. No search functionality yet (planned Phase 1)
3. No emblem images or emblem book section (planned Phase 3)
4. Map is read-only (future: interactive editing)

## Feedback & Future Development

This prototype validates the core concept:
- **Card interface works** — Clean, clickable summaries
- **Modals work** — Full essays accessible with one click
- **Map works** — Interactive visualization of Rosicrucian geography
- **Responsive design** — Works on multiple screen sizes

Future phases will expand to full knowledge portal with:
- Full research corpus (131 PDFs)
- 8-12 emblem books with 20-40 emblems
- 100+ dictionary terms
- 12-18 thematic essays
- Scholar profiles
- Full-text search
- Concept relationship network visualization
- GitHub Pages deployment

---

**Created:** 2026-05-24  
**Prototype Status:** Phase 0 (Expanded Proof-of-Concept — 50 entries with Zuber scholarship)  
**Last Updated:** 2026-05-25 (Expanded to 50 entries per category with Mike Zuber scholarship integration)
