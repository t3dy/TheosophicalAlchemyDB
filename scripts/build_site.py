#!/usr/bin/env python3
"""
Static Site Generator for TheosophicalAlchemyDB
Builds the complete interactive knowledge portal from JSON data
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
SITE_DIR = PROJECT_ROOT / "site"
DB_PATH = DATA_DIR / "theosophical_alchemy.db"
PROTOTYPE_DATA = DATA_DIR / "prototype_data.json"

def load_prototype_data():
    if PROTOTYPE_DATA.exists():
        with open(PROTOTYPE_DATA, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"figures": [], "concepts": [], "texts": []}

def load_corpus_sources():
    sources = []
    if DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM sources")
            for row in c.fetchall():
                sources.append({'id': row[0], 'filename': row[1], 'title': row[2],
                                 'authors': row[3], 'year': row[4], 'source_type': row[5],
                                 'word_count': row[7]})
        except:
            pass
        conn.close()
    return sources

def filter_bar_html(section, filters):
    selects = ''
    for (attr, placeholder) in filters:
        selects += f'\n        <select class="filter-select" data-filter="{attr}" data-section="{section}"><option value="">{placeholder}</option></select>'
    selects += f'''
        <select class="filter-select" data-filter="sort" data-section="{section}">
          <option value="default">Sort: Default</option>
          <option value="alpha">A&ndash;Z</option>
          <option value="alpha-rev">Z&ndash;A</option>
          <option value="chrono">Oldest First</option>
          <option value="chrono-rev">Newest First</option>
        </select>
        <button class="filter-reset btn-sm" data-section="{section}">Reset</button>'''
    return f'''<div class="section-controls">
        <div class="filter-bar">{selects}
        </div>
        <span id="{section}-count" class="section-count"></span>
      </div>
      <div id="{section}-gallery" class="gallery"></div>'''

def generate_index_html():
    prototype = load_prototype_data()
    sources = load_corpus_sources()
    stats = {
        'figures':  len(prototype.get('figures', [])),
        'concepts': len(prototype.get('concepts', [])),
        'texts':    len(prototype.get('texts', [])),
        'emblems':  len(prototype.get('emblems', [])),
        'sources':  len(sources)
    }
    figures_filters  = [('nationality', 'All Nationalities'), ('scholar', 'All Scholars'), ('century', 'All Centuries')]
    concepts_filters = [('category', 'All Categories')]
    texts_filters    = [('language', 'All Languages'), ('century', 'All Centuries')]
    emblems_filters  = [('source_book', 'All Books'), ('type', 'All Types')]

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TheosophicalAlchemyDB - Rosicrucian &amp; Spiritual Alchemy Portal</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
</head>
<body>

<!-- HEADER -->
<header class="main-header">
  <div class="header-content">
    <div class="header-top-row">
      <h1>TheosophicalAlchemyDB</h1>
      <button id="dark-mode-toggle" class="dark-toggle">&#9790; Dark</button>
    </div>
    <p class="subtitle">Interactive Knowledge Portal: Rosicrucian &amp; Spiritual Alchemy Traditions (16th&ndash;19th c.)</p>
    <div class="portal-stats">
      <span class="stat-box"><span class="stat-number" id="stat-figures">{stats['figures']}</span><span class="stat-label">Historical Figures</span></span>
      <span class="stat-box"><span class="stat-number" id="stat-concepts">{stats['concepts']}</span><span class="stat-label">Concepts &amp; Principles</span></span>
      <span class="stat-box"><span class="stat-number" id="stat-texts">{stats['texts']}</span><span class="stat-label">Scholarly Texts</span></span>
      <span class="stat-box"><span class="stat-number" id="stat-emblems">{stats['emblems']}</span><span class="stat-label">Emblems</span></span>
    </div>
    <div class="search-bar-container">
      <input type="text" id="global-search" placeholder="Search figures, concepts, texts, emblems&hellip;" autocomplete="off" aria-label="Search">
      <button id="search-clear" aria-label="Clear search">&times;</button>
      <div id="search-results-panel" hidden></div>
    </div>
  </div>
</header>

<!-- NAV -->
<nav class="main-nav">
  <button class="nav-btn active" data-section="figures">Figures</button>
  <button class="nav-btn" data-section="concepts">Concepts</button>
  <button class="nav-btn" data-section="texts">Texts</button>
  <button class="nav-btn" data-section="emblems">Emblems</button>
  <button class="nav-btn" data-section="essays">Essays</button>
  <button class="nav-btn" data-section="map">Map</button>
  <button class="nav-btn" data-section="timeline">Timeline</button>
  <button class="nav-btn" data-section="about">About</button>
  <button class="nav-btn nav-serendipity" id="serendipity-btn">&#10022; Surprise</button>
</nav>

<!-- MAIN -->
<main class="portal-container">

  <section id="figures" class="section active">
    <div class="section-header"><h2>Historical Figures</h2><p>Explore {stats['figures']} key figures in Rosicrucian and spiritual alchemy traditions</p></div>
    {filter_bar_html('figures', figures_filters)}
  </section>

  <section id="concepts" class="section">
    <div class="section-header"><h2>Concepts &amp; Principles</h2><p>Understand {stats['concepts']} central philosophical and alchemical concepts</p></div>
    {filter_bar_html('concepts', concepts_filters)}
  </section>

  <section id="texts" class="section">
    <div class="section-header"><h2>Scholarly Texts</h2><p>Study {stats['texts']} foundational and contemporary texts</p></div>
    {filter_bar_html('texts', texts_filters)}
  </section>

  <section id="emblems" class="section">
    <div class="section-header"><h2>Emblem Gallery</h2><p>Browse {stats['emblems']} emblems from Rosicrucian and alchemical emblem books</p></div>
    {filter_bar_html('emblems', emblems_filters)}
  </section>

  <section id="essays" class="section">
    <div class="section-header"><h2>Thematic Essays</h2><p>Cross-cutting scholarly essays on Rosicrucian and alchemical traditions</p></div>
    <div class="section-controls">
      <div class="filter-bar">
        <select class="filter-select" data-filter="sort" data-section="essays">
          <option value="default">Sort: Default</option>
          <option value="alpha">A&ndash;Z</option>
          <option value="alpha-rev">Z&ndash;A</option>
        </select>
        <button class="filter-reset btn-sm" data-section="essays">Reset</button>
      </div>
      <span id="essays-count" class="section-count"></span>
    </div>
    <div id="essays-gallery" class="gallery"></div>
  </section>

  <section id="map" class="section">
    <div class="section-header"><h2>Geographic Distribution</h2><p>Explore the historical geography of Rosicrucian figures and text publication</p></div>
    <div id="map-layer-controls" class="map-controls">
      <div class="map-legend">
        <label><input type="checkbox" id="layer-figures" checked><span class="legend-dot figures"></span> Figures</label>
        <label><input type="checkbox" id="layer-texts" checked><span class="legend-dot texts"></span> Texts</label>
        <label><input type="checkbox" id="layer-emblems" checked><span class="legend-dot emblems"></span> Emblem Centers</label>
        <label><input type="checkbox" id="layer-centers" checked><span class="legend-dot centers"></span> Learning Centers</label>
        <label><input type="checkbox" id="layer-lines"><span class="legend-dot lines"></span> Influence Lines</label>
      </div>
      <div class="map-date-filter">
        <span>Date range:</span>
        <span id="map-date-from">1400</span>
        <div class="slider-row">
          <input type="range" id="map-slider-from" min="1400" max="1800" value="1400" step="10">
          <input type="range" id="map-slider-to"   min="1400" max="1800" value="1800" step="10">
        </div>
        <span id="map-date-to">1800</span>
      </div>
    </div>
    <div class="map-wrap">
      <div id="map-container" class="map-container"></div>
      <div id="map-side-panel" class="map-side-panel">
        <div class="map-side-header">
          <h3 id="map-side-title"></h3>
          <button id="map-side-close" class="map-side-close">&times;</button>
        </div>
        <div id="map-side-content" class="map-side-content"></div>
      </div>
    </div>
  </section>

  <section id="timeline" class="section">
    <div class="section-header"><h2>Historical Timeline</h2><p>Key events from 1317 to 1850 in Rosicrucian and alchemical traditions</p></div>
    <div class="timeline-controls">
      <button class="tl-filter active" data-category="all">All Events</button>
      <button class="tl-filter" data-category="historical">Historical</button>
      <button class="tl-filter" data-category="text">Publications</button>
      <button class="tl-filter" data-category="figure">Figures</button>
      <button class="tl-filter" data-category="discovery">Discoveries</button>
    </div>
    <div id="timeline-container" class="timeline-container"></div>
  </section>

  <section id="about" class="section">
    <div class="section-header"><h2>About This Portal</h2></div>
    <div class="about-content">
      <h3>Project Overview</h3>
      <p>TheosophicalAlchemyDB is a comprehensive digital humanities resource documenting the history and significance of Rosicrucian and spiritual alchemy traditions from the 16th to 19th centuries.</p>
      <h3>Scholarly Framework</h3>
      <p>This portal integrates scholarship from key historians including Frances Yates, Joscelyn Godwin, Tobias Churton, Urszula Szulakowska, and Mike Zuber&rsquo;s definitive work on spiritual alchemy from Jacob B&ouml;hme to Mary Anne Atwood.</p>
      <h3>Data Sources</h3>
      <p>The portal incorporates {stats['sources']} primary and secondary sources, including manifestos, treatises, biographical materials, and contemporary scholarly analysis.</p>
      <h3>Navigation Tips</h3>
      <ul>
        <li>Use the <strong>search bar</strong> at the top to find any figure, concept, text, or emblem instantly</li>
        <li>Click <strong>&#10022; Surprise</strong> in the nav for a random entity</li>
        <li>In any concept modal, click <strong>&ldquo;Browse all entries tagged with this concept&rdquo;</strong> to see all related figures, texts, and emblems</li>
        <li>Share any open modal with the <strong>Share</strong> button &mdash; or bookmark the URL directly</li>
        <li>Use <strong>Compare</strong> to view two entries side by side</li>
        <li>On the <strong>Map</strong>, use the date slider to filter markers by century, and toggle Influence Lines to visualise intellectual transmission</li>
      </ul>
      <h3>Technology</h3>
      <p>Built with vanilla JavaScript, Leaflet.js for mapping, and a comprehensive database infrastructure supporting both historical scholarship and interactive exploration.</p>
      <h3>Citation</h3>
      <p><strong>TheosophicalAlchemyDB</strong> (2026). Interactive Portal of Rosicrucian and Theosophical Alchemy. <a href="https://github.com/t3dy/TheosophicalAlchemyDB">github.com/t3dy/TheosophicalAlchemyDB</a></p>
    </div>
  </section>

</main>

<!-- MODAL -->
<div id="modal" class="modal">
  <div class="modal-content">
    <div class="modal-toolbar">
      <div class="modal-nav-left">
        <button id="modal-back" class="modal-back" hidden>&#8592; Back</button>
        <span id="modal-breadcrumb" class="modal-breadcrumb"></span>
      </div>
      <div class="modal-actions">
        <button id="modal-compare" class="modal-action-btn" title="Compare side by side">&#8862; Compare</button>
        <button id="modal-share"   class="modal-action-btn" title="Copy shareable link">&#8679; Share</button>
        <button id="modal-close"   class="modal-close" aria-label="Close">&times;</button>
      </div>
    </div>
    <div id="modal-body"></div>
  </div>
</div>

<!-- COMPARE OVERLAY -->
<div id="compare-modal" hidden>
  <div class="compare-wrap">
    <button id="compare-close" class="compare-close">&times; Close Compare</button>
    <div class="compare-panels">
      <div id="compare-panel-a" class="compare-panel"></div>
      <div class="compare-divider"></div>
      <div id="compare-panel-b" class="compare-panel"></div>
    </div>
  </div>
</div>

<!-- CONCEPT BROWSER OVERLAY -->
<div id="concept-browser" hidden>
  <div class="cb-wrap">
    <div class="cb-header">
      <h2 id="cb-title"></h2>
      <button id="cb-close" class="cb-close">&times;</button>
    </div>
    <div id="cb-body" class="cb-body"></div>
  </div>
</div>

<footer class="main-footer">
  <p>&copy; 2026 TheosophicalAlchemyDB. Digital Humanities Research Portal.</p>
</footer>

<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
<script src="app.js"></script>
</body>
</html>
"""
    return html

