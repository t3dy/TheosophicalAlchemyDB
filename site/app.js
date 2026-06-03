/* =====================================================================
   TheosophicalAlchemyDB — app.js
   Features: search, filter/sort, relational modal chaining, emblems,
             map + timeline slider + influence lines, dark mode,
             serendipity, URL hash routing, compare overlay,
             concept browser, share button.
   ===================================================================== */

'use strict';

// ─── State ────────────────────────────────────────────────────────────────────

let allData = { figures: [], concepts: [], texts: [], essays: [], emblems: [], scholars: [], debates: [], reading_paths: [], dictionary: [] };
let activeSection = 'figures';

const filterState = {
    figures:        { sort: 'default', nationality: '', scholar: '', century: '' },
    concepts:       { sort: 'default', category: '' },
    texts:          { sort: 'default', language: '', century: '' },
    essays:         { sort: 'default' },
    emblems:        { sort: 'default', source_book: '', type: '' },
    'emblem-books': { sort: 'default', source_book: '', theme: '' },
    scholars:       { sort: 'default', nationality: '' },
    debates:        { sort: 'default' },
    glossary:       { sort: 'default', category: '', letter: '' },
    paths:          { sort: 'default' },
};

// Modal navigation stack: [{section, id}]
const modalStack = [];

// ─── Boot ─────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('./data/prototype_data.json');
        allData = await response.json();
        allData.emblems       = allData.emblems       || [];
        allData.essays        = allData.essays        || [];
        allData.scholars      = allData.scholars      || [];
        allData.debates       = allData.debates       || [];
        allData.reading_paths = allData.reading_paths || [];
        allData.dictionary    = allData.dictionary    || [];

        updateStats();
        populateFilterDropdowns();

        ['figures', 'concepts', 'texts', 'essays', 'emblems', 'scholars', 'debates', 'paths'].forEach(s => renderGallery(s));
        renderEmblemBooks();
        renderGlossary();

        setupDarkMode();
        setupSerendipity();
        setupModal();
        setupShareButton();
        setupCompare();
        setupSearch();
        setupFilterListeners();
        setupGlossaryFilters();
        setupNavigation();
        setupMapViewToggle();
        initializeMap();
        renderTimeline();
        setupTimelineFilters();

        // Hash routing must come last — after all setup is done
        loadFromHash();
    } catch (err) {
        console.error('Error loading data:', err);
        document.body.innerHTML =
            `<div style="padding:2rem;color:red"><h2>Error Loading Portal</h2><p>${err.message}</p></div>`;
    }
});

// ─── Stats ────────────────────────────────────────────────────────────────────

function updateStats() {
    const set = (id, val) => { const el = document.getElementById(id); if (el) el.textContent = val; };
    set('stat-figures',  allData.figures.length);
    set('stat-concepts', allData.concepts.length);
    set('stat-texts',    allData.texts.length);
    set('stat-emblems',  allData.emblems.length);
}

// ─── Filter dropdown population ───────────────────────────────────────────────

function populateFilterDropdowns() {
    const nats = [...new Set(allData.figures.map(f => f.nationality).filter(Boolean))].sort();
    fillSelect('[data-filter="nationality"][data-section="figures"]', nats);

    const scholars = [...new Set(allData.figures.flatMap(f => f.scholars || []).filter(Boolean))].sort();
    fillSelect('[data-filter="scholar"][data-section="figures"]', scholars);

    const figCenturies = centuriesFrom(allData.figures.map(f => f.birth_year));
    fillSelect('[data-filter="century"][data-section="figures"]', figCenturies, c => `${c}th century`);

    const cats = [...new Set(allData.concepts.map(c => c.category).filter(Boolean))].sort();
    fillSelect('[data-filter="category"][data-section="concepts"]', cats, humaniseCategory);

    const langs = [...new Set(allData.texts.map(t => t.language).filter(Boolean))].sort();
    fillSelect('[data-filter="language"][data-section="texts"]', langs);

    const txtCenturies = centuriesFrom(allData.texts.map(t => Number(t.year)));
    fillSelect('[data-filter="century"][data-section="texts"]', txtCenturies, c => `${c}th century`);

    const embBooks = [...new Set(allData.emblems.map(e => e.source_book).filter(Boolean))].sort();
    fillSelect('[data-filter="source_book"][data-section="emblems"]', embBooks);
    fillSelect('[data-filter="source_book"][data-section="emblem-books"]', embBooks);

    const embTypes = [...new Set(allData.emblems.map(e => e.type).filter(Boolean))].sort();
    fillSelect('[data-filter="type"][data-section="emblems"]', embTypes);

    const scholNats = [...new Set(allData.scholars.map(s => s.nationality).filter(Boolean))].sort();
    fillSelect('[data-filter="nationality"][data-section="scholars"]', scholNats);
}

function fillSelect(selector, values, labelFn = v => v) {
    const sel = document.querySelector(selector);
    if (!sel) return;
    values.forEach(v => {
        const opt = document.createElement('option');
        opt.value = v;
        opt.textContent = labelFn(v);
        sel.appendChild(opt);
    });
}

function centuriesFrom(years) {
    return [...new Set(years.filter(y => y && y > 0).map(y => Math.ceil(y / 100)))].sort((a, b) => a - b);
}

function humaniseCategory(raw) {
    return raw.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
}

// ─── Filter listeners ─────────────────────────────────────────────────────────

function setupFilterListeners() {
    document.querySelectorAll('.filter-select').forEach(sel => {
        sel.addEventListener('change', () => {
            const section = sel.dataset.section;
            const filter  = sel.dataset.filter;
            filterState[section][filter] = sel.value;
            if (section === 'emblem-books') renderEmblemBooks();
            else renderGallery(section);
        });
    });

    document.querySelectorAll('.filter-reset').forEach(btn => {
        btn.addEventListener('click', () => {
            const section = btn.dataset.section;
            Object.keys(filterState[section]).forEach(k => { filterState[section][k] = k === 'sort' ? 'default' : ''; });
            document.querySelectorAll(`.filter-select[data-section="${section}"]`).forEach(s => s.value = s.options[0].value);
            if (section === 'emblem-books') renderEmblemBooks();
            else renderGallery(section);
        });
    });
}

// ─── Data filtering & sorting ─────────────────────────────────────────────────

function applyFiltersAndSort(section) {
    const dataKey = section === 'paths' ? 'reading_paths' : section;
    let items = [...(allData[dataKey] || [])];
    const state = filterState[section] || { sort: 'default' };

    if (section === 'figures') {
        if (state.nationality) items = items.filter(f => f.nationality === state.nationality);
        if (state.scholar)     items = items.filter(f => (f.scholars || []).includes(state.scholar));
        if (state.century)     items = items.filter(f => f.birth_year && Math.ceil(f.birth_year / 100) === Number(state.century));
    }
    if (section === 'concepts') {
        if (state.category) items = items.filter(c => c.category === state.category);
    }
    if (section === 'texts') {
        if (state.language) items = items.filter(t => t.language === state.language);
        if (state.century)  items = items.filter(t => t.year && Math.ceil(Number(t.year) / 100) === Number(state.century));
    }
    if (section === 'emblems') {
        if (state.source_book) items = items.filter(e => e.source_book === state.source_book);
        if (state.type)        items = items.filter(e => e.type === state.type);
    }
    if (section === 'scholars') {
        if (state.nationality) items = items.filter(s => s.nationality === state.nationality);
    }

    switch (state.sort) {
        case 'alpha':      items.sort((a, b) => (a.name || a.title || '').localeCompare(b.name || b.title || '')); break;
        case 'alpha-rev':  items.sort((a, b) => (b.name || b.title || '').localeCompare(a.name || a.title || '')); break;
        case 'chrono':     items.sort((a, b) => (a.birth_year || a.year || 9999) - (b.birth_year || b.year || 9999)); break;
        case 'chrono-rev': items.sort((a, b) => (b.birth_year || b.year || 0) - (a.birth_year || a.year || 0)); break;
    }
    return items;
}

// ─── Gallery rendering ────────────────────────────────────────────────────────

