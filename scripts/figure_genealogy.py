"""
Figure Genealogy: deduplicate figures, add creators, fix emblem refs, add influence chains.
"""
import json, pathlib, re

DB = pathlib.Path("site/data/prototype_data.json")

# ── 1. INFLUENCE NETWORK ─────────────────────────────────────────────────────
# Map: figure name (or partial) -> list of names they were influenced by
# Names should match the canonical figure name (or close enough to grep).
INFLUENCES = {
    "Hermes Trismegistus": [],
    "Plotinus": ["Plato", "Hermes Trismegistus"],
    "Zosimos of Panopolis": ["Hermes Trismegistus"],
    "Jabir ibn Hayyan": ["Hermes Trismegistus"],
    "Jābir ibn Ḥayyān": ["Hermes Trismegistus"],
    "al-Rāzī": ["Jabir ibn Hayyan"],
    "Albertus Magnus": ["Jabir ibn Hayyan", "Aristotle"],
    "Roger Bacon": ["Albertus Magnus", "Jabir ibn Hayyan"],
    "Thomas Aquinas": ["Albertus Magnus"],
    "Arnauld de Villeneuve": ["Jabir ibn Hayyan", "al-Rāzī", "Roger Bacon"],
    "Arnaldus de Villanova": ["Jabir ibn Hayyan", "al-Rāzī", "Roger Bacon"],
    "Meister Eckhart": ["Thomas Aquinas", "Plotinus"],
    "Johann Tauler": ["Meister Eckhart"],
    "Nicolas Flamel": ["Roger Bacon", "Jabir ibn Hayyan"],
    "Nicholas Flamel": ["Roger Bacon", "Jabir ibn Hayyan"],
    "Catherine of Siena": ["Meister Eckhart", "Johann Tauler"],
    "Marsilio Ficino": ["Plotinus", "Hermes Trismegistus", "Plato"],
    "Pico della Mirandola": ["Marsilio Ficino", "Kabbalah"],
    "Johannes Trithemius": ["Marsilio Ficino", "Pico della Mirandola"],
    "Symphorien Champier": ["Marsilio Ficino", "Johannes Trithemius"],
    "Henry Cornelius Agrippa": ["Marsilio Ficino", "Pico della Mirandola", "Johannes Trithemius"],
    "Heinrich Cornelius Agrippa": ["Marsilio Ficino", "Pico della Mirandola", "Johannes Trithemius"],
    "Paracelsus": ["Marsilio Ficino", "Johannes Trithemius", "Arnauld de Villeneuve", "Henry Cornelius Agrippa"],
    "Philippus Aureolus": ["Marsilio Ficino", "Johannes Trithemius", "Arnauld de Villeneuve"],
    "Catherine de Medici": ["Italian Renaissance culture", "Marsilio Ficino"],
    "Gerhard Dorn": ["Paracelsus"],
    "Giambattista della Porta": ["Marsilio Ficino", "natural magic tradition"],
    "John Dee": ["Roger Bacon", "Marsilio Ficino", "Henry Cornelius Agrippa"],
    "Anna Zieglerin": ["Paracelsus", "court alchemy tradition"],
    "Giordano Bruno": ["Marsilio Ficino", "Hermes Trismegistus", "Ramon Llull"],
    "Philip Sidney": ["Giordano Bruno", "court humanism"],
    "Johann Arndt": ["Johann Tauler", "Meister Eckhart", "Paracelsus"],
    "Heinrich Khunrath": ["Paracelsus", "Gerhard Dorn", "John Dee"],
    "Henry Khunrath": ["Paracelsus", "Gerhard Dorn", "John Dee"],
    "Francis Bacon": ["natural magic tradition", "Giordano Bruno"],
    "Michael Maier": ["Paracelsus", "Heinrich Khunrath", "John Dee", "Henry Cornelius Agrippa"],
    "Robert Fludd": ["John Dee", "Henry Cornelius Agrippa", "Paracelsus", "Michael Maier"],
    "Jacob Böhme": ["Paracelsus", "Johann Tauler", "Meister Eckhart"],
    "Jan Baptist van Helmont": ["Paracelsus"],
    "Johann Valentin Andreae": ["Heinrich Khunrath", "Jacob Böhme", "John Dee"],
    "Samuel Fictuld": ["Rosicrucian tradition", "Johann Valentin Andreae"],
    "Rudolf II": ["Renaissance Hermeticism", "John Dee"],
    "Oswald Croll": ["Paracelsus"],
    "Andreas Libavius": ["Paracelsus", "iatrochemical tradition"],
    "Jean d'Espagnet": ["Paracelsus", "French Hermeticism"],
    "Sendivogius": ["Paracelsus", "Michael Sendivog"],
    "Thomas Vaughan": ["Henry Cornelius Agrippa", "Robert Fludd", "Jacob Böhme"],
    "Jane Lead": ["Jacob Böhme", "John Pordage"],
    "Henry More": ["Platonism", "Cambridge Neoplatonism"],
    "Elias Ashmole": ["John Dee", "English alchemical tradition"],
    "Ashmole, Elias": ["John Dee", "English alchemical tradition"],
    "Isaac Newton": ["Henry More", "Robert Boyle", "Giordano Bruno"],
    "Robert Boyle": ["Jan Baptist van Helmont", "Francis Bacon"],
    "Johann Georg Gichtel": ["Jacob Böhme"],
    "Joseph Glanvill": ["Henry More", "Cambridge Platonism"],
    "Leibniz": ["Giordano Bruno", "Hermeticism", "Michael Maier"],
    "George Cheyne": ["Isaac Newton", "Robert Boyle", "Henry More"],
    "Emmanuel Swedenborg": ["Plotinus", "Henry More", "Isaac Newton"],
    "William Law": ["Jacob Böhme"],
    "Claude de Saint-Martin": ["Martinez de Pasqually", "Jacob Böhme"],
    "Louis-Claude de Saint-Martin": ["Martinez de Pasqually", "Jacob Böhme"],
    "Karl von Eckartshausen": ["Jacob Böhme", "Emmanuel Swedenborg"],
    "Adam Weishaupt": ["Enlightenment philosophy"],
    "Cagliostro": ["Freemasonry", "Egyptian alchemy"],
    "William Blake": ["Jacob Böhme", "Emmanuel Swedenborg", "Paracelsus"],
    "Joseph Ennemoser": ["Mesmerism", "Romantic Naturphilosophie"],
    "Mary Anne Atwood": ["Jacob Böhme", "Emmanuel Swedenborg", "alchemical tradition"],
    "Éliphas Lévi": ["Karl von Eckartshausen", "occult philosophy"],
    "Anna Bonus Kingsford": ["Éliphas Lévi", "Hermeticism"],
    "Arthur Edward Waite": ["Éliphas Lévi", "Anna Bonus Kingsford"],
    "Brian Vickers": ["academic historiography", "Frances Yates"],
    "Adam McLean": ["alchemical scholarship tradition"],
    "Leonhard Thurneiser": ["Paracelsus"],
    "Jacques Gohory": ["Paracelsus", "French Humanism"],
    "Adam von Bodenstein": ["Paracelsus"],
    "Jean Thibault": ["Paracelsus", "court astrology"],
    "Henri Rantzau": ["Tycho Brahe", "Renaissance learning"],
    "Tycho Brahe": ["Renaissance astronomy", "Rudolf II"],
    "Pierre Potier": ["Paracelsus", "French iatrochemistry"],
    "Louis Camelle": ["Paracelsus"],
    "Godefridus Steidel": ["Paracelsus"],
    "Antoine de Gohorry": ["Paracelsus"],
    "Alonso Pena": ["Paracelsus"],
    "Bernard Palissy": ["Paracelsus", "craft knowledge"],
    "Balthasar Walther": ["Paracelsus", "Kabbalah"],
    "Leonhard Fuchs": ["Renaissance botany"],
    "Johannes Guinter": ["Galen", "Renaissance medicine"],
    "Iuliana Covaci": ["Paracelsian tradition"],
    "Benedict Chabotas": ["Paracelsian tradition"],
    "Franciscus Sylvius": ["Jan Baptist van Helmont", "iatrochemistry"],
    "William Bradwardine": ["Oxford mathematics", "natural philosophy"],
}

