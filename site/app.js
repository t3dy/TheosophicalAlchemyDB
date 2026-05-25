// Prototype Data - Embedded
const prototypeData = {
    figures: [],
    concepts: [],
    texts: []
};

// Load data from JSON file
let allData = {};

// Initialize the application
document.addEventListener('DOMContentLoaded', async () => {
    try {
        // Load prototype data from JSON
        const response = await fetch('../data/prototype_data.json');
        allData = await response.json();

        // Render galleries
        renderGallery('figures');
        renderGallery('concepts');
        renderGallery('texts');

        // Initialize map
        initializeMap();

        // Setup navigation
        setupNavigation();

        // Setup modal
        setupModal();
    } catch (error) {
        console.error('Error loading data:', error);
        // Provide fallback message
        document.body.innerHTML = '<div style="padding: 20px; color: red;"><h2>Error Loading Portal</h2><p>Please ensure prototype_data.json is in the ../data/ directory.</p><p>Error: ' + error.message + '</p></div>';
    }
});

/**
 * Render gallery of cards
 */
function renderGallery(section) {
    const data = allData[section];
    const galleryEl = document.getElementById(`${section}-gallery`);

    if (!data || data.length === 0) {
        galleryEl.innerHTML = '<p>Loading...</p>';
        return;
    }

    galleryEl.innerHTML = data.map((item, index) => `
        <div class="card" data-index="${index}" data-section="${section}">
            <div class="card-title">${item.name || item.title}</div>
            ${item.birth_year ? `<div class="card-meta">${item.birth_year}–${item.death_year} | ${item.nationality}</div>` : ''}
            ${item.year ? `<div class="card-meta">${item.year} | ${item.language}</div>` : ''}
            ${item.category ? `<div class="card-meta">Category: ${item.category}</div>` : ''}
            <div class="card-summary">${item.summary}</div>
            <a href="#" class="card-read-more">Read full essay →</a>
        </div>
    `).join('');

    // Add click handlers to cards
    galleryEl.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', (e) => {
            e.preventDefault();
            const index = parseInt(card.dataset.index);
            const section = card.dataset.section;
            openModal(section, index);
        });
    });
}

/**
 * Open modal with full essay
 */
function openModal(section, index) {
    const item = allData[section][index];
    const modalBody = document.getElementById('modal-body');

    let content = `
        <h2>${item.name || item.title}</h2>
    `;

    if (item.birth_year) {
        content += `
            <h3>Life</h3>
            <p>${item.birth_year}–${item.death_year} | ${item.nationality}</p>
            ${item.location ? `<p><strong>Location:</strong> ${item.location}</p>` : ''}
        `;
    }

    if (item.year) {
        content += `
            <h3>Publication</h3>
            <p>${item.year} | ${item.language}</p>
            ${item.location ? `<p><strong>Location:</strong> ${item.location}</p>` : ''}
        `;
    }

    if (item.category) {
        content += `
            <h3>Category</h3>
            <p>${item.category}</p>
        `;
    }

    content += `
        <h3>Essay</h3>
        <p>${item.essay}</p>
    `;

    if (item.primary_discipline) {
        content += `
            <h3>Discipline</h3>
            <p>${item.primary_discipline}</p>
        `;
    }

    if (item.concepts) {
        const conceptNames = item.concepts.map(cid => {
            const concept = allData.concepts.find(c => c.id === cid);
            return concept ? concept.name : '';
        }).filter(n => n).join(', ');
        if (conceptNames) {
            content += `
                <h3>Related Concepts</h3>
                <p>${conceptNames}</p>
            `;
        }
    }

    if (item.key_works) {
        content += `
            <h3>Key Works</h3>
            <ul>
                ${item.key_works.map(work => `<li>${work}</li>`).join('')}
            </ul>
        `;
    }

    if (item.scholars) {
        content += `
            <h3>Primary Scholars</h3>
            <p>${item.scholars.join(', ')}</p>
        `;
    }

    modalBody.innerHTML = content;
    document.getElementById('modal').classList.add('open');
}

/**
 * Setup modal close functionality
 */
function setupModal() {
    const modal = document.getElementById('modal');
    const closeBtn = document.querySelector('.modal-close');

    closeBtn.addEventListener('click', () => {
        modal.classList.remove('open');
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('open');
        }
    });
}

/**
 * Setup navigation between sections
 */
function setupNavigation() {
    const navBtns = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.section');

    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const sectionId = btn.dataset.section;

            // Update active button
            navBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Update active section
            sections.forEach(s => s.classList.remove('active'));
            document.getElementById(sectionId).classList.add('active');

            // Reinitialize map if needed
            if (sectionId === 'map') {
                setTimeout(() => {
                    if (window.map) {
                        window.map.invalidateSize();
                    }
                }, 100);
            }
        });
    });
}