function renderGallery(section) {
    const items   = applyFiltersAndSort(section);
    const gallery = document.getElementById(`${section}-gallery`);
    if (!gallery) return;
    const counter = document.getElementById(`${section}-count`);
    const dataKey = section === 'paths' ? 'reading_paths' : section;
    const total   = (allData[dataKey] || []).length;

    if (counter) {
        counter.textContent = items.length < total
            ? `Showing ${items.length} of ${total}`
            : `${total} entries`;
    }

    if (!items.length) {
        gallery.innerHTML = '<p class="no-results">No entries match the current filters.</p>';
        return;
    }

    gallery.innerHTML = items.map(item => buildCard(section, item, section)).join('');
    gallery.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', e => {
            if (e.target.closest('a, button')) return;
            openModal(card.dataset.section, card.dataset.id, true);
        });
    });
}

function buildCard(section, item, currentContext = activeSection) {
    const id   = item.id;
    const name = item.name || item.title || '—';
    const meta = buildCardMeta(section, item);
    const badge = buildBadgeInline(section, currentContext);
    const imageHtml = (section === 'figures' || section === 'emblems' || section === 'essays') && item.image_url
        ? `<img src="${item.image_url}" alt="${name}" class="card-image" onerror="this.style.display='none'">`
        : '';

    return `<div class="card card-${section}" data-section="${section}" data-id="${id}">
        ${imageHtml}
        <div class="card-header">
            <div class="card-title">${name}</div>
            <div class="card-meta-inline">${meta}</div>
        </div>
        <div class="card-summary">${item.summary || ''}</div>
        <div class="card-footer">
            <span class="card-read-more">Read full essay →</span>
            ${badge}
        </div>
    </div>`;
}

function buildCardMeta(section, item) {
    if (section === 'figures') {
        const years = item.birth_year ? `${item.birth_year}–${item.death_year || '?'}` : '';
        return `<div class="card-meta">${[years, item.nationality, item.location].filter(Boolean).join(' · ')}</div>`;
    }
    if (section === 'texts')    return `<div class="card-meta">${[item.year, item.language, item.location].filter(Boolean).join(' · ')}</div>`;
    if (section === 'concepts') return item.category ? `<div class="card-meta">${humaniseCategory(item.category)}</div>` : '';
    if (section === 'emblems')  return `<div class="card-meta">${[item.source_book, item.year].filter(Boolean).join(' · ')}</div>`;
    if (section === 'essays')   return item.period ? `<div class="card-meta">${item.period}</div>` : '';
    if (section === 'scholars') {
        const dates = item.birth_year ? `${item.birth_year}–${item.death_year || 'present'}` : '';
        return `<div class="card-meta">${[dates, item.nationality, item.institution].filter(Boolean).join(' · ')}</div>`;
    }
    if (section === 'debates')  return `<div class="card-meta">${[item.period, item.positions?.map(p=>p.scholar).slice(0,2).join(' vs. ')].filter(Boolean).join(' · ')}</div>`;
    if (section === 'paths') {
        const diff = item.difficulty ? `<span class="path-difficulty">${capitalise(item.difficulty)}</span>` : '';
        const time = item.estimated_time ? item.estimated_time : '';
        return `<div class="card-meta">${[diff, time, item.steps ? `${item.steps.length} steps` : ''].filter(Boolean).join(' · ')}</div>`;
    }
    return '';
}

function buildBadgeInline(section, currentContext = activeSection) {
    if (currentContext === section && !modalStack.length) return '';
    return `<span class="card-badge card-badge-inline badge-${section}"></span>`;
}

function buildBadge(section) {
    const labels = { figures: 'Figure', concepts: 'Concept', texts: 'Text', essays: 'Essay', emblems: 'Emblem', scholars: 'Scholar', debates: 'Debate', paths: 'Path' };
    return `<span class="card-badge badge-${section}">${labels[section] || section}</span>`;
}

// ─── Emblem Books (grouped view) ───────────────────────────────────────────────

function renderEmblemBooks() {
    const container = document.getElementById('emblem-books-container');
    if (!container) return;
    const state = filterState['emblem-books'];
    let emblems = [...allData.emblems];

    if (state.source_book) emblems = emblems.filter(e => e.source_book === state.source_book);
    if (state.theme) {
        const themeConceptMap = { 'nigredo': [1], 'albedo': [2], 'rubedo': [3], 'hermetic': [14,15,16], 'rosy-cross': [30] };
        const targetIds = themeConceptMap[state.theme] || [];
        emblems = emblems.filter(e => (e.concepts || []).some(cid => targetIds.includes(cid)));
    }

    switch (state.sort) {
        case 'alpha': emblems.sort((a, b) => (a.title || '').localeCompare(b.title || '')); break;
        case 'theme': emblems.sort((a, b) => (getEmblemTheme(a) || '').localeCompare(getEmblemTheme(b) || '')); break;
    }

    if (!emblems.length) { container.innerHTML = '<p class="no-results">No emblems match the current filters.</p>'; return; }

    const grouped = {};
    emblems.forEach(e => { const book = e.source_book || 'Unknown'; if (!grouped[book]) grouped[book] = []; grouped[book].push(e); });

    const bookOrder = ['Rosicrucian Emblems', 'Atalanta Fugiens', 'Hermetic Garden'];
    const orderedBooks = bookOrder.filter(b => grouped[b]).concat(Object.keys(grouped).filter(b => !bookOrder.includes(b)));

    let html = '';
    orderedBooks.forEach(bookName => {
        const be = grouped[bookName];
        const info = { 'Rosicrucian Emblems': { author:'Cramer',year:1617 }, 'Atalanta Fugiens': { author:'Maier',year:1617 }, 'Hermetic Garden': { author:'Stolcius',year:1624 } }[bookName] || { author:'—',year:'—' };
        html += `<div class="emblem-book-section">
            <div class="emblem-book-header"><h3>${bookName}</h3><div class="emblem-book-meta">${info.author} (${info.year}) — ${be.length} emblems</div></div>
            <div class="emblem-gallery">${be.map(emb => buildCard('emblems', emb)).join('')}</div>
        </div>`;
    });

    container.innerHTML = html;
    container.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', e => {
            if (e.target.closest('a, button')) return;
            openModal(card.dataset.section, card.dataset.id, true);
        });
    });
}

function getEmblemTheme(emblem) {
    const conceptIds = emblem.concepts || [];
    const map = { 'Nigredo': [1], 'Albedo': [2], 'Rubedo': [3], 'Theosis': [4], 'Hieros Gamos': [5] };
    for (const [theme, ids] of Object.entries(map)) {
        if (conceptIds.some(cid => ids.includes(cid))) return theme;
    }
    return 'Other';
}

// ─── Modal system ─────────────────────────────────────────────────────────────

function setupModal() {
    const closeBtn = document.getElementById('modal-close');
    const backBtn  = document.getElementById('modal-back');
    const overlay  = document.getElementById('modal');
    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (backBtn)  backBtn.addEventListener('click', modalBack);
    if (overlay)  overlay.addEventListener('click', e => { if (e.target === overlay) closeModal(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') { closeModal(); closeCompare(); closeConceptBrowser(); } });
}

function openModal(section, id, clearStack = false) {
    if (clearStack) modalStack.length = 0;
    const dataKey = section === 'paths' ? 'reading_paths' : section;
    const item = (allData[dataKey] || []).find(x => String(x.id) === String(id));
    if (!item) return;
    modalStack.push({ section, id });
    renderModal(section, item);
    updateHash(section, id);
    document.getElementById('modal').classList.add('open');
}

function renderModal(section, item) {
    const body    = document.getElementById('modal-body');
    const backBtn = document.getElementById('modal-back');
    const crumb   = document.getElementById('modal-breadcrumb');

    if (backBtn) backBtn.hidden = modalStack.length <= 1;
    if (crumb)   crumb.textContent = modalStack.length > 1
        ? modalStack.slice(0, -1).map(s => {
            const prev = (allData[s.section] || []).find(x => String(x.id) === String(s.id));
            return prev ? (prev.name || prev.title) : '';
          }).join(' › ')
        : '';

    body.innerHTML = buildModalContent(section, item);

    body.querySelectorAll('[data-link-section][data-link-id]').forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            const ls = link.dataset.linkSection, li = link.dataset.linkId;
            if (link.classList.contains('step-open-btn') || link.tagName === 'BUTTON') {
                closeModal();
                navigateTo(ls);
                openModal(ls, li, true);
            } else {
                openModal(ls, li, false);
            }
        });
    });
}