# ── 2. FIGURE ESSAYS FOR NEW CREATORS ────────────────────────────────────────
CRAMER_ESSAY = (
    "Daniel Cramer (1568-1637) was a German Lutheran theologian, pastor, and emblematist whose "
    "Emblemata Sacra (Emblemata Sacra Novi et Veteris Testamenti, Frankfurt, 1624) produced one of "
    "the most theologically sophisticated collections of sacred emblems of the seventeenth century. "
    "As pastor at the Marienkirche in Stettin (modern Szczecin) and later superintendent of Pomeranian "
    "churches, Cramer combined rigorous Lutheran orthodoxy with a deeply meditative piety that drew "
    "on the same devotional currents as the Rosicrucian movement without adopting its heterodox "
    "implications.\n\n"
    "The Emblemata Sacra presents forty emblems organized around scriptural emblematic sequences, "
    "each combining a symbolic image with a biblical motto, verse, and interpretive commentary. "
    "Cramer's imagery draws heavily on alchemical symbolism -- the cross within the circle, the "
    "phoenix, the pelican feeding its young -- but reframes these as Christian devotional figures "
    "rather than philosophical-alchemical instruments. The collection thus occupies a distinctive "
    "position at the intersection of Lutheran emblem culture and Rosicrucian symbolic vocabulary, "
    "demonstrating how alchemical visual language could be appropriated for orthodox purposes.\n\n"
    "Urszula Szulakowska's analysis of Cramer situates him within the broader German Reformation "
    "emblem tradition that transformed alchemical imagery into instruments of Lutheran spirituality. "
    "The Emblemata Sacra was published in the same year as Daniel Stolcius's Viridarium Chymicum "
    "(1624), and both collections reflect the emblematic florescence of the years immediately "
    "following the Rosicrucian manifestos. Cramer's work differs from Stolcius's in its strictly "
    "biblical and theological orientation; where Stolcius catalogues the alchemical process, Cramer "
    "meditates on Christian redemption using alchemical figures as spiritual metaphors.\n\n"
    "The historiographical significance of the Emblemata Sacra lies in its evidence for the "
    "permeation of alchemical visual culture into mainstream Lutheran devotional literature, a "
    "phenomenon that complicates simple divisions between 'religious' and 'alchemical' uses of "
    "emblematic symbolism. Cramer's forty emblems are among the most frequently reprinted and "
    "widely disseminated sacred emblems of the seventeenth century, indicating that his meditative "
    "appropriation of alchemical imagery resonated with a broad audience within Lutheran Germany."
)

