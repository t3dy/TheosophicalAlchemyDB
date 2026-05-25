# TheosophicalAlchemyDB — Deployment & Operations Guide

## Project Status

✓ **Initial Release** — Deployed and live at GitHub Pages  
✓ **Core Architecture** — Functional knowledge portal with 50-entry prototype  
✓ **Repository** — https://github.com/t3dy/TheosophicalAlchemyDB  
✓ **Live Site** — https://t3dy.github.io/TheosophicalAlchemyDB/

---

## Quick Start

### Local Development

```bash
cd C:\Dev\TheosophicalAlchemyDB

# Start development server
cd docs
python -m http.server 8000

# Visit http://localhost:8000
```

### Project Structure

```
C:\Dev\TheosophicalAlchemyDB/
├── docs/                    # GitHub Pages (deployed site)
│   ├── index.html          # Main portal page
│   ├── style.css           # Dark scholarly design
│   ├── app.js              # JavaScript application logic
│   └── data/
│       └── prototype_data.json  # 50 figures, concepts, texts
├── site/                    # Source site files
├── scripts/
│   ├── build_site.py       # Generate static site from data
│   └── ingest_pdfs.py      # Process PDFs and convert to markdown
├── data/
│   ├── prototype_data.json  # Live dataset (50 entries per category)
│   └── theosophical_alchemy.db  # SQLite database (future)
├── CLAUDE.md               # Project overview
├── PHASESTATUS.md          # Development phases and progress
└── README.md               # Public-facing summary
```

---

## GitHub Pages Deployment

The site is automatically deployed via GitHub Pages from the `docs/` directory.

### Manual Deployment Steps

1. **Build the site:**
   ```bash
   python scripts/build_site.py
   ```

2. **Update docs directory:**
   ```bash
   cp -r site/* docs/
   cp data/prototype_data.json docs/data/
   ```

3. **Commit and push:**
   ```bash
   git add docs/
   git commit -m "Update site"
   git push origin main
   ```

4. **Verify at:** https://t3dy.github.io/TheosophicalAlchemyDB/

---

## Content Management

### Adding New Entries

Edit `data/prototype_data.json` to add new figures, concepts, or texts:

```json
{
  "figures": [...],
  "concepts": [...],
  "texts": [...]
}
```

Then rebuild the site:
```bash
python scripts/build_site.py
```

### PDF Ingestion

To ingest the 62 source PDFs from E:\pdf\ directories:

```bash
python scripts/ingest_pdfs.py
```

This will:
- Extract text from PDFs/EPUBs
- Create markdown summaries
- Populate SQLite database
- Index key concepts

---

## Technology Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript (no frameworks)
- **Mapping:** Leaflet.js (interactive Europe map)
- **Data:** JSON (prototype), SQLite (corpus database)
- **Hosting:** GitHub Pages
- **Build:** Python scripts
- **Design:** Dark scholarly aesthetic (parchment + burnt sienna)

---

## Features

### 1. Card-Based Gallery
- Index card summaries (100-150 words)
- Click-to-expand modal essays (300-500 words)
- Responsive grid layout (4 columns on desktop, 1 on mobile)

### 2. Interactive Map
- Leaflet.js map of Europe
- 50 figure locations (red markers)
- 50 text publication locations (blue markers)
- 6 major learning centers (gold markers)
- Hover tooltips with summaries
- Click integration to open full essays

### 3. Concept Linking
- 50 philosophical and alchemical concepts
- Cross-referenced with figures and texts
- Categories: stages, principles, practices, symbols

### 4. Scholar Attribution
- Integrated scholarship from Yates, Godwin, Churton, Szulakoska, Zuber
- Primary scholars: ["Author Name", ...] in each entry
- Full citations in modal essays

---

## Scholarship Focus

### Key Scholars
- **Frances Yates** — Rosicrucian intellectual history
- **Joscelyn Godwin** — Hermetic philosophy
- **Tobias Churton** — Esoteric Christianity
- **Urszula Szulakowska** — Alchemical iconography
- **Mike Zuber** — Spiritual alchemy (Böhme–Atwood narrative)

### Historical Period
**16th–19th centuries** with emphasis on:
- Rosicrucian manifestos (1614–1616)
- Spiritual alchemy synthesis (1575–1910)
- Enlightenment mysticism (1700–1850)

---

## Performance & Optimization

### Current Metrics
- **Site size:** ~50KB (HTML + CSS + JS)
- **Data size:** 144KB (50-entry JSON)
- **Load time:** <2 seconds (full page)
- **Mobile responsive:** Yes (tested on 375px width)

### Scaling
- Current: 50 entries per category
- Phase 1 target: 60 concepts, 40 figures, 35 texts
- Final target: 100+ dictionary terms, 20–40 emblems, 12–18 essays

---

## Next Steps

1. **PDF Corpus Integration** (Phase 1)
   - Run `scripts/ingest_pdfs.py` on 62 source files
   - Extract 500+ key passages
   - Auto-generate concept index

2. **Emblem Cataloging** (Phase 3)
   - Source 20–40 emblems from emblem books
   - Create SVG/image gallery
   - Link to concepts and figures

3. **Concept Network Visualization** (Phase 5–6)
   - D3.js relationship network
   - Interactive concept graph
   - Full-text search across corpus

4. **Backend Integration** (Optional)
   - SQLite database for corpus
   - Search API
   - Dynamic content management

---

## Troubleshooting

### Site not loading from GitHub Pages
1. Check repository settings: Settings → Pages
2. Ensure source is set to "Deploy from a branch" (main branch, /docs folder)
3. Verify docs/index.html exists
4. Clear browser cache and hard refresh

### Data not loading in the portal
1. Check docs/data/prototype_data.json exists
2. Verify JSON is valid: `python -m json.tool docs/data/prototype_data.json`
3. Check browser console for CORS errors
4. Ensure app.js is loading the correct path

### Local server not working
1. Make sure port 8000 is not in use: `netstat -ano | findstr :8000`
2. Kill existing process: `taskkill /PID <PID> /F`
3. Restart server: `python -m http.server 8000`

---

## Contributing

To contribute new entries or improvements:

1. Create a new branch: `git checkout -b feature/new-entry`
2. Edit `data/prototype_data.json` with new data
3. Run `python scripts/build_site.py` to rebuild
4. Test locally: `python -m http.server 8000`
5. Commit: `git add . && git commit -m "Add: [description]"`
6. Push: `git push origin feature/new-entry`
7. Create Pull Request on GitHub

---

## License

This project is part of a digital humanities research initiative. All scholarly content is derived from published academic sources. See README.md for detailed attribution.

---

## Contact & Support

**Repository:** https://github.com/t3dy/TheosophicalAlchemyDB  
**Project Owner:** t3dy  
**Email:** ted.hand@gmail.com

For issues, questions, or contributions, please use GitHub Issues or contact the project owner.

---

**Last Updated:** 2026-05-25  
**Version:** 1.0 (Initial Release)