function closeModal() {
    clearHash();
    document.getElementById('modal').classList.remove('open');
    modalStack.length = 0;
}

function modalBack() {
    if (modalStack.length <= 1) return;
    modalStack.pop();
    const prev = modalStack[modalStack.length - 1];
    const dk   = prev.section === 'paths' ? 'reading_paths' : prev.section;
    const item = (allData[dk] || []).find(x => String(x.id) === String(prev.id));
    if (item) { renderModal(prev.section, item); updateHash(prev.section, prev.id); }
}

// ─── Modal content builders ───────────────────────────────────────────────────

function buildModalContent(section, item) {
    switch (section) {
        case 'figures':  return buildFigureModal(item);
        case 'concepts': return buildConceptModal(item);
        case 'texts':    return buildTextModal(item);
        case 'essays':   return buildEssayModal(item);
        case 'emblems':  return buildEmblemModal(item);
        case 'scholars': return buildScholarModal(item);
        case 'debates':  return buildDebateModal(item);
        case 'paths':    return buildPathModal(item);
        default: return '';
    }
}

function relLink(section, id, label) {
    return `<a href="#" class="rel-link" data-link-section="${section}" data-link-id="${id}">${label}</a>`;
}

function buildFigureModal(f) {
    let h = `<h2>${f.name}</h2>`;
    if (f.birth_year) {
        h += `<div class="modal-meta-row">
            <span class="meta-pill">${f.birth_year}–${f.death_year || '?'}</span>
            <span class="meta-pill">${f.nationality || ''}</span>
            <span class="meta-pill">${f.primary_discipline || ''}</span>
            ${f.location ? `<span class="meta-pill">📍 ${f.location}</span>` : ''}
        </div>`;
    }
    if (f.essay) h += `<div class="modal-essay">${paragraphify(f.essay)}</div>`;
    if (f.genealogical_position) h += `<h3>Genealogical Position</h3><p>${f.genealogical_position}</p>`;
    if (f.embodied_practice)     h += `<h3>Practice &amp; Method</h3><p>${f.embodied_practice}</p>`;
    if (f.emblem_books_created?.length) {
        h += `<h3>Emblem Books Created</h3><ul>`;
        f.emblem_books_created.forEach(book => {
            if (typeof book === 'string') h += `<li><em>${escHtml(book)}</em></li>`;
            else {
                h += `<li><em>${escHtml(book.title)}</em> (${book.year}, ${book.location})`;
                if (book.total_emblems) h += ` — ${book.total_emblems} emblems`;
                if (book.innovation)    h += ` — ${book.innovation}`;
                h += `</li>`;
            }
        });
        h += '</ul>';
    }
    if (f.scholarly_debates) {
        h += `<h3>Historiographical Debate: ${f.scholarly_debates.topic}</h3><ul>`;
        f.scholarly_debates.positions.forEach(p => { h += `<li>${p}</li>`; });
        h += '</ul>';
    }
    if (f.key_works?.length) h += `<h3>Key Works</h3><ul>${f.key_works.map(w => `<li><em>${w}</em></li>`).join('')}</ul>`;
    if (f.concepts?.length) {
        const links = f.concepts.map(cid => { const c = allData.concepts.find(x => x.id === cid); return c ? relLink('concepts', cid, c.name) : null; }).filter(Boolean);
        if (links.length) h += `<h3>Related Concepts</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (f.influenced_figures?.length) {
        const links = f.influenced_figures.map(ifig => {
            if (!ifig.figure_id) return null;
            const fig = allData.figures.find(x => x.id === ifig.figure_id);
            if (!fig) return null;
            const label = ifig.influence_type ? `${fig.name} <span class="influence-type">(${ifig.influence_type})</span>` : fig.name;
            return relLink('figures', ifig.figure_id, label);
        }).filter(Boolean);
        if (links.length) h += `<h3>Influenced Figures</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (f.influenced_by_figures?.length) {
        const links = f.influenced_by_figures.map(ibyfig => {
            if (!ibyfig.figure_id) return null;
            const label = ibyfig.influence_type ? `${ibyfig.figure_name} <span class="influence-type">(${ibyfig.influence_type})</span>` : ibyfig.figure_name;
            return `<span class="rel-link-text">${label}</span>`;
        }).filter(Boolean);
        if (links.length) h += `<h3>Influenced By</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (f.influences?.length) {
        const links = f.influences.map(name => {
            const fig = allData.figures.find(x => x.name.toLowerCase().includes(name.toLowerCase()) || name.toLowerCase().includes(x.name.toLowerCase()));
            return fig ? relLink('figures', fig.id, name) : `<span class="rel-link-text">${escHtml(name)}</span>`;
        });
        h += `<h3>Intellectual Influences</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (f.scholars?.length) h += `<h3>Primary Scholars</h3><p class="scholars-list">${f.scholars.join(', ')}</p>`;
    if (f.gender_awareness) h += `<h3>Gender &amp; Access</h3><p class="gender-note">${f.gender_awareness}</p>`;
    if (f.scholarship?.length) h += buildScholarshipSection(f.scholarship);
    return h;
}

function buildConceptModal(c) {
    let h = `<h2>${c.name}</h2>`;
    if (c.category) h += `<div class="modal-meta-row"><span class="meta-pill">${humaniseCategory(c.category)}</span></div>`;

    // Cross-filter button
    h += `<button class="concept-browse-btn" onclick="openConceptBrowser(${c.id}, '${escHtml(c.name).replace(/'/g, "\\'")}')">Browse all entries tagged with this concept →</button>`;

    if (c.essay) h += `<div class="modal-essay">${paragraphify(c.essay)}</div>`;
    if (c.operational_meaning || c.philosophical_meaning || c.spiritual_meaning) {
        h += `<h3>Dimensions of Meaning</h3>`;
        if (c.operational_meaning)   h += `<p><strong>Operational:</strong> ${c.operational_meaning}</p>`;
        if (c.philosophical_meaning) h += `<p><strong>Philosophical:</strong> ${c.philosophical_meaning}</p>`;
        if (c.spiritual_meaning)     h += `<p><strong>Spiritual:</strong> ${c.spiritual_meaning}</p>`;
    }
    if (c.transmission_genealogy) h += `<h3>Transmission</h3><p>${c.transmission_genealogy}</p>`;
    if (c.related_concepts?.length) {
        const links = c.related_concepts.map(rcid => { const rc = allData.concepts.find(x => x.id === rcid); return rc ? relLink('concepts', rcid, rc.name) : null; }).filter(Boolean);
        if (links.length) h += `<h3>Related Concepts</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (c.emblem_links?.length) {
        const emblemLinks = [];
        c.emblem_links.forEach(eref => {
            const emblem = allData.emblems.find(x => x.id === eref.emblem_id);
            if (emblem) emblemLinks.push(relLink('emblems', eref.emblem_id, `${emblem.title} <span class="emblem-link-type">(${eref.link_type})</span>`));
        });
        if (emblemLinks.length) {
            h += `<h3>Exemplified By Emblems</h3><div class="rel-links">${emblemLinks.join('')}</div>`;
            if (c.emblem_links.some(e => e.explanation)) {
                h += `<div class="emblem-explanations">`;
                c.emblem_links.forEach(eref => {
                    if (eref.explanation) {
                        const emblem = allData.emblems.find(x => x.id === eref.emblem_id);
                        if (emblem) h += `<p><em>${emblem.title}:</em> ${eref.explanation}</p>`;
                    }
                });
                h += `</div>`;
            }
        }
    } else if (c.emblems?.length) {
        const links = c.emblems.slice(0, 12).map(eid => { const e = allData.emblems.find(x => x.id === eid); return e ? relLink('emblems', eid, e.title) : null; }).filter(Boolean);
        if (links.length) {
            const more = c.emblems.length > 12 ? ` <span class="rel-more">+${c.emblems.length - 12} more</span>` : '';
            h += `<h3>Illustrated By</h3><div class="rel-links">${links.join('')}${more}</div>`;
        }
    }
    return h;
}

function buildTextModal(t) {
    let h = `<h2>${t.title}</h2>`;
    h += `<div class="modal-meta-row">
        ${t.year     ? `<span class="meta-pill">${t.year}</span>` : ''}
        ${t.language ? `<span class="meta-pill">${t.language}</span>` : ''}
        ${t.location ? `<span class="meta-pill">📍 ${t.location}</span>` : ''}
    </div>`;
    if (t.essay) h += `<div class="modal-essay">${paragraphify(t.essay)}</div>`;
    if (t.historical_context)  h += `<h3>Historical Context</h3><p>${t.historical_context}</p>`;
    if (t.transmission_history) h += `<h3>Transmission</h3><p>${t.transmission_history}</p>`;
    if (t.concepts?.length) {
        const links = t.concepts.map(cid => { const c = allData.concepts.find(x => x.id === cid); return c ? relLink('concepts', cid, c.name) : null; }).filter(Boolean);
        if (links.length) h += `<h3>Related Concepts</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (t.scholarship?.length) h += buildScholarshipSection(t.scholarship);
    return h;
}

function buildEssayModal(essay) {
    let h = `<h2>${essay.title}</h2>`;
    h += `<div class="modal-meta-row">
        ${essay.author ? `<span class="meta-pill">${essay.author}</span>` : ''}
        ${essay.period ? `<span class="meta-pill">${essay.period}</span>` : ''}
    </div>`;
    if (essay.essay) h += `<div class="modal-essay">${paragraphify(essay.essay)}</div>`;
    if (essay.related_figures?.length) {
        const links = essay.related_figures.map(fname => { const fig = allData.figures.find(f => f.name === fname); return fig ? relLink('figures', fig.id, fname) : fname; });
        h += `<h3>Related Figures</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (essay.related_concepts?.length) {
        const links = essay.related_concepts.map(cname => { const c = allData.concepts.find(x => x.name === cname); return c ? relLink('concepts', c.id, cname) : cname; });
        h += `<h3>Related Concepts</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (essay.scholarship?.length) h += buildScholarshipSection(essay.scholarship);
    if (essay.scholarly_debates) {
        h += `<h3>Historiographical Debate: ${essay.scholarly_debates.topic}</h3><ul>`;
        essay.scholarly_debates.positions.forEach(p => {
            if (typeof p === 'object' && p.scholar) h += `<li><strong>${p.scholar}:</strong> ${p.position}</li>`;
            else h += `<li>${p}</li>`;
        });
        h += '</ul>';
    }
    return h;
}

function buildEmblemModal(e) {
    let h = `<h2>${e.title}</h2>`;
    if (e.image_url && !e.image_url.includes('placeholder')) {
        h += `<img src="${e.image_url}" class="emblem-plate" alt="${escHtml(e.title)} — emblem plate" onerror="this.style.display='none'">`;
    }
    h += `<div class="modal-meta-row">
        <span class="meta-pill">${e.source_book}</span>
        ${e.year     ? `<span class="meta-pill">${e.year}</span>` : ''}
        ${e.type     ? `<span class="meta-pill">${capitalise(e.type)}</span>` : ''}
        ${e.location ? `<span class="meta-pill">📍 ${e.location}</span>` : ''}
    </div>`;
    if (e.summary) h += `<blockquote class="visual-desc">${e.summary}</blockquote>`;
    if (e.essay && e.essay !== `[Essay on ${e.title}]` && !e.essay.startsWith('[')) {
        h += `<div class="modal-essay">${paragraphify(e.essay)}</div>`;
    }
    if (e.visual_elements?.length) {
        h += `<h3>Visual Elements</h3><div class="tag-list">${e.visual_elements.map(v => `<span class="tag">${v}</span>`).join('')}</div>`;
    }
    if (e.concepts?.length) {
        const links = e.concepts.map(cid => { const c = allData.concepts.find(x => x.id === cid); return c ? relLink('concepts', cid, c.name) : null; }).filter(Boolean);
        if (links.length) h += `<h3>Concepts Illustrated</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (e.figures?.length) {
        const links = e.figures.map(fid => { const f = allData.figures.find(x => x.id === fid); return f ? relLink('figures', fid, f.name) : null; }).filter(Boolean);
        if (links.length) h += `<h3>Creator / Associated Figures</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (e.authenticity) h += `<p class="authenticity-note">Authenticity: <strong>${capitalise(e.authenticity)}</strong></p>`;
    if (e.scholarship?.length) h += buildScholarshipSection(e.scholarship);
    return h;
}

function buildScholarshipSection(scholarship) {
    if (!scholarship?.length) return '';
    let h = '<h3>Scholarly Apparatus</h3><div class="scholarship-list">';
    scholarship.forEach(s => {
        if (!s.scholar) return;
        h += `<div class="scholarship-entry">
            <span class="scholar-name">${s.scholar}</span>
            <span class="scholar-ref">${s.reference || ''}</span>
            ${s.quote ? `<blockquote class="scholar-quote">"${s.quote}"</blockquote>` : ''}
        </div>`;
    });
    h += '</div>';
    return h;
}

function buildScholarModal(s) {
    let h = `<h2>${escHtml(s.name)}</h2>`;
    h += `<div class="modal-meta-row">
        ${s.birth_year ? `<span class="meta-pill">${s.birth_year}–${s.death_year || 'present'}</span>` : ''}
        ${s.nationality  ? `<span class="meta-pill">${escHtml(s.nationality)}</span>` : ''}
        ${s.institution  ? `<span class="meta-pill">${escHtml(s.institution)}</span>` : ''}
        ${s.scholarly_position ? `<span class="meta-pill">${escHtml(s.scholarly_position)}</span>` : ''}
    </div>`;
    if (s.essay) h += `<div class="modal-essay">${paragraphify(s.essay)}</div>`;
    if (s.methodology) h += `<h3>Methodology</h3><p>${escHtml(s.methodology)}</p>`;
    if (s.key_arguments?.length) {
        h += `<h3>Key Arguments</h3><ul>${s.key_arguments.map(a => `<li>${escHtml(a)}</li>`).join('')}</ul>`;
    }
    if (s.key_works?.length) {
        h += `<h3>Key Works</h3><ul>${s.key_works.map(w => `<li><em>${escHtml(w)}</em></li>`).join('')}</ul>`;
    }
    if (s.debates?.length) {
        const links = s.debates.map(did => {
            const d = allData.debates.find(x => x.id === did);
            return d ? relLink('debates', did, d.short_title || d.title) : null;
        }).filter(Boolean);
        if (links.length) h += `<h3>Debates</h3><div class="rel-links">${links.join('')}</div>`;
    }
    return h;
}

function buildDebateModal(d) {
    let h = `<h2>${escHtml(d.title)}</h2>`;
    if (d.question) h += `<blockquote class="visual-desc"><em>${escHtml(d.question)}</em></blockquote>`;
    h += `<div class="modal-meta-row">
        ${d.period ? `<span class="meta-pill">${escHtml(d.period)}</span>` : ''}
    </div>`;
    if (d.positions?.length) {
        h += `<h3>Positions</h3>`;
        d.positions.forEach(p => {
            h += `<div class="debate-position">
                <strong>${escHtml(p.scholar)}</strong>
                ${p.label ? ` — <em>${escHtml(p.label)}</em>` : ''}
                <p style="margin:.5rem 0 .25rem">${escHtml(p.argument)}</p>
                ${p.key_work ? `<div class="debate-key-work">Key work: <em>${escHtml(p.key_work)}</em></div>` : ''}
            </div>`;
        });
    }
    if (d.current_consensus) h += `<h3>Current Consensus</h3><p>${escHtml(d.current_consensus)}</p>`;
    if (d.essay) h += `<div class="modal-essay">${paragraphify(d.essay)}</div>`;
    if (d.related_figure_ids?.length) {
        const links = d.related_figure_ids.map(fid => {
            const f = allData.figures.find(x => String(x.id) === String(fid));
            return f ? relLink('figures', fid, f.name) : null;
        }).filter(Boolean);
        if (links.length) h += `<h3>Related Figures</h3><div class="rel-links">${links.join('')}</div>`;
    }
    if (d.related_concept_ids?.length) {
        const links = d.related_concept_ids.map(cid => {
            const c = allData.concepts.find(x => String(x.id) === String(cid));
            return c ? relLink('concepts', cid, c.name) : null;
        }).filter(Boolean);
        if (links.length) h += `<h3>Related Concepts</h3><div class="rel-links">${links.join('')}</div>`;
    }
    return h;
}

function buildPathModal(p) {
    let h = `<h2>${escHtml(p.title)}</h2>`;
    if (p.subtitle) h += `<p style="font-style:italic;color:var(--deep-brown);margin:.25rem 0 1rem">${escHtml(p.subtitle)}</p>`;
    h += `<div class="modal-meta-row">
        ${p.difficulty      ? `<span class="meta-pill">${capitalise(p.difficulty)}</span>` : ''}
        ${p.estimated_time  ? `<span class="meta-pill">${escHtml(p.estimated_time)}</span>` : ''}
        ${p.steps           ? `<span class="meta-pill">${p.steps.length} steps</span>` : ''}
    </div>`;
    if (p.description) h += `<p>${escHtml(p.description)}</p>`;
    if (p.steps?.length) {
        h += `<ol class="path-steps">`;
        p.steps.forEach(step => {
            const dataSection = step.section || 'figures';
            const dataId      = step.entity_id;
            h += `<li class="path-step">
                <div class="step-num">${step.order}</div>
                <div>
                    <div class="step-title" data-link-section="${dataSection}" data-link-id="${dataId}">
                        ${escHtml(step.entity_title || '')}
                    </div>
                    <div class="step-rationale">${escHtml(step.rationale || '')}</div>
                    ${step.reading_note ? `<div class="step-note">${escHtml(step.reading_note)}</div>` : ''}
                    <button class="step-open-btn" data-link-section="${dataSection}" data-link-id="${dataId}">Open entry →</button>
                </div>
            </li>`;
        });
        h += `</ol>`;
    }
    return h;
}

function paragraphify(text) {
    if (!text) return '';
    return text.split(/\n\n+/).map(p => `<p>${p.trim()}</p>`).join('');
}

function capitalise(s) { return s ? s[0].toUpperCase() + s.slice(1) : ''; }

// ─── Global search ────────────────────────────────────────────────────────────

function setupSearch() {
    const input    = document.getElementById('global-search');
    const panel    = document.getElementById('search-results-panel');
    const clearBtn = document.getElementById('search-clear');
    if (!input) return;

    let debounceTimer;
    input.addEventListener('input', () => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => runSearch(input.value.trim()), 200);
    });

    if (clearBtn) clearBtn.addEventListener('click', () => {
        input.value = '';
        if (panel) { panel.hidden = true; panel.innerHTML = ''; }
    });

    document.addEventListener('click', e => {
        if (panel && !e.target.closest('.search-bar-container')) panel.hidden = true;
    });

    input.addEventListener('focus', () => {
        if (input.value.trim().length >= 2) runSearch(input.value.trim());
    });
}

function getSearchTypes() {
    return ['figures', 'concepts', 'texts', 'emblems', 'essays', 'scholars', 'debates'];
}

function runSearch(query) {
    const panel = document.getElementById('search-results-panel');
    if (!panel) return;
    if (query.length < 2) { panel.hidden = true; return; }

    const types  = getSearchTypes();
    const qLower = query.toLowerCase();
    const results = [];

    types.forEach(section => {
        (allData[section] || []).forEach(item => {
            const name    = (item.name || item.title || '').toLowerCase();
            const summary = (item.summary || '').toLowerCase();
            const essay   = (item.essay || '').toLowerCase();
            let score = 0;
            if (name.includes(qLower))    score += 10;
            if (summary.includes(qLower)) score += 5;
            if (essay.includes(qLower))   score += 1;
            if (score > 0) results.push({ section, item, score });
        });
    });

    results.sort((a, b) => b.score - a.score);
    renderSearchResults(results, query, panel);
}

function renderSearchResults(results, query, panel) {
    if (!results.length) {
        panel.innerHTML = '<p class="search-no-results">No results found.</p>';
        panel.hidden = false;
        return;
    }

    const shown = results.slice(0, 30);
    const labels = { figures: 'Figure', concepts: 'Concept', texts: 'Text', essays: 'Essay', emblems: 'Emblem', scholars: 'Scholar', debates: 'Debate' };
    panel.innerHTML = `
        <div class="search-result-header">${results.length} result${results.length !== 1 ? 's' : ''} for "<em>${escHtml(query)}</em>"</div>
        ${shown.map(r => {
            const name    = r.item.name || r.item.title || '—';
            const snippet = highlight(truncate(r.item.summary || '', 120), query);
            return `<div class="search-result-item" data-section="${r.section}" data-id="${r.item.id}">
                <span class="card-badge badge-${r.section}">${labels[r.section] || r.section}</span>
                <span class="search-result-name">${highlight(name, query)}</span>
                <span class="search-result-snippet">${snippet}</span>
            </div>`;
        }).join('')}
        ${results.length > 30 ? `<div class="search-result-footer">Showing top 30 of ${results.length}</div>` : ''}
    `;
    panel.hidden = false;

    panel.querySelectorAll('.search-result-item').forEach(el => {
        el.addEventListener('click', () => {
            openModal(el.dataset.section, el.dataset.id, true);
            panel.hidden = true;
            const inp = document.getElementById('global-search');
            if (inp) inp.value = '';
        });
    });
}

function highlight(text, query) {
    if (!query) return escHtml(text);
    const safe  = escHtml(text);
    const safeQ = escHtml(query);
    const re    = new RegExp(`(${escRe(safeQ)})`, 'gi');
    return safe.replace(re, '<mark>$1</mark>');
}

function truncate(str, max) { return str.length <= max ? str : str.slice(0, max) + '…'; }

function escHtml(s) {
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function escRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

// ─── Navigation ───────────────────────────────────────────────────────────────

function setupNavigation() {
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const section = btn.dataset.section;
            if (!section) return;  // serendipity button has no data-section
            navigateTo(section);
            if (section === 'map') {
                setTimeout(() => {
                    if (window._leafletMap) { window._leafletMap.invalidateSize(); window._leafletMap.setView([50, 12], 4); }
                }, 150);
            } else if (section === 'emblem-books') {
                renderEmblemBooks();
            }
        });
    });
}

