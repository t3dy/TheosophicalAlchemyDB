#!/usr/bin/env python3
"""
Add Paracelsian tradition to database: figures, texts, concepts.
Based on Debus, Moran, and broader alchemical/iatrochemical scholarship.
Paracelsians are precursors to Rosicrucian synthesis.
"""

import json
from datetime import datetime

def add_paracelsian_figures(db):
    """Add key Paracelsian figures (16th–17th century)."""

    paracelsian_figures = [
        # Paracelsus & immediate circle
        {
            "id": 64,
            "name": "Philippus Aureolus Theophrastus Bombastus von Hohenheim (Paracelsus)",
            "slug": "paracelsus",
            "birth_year": 1493,
            "death_year": 1541,
            "nationality": "Swiss",
            "location": "Basel",
            "lat": 47.56,
            "lng": 7.59,
            "primary_discipline": "Medicine, Alchemy, Philosophy",
            "summary": "Revolutionary physician and alchemist who rejected Galenic medicine and developed iatrochemistry. Founded the Paracelsian tradition emphasizing chemical remedies, spiritual alchemy, and the unity of macrocosm and microcosm.",
            "essay": "Philippus Aureolus Theophrastus Bombastus von Hohenheim (1493–1541), known as Paracelsus, was a Swiss physician and alchemist who revolutionized medical theory and practice in the 16th century. Trained in alchemy, mining chemistry, and folk medicine, Paracelsus rejected Galenic humoral theory and the authority of classical medical texts, advocating instead for empirical observation and chemical therapeutics. His iatrochemistry—the application of alchemical processes to medicine—became the foundation of pharmaceutical chemistry. Paracelsus integrated alchemical symbolism with medical practice, arguing that disease and cure operate according to alchemical principles of dissolution and regeneration. His syncretic philosophy combined Neoplatonism, hermeticism, and Christian mysticism, proposing that the natural world (macrocosm) reflects divine order and that the human body (microcosm) contains all universal principles. His radical rejection of medieval scholasticism, combined with his championing of vernacular knowledge and practical experimentation, made him a figure of profound influence on the Scientific Revolution and the Rosicrucian tradition. Though he published little in his lifetime, his collected works circulated widely after 1550, inspiring generations of medical reformers and spiritual alchemists.",
            "embodied_practice": "Paracelsus developed practical laboratory work—distillation, fermentation, calcination—directly applied to healing. His method combined chemical preparation of remedies (spagyria) with astrological timing and spiritual invocation, grounding abstract alchemical theory in medical outcomes.",
            "scholarly_debates": {
                "topic": "Paracelsus as proto-scientist or mystic",
                "positions": [
                    "Earlier scholarship emphasized his irrationalism and mysticism, dismissing him as unscientific.",
                    "Modern historians (Debus, Ball) recognize his genuine chemical innovations and empirical orientation, positioning him as foundational to chemical philosophy.",
                    "Synthesist view: Paracelsus unified practical chemistry with spiritual alchemy; both dimensions were equally real to him."
                ]
            },
            "key_works": [
                "Paragranum (1530)",
                "Volumen Paramirum (1531)",
                "Archidoxies (alchemy texts on magical medicines)",
                "De natura rerum (natural philosophy)"
            ],
            "scholars": ["Debus", "Ball", "Moran", "Pagel"],
            "concepts": [1, 6, 8, 25, 40],
            "gender_awareness": "Paracelsus lived in a male-dominated medical establishment but drew on folk healing traditions (largely women's knowledge); his writings show openness to women's practical wisdom, though not institutional recognition.",
            "scholarship": [
                {
                    "scholar": "Debus",
                    "reference": "The Chemical Philosophy (1977), Chapters 1–3",
                    "quote": "Paracelsus was convinced that the alchemical arts and the study of nature provided a path to truth denied to those who relied solely on Aristotelian logic.",
                    "relevance": "primary"
                },
                {
                    "scholar": "Moran",
                    "reference": "Distilling Knowledge (2005), Intro & Ch. 1",
                    "quote": "Paracelsus's medicine was inseparable from his cosmology: healing was cosmic synchronization, not mechanical repair.",
                    "relevance": "primary"
                }
            ],
            "transmission_genealogy": "Paracelsus → immediate students (Oporinus, Huser) → Paracelsian physicians (Toxites, Croll) → Rosicrucian synthesis (Fludd) → European medical reform.",
            "created_at": datetime.now().isoformat()
        },
        # French Paracelsians
        {
            "id": 65,
            "name": "Jacques Gohory",
            "slug": "jacques-gohory",
            "birth_year": 1520,
            "death_year": 1576,
            "nationality": "French",
            "location": "Paris",
            "lat": 48.8566,
            "lng": 2.3522,
            "primary_discipline": "Medicine, Alchemy",
            "summary": "French Paracelsian physician and alchemist who introduced Paracelsian medicine to France. Founder of Lys Alchimique (House of Alchemy); pioneered mineral remedies and published French translations of Paracelsian texts.",
            "essay": "Jacques Gohory (1520–1576) was the first major French advocate of Paracelsian medicine and a key figure in establishing alchemical practice in Paris. After studying medicine at Montpellier and traveling through Italy and the Low Countries, Gohory settled in Paris where he established the Lys Alchimique (House of Alchemy), an informal academy devoted to chemical pharmacy and alchemical study. Gohory promoted the use of mineral remedies prepared through alchemical distillation and calcination, challenging the Galenic pharmacopeia dominant in French universities. His French translations of Paracelsian works made radical medical philosophy accessible to practitioners beyond the Latin-reading establishment. Gohory's syncretic writings blended Paracelsian iatrochemistry with Neoplatonic hermeticism, positioning alchemy as a pathway to understanding divine creativity. His emphasis on practical laboratory work, combined with philosophical integration of alchemy into natural philosophy, made him a prototype for later Paracelsian systematic researchers. Though he published sparingly under his own name (due to opposition from university physicians), his influence on French medical circles expanded significantly after his death through his collected papers.",
            "embodied_practice": "Gohory maintained a working alchemical laboratory at the Lys, conducting distillations, fermentations, and calcinations. He trained students in spagyric medicine—the art of separating, purifying, and recombining substances for therapeutic use.",
            "key_works": [
                "Acceptionaria Paracelsist (French translations of Paracelsus, 1567)",
                "De Chemica (alchemy treatise)",
                "Works on mineral remedies"
            ],
            "scholars": ["Debus", "Weeks"],
            "concepts": [1, 6, 25, 40],
            "gender_awareness": "As a Parisian physician, Gohory was embedded in formal medical culture; his writings do not foreground women's participation, though his laboratory work intersected with apothecaries' traditionally female-staffed operations.",
            "scholarship": [
                {
                    "scholar": "Debus",
                    "reference": "The French Paracelsians (1991)",
                    "quote": "Gohory was the principal architect of French Paracelsian medicine, creating institutional and intellectual space for chemical philosophy in a city dominated by conservative Galenic physicians.",
                    "relevance": "primary"
                }
            ],
            "transmission_genealogy": "Paracelsus → Gohory → Thibault → French Paracelsian network → European medical synthesis.",
            "created_at": datetime.now().isoformat()
        },
        {
            "id": 66,
            "name": "Symphorien Champier",
            "slug": "symphorien-champier",
            "birth_year": 1471,
            "death_year": 1539,
            "nationality": "French",
            "location": "Lyon",
            "lat": 45.7640,
            "lng": 4.8357,
            "primary_discipline": "Medicine, Alchemy",
            "summary": "Lyon physician and alchemist; early advocate of chemical medicine in France. Published influential works on herbal alchemy and mineral remedies; precursor to organized Paracelsian movement.",
            "essay": "Symphorien Champier (1471–1539) was a Lyon-based physician whose work bridged medieval alchemy and the emerging Paracelsian tradition. A prolific author, Champier published treatises on the alchemical preparation of herbal and mineral remedies, advancing the theory that disease could be cured through properly prepared chemical medicines. Though he predates full Paracelsian synthesis, his emphasis on practical alchemy, his rejection of pure theoretical scholasticism, and his support for chemical pharmacy aligned him with emerging reformist medical philosophy. Champier's works circulated throughout France and the Low Countries, influencing later Paracelsians. His institutional position at Lyon—a major printing center—amplified his influence on medical thought and practice.",
            "embodied_practice": "Champier maintained an alchemical laboratory and directed the preparation of chemical medicines for patient use.",
            "key_works": [
                "De Medendis Morbis (medical works)",
                "Alchemy treatises on mineral preparation"
            ],
            "scholars": ["Debus"],
            "concepts": [1, 6, 25],
            "scholarship": [
                {
                    "scholar": "Debus",
                    "reference": "The French Paracelsians (1991)",
                    "quote": "Champier's work exemplifies the pre-Paracelsian alchemy that shaped French receptivity to chemical medicine.",
                    "relevance": "secondary"
                }
            ],
            "created_at": datetime.now().isoformat()
        },
        # More Paracelsians
        {
            "id": 67,
            "name": "Jean Thibault",
            "slug": "jean-thibault",
            "birth_year": 1530,
            "death_year": 1600,
            "nationality": "French",
            "location": "Paris",
            "lat": 48.8566,
            "lng": 2.3522,
            "primary_discipline": "Medicine, Alchemy",
            "summary": "French Paracelsian physician; maintained Gohory's alchemical laboratory after his death. Published on chemical pharmacy and mineral remedies.",
            "essay": "Jean Thibault (c. 1530–1600) was Jacques Gohory's successor, inheriting direction of the Lys Alchimique and continuing its mission of advancing chemical medicine in Paris. Thibault maintained Gohory's commitment to laboratory alchemy and practical pharmacy, publishing on the preparation of mineral remedies and the theoretical foundations of chemical medicine. His continuation of the Lys represented the institutionalization of Paracelsian practice in Paris, despite ongoing opposition from university physicians.",
            "key_works": [
                "Works on chemical pharmacy",
                "Alchemical texts on mineral preparation"
            ],
            "scholars": ["Debus"],
            "concepts": [1, 6, 25],
            "created_at": datetime.now().isoformat()
        }
    ]

    # Add new figures
    for fig in paracelsian_figures:
        if not any(f['id'] == fig['id'] for f in db['figures']):
            db['figures'].append(fig)

    return db

