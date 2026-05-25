# Portrait Image Sourcing Strategy

## Status
Phase 2 portrait integration: CSS styling implemented; automated fetching blocked by API/URL accessibility issues.

## Figures with Confirmed Public-Domain Portraits

### Tier 1: Core Rosicrucian Figures (Priority)
- **Paracelsus** — Multiple portraits available (Wikimedia Commons)
- **John Dee** — 16th-century portrait (Ashmolean Museum, Wikimedia)
- **Robert Fludd** — Engraved portrait from Utriusque Cosmi (Wikimedia)
- **Jacob Böhme** — 17th-century portrait engraving (PICRYL, Yale Art Gallery)
- **Michael Maier** — 1617 engraved portrait (Wikimedia, Symbolae Aureae Mensae)
- **Emmanuel Swedenborg** — Multiple 18th-century portraits (Wikimedia, Carl Frederik von Breda)
- **Jan Baptist van Helmont** — 1666 line engraving (Wellcome Collection, PICRYL)

### Tier 2: Renaissance Philosophers & Precursors (Secondary)
- **Marsilio Ficino** — Renaissance portrait (Wikimedia)
- **Pico della Mirandola** — Renaissance portrait (Wikimedia)
- **Giordano Bruno** — 18th-century engraving based on lost original (PICRYL, Wikimedia)
- **Henry Cornelius Agrippa** — 16th-century engraving (Wikimedia)
- **Thomas Aquinas** — Medieval portrait (Wikimedia)
- **Roger Bacon** — Medieval portrait (Wikimedia)

### Tier 3: Scientific Revolution Figures (Tertiary)
- **Tycho Brahe** — Observatory portrait with astronomical instruments (Wikimedia)
- **Isaac Newton** — Engraved portrait (Wikimedia)
- **Francis Bacon** — 16th-century portrait (Wikimedia)
- **Robert Boyle** — 17th-century portrait (likely available)

## Sourcing Locations

| Source | Reliability | Access | Notes |
|--------|-------------|--------|-------|
| **Wikimedia Commons** | High | Direct | Often 404 on direct URLs; must use file pages |
| **Public Domain Image Archive** | High | Direct | pdimagearchive.org; works reliably |
| **PICRYL** | High | Direct | Public domain search engine; reliable downloads |
| **Wellcome Collection** | High | Direct | 17th-century engravings; open access |
| **Wikipedia** | Medium | Via REST API | `/api/rest_v1/page/summary/` endpoint |
| **Yale Art Gallery** | Medium | Direct | Some works public domain |
| **Archive.org** | Medium | API-dependent | Large digitized collections |

## Technical Blockers Encountered

### Attempted Approaches
1. **Wikimedia Commons API search** — HTTPError on all requests (likely parameter or authentication issue)
2. **Wikipedia REST API** — `/page/summary/` returned no images for search terms
3. **Direct Wikimedia URLs** — Many return 404 (URLs may be outdated or invalid format)
4. **Commons allimages API** — Timeout and connectivity issues
5. **Custom portrait mapping** — Direct URLs from Wikimedia failed; format may be incorrect

### Root Causes
- Wikimedia Commons API search may require specific parameter format
- Direct image URLs from `commons.wikimedia.org/wiki/Special:FilePath/` may not resolve
- File:// pages require API lookup to get actual image URL (`upload.wikimedia.org/` format)
- API throttling or bot detection blocking requests

## Recommended Next Steps

### Option A: Manual Curation (Immediate)
1. For each Tier 1 figure, manually browse Wikimedia Commons / PICRYL / Archive.org
2. Download high-res public domain portrait to `site/images/figures/`
3. Update `prototype_data.json` with `image_url` field
4. Test in portal; validate display
5. **Timeline:** 2–3 hours for 7 key figures

### Option B: Google Custom Search API (If Credentials Available)
1. Set up Google Custom Search with public-domain image filter
2. Query API for each figure
3. Programmatically download results
4. **Blocker:** Requires API key and quota

### Option C: Fallback to Public Domain Image Repositories
1. Use Archive.org API for batch downloads
2. Use Europeana API for 16th–18th century portraits
3. Implement fallback to generic scholarly avatar
4. **Timeline:** 4–5 hours

## Implementation Plan for Phase 2 Completion

**Goal:** 50% of figures (50/100) with portrait images by end of Phase 2

**Approach:**
1. ✅ CSS styling for `.card-image` (DONE)
2. Manually download 20–30 key figures from public domain sources (2–3 hours)
3. Batch-update `prototype_data.json` with `image_url` paths
4. Deploy and verify on GitHub Pages
5. Document any figures with no available public domain portraits
6. Flag Tier 2/3 figures for future manual addition

## Figures Without Readily Available Public-Domain Portraits

- Modern/Contemporary scholars (Vickers, Akerman, Szulakowska, etc.) — copyright restrictions
- Scholars who requested privacy (Zuber, etc.)
- Very obscure historical figures with no surviving portraits (many esoteric practitioners)
- Fictional/mythological figures (Hermes Trismegistus, Zosimos of Panopolis if no genuine portrait)

**Fallback:** Use a generic scholarly avatar icon or initials badge

---

**Last Updated:** 2026-05-25
**Owner:** Phase 2 Workstream 1 (Figure-Emblem Genealogy & Enrichment)