function navigateTo(section) {
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    const btn = document.querySelector(`.nav-btn[data-section="${section}"]`);
    if (btn) btn.classList.add('active');
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    const sec = document.getElementById(section);
    if (sec) sec.classList.add('active');
    activeSection = section;
}

// ─── Dark mode ────────────────────────────────────────────────────────────────

function setupDarkMode() {
    const btn = document.getElementById('dark-mode-toggle');
    const apply = (dark) => {
        document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
        localStorage.setItem('darkMode', dark ? '1' : '0');
        if (btn) btn.textContent = dark ? '☀ Light' : '☾ Dark';
    };
    apply(localStorage.getItem('darkMode') === '1');
    if (btn) btn.addEventListener('click', () =>
        apply(document.documentElement.getAttribute('data-theme') !== 'dark'));
}

// ─── Serendipity ──────────────────────────────────────────────────────────────

function setupSerendipity() {
    const btn = document.getElementById('serendipity-btn');
    if (!btn) return;
    btn.addEventListener('click', openRandom);
}

function openRandom() {
    const pool = ['figures', 'concepts', 'texts', 'emblems'].filter(s => allData[s]?.length);
    if (!pool.length) return;
    const section = pool[Math.floor(Math.random() * pool.length)];
    const items   = allData[section];
    const item    = items[Math.floor(Math.random() * items.length)];
    navigateTo(section);
    openModal(section, item.id, true);
}

