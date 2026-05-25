#!/usr/bin/env python3
"""Quick final push: add 15 more figures/concepts to reach 50+ target."""

import json
from datetime import datetime

db_path = "data/prototype_data.json"
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

more_figures = [
    {"id": 89, "name": "Bernard Palissy", "slug": "bernard-palissy", "birth_year": 1510, "death_year": 1589, "nationality": "French", "location": "Saintes", "lat": 45.7489, "lng": -0.6328, "primary_discipline": "Pottery, Alchemy", "summary": "French ceramicist and alchemist; conducted alchemical experiments seeking transmutation.", "essay": "Bernard Palissy (c. 1510–1589) was a French master ceramicist famous for his innovative pottery techniques. Palissy was equally devoted to alchemy, conducting experiments seeking transmutation and the Philosopher's Stone.", "concepts": [1, 6, 25], "created_at": datetime.now().isoformat()},
    {"id": 90, "name": "Michael Maier", "slug": "michael-maier", "birth_year": 1568, "death_year": 1622, "nationality": "German", "location": "Prague", "lat": 50.0755, "lng": 14.4378, "primary_discipline": "Alchemy, Medicine", "summary": "German alchemist; created elaborate alchemical emblems (Atalanta Fugiens).", "essay": "Michael Maier (1568–1622) was a German alchemist and court physician to Rudolf II. His Atalanta Fugiens presents 50 alchemical emblems with musical compositions.", "concepts": [1, 6, 25, 62], "created_at": datetime.now().isoformat()},
    {"id": 91, "name": "Johann Arndt", "slug": "johann-arndt", "birth_year": 1555, "death_year": 1621, "nationality": "German", "location": "Eisleben", "lat": 51.5294, "lng": 11.5517, "primary_discipline": "Theology, Alchemy", "summary": "German theologian; integrated alchemy into Christian spiritual practice.", "essay": "Johann Arndt (1555–1621) integrated alchemical principles into Christian mysticism, teaching spiritual transformation through alchemical metaphor.", "concepts": [1, 6, 25], "created_at": datetime.now().isoformat()},
    {"id": 92, "name": "Gerhard Dorn", "slug": "gerhard-dorn", "birth_year": 1530, "death_year": 1600, "nationality": "German", "location": "Frankfurt", "lat": 50.1109, "lng": 8.6821, "primary_discipline": "Medicine, Alchemy", "summary": "German Paracelsian; published alchemical-medical treatises.", "essay": "Gerhard Dorn (1530–1600) was a German Paracelsian who synthesized Paracelsian medicine with Hermetic philosophy.", "concepts": [1, 25, 61], "created_at": datetime.now().isoformat()},
    {"id": 93, "name": "Jābir ibn Ḥayyān (Geber)", "slug": "jabir", "birth_year": 721, "death_year": 815, "nationality": "Persian", "location": "Khorasan", "lat": 35.0, "lng": 65.0, "primary_discipline": "Alchemy", "summary": "Islamic Golden Age alchemist; foundational work on distillation.", "essay": "Jābir ibn Ḥayyān was an 8th-century Persian alchemist whose systematic work on distillation and mineral preparation became foundational to European alchemy.", "concepts": [1, 6, 25, 61, 65], "created_at": datetime.now().isoformat()},
    {"id": 94, "name": "al-Rāzī", "slug": "al-razi", "birth_year": 854, "death_year": 925, "nationality": "Persian", "location": "Rey", "lat": 35.7, "lng": 51.3, "primary_discipline": "Medicine, Alchemy", "summary": "Islamic Golden Age physician; pioneering work on pharmaceutical chemistry.", "essay": "Muhammad al-Rāzī (854–925) was a Persian physician whose medical works became foundational to pharmaceutical practice.", "concepts": [1, 25, 61], "created_at": datetime.now().isoformat()},
    {"id": 95, "name": "Albertus Magnus", "slug": "albertus-magnus", "birth_year": 1193, "death_year": 1280, "nationality": "German", "location": "Cologne", "lat": 50.9355, "lng": 6.9582, "primary_discipline": "Alchemy", "summary": "Medieval Dominican; integrated alchemy into natural philosophy.", "essay": "Albertus Magnus (1193–1280) integrated alchemy into scholastic natural philosophy, influencing Renaissance thought.", "concepts": [1, 6, 25], "created_at": datetime.now().isoformat()},
    {"id": 96, "name": "Roger Bacon", "slug": "roger-bacon", "birth_year": 1214, "death_year": 1292, "nationality": "English", "location": "Oxford", "lat": 51.7520, "lng": -1.2578, "primary_discipline": "Alchemy", "summary": "Medieval friar; advocate of experimentation; conducted alchemical research.", "essay": "Roger Bacon (c. 1214–1292) was a medieval Franciscan whose advocacy of experimentation influenced early modern science.", "concepts": [1, 6, 25], "created_at": datetime.now().isoformat()},
    {"id": 97, "name": "Nicholas Flamel", "slug": "nicholas-flamel", "birth_year": 1330, "death_year": 1418, "nationality": "French", "location": "Paris", "lat": 48.8566, "lng": 2.3522, "primary_discipline": "Alchemy", "summary": "Legendary French alchemist; icon of alchemical aspiration.", "essay": "Nicholas Flamel became legendary for his claimed transmutation achievement, profoundly influencing European alchemy.", "concepts": [1, 6, 8], "created_at": datetime.now().isoformat()},
    {"id": 98, "name": "Arnaldus de Villanova", "slug": "arnaldus-villanova", "birth_year": 1240, "death_year": 1311, "nationality": "Catalan", "location": "Valencia", "lat": 39.4699, "lng": -0.3763, "primary_discipline": "Medicine, Alchemy", "summary": "Medieval physician; pioneering work on distillation.", "essay": "Arnaldus de Villanova (c. 1240–1311) pioneered chemical preparation of medicines, prefiguring Paracelsian spagyria.", "concepts": [1, 25, 61, 65], "created_at": datetime.now().isoformat()},
    {"id": 99, "name": "Meister Eckhart", "slug": "meister-eckhart", "birth_year": 1260, "death_year": 1328, "nationality": "German", "location": "Cologne", "lat": 50.9355, "lng": 6.9582, "primary_discipline": "Mysticism", "summary": "Medieval mystic; emphasized ego dissolution resonating with alchemy.", "essay": "Meister Eckhart's theology of divine nothingness influenced alchemical-mystical thought.", "concepts": [1, 6], "created_at": datetime.now().isoformat()},
    {"id": 100, "name": "Johann Tauler", "slug": "johann-tauler", "birth_year": 1300, "death_year": 1361, "nationality": "German", "location": "Strasbourg", "lat": 48.5734, "lng": 7.7521, "primary_discipline": "Mysticism", "summary": "Medieval mystic; influenced alchemical-mystical synthesis.", "essay": "Johann Tauler's emphasis on inner transformation influenced Paracelsian mysticism.", "concepts": [1, 6], "created_at": datetime.now().isoformat()},
]

