"""Patch final remaining thin entries."""
import json, pathlib

DB = pathlib.Path("site/data/prototype_data.json")

QUERCETANUS = (
    "Joseph Duchesne (c. 1544-1609), known by his Latinized name Quercetanus, was the most prominent "
    "French Paracelsian physician of the late sixteenth and early seventeenth centuries, serving as "
    "physician to Henri IV of France and the most eloquent defender of chemical medicine against "
    "Galenist critics at the Paris medical faculty. His Sclopetarius (1576), Pharmaceutica (1607), "
    "and Diaetetycon Polyhistoricon (1606) elaborated the Paracelsian pharmaceutical system in a form "
    "adapted to learned French medical culture.\n\n"
    "Duchesne's central controversy was the Paris Faculty of Medicine's formal condemnation of "
    "antimony-based chemical remedies in 1566 and its sustained campaign against iatrochemical "
    "practice. Duchesne's defense of antimony and other Paracelsian remedies--backed by the royal "
    "court's patronage and by the practical efficacy that many physicians reported--represented the "
    "most sustained confrontation between Paracelsian and Galenic medicine in French institutional "
    "history. The controversy continued through the careers of his successors and was not formally "
    "resolved until the Faculty's grudging acceptance of antimony remedies in 1666.\n\n"
    "Duchesne's philosophical framework modified strict Paracelsian tria prima by incorporating "
    "elements of van Helmont's more empirically grounded iatrochemistry and by attempting to reconcile "
    "Paracelsian and Galenic categories where possible. His Pharmacopoea and related works provided "
    "practical formularies usable by physicians trained in both traditions. Lawrence Principe's "
    "historiographical work situates Duchesne within the network of court-supported Paracelsians who "
    "transformed Paracelsus from a heterodox reformer into an institutionally viable alternative to "
    "Galenic orthodoxy, demonstrating that the success of iatrochemistry in France depended as much "
    "on royal patronage and court politics as on philosophical argument."
)

IATROCHEM_CHEM = (
    "Iatrochemistry (from Greek iatros, physician, + chemia) is the systematic application of "
    "alchemical principles and laboratory procedures to medicine--the reform program that Paracelsus "
    "inaugurated in the early sixteenth century and that was elaborated by his successors into a "
    "comprehensive alternative to Galenic medicine. Chemical medicine diagnosed disease through the "
    "disruption of the tria prima (Sulphur, Mercury, Salt) and treated it with specific chemical "
    "remedies: antimony, mercury, vitriol, and spagyric preparations from medicinal plants.\n\n"
    "The movement's institutional development is complex. The Paris medical faculty condemned antimony "
    "remedies in 1566; the Royal College of Physicians in England similarly resisted iatrochemical "
    "practice. But court patronage--Henri IV's support of Duchesne, Rudolf II's invitation to "
    "Paracelsian practitioners--created protected spaces in which iatrochemical medicine could "
    "develop. By the mid-seventeenth century, practitioners like Johann Rudolf Glauber and, at "
    "Leiden, Franciscus Sylvius de le Boe had successfully pressed iatrochemistry into academic "
    "medicine, teaching acid-alkali chemistry as the foundation of physiology and pathology.\n\n"
    "The historiographical debate about iatrochemistry's relationship to early modern science has been "
    "transformed by Newman and Principe's revisionist work. Against the older narrative that positioned "
    "iatrochemistry as a failed proto-chemistry eventually superseded by Lavoisier's rational "
    "chemistry, Newman and Principe show that iatrochemical laboratory practice generated genuine "
    "chemical knowledge--new substances, new reactions, new analytical techniques--that fed directly "
    "into what is retrospectively called scientific chemistry. The boundary between iatrochemistry and "
    "chemistry is a historical construction; actual early modern practitioners often worked on both "
    "sides of it simultaneously, pursuing alchemical transmutation and pharmaceutical chemical analysis "
    "within the same laboratory practice."
)

ENS_ASTRALIS = (
    "Ens Astralis (astral being, astral disease) is a category in Paracelsian disease classification "
    "designating illness caused by adverse astral influence--disease whose ultimate cause lies not in "
    "the immediate physical constitution of the patient but in the malign influence of a specific "
    "celestial configuration acting through the astral body (corpus astralis) of the afflicted person. "
    "Paracelsus distinguished five types of disease cause (ens): ens astrale (astral), ens veneni "
    "(poison), ens naturale (natural constitution), ens spirituale (spiritual), and ens Deale "
    "(divine)--each requiring a different therapeutic approach.\n\n"
    "The concept of ens astralis depends on the Paracelsian account of the astral body as the subtle "
    "vehicle through which celestial influences act on the physical organism. The astral body mediates "
    "between the celestial macrocosm and the physical microcosm, making it the site of astrological "
    "influence on health and disease. When a malign celestial configuration affects the astral body, "
    "the resulting astral disease manifests in the physical body through characteristic symptoms "
    "determined by the nature of the influencing planet.\n\n"
    "This classification system enables Paracelsian medicine to integrate astrological diagnosis with "
    "chemical therapy: an ens astralis disease requires both an astral remedy (preparations associated "
    "with the planet governing the condition, selected and prepared at astrologically propitious times) "
    "and possibly a chemical remedy addressing the physical manifestation. Heinrich Khunrath's "
    "Amphitheatrum Sapientiae Aeternae invokes ens astralis in the context of its discussion of the "
    "philosopher's stone as the universal medicine capable of addressing disease at all five levels "
    "simultaneously. Urszula Szulakowska's work on Paracelsian medical iconography demonstrates how "
    "the ens classification was visualized in alchemical emblem literature, with each ens represented "
    "by characteristic symbols linking disease causation to cosmic structure."
)

with open(DB, encoding='utf-8') as f:
    db = json.load(f)

updates = 0
for fig in db['figures']:
    if 'Quercetanus' in fig.get('name', ''):
        fig['essay'] = QUERCETANUS
        updates += 1

for con in db['concepts']:
    name = con.get('name', '')
    if name == 'Iatrochemistry / Chemical Medicine':
        con['essay'] = IATROCHEM_CHEM
        updates += 1
    elif name == 'Ens Astralis / Astral Disease':
        con['essay'] = ENS_ASTRALIS
        updates += 1

with open(DB, 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f'Updated {updates} entries')

with open(DB, encoding='utf-8') as f:
    db2 = json.load(f)
for section, key in [('figures', 'name'), ('concepts', 'name'), ('texts', 'title')]:
    thin = [i for i in db2[section] if len(i.get('essay', '') or '') < 800]
    print(f'{section}: {len(thin)} still thin (<800 chars)')