// ─── URL hash routing ─────────────────────────────────────────────────────────

function updateHash(section, id) {
    history.replaceState(null, '', `#${section}:${encodeURIComponent(id)}`);
}

function clearHash() {
    history.replaceState(null, '', location.pathname + location.search);
}

function loadFromHash() {
    const hash = decodeURIComponent(location.hash.slice(1));
    if (!hash) return;
    const colonIdx = hash.indexOf(':');
    if (colonIdx === -1) return;
    const section = hash.slice(0, colonIdx);
    const id      = hash.slice(colonIdx + 1);
    if (!allData[section]) return;
    const item = allData[section].find(x => String(x.id) === String(id));
    if (!item) return;
    navigateTo(section);
    openModal(section, id, true);
}

// ─── Share button ─────────────────────────────────────────────────────────────

function setupShareButton() {
    const btn = document.getElementById('modal-share');
    if (!btn) return;
    btn.addEventListener('click', () => {
        const url = location.href;
        const orig = btn.textContent;
        if (navigator.clipboard) {
            navigator.clipboard.writeText(url).then(() => {
                btn.textContent = '✓ Copied!';
                setTimeout(() => { btn.textContent = orig; }, 1500);
            }).catch(() => { prompt('Copy this link:', url); });
        } else {
            prompt('Copy this link:', url);
        }
    });
}

