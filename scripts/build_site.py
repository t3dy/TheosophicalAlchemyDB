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
    """Load the 50-entry prototype data"""
    if PROTOTYPE_DATA.exists():
        with open(PROTOTYPE_DATA, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"figures": [], "concepts": [], "texts": []}

def load_corpus_sources():
    """Load ingested sources from database"""
    sources = []
    if DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM sources")
            for row in c.fetchall():
                sources.append({
                    'id': row[0],
                    'filename': row[1],
                    'title': row[2],
                    'authors': row[3],
                    'year': row[4],
                    'source_type': row[5],
                    'word_count': row[7]
                })
        except:
            pass
        conn.close()
    return sources

def generate_index_html():
    """Generate the main index.html"""
    prototype = load_prototype_data()
    sources = load_corpus_sources()

    stats = {
        'figures': len(prototype.get('figures', [])),
        'concepts': len(prototype.get('concepts', [])),
        'texts': len(prototype.get('texts', [])),
        'sources': len(sources)
    }

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TheosophicalAlchemyDB - Rosicrucian & Spiritual Alchemy Portal</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
</head>
<body>
    <header class="main-header">
        <div class="header-content">
            <h1>TheosophicalAlchemyDB</h1>
            <p class="subtitle">Interactive Knowledge Portal: Rosicrucian & Spiritual Alchemy Traditions (16th–19th c.)</p>
            <div class="portal-stats">
                <span class="stat-box">
                    <span class="stat-number">{stats['figures']}</span>
                    <span class="stat-label">Historical Figures</span>
                </span>
                <span class="stat-box">
                    <span class="stat-number">{stats['concepts']}</span>
                    <span class="stat-label">Concepts & Principles</span>
                </span>
                <span class="stat-box">
                    <span class="stat-number">{stats['texts']}</span>
                    <span class="stat-label">Scholarly Texts</span>
                </span>
                <span class="stat-box">
                    <span class="stat-number">{stats['sources']}</span>
                    <span class="stat-label">Research Sources</span>
                </span>
            </div>
        </div>
    </header>

    <nav class="main-nav">
        <button class="nav-btn active" data-section="figures">Figures</button>
        <button class="nav-btn" data-section="concepts">Concepts</button>
        <button class="nav-btn" data-section="texts">Texts</button>
        <button class="nav-btn" data-section="map">Map</button>
        <button class="nav-btn" data-section="about">About</button>
    </nav>

    <main class="portal-container">
        <!-- Figures Section -->
        <section id="figures" class="section active">
            <div class="section-header">
                <h2>Historical Figures</h2>
                <p>Explore {stats['figures']} key figures in Rosicrucian and spiritual alchemy traditions</p>
            </div>
            <div id="figures-gallery" class="gallery"></div>
        </section>

        <!-- Concepts Section -->
        <section id="concepts" class="section">
            <div class="section-header">
                <h2>Concepts & Principles</h2>
                <p>Understand {stats['concepts']} central philosophical and alchemical concepts</p>
            </div>
            <div id="concepts-gallery" class="gallery"></div>
        </section>

        <!-- Texts Section -->
        <section id="texts" class="section">
            <div class="section-header">
                <h2>Scholarly Texts</h2>
                <p>Study {stats['texts']} foundational and contemporary texts</p>
            </div>
            <div id="texts-gallery" class="gallery"></div>
        </section>

        <!-- Map Section -->
        <section id="map" class="section">
            <div class="section-header">
                <h2>Geographic Distribution</h2>
                <p>Explore the historical geography of Rosicrucian figures and text publication</p>
            </div>
            <div id="map-container" class="map-container"></div>
        </section>

        <!-- About Section -->
        <section id="about" class="section">
            <div class="section-header">
                <h2>About This Portal</h2>
            </div>
            <div class="about-content">
                <h3>Project Overview</h3>
                <p>TheosophicalAlchemyDB is a comprehensive digital humanities resource documenting the history and significance of Rosicrucian and spiritual alchemy traditions from the 16th to 19th centuries.</p>

                <h3>Scholarly Framework</h3>
                <p>This portal integrates scholarship from key historians including Frances Yates, Joscelyn Godwin, Tobias Churton, Urszula Szulakowska, and Mike Zuber's definitive work on spiritual alchemy from Jacob Böhme to Mary Anne Atwood.</p>

                <h3>Data Sources</h3>
                <p>The portal incorporates {stats['sources']} primary and secondary sources, including manifestos, treatises, biographical materials, and contemporary scholarly analysis.</p>

                <h3>Technology</h3>
                <p>Built with vanilla JavaScript, Leaflet.js for mapping, and a comprehensive database infrastructure supporting both historical scholarship and interactive exploration.</p>

                <h3>Citation</h3>
                <p><strong>TheosophicalAlchemyDB</strong> (2026). Interactive Portal of Rosicrucian and Theosophical Alchemy. <a href="https://github.com/t3dy/TheosophicalAlchemyDB">github.com/t3dy/TheosophicalAlchemyDB</a></p>
            </div>
        </section>
    </main>

    <!-- Modal for full essays -->
    <div id="modal" class="modal">
        <div class="modal-content">
            <button class="modal-close">&times;</button>
            <div id="modal-body"></div>
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
    """Generate enhanced CSS for the portal"""
    css = """/* TheosophicalAlchemyDB — Enhanced Dark Scholarly Design */

:root {
    --parchment: #f5f0e8;
    --dark-text: #2c2418;
    --burnt-sienna: #8b4513;
    --tan-gold: #d4a574;
    --deep-brown: #5c3d2e;
    --light-parchment: #faf6f0;
    --accent-dark: #6d3410;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Georgia', 'Garamond', serif;
    background-color: var(--parchment);
    color: var(--dark-text);
    line-height: 1.7;
}

/* Header */
.main-header {
    background: linear-gradient(135deg, var(--dark-text) 0%, var(--deep-brown) 100%);
    color: var(--parchment);
    padding: 3rem 2rem;
    border-bottom: 3px solid var(--burnt-sienna);
}

.header-content {
    max-width: 1200px;
    margin: 0 auto;
}

.main-header h1 {
    font-size: 2.5rem;
    font-weight: normal;
    letter-spacing: 2px;
    margin-bottom: 0.5rem;
}

.subtitle {
    font-size: 1rem;
    font-style: italic;
    opacity: 0.9;
    margin-bottom: 2rem;
}

.portal-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.stat-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.1);
    border-left: 3px solid var(--tan-gold);
}

.stat-number {
    font-size: 2rem;
    font-weight: bold;
    color: var(--tan-gold);
}

.stat-label {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 0.5rem;
}

/* Navigation */
.main-nav {
    background: var(--dark-text);
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    border-bottom: 2px solid var(--burnt-sienna);
    position: sticky;
    top: 0;
    z-index: 100;
}

.nav-btn {
    flex: 1;
    padding: 1rem;
    background: var(--dark-text);
    color: var(--parchment);
    border: none;
    border-right: 1px solid var(--burnt-sienna);
    cursor: pointer;
    font-family: 'Georgia', serif;
    font-size: 0.95rem;
    transition: all 0.3s ease;
}

.nav-btn:hover {
    background: var(--burnt-sienna);
}

.nav-btn.active {
    background: var(--burnt-sienna);
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.3);
}

/* Portal Container */
.portal-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 2rem;
}

.section {
    display: none;
    animation: fadeIn 0.5s ease-in;
}

.section.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.section-header {
    text-align: center;
    margin-bottom: 3rem;
    border-bottom: 2px solid var(--tan-gold);
    padding-bottom: 2rem;
}

.section-header h2 {
    font-size: 2rem;
    color: var(--burnt-sienna);
    margin-bottom: 0.5rem;
}

.section-header p {
    font-size: 1.1rem;
    color: var(--deep-brown);
}

/* Gallery */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.card {
    background: var(--light-parchment);
    border: 1px solid var(--tan-gold);
    border-left: 4px solid var(--burnt-sienna);
    padding: 1.5rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(139, 69, 19, 0.2);
    border-left-width: 6px;
}

.card-title {
    font-size: 1.1rem;
    font-weight: bold;
    color: var(--burnt-sienna);
    margin-bottom: 0.5rem;
}

.card-meta {
    font-size: 0.85rem;
    color: var(--deep-brown);
    margin-bottom: 0.5rem;
}

.card-summary {
    font-size: 0.95rem;
    line-height: 1.6;
    color: var(--dark-text);
    margin: 1rem 0;
}

.card-read-more {
    font-size: 0.85rem;
    color: var(--burnt-sienna);
    text-decoration: none;
    font-weight: bold;
    transition: all 0.3s ease;
}

.card-read-more:hover {
    color: var(--accent-dark);
}

/* Modal */
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    z-index: 1000;
    overflow-y: auto;
}

.modal.open {
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal-content {
    background: var(--parchment);
    padding: 2.5rem;
    max-width: 800px;
    width: 90%;
    max-height: 90vh;
    overflow-y: auto;
    border: 2px solid var(--burnt-sienna);
    position: relative;
}

.modal-close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: var(--burnt-sienna);
    color: var(--parchment);
    border: none;
    font-size: 2rem;
    cursor: pointer;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
}

#modal-body h2 {
    color: var(--burnt-sienna);
    margin-bottom: 1rem;
    border-bottom: 2px solid var(--tan-gold);
    padding-bottom: 0.5rem;
}

#modal-body h3 {
    color: var(--deep-brown);
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
}

#modal-body p {
    margin-bottom: 1rem;
}

#modal-body ul {
    margin-left: 2rem;
    margin-bottom: 1rem;
}

/* Map */
.map-container {
    width: 100%;
    height: 600px;
    border: 2px solid var(--burnt-sienna);
    margin-bottom: 2rem;
}

#map-container {
    width: 100%;
    height: 600px;
}

.leaflet-popup-content {
    font-family: 'Georgia', serif;
    color: var(--dark-text);
}

.leaflet-popup-content h3 {
    color: var(--burnt-sienna);
}

.popup-summary {
    font-size: 0.9rem;
    margin: 0.5rem 0;
}

/* About Section */
.about-content {
    background: var(--light-parchment);
    padding: 2rem;
    border-left: 4px solid var(--burnt-sienna);
    max-width: 900px;
    margin: 0 auto;
}

.about-content h3 {
    color: var(--burnt-sienna);
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.about-content p {
    line-height: 1.8;
    margin-bottom: 1rem;
}

.about-content a {
    color: var(--burnt-sienna);
    text-decoration: none;
}

.about-content a:hover {
    text-decoration: underline;
}

/* Footer */
.main-footer {
    background: var(--dark-text);
    color: var(--parchment);
    text-align: center;
    padding: 2rem;
    margin-top: 3rem;
    border-top: 2px solid var(--burnt-sienna);
}

/* Responsive */
@media (max-width: 768px) {
    .main-header h1 {
        font-size: 1.8rem;
    }

    .portal-stats {
        grid-template-columns: repeat(2, 1fr);
    }

    .nav-btn {
        flex: 0 1 50%;
    }

    .gallery {
        grid-template-columns: 1fr;
    }

    .modal-content {
        width: 95%;
        padding: 1.5rem;
    }

    .map-container {
        height: 400px;
    }
}
"""
    return css

def build():
    """Build the complete static site"""
    print("Building TheosophicalAlchemyDB site...")

    # Generate and write index.html
    html = generate_index_html()
    index_path = SITE_DIR / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[OK] Generated {index_path}")

    # Generate and write enhanced CSS
    css = generate_enhanced_css()
    css_path = SITE_DIR / "style.css"
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print(f"[OK] Generated {css_path}")

    print("Site build complete!")

if __name__ == '__main__':
    build()