STOLCIUS_ESSAY = (
    "Daniel Stolcius de Stolcenberg (c. 1600-after 1644) was a Bohemian physician and emblematist "
    "whose Viridarium Chymicum (Chemical Garden, Frankfurt, 1624) constitutes one of the most "
    "comprehensive alchemical emblem collections of the seventeenth century. Drawing on copper "
    "plates from the Musaeum Hermeticum (1625) and other Paracelsian collections, Stolcius produced "
    "107 emblems illustrating the stages and principles of alchemical transformation, accompanied "
    "by Latin verses in elegiac couplets that offered poetic meditations on each stage.\n\n"
    "The Viridarium Chymicum is structurally organized as a botanical metaphor -- a 'chemical "
    "garden' in which alchemical processes are presented as natural growth and transformation -- "
    "reflecting the Paracelsian integration of botanical, agricultural, and chemical imagery. "
    "Stolcius studied medicine at Marburg and Frankfurt and appears to have practiced medicine in "
    "Bohemia after the completion of his emblem collection; his subsequent biography is obscure, "
    "partly because of disruptions caused by the Thirty Years War.\n\n"
    "Lyndy Abraham's Dictionary of Alchemical Imagery provides detailed analysis of individual "
    "Viridarium emblems, tracing their visual sources and symbolic meanings within the broader "
    "alchemical tradition. De Jong's scholarship situates the collection within the post-Rosicrucian "
    "emblematic florescence of the 1620s, when the release of the Rosicrucian manifestos (1614-16) "
    "had stimulated intense interest in alchemical philosophy and its visual representation. The "
    "Viridarium Chymicum recycled copper plates from earlier publications, making it both an "
    "economic production and a systematic anthology of the alchemical visual tradition up to 1624.\n\n"
    "The historiographical significance of Stolcius lies in his position as an anthologist and "
    "systematizer of alchemical visual culture rather than as an original philosopher. His "
    "collection preserves and transmits imagery from the Rosarium Philosophorum and other earlier "
    "sources that might otherwise be accessible only in rare editions, making the Viridarium "
    "Chymicum an important resource for understanding how alchemical imagery circulated and was "
    "standardized in the early seventeenth century. The collection's organization around natural "
    "growth metaphors reflects the Paracelsian spagyric understanding of nature as an alchemical "
    "process."
)