// ─── Concept browser (cross-section filter) ───────────────────────────────────

function openConceptBrowser(conceptId, conceptName) {
    const overlay = document.getElementById('concept-browser');
    const title   = document.getElementById('cb-title');
    const body    = document.getElementById('cb-body');
    if (!overlay) return;

    title.textContent = `All entries tagged: "${conceptName}"`;

    const sections = [
        { key: 'figures', label: 'Historical Figures', id_field: 'concepts' },
        { key: 'texts',   label: 'Texts',              id_field: 'concepts' },
        { key: 'emblems', label: 'Emblems',             id_field: 'concepts' },
    ];

    let html = '';
    sections.forEach(({ key, label, id_field }) => {
        const matched = (allData[key] || []).filter(item =>
            (item[id_field] || []).map(Number).includes(Number(conceptId))
        );
        if (!matched.length) return;
        html += `<h3 class="cb-section-title">${label} (${matched.length})</h3><div class="cb-cards">`;
        matched.forEach(item => {
            const name = item.name || item.title || '—';
            const meta = item.birth_year ? `${item.birth_year}–${item.death_year || '?'}` : item.year ? item.year : '';
            html += `<div class="cb-card" data-section="${key}" data-id="${item.id}">
                <div class="cb-card-title">${escHtml(name)}</div>
                ${meta ? `<div class="cb-card-meta">${escHtml(meta)}</div>` : ''}
                <div class="cb-card-summary">${escHtml((item.summary || '').slice(0, 120))}…</div>
            </div>`;
        });
        html += '</div>';
    });

    if (!html) html = '<p style="color:var(--deep-brown);font-style:italic">No entries found tagged with this concept.</p>';
    body.innerHTML = html;
    overlay.hidden = false;

    body.querySelectorAll('.cb-card').forEach(card => {
        card.addEventListener('click', () => {
            overlay.hidden = true;
            navigateTo(card.dataset.section);
            openModal(card.dataset.section, card.dataset.id, true);
        });
    });

    document.getElementById('cb-close').onclick = () => { overlay.hidden = true; };
}

function closeConceptBrowser() {
    const overlay = document.getElementById('concept-browser');
    if (overlay) overlay.hidden = true;
}

// ─── Compare mode ─────────────────────────────────────────────────────────────

let compareActive = false;

function setupCompare() {
    const btn   = document.getElementById('modal-compare');
    const close = document.getElementById('compare-close');
    if (btn)   btn.addEventListener('click',   openCompare);
    if (close) close.addEventListener('click', closeCompare);
}

function openCompare() {
    const overlay = document.getElementById('compare-modal');
    if (!overlay || !modalStack.length) return;
    const cur  = modalStack[modalStack.length - 1];
    const item = (allData[cur.section] || []).find(x => String(x.id) === String(cur.id));
    if (!item) return;

    document.getElementById('compare-panel-a').innerHTML = buildModalContent(cur.section, item);
    document.getElementById('compare-panel-b').innerHTML = '<div class="compare-placeholder">Click any card or relational link while Compare is open to load it here.</div>';

    compareActive = true;
    overlay.hidden = false;
    closeModal();

    // Wire rel links in panel A to load into panel B
    wireComparePanelLinks(document.getElementById('compare-panel-a'));
}

function loadCompareB(section, id) {
    const item   = (allData[section] || []).find(x => String(x.id) === String(id));
    if (!item) return;
    const panelB = document.getElementById('compare-panel-b');
    panelB.innerHTML = buildModalContent(section, item);
    wireComparePanelLinks(panelB);
}

function wireComparePanelLinks(panel) {
    panel.querySelectorAll('[data-link-section][data-link-id]').forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            loadCompareB(link.dataset.linkSection, link.dataset.linkId);
        });
    });
}

function closeCompare() {
    const overlay = document.getElementById('compare-modal');
    if (overlay) overlay.hidden = true;
    compareActive = false;
}

// ─── Map ──────────────────────────────────────────────────────────────────────