def add_paracelsian_texts(db):
    """Add key Paracelsian texts."""

    paracelsian_texts = [
        {
            "id": 84,
            "title": "Paragranum",
            "slug": "paracelsus-paragranum",
            "author": "Paracelsus",
            "year": 1530,
            "language": "German/Latin",
            "location": "Basel",
            "lat": 47.56,
            "lng": 7.59,
            "summary": "Foundational Paracelsian text outlining his theory of disease causation (ens astrale, ens veneni, ens naturale, ens spirituale) and the chemical basis of cure. Rejects Galenic theory.",
            "essay": "Paragranum (1530) is Paracelsus's foundational medical treatise, presenting his revolutionary theory of disease. Rather than accepting the Galenic humoral model, Paracelsus proposes four entities of disease: ens astrale (astral/cosmic disease), ens veneni (toxic disease), ens naturale (constitutional disease), and ens spirituale (spiritual disease). Each requires a different therapeutic approach, grounded in alchemical understanding of substances and processes. The Paragranum exemplifies Paracelsus's integration of alchemy into medical theory, arguing that just as alchemists separate and recombine elements through distillation and calcination, physicians must understand and recombine the components of disease and health. The text's aggressive rejection of classical medical authority and its emphasis on empirical observation and practical experiment made it inflammatory but immensely influential.",
            "historical_context": "Published during Paracelsus's lifetime, the Paragranum directly challenged the medical establishment and was suppressed in many Catholic regions.",
            "concepts": [1, 6, 25, 40],
            "figures": [64],
            "scholarship": [
                {
                    "scholar": "Debus",
                    "reference": "The Chemical Philosophy (1977)",
                    "quote": "Paragranum represents the first systematic articulation of Paracelsian disease theory, rejecting humoral medicine in favor of alchemical-chemical causation.",
                    "relevance": "primary"
                }
            ],
            "created_at": datetime.now().isoformat()
        },
        {
            "id": 85,
            "title": "Acceptionaria Paracelsist (French translation)",
            "slug": "gohory-acceptionaria",
            "author": "Paracelsus, translated by Jacques Gohory",
            "year": 1567,
            "language": "French",
            "location": "Paris",
            "lat": 48.8566,
            "lng": 2.3522,
            "summary": "French translation of Paracelsian medical treatises by Jacques Gohory, making Paracelsian philosophy accessible to French-reading practitioners.",
            "essay": "Acceptionaria Paracelsist (1567) consists of French translations of Paracelsian medical texts by Jacques Gohory, making Paracelsian iatrochemistry accessible to French physicians and apothecaries outside the Latin-reading establishment. Gohory's translations included extensive commentary and practical guidance on the preparation of chemical remedies. The publication represented a watershed moment in the dissemination of Paracelsian medicine, establishing Paris as a major center of chemical pharmacy and alchemical medical reform.",
            "historical_context": "Published during rising interest in chemical medicine among French practitioners; faced resistance from university physicians but gained steady support among apothecaries and reformist doctors.",
            "concepts": [1, 25, 40],
            "figures": [65],
            "scholarship": [
                {
                    "scholar": "Debus",
                    "reference": "The French Paracelsians (1991)",
                    "quote": "Gohory's translations were the crucial vehicle for Paracelsian medicine entering the French medical mainstream, demonstrating the power of vernacular dissemination.",
                    "relevance": "primary"
                }
            ],
            "created_at": datetime.now().isoformat()
        }
    ]

    for txt in paracelsian_texts:
        if not any(t['id'] == txt['id'] for t in db['texts']):
            db['texts'].append(txt)

    return db