def generate_enhanced_css():
    css = """/* TheosophicalAlchemyDB -- Enhanced Dark Scholarly Design */

/* Light theme (default) */
:root {
    --parchment: #f5f0e8;
    --dark-text: #2c2418;
    --burnt-sienna: #8b4513;
    --tan-gold: #d4a574;
    --deep-brown: #5c3d2e;
    --light-parchment: #faf6f0;
    --accent-dark: #6d3410;
    --header-bg-from: #2c2418;
    --header-bg-to: #5c3d2e;
    --nav-bg: #2c2418;
}

/* Dark theme */
[data-theme="dark"] {
    --parchment: #1e1b16;
    --dark-text: #e8e0d0;
    --burnt-sienna: #cd8a5a;
    --tan-gold: #c49850;
    --deep-brown: #b09070;
    --light-parchment: #2a2520;
    --accent-dark: #e09060;
    --header-bg-from: #0d0b08;
    --header-bg-to: #1a1510;
    --nav-bg: #0d0b08;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Georgia', 'Garamond', serif;
    background-color: var(--parchment);
    color: var(--dark-text);
    line-height: 1.7;
}

/* Header */
.main-header {
    background: linear-gradient(135deg, var(--header-bg-from) 0%, var(--header-bg-to) 100%);
    color: var(--parchment);
    padding: 2rem 2rem 1.5rem;
    border-bottom: 3px solid var(--burnt-sienna);
}
.header-content { max-width: 1200px; margin: 0 auto; }
.header-top-row { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem; }
.main-header h1 { font-size: 2.5rem; font-weight: normal; letter-spacing: 2px; }
.subtitle { font-size: 1rem; font-style: italic; opacity: 0.9; margin-bottom: 1.5rem; }

/* Dark toggle */
.dark-toggle {
    background: none; border: 1px solid var(--tan-gold); color: var(--parchment);
    padding: 0.3rem 0.8rem; cursor: pointer; font-size: 0.85rem; font-family: Georgia,serif;
    flex-shrink: 0; transition: background 0.2s;
}
.dark-toggle:hover { background: rgba(255,255,255,0.1); }

/* Stats */
.portal-stats {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(160px,1fr));
    gap: 1rem; margin-top: 1.25rem;
}
.stat-box {
    display: flex; flex-direction: column; align-items: center;
    padding: 0.85rem 1rem; background: rgba(255,255,255,0.1); border-left: 3px solid var(--tan-gold);
}
.stat-number { font-size: 1.9rem; font-weight: bold; color: var(--tan-gold); }
.stat-label  { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 1px; margin-top: 0.25rem; text-align: center; }

/* Search bar */
.search-bar-container { position: relative; margin-top: 1.25rem; }
#global-search {
    width: 100%; padding: 0.75rem 2.5rem 0.75rem 1rem;
    font-size: 1rem; font-family: Georgia,serif;
    background: rgba(255,255,255,0.12); border: 1px solid var(--tan-gold);
    color: var(--parchment); outline: none;
}
#global-search::placeholder { color: rgba(255,255,255,0.55); }
#global-search:focus { background: rgba(255,255,255,0.18); border-color: var(--burnt-sienna); }

#search-clear {
    position: absolute; right: 0.5rem; top: 50%; transform: translateY(-50%);
    background: none; border: none; color: var(--parchment); font-size: 1.3rem;
    cursor: pointer; opacity: 0.7; line-height: 1; padding: 0.2rem 0.4rem;
}
#search-clear:hover { opacity: 1; }

#search-results-panel {
    position: absolute; top: 100%; left: 0; right: 0;
    background: var(--light-parchment); border: 1px solid var(--tan-gold); border-top: none;
    z-index: 200; max-height: 420px; overflow-y: auto;
    color: var(--dark-text); box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.search-result-header {
    padding: 0.5rem 1rem; font-size: 0.82rem; color: var(--deep-brown);
    border-bottom: 1px solid var(--tan-gold); background: var(--parchment); font-style: italic;
}
.search-result-item {
    display: flex; flex-direction: column; gap: 0.1rem;
    padding: 0.6rem 1rem; cursor: pointer;
    border-bottom: 1px solid rgba(212,165,116,0.3); transition: background 0.15s;
}
.search-result-item:hover { background: rgba(139,69,19,0.07); }
.search-result-name   { font-weight: bold; color: var(--burnt-sienna); font-size: 0.95rem; }
.search-result-snippet { font-size: 0.82rem; color: var(--deep-brown); }
.search-no-results, .search-result-footer {
    padding: 0.75rem 1rem; font-size: 0.85rem; color: var(--deep-brown); font-style: italic;
}
mark { background: rgba(212,165,116,0.5); color: inherit; }

/* Navigation */
.main-nav {
    background: var(--nav-bg); padding: 0; display: flex; flex-wrap: wrap;
    border-bottom: 2px solid var(--burnt-sienna); position: sticky; top: 0; z-index: 100;
}
.nav-btn {
    flex: 1; padding: 0.9rem 0.5rem;
    background: var(--nav-bg); color: var(--parchment);
    border: none; border-right: 1px solid var(--burnt-sienna);
    cursor: pointer; font-family: 'Georgia',serif; font-size: 0.9rem;
    transition: background 0.25s ease; white-space: nowrap;
}
.nav-btn:hover  { background: var(--burnt-sienna); }
.nav-btn.active { background: var(--burnt-sienna); box-shadow: inset 0 2px 5px rgba(0,0,0,0.3); }
.nav-serendipity {
    flex: 0 1 auto; padding-left: 1rem; padding-right: 1rem;
    background: var(--deep-brown); border-left: 2px solid var(--tan-gold); font-style: italic;
}
.nav-serendipity:hover { background: var(--burnt-sienna); }

/* Portal Container */
.portal-container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
.section { display: none; animation: fadeIn 0.4s ease-in; }
.section.active { display: block; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

.section-header {
    text-align: center; margin-bottom: 2.5rem;
    border-bottom: 2px solid var(--tan-gold); padding-bottom: 1.75rem;
}
.section-header h2 { font-size: 2rem; color: var(--burnt-sienna); margin-bottom: 0.5rem; }
.section-header p  { font-size: 1.05rem; color: var(--deep-brown); }

/* Filter bar */
.section-controls {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.5rem;
}
.filter-bar { display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center; }
.filter-select {
    padding: 0.35rem 0.7rem; border: 1px solid var(--tan-gold);
    background: var(--light-parchment); color: var(--dark-text);
    font-family: Georgia,serif; font-size: 0.85rem; cursor: pointer; outline: none;
}
.filter-select:focus { border-color: var(--burnt-sienna); }
.btn-sm {
    padding: 0.35rem 0.75rem; background: none; border: 1px solid var(--tan-gold);
    color: var(--deep-brown); font-family: Georgia,serif; font-size: 0.82rem;
    cursor: pointer; transition: background 0.2s;
}
.btn-sm:hover { background: var(--tan-gold); color: var(--dark-text); }
.section-count { font-size: 0.85rem; color: var(--deep-brown); font-style: italic; }

/* Gallery */
.gallery {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(280px,1fr));
    gap: 2rem; margin-bottom: 3rem;
}
.no-results { grid-column: 1/-1; text-align: center; color: var(--deep-brown); font-style: italic; padding: 2rem; }

/* Cards */
.card {
    background: var(--light-parchment); border: 1px solid var(--tan-gold);
    border-left: 4px solid var(--burnt-sienna); padding: 1.5rem; cursor: pointer;
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-left-width 0.25s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.card:hover { transform: translateY(-4px); box-shadow: 0 8px 16px rgba(139,69,19,0.2); border-left-width: 6px; }
.card-header { margin-bottom: 0.5rem; }
.card-title { font-size: 1.05rem; font-weight: bold; color: var(--burnt-sienna); margin-bottom: 0.3rem; }
.card-meta, .card-meta-inline { font-size: 0.82rem; color: var(--deep-brown); margin-bottom: 0.3rem; }
.card-summary { font-size: 0.92rem; line-height: 1.6; color: var(--dark-text); margin: 0.75rem 0; }
.card-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 0.75rem; }
.card-read-more { font-size: 0.82rem; color: var(--burnt-sienna); font-weight: bold; transition: color 0.2s; }
.card-read-more:hover { color: var(--accent-dark); }
.card-image { width: 100%; max-height: 160px; object-fit: cover; margin-bottom: 0.75rem; }

/* Card badges */
.card-badge {
    font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.5px;
    padding: 0.12rem 0.45rem; border-radius: 2px; font-family: sans-serif;
}
.card-badge-inline { display: inline-block; }
.badge-figures  { background: #fde8e8; color: #c0392b; }
.badge-concepts { background: #e8f4fd; color: #2471a3; }
.badge-texts    { background: #e8fde8; color: #1a7a1a; }
.badge-essays   { background: #fef9e8; color: #b7770d; }
.badge-emblems  { background: #f3e8fd; color: #7d3c98; }

/* Modal */
.modal {
    display: none; position: fixed; inset: 0;
    background: rgba(0,0,0,0.72); z-index: 1000; overflow-y: auto;
}
.modal.open {
    display: flex; align-items: flex-start; justify-content: center; padding: 2rem 1rem;
}
.modal-content {
    background: var(--parchment); padding: 2rem 2.5rem 2.5rem;
    max-width: 820px; width: 100%; max-height: 90vh; overflow-y: auto;
    border: 2px solid var(--burnt-sienna); position: relative;
}

/* Modal toolbar */
.modal-toolbar {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 1.25rem; padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--tan-gold); flex-wrap: wrap; gap: 0.5rem;
}
.modal-nav-left { display: flex; align-items: center; gap: 0.75rem; flex: 1; min-width: 0; }
.modal-back {
    background: none; border: 1px solid var(--burnt-sienna); color: var(--burnt-sienna);
    font-family: Georgia,serif; font-size: 0.82rem; padding: 0.28rem 0.7rem;
    cursor: pointer; flex-shrink: 0; transition: background 0.2s;
}
.modal-back:hover { background: var(--burnt-sienna); color: var(--parchment); }
.modal-breadcrumb {
    font-size: 0.8rem; color: var(--deep-brown); font-style: italic;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.modal-actions { display: flex; gap: 0.4rem; align-items: center; flex-shrink: 0; }
.modal-action-btn {
    background: none; border: 1px solid var(--tan-gold); color: var(--burnt-sienna);
    font-family: Georgia,serif; font-size: 0.78rem; padding: 0.25rem 0.6rem;
    cursor: pointer; transition: background 0.2s; white-space: nowrap;
}
.modal-action-btn:hover { background: var(--tan-gold); color: var(--dark-text); }
.modal-close {
    background: var(--burnt-sienna); color: var(--parchment); border: none;
    font-size: 1.4rem; cursor: pointer; width: 34px; height: 34px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0; transition: background 0.2s;
}
.modal-close:hover { background: var(--accent-dark); }

/* Modal body */
#modal-body h2 {
    color: var(--burnt-sienna); margin-bottom: 1rem;
    border-bottom: 2px solid var(--tan-gold); padding-bottom: 0.5rem; font-size: 1.6rem;
}
#modal-body h3 { color: var(--deep-brown); margin-top: 1.5rem; margin-bottom: 0.5rem; font-size: 1.05rem; }
#modal-body p  { margin-bottom: 1rem; }
#modal-body ul { margin-left: 2rem; margin-bottom: 1rem; }
.modal-meta-row { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.25rem; }
.meta-pill {
    display: inline-block; padding: 0.2rem 0.65rem;
    background: var(--light-parchment); border: 1px solid var(--tan-gold);
    font-size: 0.82rem; color: var(--deep-brown);
}
.modal-essay { line-height: 1.85; margin: 1.25rem 0; }
.modal-essay p { margin-bottom: 0.85rem; }
.rel-links { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem; }
.rel-link, .rel-link-text {
    display: inline-block; padding: 0.18rem 0.55rem;
    background: var(--light-parchment); border: 1px solid var(--tan-gold);
    color: var(--burnt-sienna); font-size: 0.85rem; text-decoration: none;
    cursor: pointer; transition: background 0.15s;
}
.rel-link:hover { background: var(--tan-gold); color: var(--dark-text); }
.influence-type, .emblem-link-type { font-size: 0.75em; color: var(--deep-brown); }
.visual-desc {
    border-left: 3px solid var(--tan-gold); padding: 0.75rem 1.25rem; margin: 1rem 0;
    font-style: italic; color: var(--deep-brown); background: var(--light-parchment);
}
.tag-list { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.5rem 0; }
.tag {
    display: inline-block; padding: 0.15rem 0.5rem;
    background: var(--light-parchment); border: 1px solid var(--tan-gold);
    font-size: 0.8rem; color: var(--dark-text);
}
.authenticity-note {
    font-size: 0.85rem; margin-top: 1rem; padding: 0.4rem 0.8rem;
    background: var(--light-parchment); border-left: 3px solid var(--tan-gold);
}
.scholars-list { font-style: italic; }
.gender-note   { font-style: italic; color: var(--deep-brown); }
.scholarship-list  { margin-top: 0.5rem; }
.scholarship-entry {
    margin-bottom: 1rem; padding: 0.75rem;
    background: var(--light-parchment); border-left: 3px solid var(--tan-gold);
}
.scholar-name  { font-weight: bold; color: var(--burnt-sienna); display: block; }
.scholar-ref   { font-size: 0.82rem; color: var(--deep-brown); font-style: italic; display: block; margin-bottom: 0.25rem; }
.scholar-quote { margin: 0.5rem 0 0; font-size: 0.88rem; border-left: 2px solid var(--burnt-sienna); padding-left: 0.75rem; }
.emblem-explanations { margin-top: 0.5rem; font-size: 0.88rem; color: var(--deep-brown); }
.rel-more { font-size: 0.78rem; color: var(--deep-brown); font-style: italic; margin-left: 0.25rem; }

/* Compare overlay */
#compare-modal { position: fixed; inset: 0; background: rgba(0,0,0,0.88); z-index: 2000; }
#compare-modal[hidden] { display: none; }
#compare-modal:not([hidden]) { display: flex; flex-direction: column; align-items: center; justify-content: center; }
.compare-wrap {
    background: var(--parchment); width: 96vw; height: 93vh;
    display: flex; flex-direction: column; border: 2px solid var(--burnt-sienna); overflow: hidden;
}
.compare-close {
    align-self: flex-end; margin: 0.5rem 0.75rem; padding: 0.3rem 0.9rem;
    background: var(--burnt-sienna); color: var(--parchment); border: none;
    font-family: Georgia,serif; font-size: 0.85rem; cursor: pointer; flex-shrink: 0; transition: background 0.2s;
}
.compare-close:hover { background: var(--accent-dark); }
.compare-panels { display: grid; grid-template-columns: 1fr 4px 1fr; flex: 1; overflow: hidden; }
.compare-panel { overflow-y: auto; padding: 1.5rem; }
.compare-panel h2 { color: var(--burnt-sienna); margin-bottom: 0.75rem; border-bottom: 2px solid var(--tan-gold); padding-bottom: 0.4rem; }
.compare-panel h3 { color: var(--deep-brown); margin-top: 1.25rem; margin-bottom: 0.4rem; font-size: 1rem; }
.compare-panel p  { margin-bottom: 0.75rem; }
.compare-divider  { background: var(--tan-gold); }
.compare-placeholder { padding: 3rem 2rem; text-align: center; color: var(--deep-brown); font-style: italic; }

/* Concept browser overlay */
#concept-browser { position: fixed; inset: 0; background: rgba(0,0,0,0.82); z-index: 1500; }
#concept-browser[hidden] { display: none; }
#concept-browser:not([hidden]) { display: flex; flex-direction: column; align-items: center; justify-content: center; }
.cb-wrap {
    background: var(--parchment); width: 94vw; max-height: 90vh;
    display: flex; flex-direction: column; border: 2px solid var(--burnt-sienna); overflow: hidden;
}
.cb-header {
    display: flex; justify-content: space-between; align-items: center;
    padding: 1rem 1.5rem; background: var(--dark-text); color: var(--parchment); flex-shrink: 0;
}
.cb-header h2 { font-size: 1.1rem; color: var(--tan-gold); margin: 0; }
.cb-close {
    background: none; border: 1px solid var(--tan-gold); color: var(--tan-gold);
    font-size: 1.2rem; cursor: pointer; padding: 0.15rem 0.6rem;
}
.cb-close:hover { background: var(--tan-gold); color: var(--dark-text); }
.cb-body { flex: 1; overflow-y: auto; padding: 1.5rem; max-width: 1200px; margin: 0 auto; width: 100%; }
.cb-section-title { color: var(--burnt-sienna); margin: 1.5rem 0 0.75rem; border-bottom: 1px solid var(--tan-gold); padding-bottom: 0.3rem; font-size: 1.05rem; }
.cb-cards { display: grid; grid-template-columns: repeat(auto-fill,minmax(260px,1fr)); gap: 1rem; margin-bottom: 1rem; }
.cb-card {
    background: var(--light-parchment); border: 1px solid var(--tan-gold);
    border-left: 3px solid var(--burnt-sienna); padding: 1rem; cursor: pointer;
    transition: border-left-color 0.2s, background 0.2s;
}
.cb-card:hover { border-left-color: var(--tan-gold); background: var(--parchment); }
.cb-card-title   { font-weight: bold; color: var(--burnt-sienna); margin-bottom: 0.25rem; font-size: 0.95rem; }
.cb-card-meta    { font-size: 0.8rem; color: var(--deep-brown); margin-bottom: 0.35rem; }
.cb-card-summary { font-size: 0.85rem; color: var(--dark-text); line-height: 1.5; }

/* Concept browse button */
.concept-browse-btn {
    display: inline-block; margin: 0.5rem 0 1.5rem; padding: 0.4rem 1rem;
    background: none; border: 1px solid var(--burnt-sienna); color: var(--burnt-sienna);
    font-family: Georgia,serif; font-size: 0.9rem; cursor: pointer; transition: background 0.2s, color 0.2s;
}
.concept-browse-btn:hover { background: var(--burnt-sienna); color: var(--parchment); }

/* Map */
.map-wrap { position: relative; }
.map-container, #map-container {
    width: 100%; height: 580px;
    border: 2px solid var(--burnt-sienna); margin-bottom: 2rem;
}
.map-controls { margin-bottom: 0.75rem; }
.map-legend {
    display: flex; flex-wrap: wrap; gap: 1.25rem;
    padding: 0.6rem 1rem; background: var(--light-parchment);
    border: 1px solid var(--tan-gold); border-left: 3px solid var(--burnt-sienna); font-size: 0.88rem;
}
.map-legend label { display: flex; align-items: center; gap: 0.4rem; cursor: pointer; color: var(--dark-text); }
.legend-dot { display: inline-block; width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
.legend-dot.figures { background: #e74c3c; }
.legend-dot.texts   { background: #3498db; }
.legend-dot.emblems { background: #8e44ad; }
.legend-dot.centers { background: #f39c12; }
.legend-dot.lines   { background: none; border: 2px dashed #e67e22; border-radius: 0; width: 20px; height: 2px; }
.map-date-filter {
    display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;
    margin-top: 0.5rem; padding: 0.5rem 1rem;
    background: var(--light-parchment); border: 1px solid var(--tan-gold);
    font-size: 0.85rem; color: var(--dark-text);
}
.slider-row { display: flex; gap: 0.5rem; }
input[type=range] { width: 140px; accent-color: var(--burnt-sienna); cursor: pointer; }

/* Map side panel */
.map-side-panel {
    display: none; position: absolute; top: 0; right: 0; width: 290px; height: 100%;
    background: var(--light-parchment); border-left: 3px solid var(--burnt-sienna);
    overflow-y: auto; z-index: 500; box-shadow: -4px 0 12px rgba(0,0,0,0.15);
}
.map-side-panel.open { display: block; }
.map-side-header {
    display: flex; justify-content: space-between; align-items: flex-start;
    padding: 0.75rem 1rem; background: var(--deep-brown); color: var(--parchment); position: sticky; top: 0;
}
.map-side-header h3 { margin: 0; font-size: 0.95rem; line-height: 1.3; color: var(--tan-gold); flex: 1; }
.map-side-close { background: none; border: none; color: var(--parchment); font-size: 1.3rem; cursor: pointer; padding: 0 0.25rem; }
.map-side-close:hover { color: var(--tan-gold); }
.map-side-content { padding: 0.85rem 1rem; font-size: 0.88rem; line-height: 1.6; color: var(--dark-text); }
.map-side-content p      { margin-bottom: 0.55rem; }
.map-side-content strong { color: var(--burnt-sienna); }
.map-side-summary        { margin-top: 0.6rem; }
.map-tooltip { font-family: Georgia,serif; font-size: 0.85rem; }
.leaflet-popup-content { font-family: Georgia,serif; color: #2c2418; font-size: 0.9rem; }

/* Timeline */
.timeline-controls {
    display: flex; flex-wrap: wrap; gap: 0.5rem;
    margin-bottom: 2rem; padding-bottom: 1.25rem; border-bottom: 1px solid var(--tan-gold);
}
.tl-filter {
    padding: 0.35rem 0.9rem; background: var(--light-parchment); border: 1px solid var(--tan-gold);
    color: var(--deep-brown); cursor: pointer; font-family: Georgia,serif; font-size: 0.83rem;
    transition: background 0.2s, color 0.2s;
}
.tl-filter:hover  { background: var(--tan-gold); color: var(--dark-text); }
.tl-filter.active { background: var(--burnt-sienna); border-color: var(--burnt-sienna); color: var(--parchment); }
.timeline-container { position: relative; padding-left: 3rem; max-width: 860px; margin: 0 auto; }
.timeline-container::before {
    content: ''; position: absolute; left: 1.15rem; top: 0; bottom: 0;
    width: 2px; background: linear-gradient(to bottom,var(--burnt-sienna),var(--tan-gold));
}
.tl-event { position: relative; margin-bottom: 1.75rem; }
.tl-event.hidden { display: none; }
.tl-dot { position: absolute; left: -2.2rem; top: 0.45rem; width: 13px; height: 13px; border-radius: 50%; border: 2px solid var(--parchment); z-index: 1; }
.tl-dot.historical { background: #7f8c8d; }
.tl-dot.text       { background: var(--burnt-sienna); }
.tl-dot.figure     { background: var(--tan-gold); }
.tl-dot.discovery  { background: #2980b9; }
.tl-card { background: var(--light-parchment); border: 1px solid var(--tan-gold); border-left: 4px solid transparent; padding: 0.9rem 1.1rem; box-shadow: 0 1px 4px rgba(0,0,0,0.07); }
.tl-event.historical .tl-card { border-left-color: #7f8c8d; }
.tl-event.text       .tl-card { border-left-color: var(--burnt-sienna); }
.tl-event.figure     .tl-card { border-left-color: var(--tan-gold); }
.tl-event.discovery  .tl-card { border-left-color: #2980b9; }
.tl-header { display: flex; align-items: baseline; gap: 0.65rem; margin-bottom: 0.4rem; flex-wrap: wrap; }
.tl-year  { font-size: 1.2rem; font-weight: bold; color: var(--burnt-sienna); min-width: 3rem; }
.tl-title { font-size: 0.97rem; font-weight: bold; color: var(--dark-text); flex: 1; }
.tl-badge { font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.5px; padding: 0.12rem 0.45rem; border-radius: 2px; font-family: sans-serif; }
.tl-badge.historical { background: #ecf0f1; color: #7f8c8d; }
.tl-badge.text       { background: #fdf0e8; color: #8b4513; }
.tl-badge.figure     { background: #fef9f0; color: #b7770d; }
.tl-badge.discovery  { background: #eaf4fb; color: #2980b9; }
.tl-desc    { font-size: 0.88rem; line-height: 1.65; color: var(--dark-text); }
.tl-related { margin-top: 0.5rem; font-size: 0.78rem; color: var(--deep-brown); }

/* About */
.about-content { background: var(--light-parchment); padding: 2rem; border-left: 4px solid var(--burnt-sienna); max-width: 900px; margin: 0 auto; }
.about-content h3 { color: var(--burnt-sienna); margin-top: 2rem; margin-bottom: 1rem; }
.about-content p, .about-content li { line-height: 1.8; margin-bottom: 0.75rem; }
.about-content ul { margin-left: 1.5rem; margin-bottom: 1rem; }
.about-content a  { color: var(--burnt-sienna); text-decoration: none; }
.about-content a:hover { text-decoration: underline; }

/* Footer */
.main-footer {
    background: var(--dark-text); color: var(--parchment);
    text-align: center; padding: 2rem; margin-top: 3rem; border-top: 2px solid var(--burnt-sienna);
}

/* Emblem book grouped view */
.emblem-book-section { margin-bottom: 3rem; }
.emblem-book-header { padding: 0.75rem 1rem; background: var(--light-parchment); border-left: 4px solid var(--burnt-sienna); margin-bottom: 1.25rem; }
.emblem-book-header h3 { color: var(--burnt-sienna); margin: 0 0 0.2rem; }
.emblem-book-meta { font-size: 0.82rem; color: var(--deep-brown); }
.emblem-gallery { display: grid; grid-template-columns: repeat(auto-fill,minmax(260px,1fr)); gap: 1.5rem; }

/* Responsive */
@media (max-width: 768px) {
    .main-header h1  { font-size: 1.8rem; }
    .portal-stats    { grid-template-columns: repeat(2,1fr); }
    .nav-btn         { flex: 0 1 33%; font-size: 0.78rem; padding: 0.65rem 0.25rem; }
    .gallery         { grid-template-columns: 1fr; }
    .modal-content   { padding: 1.25rem; }
    .map-container, #map-container { height: 400px; }
    .compare-panels  { grid-template-columns: 1fr; grid-template-rows: 1fr 4px 1fr; }
    .compare-divider { width: auto; height: 4px; }
    input[type=range] { width: 100px; }
    .cb-cards        { grid-template-columns: 1fr; }
    .header-top-row  { flex-direction: column; gap: 0.5rem; }
    .dark-toggle     { align-self: flex-end; }
}
"""
    return css

def build():
    print("Building TheosophicalAlchemyDB site...")
    html = generate_index_html()
    index_path = SITE_DIR / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[OK] Generated {index_path}")

    css = generate_enhanced_css()
    css_path = SITE_DIR / "style.css"
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print(f"[OK] Generated {css_path}")
    print("Site build complete!")

if __name__ == '__main__':
    build()