function initializeMap() {
    const map = L.map('map-container').setView([50, 12], 4);
    window._leafletMap = map;

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors', maxZoom: 19
    }).addTo(map);

    const figureGroup = L.featureGroup();
    const textGroup   = L.featureGroup();
    const emblemGroup = L.featureGroup();
    const centerGroup = L.featureGroup();

    // ── Timeline date filter state ──
    let dateFrom = 1400, dateTo = 1800;

    function applyDateFilter() {
        figureGroup.eachLayer(marker => {
            const fig = marker._data; if (!fig) return;
            const y = fig.birth_year || 0;
            if (y === 0) { marker.setStyle({ opacity: 1, fillOpacity: 0.8 }); return; }
            const vis = y >= dateFrom && y <= dateTo;
            marker.setStyle({ opacity: vis ? 1 : 0, fillOpacity: vis ? 0.8 : 0 });
        });
        textGroup.eachLayer(marker => {
            const t = marker._data; if (!t) return;
            const y = Number(t.year) || 0;
            if (y === 0) { marker.setStyle({ opacity: 1, fillOpacity: 0.8 }); return; }
            const vis = y >= dateFrom && y <= dateTo;
            marker.setStyle({ opacity: vis ? 1 : 0, fillOpacity: vis ? 0.8 : 0 });
        });
    }

    // ── Figures ──
    allData.figures.forEach(figure => {
        if (!figure.lat || !figure.lng) return;
        const marker = L.circleMarker([figure.lat, figure.lng], {
            radius: 7, fillColor: '#e74c3c', color: '#c0392b', weight: 2, opacity: 1, fillOpacity: 0.8
        });
        marker._data = figure;
        const dateRange = `${figure.birth_year || '?'}–${figure.death_year || '?'}`;
        marker.bindPopup(buildMapPopup(figure.name, `${dateRange} · ${figure.nationality || ''}`, figure.summary));
        marker.bindTooltip(buildMapTooltip(figure.name, dateRange, figure.scholars), { sticky: true, className: 'map-tooltip' });
        marker.on('click', () => { openModal('figures', figure.id, true); showMapSidePanel('figures', figure); });
        figureGroup.addLayer(marker);
    });

    // ── Texts ──
    allData.texts.forEach(text => {
        if (!text.lat || !text.lng) return;
        const marker = L.circleMarker([text.lat, text.lng], {
            radius: 6, fillColor: '#3498db', color: '#2980b9', weight: 2, opacity: 1, fillOpacity: 0.8
        });
        marker._data = text;
        const year = text.year || '?';
        marker.bindPopup(buildMapPopup(text.title, `${year} · ${text.language || ''} · ${text.location || ''}`, text.summary));
        marker.bindTooltip(buildMapTooltip(text.title, year, []), { sticky: true, className: 'map-tooltip' });
        marker.on('click', () => { openModal('texts', text.id, true); showMapSidePanel('texts', text); });
        textGroup.addLayer(marker);
    });

    // ── Emblems (grouped by publication city) ──
    const emblemCities = {
        'Frankfurt am Main': { lat: 50.1109, lng: 8.6821, books: [] },
        'Oppenheim':         { lat: 49.8612, lng: 8.3699, books: [] },
        'Prague':            { lat: 50.0755, lng: 14.4378, books: [] }
    };
    allData.emblems.forEach(emb => {
        const city = emblemCities[emb.location];
        if (city && !city.books.includes(emb.source_book)) city.books.push(emb.source_book);
    });
    Object.entries(emblemCities).forEach(([city, data]) => {
        if (!data.books.length) return;
        const count = allData.emblems.filter(e => e.location === city).length;
        const marker = L.circleMarker([data.lat, data.lng], {
            radius: 9, fillColor: '#8e44ad', color: '#6c3483', weight: 2, opacity: 1, fillOpacity: 0.85
        });
        marker.bindPopup(`<strong>${city}</strong><br><em>Emblem Books:</em><br>${data.books.join('<br>')}<br>${count} emblems`);
        emblemGroup.addLayer(marker);
    });

    // ── Learning centers ──
    const centers = allData.map_centers || [];
    centers.forEach(c => {
        const marker = L.circleMarker([c.lat, c.lng], {
            radius: 10, fillColor: '#f39c12', color: '#d68910', weight: 2, opacity: 1, fillOpacity: 0.82
        });
        const popupHtml = `<strong style="font-size:1rem;color:#8b4513">${escHtml(c.name)}</strong>
            <br><em style="font-size:0.8em;color:#5c3d2e">${escHtml(c.role)}</em>
            <br><span style="font-size:0.82em;color:#444;line-height:1.5;display:block;margin-top:0.4rem">${escHtml(truncate(c.description || '', 200))}</span>`;
        marker.bindPopup(popupHtml, { maxWidth: 300 });
        marker.bindTooltip(`<strong>${escHtml(c.name)}</strong>`, { sticky: true, className: 'map-tooltip' });
        marker.on('click', () => showMapSidePanel('center', c));
        centerGroup.addLayer(marker);
    });

    [figureGroup, textGroup, emblemGroup, centerGroup].forEach(g => g.addTo(map));
    const all = L.featureGroup([figureGroup, textGroup, emblemGroup, centerGroup]);
    if (all.getLayers().length) map.fitBounds(all.getBounds(), { padding: [50, 50], maxZoom: 6 });

    // Layer toggle checkboxes
    [
        ['layer-figures',  figureGroup],
        ['layer-texts',    textGroup],
        ['layer-emblems',  emblemGroup],
        ['layer-centers',  centerGroup],
    ].forEach(([id, group]) => {
        const cb = document.getElementById(id);
        if (!cb) return;
        cb.addEventListener('change', () => { cb.checked ? group.addTo(map) : map.removeLayer(group); });
    });

    // ── Date range sliders ──
    const sliderFrom = document.getElementById('map-slider-from');
    const sliderTo   = document.getElementById('map-slider-to');
    const labelFrom  = document.getElementById('map-date-from');
    const labelTo    = document.getElementById('map-date-to');

    if (sliderFrom && sliderTo) {
        sliderFrom.addEventListener('input', () => {
            dateFrom = Number(sliderFrom.value);
            if (dateFrom > dateTo) { dateTo = dateFrom; sliderTo.value = dateFrom; }
            if (labelFrom) labelFrom.textContent = dateFrom;
            if (labelTo)   labelTo.textContent   = dateTo;
            applyDateFilter();
        });
        sliderTo.addEventListener('input', () => {
            dateTo = Number(sliderTo.value);
            if (dateTo < dateFrom) { dateFrom = dateTo; sliderFrom.value = dateTo; }
            if (labelFrom) labelFrom.textContent = dateFrom;
            if (labelTo)   labelTo.textContent   = dateTo;
            applyDateFilter();
        });
    }

    // ── Influence / transmission lines ──
    const lineGroup    = L.featureGroup();
    const figureCoords = {};
    allData.figures.forEach(f => { if (f.lat && f.lng) figureCoords[f.id] = [f.lat, f.lng]; });

    allData.figures.forEach(f => {
        if (!f.lat || !f.lng || !f.influenced_figures?.length) return;
        f.influenced_figures.forEach(inf => {
            if (!inf.figure_id) return;
            const dest = figureCoords[inf.figure_id];
            if (!dest) return;
            const line = L.polyline([[f.lat, f.lng], dest], {
                color: '#e67e22', weight: 1.5, opacity: 0.65, dashArray: '5,5'
            });
            line.bindTooltip(`${escHtml(f.name)} → ${escHtml(inf.figure_name || '')}`, { className: 'map-tooltip' });
            lineGroup.addLayer(line);
        });
    });

    const linesCheckbox = document.getElementById('layer-lines');
    if (linesCheckbox) {
        linesCheckbox.addEventListener('change', () => {
            linesCheckbox.checked ? lineGroup.addTo(map) : map.removeLayer(lineGroup);
        });
    }
}

function buildMapTooltip(name, dateOrYear, scholars) {
    let tip = `<strong>${escHtml(name)}</strong><br><em>${escHtml(String(dateOrYear))}</em>`;
    if (scholars?.length) tip += `<br><span style="font-size:0.8em">Scholars: ${escHtml(scholars.join(', '))}</span>`;
    return tip;
}

function buildMapPopup(title, meta, summary) {
    return `<strong>${escHtml(title)}</strong><br>
            <em style="font-size:0.85em">${escHtml(meta)}</em><br>
            <span style="font-size:0.85em;color:#555">${escHtml(truncate(summary || '', 120))}</span>`;
}

function showMapSidePanel(section, item) {
    const panel   = document.getElementById('map-side-panel');
    const title   = document.getElementById('map-side-title');
    const content = document.getElementById('map-side-content');
    if (!panel || !title || !content) return;

    title.textContent = item.name || item.title || '—';
    let html = '';
    if (section === 'figures') {
        html = `<p><strong>Life Span:</strong> ${item.birth_year || '?'}–${item.death_year || '?'}</p>
                <p><strong>Nationality:</strong> ${escHtml(item.nationality || 'Unknown')}</p>
                <p><strong>Location:</strong> ${escHtml(item.location || 'Unknown')}</p>
                ${item.primary_discipline ? `<p><strong>Discipline:</strong> ${escHtml(item.primary_discipline)}</p>` : ''}
                <p class="map-side-summary">${paragraphify(item.summary || '')}</p>`;
    } else if (section === 'texts') {
        html = `<p><strong>Year:</strong> ${item.year || '?'}</p>
                <p><strong>Language:</strong> ${escHtml(item.language || 'Unknown')}</p>
                <p><strong>Location:</strong> ${escHtml(item.location || 'Unknown')}</p>
                <p class="map-side-summary">${paragraphify(item.summary || '')}</p>
                ${item.historical_context ? `<p><em>${escHtml(item.historical_context)}</em></p>` : ''}`;
    } else if (section === 'center') {
        html = `<p><em style="color:var(--burnt-sienna)">${escHtml(item.role || '')}</em></p>
                <p class="map-side-summary">${paragraphify(item.description || '')}</p>`;
    }

    content.innerHTML = html;
    panel.classList.add('open');

    const closeBtn = document.getElementById('map-side-close');
    if (closeBtn) closeBtn.onclick = () => panel.classList.remove('open');
}

// ─── Timeline ─────────────────────────────────────────────────────────────────

function renderTimeline(activeCategory = 'all') {
    const container = document.getElementById('timeline-container');
    if (!container) return;
    const events = (allData.timeline || []).slice().sort((a, b) => a.year - b.year);
    container.innerHTML = '';

    events.forEach(ev => {
        const visible = activeCategory === 'all' || ev.category === activeCategory;
        const div = document.createElement('div');
        div.className = `tl-event ${ev.category}${visible ? '' : ' hidden'}`;

        const relatedFigs  = (ev.related_figures || []).filter(Boolean);
        const relatedTexts = (ev.related_texts   || []).filter(Boolean);
        const relatedHtml  = (relatedFigs.length || relatedTexts.length)
            ? `<div class="tl-related">
                ${relatedFigs.length  ? `<strong>Figures:</strong> ${escHtml(relatedFigs.join(', '))}` : ''}
                ${relatedFigs.length && relatedTexts.length ? ' &nbsp;·&nbsp; ' : ''}
                ${relatedTexts.length ? `<strong>Texts:</strong> ${escHtml(relatedTexts.join(', '))}` : ''}
               </div>` : '';

        const badgeLabels = { historical: 'Historical', text: 'Publication', figure: 'Figure', discovery: 'Discovery' };
        div.innerHTML = `
            <span class="tl-dot ${ev.category}"></span>
            <div class="tl-card">
                <div class="tl-header">
                    <span class="tl-year">${ev.year}</span>
                    <span class="tl-title">${escHtml(ev.title)}</span>
                    <span class="tl-badge ${ev.category}">${badgeLabels[ev.category] || ev.category}</span>
                </div>
                <div class="tl-desc">${escHtml(ev.description)}</div>
                ${relatedHtml}
            </div>`;
        container.appendChild(div);
    });
}