for fig in more_figures:
    if not any(f['id'] == fig['id'] for f in db['figures']):
        db['figures'].append(fig)

more_concepts = [
    {"id": 75, "name": "Nigredo", "slug": "nigredo-stage", "category": "alchemical_stage", "summary": "First stage: putrefaction and blackening; breakdown of ego and false self.", "essay": "Nigredo is the first stage of the Great Work, characterized by putrefaction and blackening. Philosophically it represents breakdown of illusions and dissolution of ego.", "operational_meaning": "In practice: materials putrefy and blacken", "philosophical_meaning": "Breakdown of false structures", "spiritual_meaning": "Death of false self", "created_at": datetime.now().isoformat()},
    {"id": 76, "name": "Albedo", "slug": "albedo-stage", "category": "alchemical_stage", "summary": "Second stage: whitening and purification; clarification and rebirth.", "essay": "Albedo is the second stage, where matter whitens and purifies. It represents clarification and emergence of the purified self.", "operational_meaning": "Purified substances become white or crystalline", "philosophical_meaning": "Clarification, emergence of true nature", "spiritual_meaning": "Rebirth and illumination", "created_at": datetime.now().isoformat()},
    {"id": 77, "name": "Rubedo", "slug": "rubedo-stage", "category": "alchemical_stage", "summary": "Third stage: reddening and perfection; Philosopher's Stone and enlightened consciousness.", "essay": "Rubedo is the final stage, producing the Philosopher's Stone. Matter becomes red or golden, representing perfected consciousness.", "operational_meaning": "Matter achieves red/golden color", "philosophical_meaning": "Perfection and integration", "spiritual_meaning": "Enlightened consciousness", "created_at": datetime.now().isoformat()},
]

for conc in more_concepts:
    if not any(c['id'] == conc['id'] for c in db['concepts']):
        db['concepts'].append(conc)

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("=" * 70)
print(f"DATABASE: {len(db['figures'])} figures, {len(db['concepts'])} concepts, {len(db['texts'])} texts, {len(db['emblems'])} emblems")
print(f"TOTAL: {sum(len(db[k]) for k in ['figures','concepts','texts','emblems'])}")
print(f"NEW ENTRIES: {(len(db['figures']) - 63) + (len(db['concepts']) - 60) + (len(db['texts']) - 83)}")
print("=" * 70)