# ─────────────────────────────────────────────────────────────────────────────

with open(DB, encoding="utf-8") as f:
    db = json.load(f)

figures = db["figures"]
emblems = db["emblems"]

fig_by_id = {f["id"]: f for f in figures}

# ── 3. MERGE DUPLICATE PAIRS ──────────────────────────────────────────────────
# (keep_id, remove_id, fields_to_copy_from_remove)
MERGES = [
    # Jabir: keep 19, essay from 93
    (19, 93, ["essay"]),
    # Arnauld: keep 55, essay from 98
    (55, 98, ["essay"]),
    # Flamel: keep 18, essay from 97
    (18, 97, ["essay"]),
    # Agrippa: keep 33, essay+scholars from 52
    (33, 52, ["essay", "scholars"]),
    # Paracelsus: keep 4, merge richer fields from 64
    (4, 64, ["essay", "scholarly_debates", "embodied_practice", "transmission_genealogy", "scholars"]),
    # Saint-Martin: keep 9, essay+scholars from 25
    (9, 25, ["essay", "scholars"]),
    # John Dee: keep 2, merge scholars from 85
    (2, 85, ["scholars"]),
    # Khunrath: keep 14 (better essay already), remove 39 -- just merge scholars
    (14, 39, ["scholars"]),
    # Gerhard Dorn: keep 29, remove 92
    (29, 92, []),
    # Giambattista della Porta: keep 32, remove 86
    (32, 86, []),
    # Johann Arndt: keep 45, remove 91
    (45, 91, []),
    # Gichtel: keep 26, essay from 61 (better)
    (26, 61, ["essay", "scholars"]),
    # Michael Maier: keep 10, remove 90
    (10, 90, []),
    # Roger Bacon: keep 22, remove 96
    (22, 96, []),
    # Thomas Vaughan: keep 11, scholars from 53
    (11, 53, ["scholars"]),
]

remove_ids = set()
for keep_id, remove_id, copy_fields in MERGES:
    keeper = fig_by_id.get(keep_id)
    donor  = fig_by_id.get(remove_id)
    if not keeper or not donor:
        print(f"  WARN: merge {keep_id}/{remove_id} skipped (missing)")
        continue
    for field in copy_fields:
        if field in donor and donor[field]:
            # For scholars, merge lists
            if field == "scholars" and isinstance(keeper.get("scholars"), list):
                existing = set(keeper["scholars"])
                new_scholars = [s for s in (donor["scholars"] or []) if s not in existing]
                keeper["scholars"] = keeper["scholars"] + new_scholars
            else:
                keeper[field] = donor[field]
    remove_ids.add(remove_id)
    print(f"  Merged ID {remove_id} -> ID {keep_id} ({keeper['name']})")