function setupTimelineFilters() {
    document.querySelectorAll('.tl-filter').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.tl-filter').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const cat = btn.dataset.category;
            document.querySelectorAll('.tl-event').forEach(ev => {
                ev.classList.toggle('hidden', cat !== 'all' && !ev.classList.contains(cat));
            });
        });
    });
}

// ─── Glossary ─────────────────────────────────────────────────────────────────

function renderGlossary() {
    const container = document.getElementById('glossary-container');
    if (!container) return;
    const state   = filterState.glossary;
    let terms = [...allData.dictionary].sort((a, b) => (a.term || '').localeCompare(b.term || ''));
    if (state.category) terms = terms.filter(t => t.category === state.category);
    if (state.letter)   terms = terms.filter(t => (t.term || '')[0]?.toUpperCase() === state.letter);

    const count = document.getElementById('glossary-count');
    if (count) count.textContent = `${terms.length} term${terms.length !== 1 ? 's' : ''}`;

    if (!terms.length) {
        container.innerHTML = '<p class="no-results">No terms match the current filters.</p>';
        return;
    }

    container.innerHTML = terms.map(t => `
        <div class="gloss-entry" id="gloss-${t.id}">
            <span class="gloss-term">${escHtml(t.term)}</span>
            ${t.latin && t.latin !== t.term.toLowerCase() ? ` <span class="gloss-also">(${escHtml(t.latin)})</span>` : ''}
            ${t.also_known_as?.length ? ` <span class="gloss-also">/ ${t.also_known_as.map(escHtml).join(', ')}</span>` : ''}
            ${t.etymology ? `<div class="gloss-etym"><em>Etymology:</em> ${escHtml(t.etymology)}</div>` : ''}
            <div class="gloss-def">${escHtml(t.definition)}</div>
            ${t.related_concept_id ? `<div class="gloss-concept-link">→ <a href="#" class="rel-link" data-link-section="concepts" data-link-id="${t.related_concept_id}">See full concept entry</a></div>` : ''}
        </div>`).join('');

    container.querySelectorAll('[data-link-section][data-link-id]').forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            openModal(link.dataset.linkSection, link.dataset.linkId, false);
        });
    });
}

function setupGlossaryFilters() {
    const nav = document.getElementById('glossary-letter-nav');
    if (nav) {
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach(letter => {
            const btn = document.createElement('button');
            btn.className = 'gloss-letter-btn';
            btn.dataset.letter = letter;
            btn.textContent = letter;
            btn.addEventListener('click', () => {
                const wasActive = btn.classList.contains('active');
                document.querySelectorAll('.gloss-letter-btn').forEach(b => b.classList.remove('active'));
                filterState.glossary.letter = wasActive ? '' : letter;
                if (!wasActive) btn.classList.add('active');
                renderGlossary();
            });
            nav.appendChild(btn);
        });
    }
    const catSel = document.querySelector('[data-filter="category"][data-section="glossary"]');
    if (catSel) catSel.addEventListener('change', () => {
        filterState.glossary.category = catSel.value;
        renderGlossary();
    });
    const reset = document.querySelector('.filter-reset[data-section="glossary"]');
    if (reset) reset.addEventListener('click', () => {
        filterState.glossary.category = '';
        filterState.glossary.letter   = '';
        if (catSel) catSel.value = '';
        document.querySelectorAll('.gloss-letter-btn').forEach(b => b.classList.remove('active'));
        renderGlossary();
    });
}

// ─── Confessional Network ─────────────────────────────────────────────────────

function setupMapViewToggle() {
    const geoBtn = document.getElementById('map-view-geo');
    const netBtn = document.getElementById('map-view-net');
    const netDiv = document.getElementById('confessional-network');
    if (!geoBtn || !netBtn || !netDiv) return;

    geoBtn.addEventListener('click', () => {
        geoBtn.classList.add('active'); netBtn.classList.remove('active');
        const mapWrap = document.querySelector('.map-wrap');
        if (mapWrap) { mapWrap.querySelector('#map-container').style.display = ''; }
        netDiv.style.display = 'none';
    });

    netBtn.addEventListener('click', () => {
        netBtn.classList.add('active'); geoBtn.classList.remove('active');
        const mapWrap = document.querySelector('.map-wrap');
        if (mapWrap) { mapWrap.querySelector('#map-container').style.display = 'none'; }
        netDiv.style.display = '';
        if (!netDiv.dataset.rendered) { renderConfessionalNetwork(); netDiv.dataset.rendered = '1'; }
    });
}

function renderConfessionalNetwork() {
    const container = document.getElementById('confessional-network');
    if (!container) return;

    const groups = {};
    allData.figures.forEach(f => {
        const aff = f.confessional_affiliation || 'Unknown';
        if (!groups[aff]) groups[aff] = [];
        groups[aff].push(f);
    });

    const palette = {
        'Lutheran': '#c0392b', 'Reformed/Calvinist': '#e67e22', 'Catholic': '#d4ac0d',
        'Paracelsian': '#27ae60', 'Rosicrucian': '#2980b9', 'Neoplatonist': '#8e44ad',
        'Hermetist': '#a569bd', 'Theosophist (Böhmist)': '#17a589', 'Jewish': '#1e8449',
        'Anglican': '#cb4335', 'Pietist': '#d35400', 'Illuminist': '#2c3e50', 'Unknown': '#95a5a6'
    };

    const affList = Object.keys(groups).sort((a, b) => groups[b].length - groups[a].length);
    const W = 900, H = 580;
    const cols = Math.ceil(Math.sqrt(affList.length));
    const rows = Math.ceil(affList.length / cols);
    const cellW = W / cols, cellH = H / rows;

    let svg = `<svg viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg" style="font-family:Georgia,serif">`;

    affList.forEach((aff, i) => {
        const col = i % cols, row = Math.floor(i / cols);
        const cx = cellW * col + cellW / 2, cy = cellH * row + cellH / 2;
        const r = Math.min(cellW, cellH) * 0.40;
        const color = palette[aff] || '#95a5a6';
        const figs = groups[aff];

        svg += `<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="${r.toFixed(1)}" fill="${color}" fill-opacity="0.12" stroke="${color}" stroke-width="1.5"/>`;
        svg += `<text x="${cx.toFixed(1)}" y="${(cy - r + 16).toFixed(1)}" text-anchor="middle" class="conf-group-label" fill="${color}">${escHtml(aff)} (${figs.length})</text>`;

        const maxFigs = Math.min(figs.length, 14);
        figs.slice(0, maxFigs).forEach((f, fi) => {
            const angle = (2 * Math.PI * fi / maxFigs) - Math.PI / 2;
            const pr = r * 0.58;
            const fx = (cx + pr * Math.cos(angle)).toFixed(1);
            const fy = (cy + pr * Math.sin(angle) + 4).toFixed(1);
            const surname = f.name.split(' ').slice(-1)[0];
            svg += `<text x="${fx}" y="${fy}" text-anchor="middle" class="conf-fig-label" fill="#2c2418"
                onclick="navigateTo('figures');openModal('figures','${f.id}',true)">${escHtml(surname)}</text>`;
        });
        if (figs.length > 14) {
            svg += `<text x="${cx.toFixed(1)}" y="${(cy + r - 6).toFixed(1)}" text-anchor="middle" fill="${color}" style="font-size:9px;font-family:Georgia,serif">+${figs.length - 14} more</text>`;
        }
    });

    svg += `</svg>
    <p style="text-align:center;font-size:.82rem;color:var(--deep-brown);margin-top:.5rem;font-style:italic">
        Click any surname to open that figure's entry · Grouped by primary confessional affiliation
    </p>`;
    container.innerHTML = svg;
}