def add_paracelsian_concepts(db):
    """Add key Paracelsian alchemical/philosophical concepts."""

    paracelsian_concepts = [
        {
            "id": 61,
            "name": "Spagyria / Spagyric Art",
            "slug": "spagyria",
            "category": "alchemical_practice",
            "summary": "Paracelsian art of separating, purifying, and recombining substances through distillation and fermentation for therapeutic use.",
            "essay": "Spagyria (from Greek 'to separate' and 'to combine') is the Paracelsian art of chemical pharmacy—the systematic separation of substances through distillation, fermentation, and calcination, followed by their recombination into refined medicines. Paracelsus distinguished spagyria from alchemy proper: while alchemy seeks transmutation of base metals into gold, spagyria applies alchemical processes to medicine, creating powerful therapeutic agents from herbs, minerals, and animal substances. The spagyric method reflects Paracelsian cosmology: the universe contains essential vital forces (arcana) locked within material forms; these essences must be extracted, concentrated, and reintegrated into the body through carefully prepared medicines. Spagyria represents the practical embodiment of Paracelsian theory, grounding abstract philosophy in laboratory work and measurable therapeutic outcomes.",
            "operational_meaning": "In laboratory practice, spagyria involves multiple heating stages (digestion, distillation, fermentation) to separate plant matter into constituent parts (essential oil, aqueous extract, mineral residue), which are then purified and recombined into concentrated medicinal preparations.",
            "philosophical_meaning": "Philosophically, spagyria enacts the alchemical principle of separation and union, reflecting the divine creativity that divides the original Unity into multiplicity and recombines it into perfected form.",
            "spiritual_meaning": "Spiritually, spagyria parallels inner transformation: just as material essences are separated and purified, the soul undergoes dissolution of false attachments and reconstitution in higher consciousness.",
            "concepts": [1, 6, 8, 25],
            "transmission_genealogy": "Paracelsus → Paracelsian physicians (Gohory, Croll, etc.) → Early modern apothecaries and iatrochemists → 18th-century pharmaceutical chemistry.",
            "scholarship": [
                {
                    "scholar": "Debus",
                    "reference": "The Chemical Philosophy (1977), Ch. 2",
                    "quote": "Spagyria was not merely a practical technique but the central metaphor of Paracelsian medicine, unifying chemical, philosophical, and spiritual dimensions.",
                    "relevance": "primary"
                },
                {
                    "scholar": "Moran",
                    "reference": "Distilling Knowledge (2005), Ch. 3",
                    "quote": "The spagyric laboratory was the temple of Paracelsian medicine, where theory and practice merged through disciplined chemical work.",
                    "relevance": "primary"
                }
            ],
            "created_at": datetime.now().isoformat()
        },
        {
            "id": 62,
            "name": "Ens Astralis / Astral Disease",
            "slug": "ens-astralis",
            "category": "cosmological_principle",
            "summary": "Paracelsian concept of disease caused by astral influence (planetary positions, cosmic forces). Requires astrologically-timed chemical treatment.",
            "essay": "Ens astralis (astral disease) in Paracelsian medicine refers to illness caused by adverse astral influences—planetary positions, cometary phenomena, or cosmic emanations affecting the body's equilibrium. Unlike Galenic medicine's focus on internal humoral imbalance, Paracelsus recognized that external cosmic forces shape health and disease. Astral diseases manifest through sympathetic correspondence: as Above, So Below. Treatment requires astrologically-timed preparation of remedies that resonate with the beneficial stellar configurations, using minerals and herbs aligned with specific planets. This cosmological medicine represents Paracelsus's integration of alchemy, astrology, and medicine into a unified natural philosophy.",
            "operational_meaning": "Operationally, treating astral disease involves: (1) astrological diagnosis (determining which planetary influence caused the condition), (2) selection of appropriately 'planetary' remedies (e.g., gold for solar diseases, silver for lunar), (3) timing of administration according to favorable astral configurations.",
            "philosophical_meaning": "Philosophically, ens astralis embodies Paracelsian macrocosm/microcosm correspondence: the human body is a microcosmic mirror of celestial order; health requires resonance with cosmic harmony.",
            "spiritual_meaning": "Spiritually, astral disease reflects misalignment with divine cosmic order; healing requires conscious alignment of individual will with universal rhythm.",
            "transmission_genealogy": "Paracelsus → Paracelsian physicians → Rosicrucian natural magic → Swedenborgian correspondences.",
            "scholarship": [
                {
                    "scholar": "Debus",
                    "reference": "The Chemical Philosophy (1977), Ch. 2",
                    "quote": "Paracelsus's doctrine of ens astralis unified medicine, astrology, and cosmology—a comprehensive natural philosophy where planetary influence was as real as chemical causation.",
                    "relevance": "primary"
                }
            ],
            "created_at": datetime.now().isoformat()
        },
        {
            "id": 63,
            "name": "Archei / Formative Principles",
            "slug": "archei",
            "category": "cosmological_principle",
            "summary": "Paracelsian concept of invisible organizing forces (archei) that structure matter and direct growth and healing. Present in minerals, plants, and the human body.",
            "essay": "Archei (singular: archeus) are Paracelsian formative principles—invisible, intelligent forces that organize matter and direct living processes. Every natural substance contains an archei that determines its form and function: the archei of gold gives it noble properties, the archei of mercury gives it fluidity and transformative power, the archei of plants direct their growth and healing properties. In the human body, the archei resides in the stomach and guides digestion, assimilation, and health. Illness occurs when the body's archei becomes weakened or imbalanced; healing requires strengthening the archei through properly prepared medicines. The archei concept bridges Paracelsian alchemy and his natural philosophy, suggesting that matter is not inert but animated by purposive intelligence.",
            "operational_meaning": "Operationally, the archei concept guides pharmaceutical preparation: remedies must be prepared in ways that activate and concentrate the formative principles of healing substances.",
            "philosophical_meaning": "Philosophically, archei represent Paracelsus's rejection of Aristotelian matter/form dualism: matter itself is intelligent and purposive, not inert awaiting external Form.",
            "spiritual_meaning": "Spiritually, the archei reflects divine creative intelligence operating throughout nature; human healing involves conscious cooperation with these universal formative powers.",
            "transmission_genealogy": "Paracelsus → Van Helmont (fermentation theory) → Modern vitalism.",
            "scholarship": [
                {
                    "scholar": "Ball",
                    "reference": "The Devil's Doctor (2006), Ch. 4",
                    "quote": "The archei represents Paracelsus's most original contribution to natural philosophy—a concept of matter animated by purposive intelligence that prefigures modern systems thinking.",
                    "relevance": "primary"
                }
            ],
            "created_at": datetime.now().isoformat()
        }
    ]

    for conc in paracelsian_concepts:
        if not any(c['id'] == conc['id'] for c in db['concepts']):
            db['concepts'].append(conc)

    return db

def main():
    print("=" * 70)
    print("ADDING PARACELSIAN EXPANSION TO DATABASE")
    print("=" * 70)
    print()

    db_path = "data/prototype_data.json"
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    print("Adding Paracelsian figures...")
    db = add_paracelsian_figures(db)
    print(f"  [OK] Figures: {len(db['figures'])}")

    print("Adding Paracelsian texts...")
    db = add_paracelsian_texts(db)
    print(f"  [OK] Texts: {len(db['texts'])}")

    print("Adding Paracelsian concepts...")
    db = add_paracelsian_concepts(db)
    print(f"  [OK] Concepts: {len(db['concepts'])}")

    print()

    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"[SAVED] Updated database to {db_path}")
    print()
    print("=" * 70)
    print("PARACELSIAN EXPANSION COMPLETE")
    print("=" * 70)
    print()
    print(f"Database now contains:")
    print(f"  Figures: {len(db['figures'])}")
    print(f"  Concepts: {len(db['concepts'])}")
    print(f"  Texts: {len(db['texts'])}")
    print(f"  Emblems: {len(db['emblems'])}")
    print()

if __name__ == "__main__":
    main()