# Remove duplicates
orig_count = len(figures)
figures = [f for f in figures if f["id"] not in remove_ids]
db["figures"] = figures
print(f"\nRemoved {orig_count - len(figures)} duplicate figures ({len(figures)} remain)")

# ── 4. ADD NEW CREATOR FIGURES ────────────────────────────────────────────────
existing_names = {f["name"] for f in figures}
max_id = max(f["id"] for f in figures)

new_figures = []

if "Daniel Cramer" not in existing_names:
    max_id += 1
    new_figures.append({
        "id": max_id,
        "name": "Daniel Cramer",
        "slug": "daniel-cramer",
        "birth_year": 1568,
        "death_year": 1637,
        "nationality": "German",
        "location": "Stettin (Szczecin), Pomerania",
        "lat": 53.4289,
        "lng": 14.5530,
        "primary_discipline": "Theologian, Emblematist",
        "summary": (
            "Daniel Cramer (1568-1637) was a German Lutheran theologian and pastor whose "
            "Emblemata Sacra (Frankfurt, 1624) produced forty theologically sophisticated sacred "
            "emblems that appropriated alchemical symbolism for Lutheran devotional purposes."
        ),
        "essay": CRAMER_ESSAY,
        "scholars": ["Szulakowska", "Adams"],
        "key_works": ["Emblemata Sacra (1624)"],
        "image_url": "",
        "influences": ["Lutheran Reform tradition", "Rosicrucian symbolic vocabulary"],
        "concepts": [],
    })
    CRAMER_ID = max_id
    print(f"  Added Daniel Cramer (ID {max_id})")
else:
    cramer = next(f for f in figures if f["name"] == "Daniel Cramer")
    CRAMER_ID = cramer["id"]

if "Daniel Stolcius" not in existing_names and "Stolcius" not in existing_names:
    max_id += 1
    new_figures.append({
        "id": max_id,
        "name": "Daniel Stolcius de Stolcenberg",
        "slug": "daniel-stolcius-de-stolcenberg",
        "birth_year": 1600,
        "death_year": 1660,
        "nationality": "Bohemian",
        "location": "Frankfurt am Main",
        "lat": 50.1109,
        "lng": 8.6821,
        "primary_discipline": "Physician, Emblematist",
        "summary": (
            "Daniel Stolcius de Stolcenberg (c. 1600-c. 1660) was a Bohemian physician whose "
            "Viridarium Chymicum (Frankfurt, 1624) presented 107 alchemical emblems organized "
            "as a 'chemical garden', systematizing the Paracelsian alchemical visual tradition."
        ),
        "essay": STOLCIUS_ESSAY,
        "scholars": ["Abraham", "De Jong", "Szulakowska"],
        "key_works": ["Viridarium Chymicum (1624)"],
        "image_url": "",
        "influences": ["Paracelsus", "Michael Maier", "Rosicrucian emblem tradition"],
        "concepts": [],
    })
    STOLCIUS_ID = max_id
    print(f"  Added Daniel Stolcius (ID {max_id})")
else:
    stolcius = next((f for f in figures if "Stolcius" in f.get("name", "")), None)
    STOLCIUS_ID = stolcius["id"] if stolcius else None

figures.extend(new_figures)
db["figures"] = figures

# ── 5. FIX EMBLEM CREATOR REFERENCES ─────────────────────────────────────────
# Get correct Maier ID (after dedup, should be 10)
maier = next((f for f in figures if f["name"] == "Michael Maier"), None)
MAIER_ID = maier["id"] if maier else 10