/**
 * Initialize Leaflet map with figures and texts
 */
function initializeMap() {
    // Create map centered on Europe
    const map = L.map('map-container').setView([54.5260, 15.2551], 4);

    window.map = map;

    // Add tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors',
        maxZoom: 19
    }).addTo(map);

    // Create feature groups for different types
    const figureGroup = L.featureGroup();
    const textGroup = L.featureGroup();
    const conceptGroup = L.featureGroup();

    // Add figures to map
    allData.figures.forEach(figure => {
        if (figure.lat && figure.lng) {
            const marker = L.circleMarker([figure.lat, figure.lng], {
                radius: 7,
                fillColor: '#e74c3c',
                color: '#c0392b',
                weight: 2,
                opacity: 1,
                fillOpacity: 0.8
            });

            const popupContent = `
                <h3>${figure.name}</h3>
                <p class="popup-summary">${figure.summary}</p>
                <p><strong>${figure.birth_year}–${figure.death_year}</strong> | ${figure.nationality}</p>
                <p style="margin-top: 8px; font-size: 0.85em; color: #666;">Click card above to read full essay</p>
            `;

            marker.bindPopup(popupContent);
            marker.on('click', () => {
                // Find and open the corresponding card
                const idx = allData.figures.findIndex(f => f.id === figure.id);
                if (idx >= 0) {
                    openModal('figures', idx);
                }
            });

            figureGroup.addLayer(marker);
        }
    });

    // Add texts to map
    allData.texts.forEach(text => {
        if (text.lat && text.lng) {
            const marker = L.circleMarker([text.lat, text.lng], {
                radius: 6,
                fillColor: '#3498db',
                color: '#2980b9',
                weight: 2,
                opacity: 1,
                fillOpacity: 0.8
            });

            const popupContent = `
                <h3>${text.title}</h3>
                <p class="popup-summary">${text.summary}</p>
                <p><strong>${text.year}</strong> | ${text.language}</p>
                <p><strong>Location:</strong> ${text.location}</p>
                <p style="margin-top: 8px; font-size: 0.85em; color: #666;">Click card above to read full essay</p>
            `;

            marker.bindPopup(popupContent);
            marker.on('click', () => {
                const idx = allData.texts.findIndex(t => t.id === text.id);
                if (idx >= 0) {
                    openModal('texts', idx);
                }
            });

            textGroup.addLayer(marker);
        }
    });

    // Add conceptual centers (major cities/centers of learning)
    const conceptCenters = [
        { name: 'Prague', lat: 50.0755, lng: 14.4378, role: 'Center of alchemical learning under Rudolf II' },
        { name: 'Florence', lat: 43.7696, lng: 11.2558, role: 'Renaissance Neoplatonism and hermetic philosophy' },
        { name: 'Tübingen', lat: 48.5216, lng: 9.0577, role: 'Rosicrucian theological reform' },
        { name: 'London', lat: 51.5074, lng: -0.1278, role: 'English Rosicrucian and Masonic synthesis' },
        { name: 'Amsterdam', lat: 52.3676, lng: 4.9041, role: 'Martinist and Theosophical center' },
        { name: 'Paris', lat: 48.8566, lng: 2.3522, role: 'French illuminism and alchemy' }
    ];

    conceptCenters.forEach(center => {
        const marker = L.circleMarker([center.lat, center.lng], {
            radius: 8,
            fillColor: '#f39c12',
            color: '#d68910',
            weight: 2,
            opacity: 1,
            fillOpacity: 0.8
        });

        const popupContent = `
            <h3>${center.name}</h3>
            <p class="popup-summary"><strong>Role:</strong> ${center.role}</p>
        `;

        marker.bindPopup(popupContent);
        conceptGroup.addLayer(marker);
    });

    // Add all groups to map
    figureGroup.addTo(map);
    textGroup.addTo(map);
    conceptGroup.addTo(map);

    // Fit bounds to show all markers
    const allMarkers = L.featureGroup([figureGroup, textGroup, conceptGroup]);
    if (allMarkers.getLayers().length > 0) {
        map.fitBounds(allMarkers.getBounds(), { padding: [50, 50], maxZoom: 5 });
    }
}

/**
 * Search functionality (for future enhancement)
 */
function searchEntries(query) {
    query = query.toLowerCase();
    const results = [];

    ['figures', 'concepts', 'texts'].forEach(section => {
        allData[section].forEach(item => {
            const name = (item.name || item.title || '').toLowerCase();
            const summary = (item.summary || '').toLowerCase();
            if (name.includes(query) || summary.includes(query)) {
                results.push({
                    section,
                    item,
                    type: section.slice(0, -1)
                });
            }
        });
    });

    return results;
}