# Map source_book -> correct figure ID
CREATOR_MAP = {
    "Rosicrucian Emblems": CRAMER_ID,
    "Emblemata Sacra": CRAMER_ID,
    "Atalanta Fugiens": MAIER_ID,
    "Hermetic Garden": STOLCIUS_ID,
    "Viridarium Chymicum": STOLCIUS_ID,
}

emblem_fix_count = 0
for emb in db["emblems"]:
    book = emb.get("source_book", "")
    for book_name, creator_id in CREATOR_MAP.items():
        if book_name.lower() in book.lower() and creator_id:
            if emb.get("figures") != [creator_id]:
                emb["figures"] = [creator_id]
                emblem_fix_count += 1
            break

print(f"\nFixed creator refs in {emblem_fix_count} emblems")
print(f"  Rosicrucian Emblems -> Daniel Cramer (ID {CRAMER_ID})")
print(f"  Atalanta Fugiens -> Michael Maier (ID {MAIER_ID})")
if STOLCIUS_ID:
    print(f"  Hermetic Garden -> Daniel Stolcius (ID {STOLCIUS_ID})")

# ── 6. ADD INFLUENCE CHAINS ───────────────────────────────────────────────────
# Build lookup: canonical name substring -> figure record
# We'll match by checking if key is a substring of figure name
def find_figure_by_name(name, figures):
    """Find figure whose name contains the given string (case-insensitive)."""
    name_l = name.lower()
    for f in figures:
        if name_l in f["name"].lower():
            return f
    return None

figures = db["figures"]  # refresh after additions
influence_count = 0

for fig in figures:
    fname = fig["name"]
    # Find matching influence entry
    matching_key = None
    for key in INFLUENCES:
        if key.lower() in fname.lower() or fname.lower() in key.lower():
            matching_key = key
            break

    if matching_key:
        influence_list = INFLUENCES[matching_key]
        if influence_list:
            fig["influences"] = influence_list
            influence_count += 1

print(f"\nAdded influence data to {influence_count} figures")

# ── 7. ADD EMBLEM_CREATOR FIELD TO FIGURES ────────────────────────────────────
# Mark each figure as creator of their emblem book
book_creators = {
    CRAMER_ID: "Emblemata Sacra (1624)",
    MAIER_ID: "Atalanta Fugiens (1617)",
}
if STOLCIUS_ID:
    book_creators[STOLCIUS_ID] = "Viridarium Chymicum (1624)"

for fig in figures:
    if fig["id"] in book_creators:
        fig["emblem_books_created"] = [book_creators[fig["id"]]]
        print(f"  {fig['name']}: emblem_books_created = {fig['emblem_books_created']}")

# ── 8. VERIFY AND SAVE ────────────────────────────────────────────────────────
with open(DB, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("\n=== FINAL STATE ===")
with open(DB, encoding="utf-8") as f:
    db2 = json.load(f)

print(f"Figures: {len(db2['figures'])}")
print(f"Emblems: {len(db2['emblems'])}")

# Check for remaining duplicates
from collections import defaultdict
name_counts = defaultdict(list)
for f in db2["figures"]:
    core = re.sub(r'\s*\(.*?\)', '', f['name']).strip().lower().split()[:2]
    name_counts[' '.join(core)].append(f['name'])
dups = {k: v for k, v in name_counts.items() if len(v) > 1}
if dups:
    print(f"\nRemaining potential duplicates: {len(dups)}")
    for k, v in dups.items():
        print(f"  {k}: {v}")
else:
    print("\nNo duplicate figures detected")

# Check emblem creator refs
from collections import Counter
fig_ref_counts = Counter()
for e in db2['emblems']:
    for fid in (e.get('figures') or []):
        fig_ref_counts[fid] += 1
print("\nEmblem figure refs:")
fig_by_id2 = {f['id']: f['name'] for f in db2['figures']}
for fid, cnt in fig_ref_counts.most_common():
    print(f"  ID {fid} ({fig_by_id2.get(fid,'??')}): {cnt} emblems")
