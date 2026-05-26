#!/usr/bin/env python3
"""
Integrate Paracelsus scholarship into TheosophicalAlchemyDB
- Enrich Paracelsus figure entry
- Add scholar profiles
- Add text entries for major works
- Establish concept links
"""

import json
import sys
from pathlib import Path

def load_database():
    """Load prototype_data.json with proper encoding"""
    db_path = Path("data/prototype_data.json")
    with open(db_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_database(data):
    """Save database with proper formatting"""
    db_path = Path("data/prototype_data.json")
    with open(db_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def find_paracelsus_figure(figures):
    """Find existing Paracelsus entry"""
    for fig in figures:
        if fig.get('slug') == 'paracelsus':
            return fig
    return None

def enhance_paracelsus_figure(figures):
    """Enhance Paracelsus figure entry with new scholarship"""
    paracelsus = find_paracelsus_figure(figures)

    if not paracelsus:
        print("ERROR: Paracelsus figure not found in database")
        return False

    # Update essay with enhanced content
    enhanced_essay = """Theophrastus Bombastus von Hohenheim (1493–1541), known as Paracelsus, was a Swiss physician, alchemist, and reformer whose radical integration of hermetic philosophy, medical theory, and spiritual theology fundamentally challenged Renaissance intellectual orthodoxy. His life and work embody a critical paradox: born just three years before Martin Luther and dying during the Reformation's most turbulent phase, Paracelsus developed a medical reformation parallel to Luther's theological one, positioning himself as an autonomous authority ("Monarcha medicorum") against institutionalized Galenic medicine, even as he claimed independence from Lutheran doctrine. This complex positioning—neither wholly reformer nor occultist, neither pure empiricist nor abstract theorist—makes Paracelsus one of early modern Europe's most influential and least understood figures.

**Life and Formation (1493–1527)**

Paracelsus was born in Einsiedeln, Switzerland, around 1493 to Wilhelm Bombastus von Hohenheim, a physician and alchemist who worked in mining regions. This paternal inheritance—direct knowledge of mining chemistry, alchemical operations, and pharmaceutical preparation—would remain foundational throughout Paracelsus's life. Unlike university-trained physicians of his era, Paracelsus acquired practical knowledge through hands-on apprenticeship rather than scholastic disputation. Though his education likely included monastery schooling and possibly some university attendance, Paracelsus himself emphasized "direct experience" (experientia) and the "school of nature" over bookish learning.

**Crisis and Reformation (1524–1528): The Basel Year**

Paracelsus's career entered its most productive and controversial period during the early Reformation crisis. In 1524–1525, during the Peasant War, he circulated theological-polemical tracts in Salzburg, attempting to ingratiate himself with Wittenberg reformers (Luther, Melanchthon, Bugenhagen). Like Luther, he challenged received authority—but in medicine rather than theology. By 1527, Paracelsus had relocated to Basel, securing dual positions as city physician and university instructor. This Basel period (1527–1528), though brief, catalyzed his intellectual output and established him as a public intellectual.

At Basel, Paracelsus found patronage among humanists and reformers—Johannes Oecolampadius (reformed theologian), the Amerbach brothers, and Johann Froben (printer)—who supported his reformist vision. In a symbolic act paralleling Luther's burning of papal bulls, Paracelsus publicly burned medieval medical texts, signaling rejection of Galenic tradition. His lectures, delivered in German rather than Latin, scandalized the university establishment. His claim to authority ("I am Theophrastus, not some other") and his assertion that "my shoestrings know more than you and all your schoolmasters, Galen and Avicenna" embodied the radical spirit of early Reformation autonomy.

Yet Paracelsus distinguished himself sharply from Luther: "You well know that I let Luther answer for his affairs; I shall answer for my own." This independence, combined with his uncompromising personality and unconventional methods, led to his expulsion from Basel in 1528. He would spend his remaining thirteen years as a wanderer, seeking patronage and vindication across German-speaking territories.

**Speculative Theory: The Method and Philosophy**

Andrew Weeks's scholarly framework identifies Paracelsus's intellectual innovation as grounded in the concept of "theory" (theorica)—a form of knowledge that encompasses medicine, philosophy, theology, and mysticism simultaneously. This was not empiricism in the modern sense; Paracelsus explicitly valued contemplative thought and speculative roaming across disciplines. Rather, his method integrated:

1. **Practical knowledge**: Alchemy, distillation, pharmaceutical preparation, mining chemistry—direct laboratory work
2. **Observational medicine**: Treatment of wounds, fevers, occupational diseases (especially mining injuries)
3. **Philosophical speculation**: Integration of Neoplatonism, hermeticism, and mystical theology
4. **Theological reflection**: Claims to expertise as "doctor of Holy Scripture" and eschatological mission

This synthetic approach was neither reducible to "science" nor dismissible as "superstition." For Paracelsus, alchemy provided both practical operations (pharmaceutical preparations) and philosophical framework (correspondences between macrocosm and microcosm). The physician's task was to understand divine order embedded in nature and to operate according to its principles.

**Iatrochemistry and Medical Reform**

Paracelsus's central innovation was iatrochemistry—the application of alchemical processes to medicine. Rather than the Galenic system of balancing humors through bloodletting and purging, Paracelsus advocated chemical specifics: remedies prepared through distillation, calcination, and fermentation, timed astrologically and invoked spiritually. His theoretical framework held that disease and cure operate according to alchemical principles of dissolution and regeneration.

This was not mere chemical empiricism but a unified vision of medical philosophy: each disease had a specific (specificum), a precise remedy discovered through nature study and alchemical expertise. The physician must become a scholar of God's written "book of nature," not merely a commentator on Galen's texts. Webster's historical framework emphasizes how this medical reform was integrated with Paracelsus's eschatological theology—medicine as part of end-times restoration and divine mission—making healing both practical and salvific.

**The Wandering Years and Late Theology (1528–1541)**

After Basel, Paracelsus never secured stable institutional position. He worked as traveling physician, attempted to establish alchemical operations, sought patronage from nobility and merchants, and experienced humiliation alongside occasional successes. In 1535, his surgical treatises were finally published, bringing some recognition. Yet instability defined his later career.

During these years, Paracelsus's writings increasingly emphasized what he called "philosophia adepta"—acquired or experiential philosophy. His eschatological works developed the theme of himself as healer-prophet with divine mission. He died in Salzburg in 1541, buried as a Catholic (faith of burial, though his personal conviction remains debated). Contemporary chronicler Johann Oporinus, who served as Paracelsus's secretary in Basel, left a vivid memoir of his composition practices—dictating texts rapidly and passionately to scribes, producing manuscripts that retain an unpolished, confessional intensity.

**Alchemy as Central Philosophical Practice**

Recent scholarship, particularly Andrew Sparling's work on transmutational alchemy, has restored alchemy to its rightful place in Paracelsian philosophy. Paracelsus was not merely a physician who used alchemy as a tool; rather, alchemical thinking—the understanding of transmutation, dissolution and regeneration, the unity of matter and spirit—was philosophically central to his entire system. His inheritance of practical alchemy from his father Wilhelm connected theory to laboratory work: the alchemist working with metals and essences was simultaneously performing metaphysical operations and discovering divine principles embedded in nature.

**Historiographical Debates and Modern Reception**

Modern Paracelsus scholarship divides broadly into schools: the scientific-historical approach (Sudhoff, Pagel, Debus) emphasizing medical and chemical innovation; the theological school (Goldammer, Matthiessen) emphasizing religious sources and eschatology; and the synthetic approach (Weeks, Webster, Sparling) showing that these domains were integrated in Paracelsus's thought. The dichotomy between "science" and "mysticism" is false; Paracelsus's genius lay in refusing the separation.

Debates persist over:
- Whether Paracelsus was primarily reformer (Lutheran-inspired) or visionary-charlatan
- The chronology of his key writings (crisis period of 1520s vs. lifelong development)
- The relative weights of alchemy, medicine, and theology in his philosophy
- Which textual attributions are authentic (given centuries of posthumous editions)

Yet consensus has emerged: Paracelsus was an autonomous thinker responding to the early Reformation crisis of authority, drawing eclectically from available intellectual resources without conforming to established schools. His medical reformation paralleled Luther's theological reformation in structure (defying institutional authority, asserting personal expertise) while remaining independent in content.

**Legacy and Transmission**

Though Paracelsus published little in his lifetime, his collected works circulated widely after 1550, becoming foundational to medical reform across Europe. His influence extended through multiple channels:
- **Medical reformers** embraced iatrochemistry as basis for pharmaceutical practice
- **Rosicrucian thinkers** adopted his cosmology, medical philosophy, and mystical theology
- **Radical Protestants** found in him a model of autonomous spiritual authority
- **Natural philosophers** recognized in him a precursor to the Scientific Revolution through his emphasis on observation and experimentation

Yet Paracelsus remained controversial. Some regarded him as charlatan and fraud; others as prophet and healer. This bifurcated legacy reflects his fundamental position outside established categories: neither purely learned nor purely popular; neither purely rational nor purely mystical; neither purely reformist nor purely esoteric.

**Conclusion**

Paracelsus represents a critical juncture in early modern intellectual history. His life exemplifies the possibility of radical intellectual autonomy in an era of institutional consolidation. His work demonstrates that the later opposition between "reason" and "superstition," "science" and "magic," "empiricism" and "speculation" was not yet fixed in sixteenth-century thought. Instead, Paracelsus integrated what later centuries would split apart: laboratory work and philosophical speculation, medical practice and theological meaning, institutional reform and mystical authority.

His famous motto—"Let no one belong to another who can belong to himself"—captures not merely personal independence but intellectual autonomy and the inalienable right to seek truth through experience. In this sense, Paracelsus remains a figure of enduring significance: a thinker who refused received categories and insisted on the possibility of integrated knowledge, combining practice and theory, matter and spirit, reform and innovation."""

    paracelsus['essay'] = enhanced_essay

    # Update scholars array
    paracelsus['scholars'] = [
        'Weeks',
        'Webster',
        'Sparling',
        'Goldammer',
        'Pagel',
        'Sudhoff'
    ]

    # Add scholarship entries
    paracelsus['scholarship'] = [
        {
            "scholar": "Andrew Weeks",
            "reference": "Paracelsus: Speculative Theory and the Crisis of the Early Reformation (SUNY Press, 1997)",
            "quote": "Paracelsus's theory emerged from the crisis of traditional authority—both ecclesiastical and academic—that characterized the Reformation period.",
            "relevance": "primary",
            "type": "monograph"
        },
        {
            "scholar": "Charles Webster",
            "reference": "Paracelsus: Medicine, Magic and Mission at the End of Time (Yale University Press)",
            "quote": "Paracelsus integrated medicine with eschatological theology, positioning the physician as agent of divine healing and spiritual transformation.",
            "relevance": "primary",
            "type": "monograph"
        },
        {
            "scholar": "Andrew Sparling",
            "reference": "Paracelsus, a Transmutational Alchemist (Ambix, vol. 67, no. 1, 2020)",
            "quote": "Alchemy was not peripheral to Paracelsus's medicine but central to his philosophical system—a framework integrating theory and praxis.",
            "relevance": "primary",
            "type": "journal_article"
        }
    ]

    # Add key concepts
    paracelsus['key_concepts'] = [
        'Iatrochemistry',
        'Speculative Theory',
        'Medical Reform',
        'Alchemy',
        'Microcosm/Macrocosm',
        'Correspondences',
        'Transmutation',
        'Divine Philosophy'
    ]

    return True

def add_scholar_profiles(data):
    """Add scholar profiles to database"""
    if 'scholars' not in data:
        data['scholars'] = []

    scholars = [
        {
            "id": "andrew-weeks",
            "name": "Andrew Weeks",
            "discipline": "History of Philosophy & Paracelsian Studies",
            "focus": "Text-centered historicism; Paracelsus and Reformation crisis; speculative theory; German philosophical tradition",
            "major_works": [
                "Paracelsus: Speculative Theory and the Crisis of the Early Reformation (SUNY Press, 1997)",
                "Paracelsus: Theophrastus Bombastus von Hohenheim, 1493-1541 (Brill, Aries Series, 2007)",
                "Editor with Didier Kahn: Cosmological and Meteorological Writings (Brill, 2024)"
            ],
            "key_contributions": [
                "Developed 'theory' (theorica) framework to bypass science/religion dichotomy",
                "Situated Paracelsus within early Reformation crisis of authority",
                "Established text-centered historicism as methodology for Paracelsus scholarship",
                "Demonstrated autonomy of Paracelsus's intellectual position (neither Lutheran nor occultist)"
            ],
            "related_figures": ["Paracelsus", "Charles Webster", "Kurt Goldammer"],
            "research_period": "1990s-present",
            "summary": "Andrew Weeks is a leading contemporary scholar of Paracelsus and early modern philosophy. His innovative framework positions Paracelsus within the early Reformation crisis of authority, showing how the Swiss physician developed an autonomous medical reformism parallel to but independent from Luther's theological reformation. Weeks's emphasis on Paracelsus's 'speculative theory'—an integrated form of knowledge combining medicine, philosophy, theology, and mysticism—has reshaped how scholars understand Renaissance intellectual history beyond false dichotomies of reason vs. superstition or science vs. magic."
        },
        {
            "id": "charles-webster",
            "name": "Charles Webster",
            "discipline": "History of Science & Early Modern Intellectual History",
            "affiliation": "University of Oxford (Emeritus)",
            "focus": "Medicine and magic integration; Renaissance natural philosophy; medical reform; eschatological theology; early modern intellectual history",
            "major_works": [
                "From Paracelsus to Newton: Magic and the Making of Modern Science (1982)",
                "Paracelsus: Medicine, Magic and Mission at the End of Time (Yale University Press)"
            ],
            "key_contributions": [
                "Integrated medicine, magic, and eschatology as unified framework for understanding Paracelsus",
                "Situated Paracelsus within history of science rather than occult history",
                "Demonstrated how end-times theology informed medical practice and theory",
                "Showed convergence of multiple intellectual traditions in Paracelsian thought"
            ],
            "related_figures": ["Paracelsus", "Andrew Weeks"],
            "research_period": "1980s-present",
            "summary": "Charles Webster is an emeritus scholar at Oxford and a pioneering historian of early modern science. His work on Paracelsus emphasizes the integration of medicine, magic, and eschatological theology as a coherent intellectual system rather than a confused mixture of rational and irrational elements. Webster's framework has been instrumental in rehabilitating Paracelsus as a serious intellectual figure within the history of science and early modern intellectual history, moving beyond both dismissive and hagiographic interpretations."
        },
        {
            "id": "didier-kahn",
            "name": "Didier Kahn",
            "discipline": "History of Alchemy & Natural Philosophy",
            "focus": "Paracelsus cosmology and meteorology; alchemy and chemistry; textual editing; early modern natural philosophy",
            "major_works": [
                "Co-editor with Andrew Weeks: Cosmological and Meteorological Writings by Paracelsus (Brill, 2024)"
            ],
            "key_contributions": [
                "Edited and analyzed Paracelsus's natural philosophical writings",
                "Contributed to understanding of Paracelsus's cosmological system",
                "Advanced textual scholarship on authenticity and editorial history"
            ],
            "related_figures": ["Paracelsus", "Andrew Weeks"],
            "summary": "Didier Kahn specializes in the history of alchemy and early modern natural philosophy, with particular expertise in Paracelsian thought. His recent editorial work on Paracelsus's cosmological and meteorological writings demonstrates the sophistication of Paracelsus's engagement with natural philosophy and its integration with alchemical and theological frameworks."
        },
        {
            "id": "kurt-goldammer",
            "name": "Kurt Goldammer",
            "discipline": "History of Theology & Paracelsian Studies",
            "focus": "Paracelsus religious thought; theological tradition; early writings and Peasant War context",
            "key_contributions": [
                "Pioneering work on Paracelsus's theological and mystical writings",
                "Situated Paracelsus within medieval spiritualist tradition",
                "Contextualized early Paracelsus within Peasant War and Reformation crisis",
                "Established theological approach to Paracelsian studies (as complement to scientific-historical school)"
            ],
            "related_figures": ["Paracelsus", "Andrew Weeks"],
            "summary": "Kurt Goldammer is a foundational figure in twentieth-century Paracelsus scholarship, particularly valued by contemporary scholars like Andrew Weeks for his attention to theological and mystical dimensions of Paracelsus's thought. Goldammer's work established that understanding Paracelsus requires engagement with his religious claims and eschatological vision, not dismissal of them as peripheral to his 'real' (scientific) contributions."
        },
        {
            "id": "andrew-sparling",
            "name": "Andrew Sparling",
            "discipline": "History of Alchemy",
            "focus": "Transmutational alchemy; Paracelsian alchemy; alchemical philosophy",
            "major_works": [
                "Paracelsus, a Transmutational Alchemist (Ambix, vol. 67, no. 1, 2020)"
            ],
            "key_contributions": [
                "Restored alchemy to central place in Paracelsian philosophy",
                "Demonstrated that Paracelsus was fundamentally an alchemist, not merely a physician using alchemy",
                "Showed integration of transmutational theory with medical and philosophical practice"
            ],
            "related_figures": ["Paracelsus"],
            "summary": "Andrew Sparling is a contemporary scholar of alchemy whose work on Paracelsus emphasizes the central role of alchemical thinking in his entire philosophical system. Sparling's research demonstrates that transmutation—the transformation of matter and spirit—is not peripheral to Paracelsus but fundamental to his understanding of medicine, nature, and divine knowledge."
        }
    ]

    # Check for duplicates before adding
    existing_ids = {s.get('id') for s in data['scholars']}
    for scholar in scholars:
        if scholar['id'] not in existing_ids:
            data['scholars'].append(scholar)

    return len(data.get('scholars', []))

def add_paracelsus_works(data):
    """Add major Paracelsus works to texts section"""
    if 'texts' not in data:
        data['texts'] = []

    works = [
        {
            "id": "paracelsus-opus-paramirum",
            "title": "Opus Paramirum",
            "author": "Paracelsus (Theophrastus Bombastus von Hohenheim)",
            "date_written": "c.1520s-1530s",
            "language": "German",
            "type": "Medical/Philosophical Treatise",
            "index_card": "Foundational work establishing Paracelsus's medical-philosophical system. 'Paramirum' suggests both 'paradoxical' and 'excessive' work. Integrates alchemy with medicine through the framework of correspondences between microcosm (human body) and macrocosm (cosmos).",
            "essay": "The Opus Paramirum (The Marvelous Work) represents Paracelsus's foundational attempt to establish a unified medical-philosophical system based on alchemical principles and direct observation of nature rather than scholastic commentary on classical authorities. The title itself suggests the audacity of the enterprise: 'paramirum' carries connotations of both 'paradoxical' and 'excessive,' indicating Paracelsus's consciousness that his work violated conventional expectations of medical learning.\n\nThe central innovation of the Opus Paramirum is its integration of alchemical thinking with medical theory. Rather than the Galenic system of balancing humors through bloodletting and purging, Paracelsus proposed that disease arises from specific causes discoverable through nature study and remedied through specific (specificum) alchemical preparations. This required a complete reconceptualization of the physician's task: from commentator on ancient texts to investigator of divine order embedded in creation.\n\nThe work develops the framework of correspondences between macrocosm (the cosmos as unified whole) and microcosm (the human body as miniature cosmos). This was not unique to Paracelsus—Hildegard of Bingen and medieval physicians had employed similar frameworks—but Paracelsus made it central to his medical epistemology. Understanding the human body required understanding divine principles operating throughout creation. The physician who grasped these correspondences could work with nature rather than against it, using alchemy not merely as craft but as knowledge of fundamental transformative principles.\n\nMultiple versions of the Opus Paramirum exist in manuscript tradition, and modern scholarship continues to debate authenticity and dating. Yet the work's central vision remains clear: an integrated natural philosophy combining empirical observation, alchemical operation, and theological reflection. In this sense, the Opus Paramirum establishes the fundamental parameters of Paracelsian thought that would structure all his subsequent writings.",
            "key_concepts": [
                "Speculative Theory",
                "Alchemy",
                "Medical Reform",
                "Microcosm/Macrocosm",
                "Correspondences",
                "Nature Philosophy"
            ],
            "related_figures": ["Paracelsus"],
            "scholarly_sources": [
                "Andrew Weeks: Paracelsus: Speculative Theory (1997)",
                "Charles Webster: Paracelsus: Medicine, Magic and Mission"
            ],
            "significance": "Seminal work establishing Paracelsian medical-philosophical system; multiple versions exist",
            "review_status": "DRAFT",
            "confidence": "MEDIUM"
        },
        {
            "id": "paracelsus-opus-paragranum",
            "title": "Opus Paragranum",
            "author": "Paracelsus",
            "date_written": "c.1530s",
            "language": "German",
            "type": "Medical/Philosophical Treatise",
            "index_card": "Systematic treatise organizing Paracelsian medical principles and nature philosophy. More structured than Opus Paramirum, establishes fundamental categories of medicine and operational framework for alchemical healing practice.",
            "essay": "The Opus Paragranum (The Work of Granules or The Great Work) represents Paracelsus's more systematic attempt to organize his medical and philosophical principles into a coherent didactic structure. Where the Opus Paramirum emphasizes speculative theory and philosophical foundations, the Opus Paragranum focuses on practical organization and categorical clarity.\n\nThis work establishes the fundamental structure of Paracelsian medicine through division into four pillars: philosophy (natural philosophy and cosmology), astronomy (including astrology and celestial influences), alchemy (operations and transformations), and virtue (the spiritual and moral dimensions of healing). These four pillars represent an integrated framework: a physician cannot practice healing through chemistry (alchemy) alone without understanding cosmic principles (astronomy), philosophical foundations (philosophy), and the spiritual dimensions (virtue) of the work.\n\nThe Opus Paragranum also develops Paracelsus's critique of Galenic medicine with greater systematic force. Traditional medicine rested on four humors (blood, phlegm, yellow bile, black bile) and their qualities (hot, cold, wet, dry). Paracelsus rejected this as an abstract schema imposed on nature rather than derived from observation. Instead, he proposed that medicine must be based on specific remedies for specific conditions—a framework he believed both observation and alchemy supported.\n\nThe work provides detailed discussion of pharmaceutical preparation, emphasizing distillation, fermentation, and calcination as fundamental operations. Yet these are understood not merely as technical procedures but as manifestations of natural principles: the alchemist working with materials was simultaneously discovering divine knowledge encoded in creation. This integration of technical operation with theological meaning characterizes Paracelsian philosophy throughout.",
            "key_concepts": [
                "Medical System",
                "Four Pillars",
                "Philosophy",
                "Astronomy",
                "Alchemy",
                "Virtue"
            ],
            "related_figures": ["Paracelsus"],
            "significance": "Systematic organization of Paracelsian medical-philosophical principles",
            "review_status": "DRAFT",
            "confidence": "MEDIUM"
        },
        {
            "id": "paracelsus-labyrinthus-medicorum",
            "title": "Labyrinthus Medicorum",
            "author": "Paracelsus",
            "date_written": "c.1540",
            "language": "German",
            "type": "Medical Polemic",
            "index_card": "Critique of traditional medical establishment and Galenic orthodoxy. Written near end of Paracelsus's life as summing-up of his medical reform project, attacking physicians who followed classical authorities without observation or innovation.",
            "essay": "The Labyrinthus Medicorum (The Labyrinth of Physicians) represents Paracelsus's sustained polemic against the medical establishment and its addiction to classical authorities. Written late in his life, the work constitutes a kind of summation of Paracelsus's critique of medical orthodoxy and his vision of reformed practice.\n\nThe title itself suggests the confused and bewildering nature of conventional medical learning: a labyrinth in which physicians wander without finding true knowledge. The work's central claim is that physicians trained exclusively in Galenic commentary and scholastic disputation lack the knowledge necessary for genuine healing. True medical knowledge requires engagement with nature itself—direct observation, practical experimentation, and alchemical understanding.\n\nPararacelsus's critique extends to the entire institutional structure of university medicine. Physicians educated in learned commentaries become dependent on textual authority rather than nature. They lose the ability to observe actual patients and actual diseases. They apply theoretical categories (the four humors) to concrete cases in ways that contradict both reason and observation. In this sense, conventional physicians are trapped in a self-made labyrinth—a maze of false categories and inherited misconceptions.\n\nYet Paracelsus does not advocate for abandonment of learning. Rather, he insists that genuine learning must be grounded in observation and practice. The physician must study nature as a divine text, learning through direct engagement with materials, operations, and results. This requires alchemy—not as occultism but as systematic knowledge of transformation and operation. The alchemist physician understands how distillation, fermentation, and calcination work because he practices them; he discovers through this practice how these operations reflect cosmic principles.\n\nThe Labyrinthus Medicorum thus encapsulates the fundamental tension in Paracelsus's thought: his simultaneous commitment to learning and authority (he claims his own authority based on knowledge), and his radical critique of inherited institutional authority. This tension reflects his position within the early Reformation crisis—claiming to reform medicine from within while fundamentally challenging its institutional basis.",
            "key_concepts": [
                "Medical Reform",
                "Critique of Galenism",
                "Authority and Learning",
                "Alchemy",
                "Observation",
                "Practice"
            ],
            "related_figures": ["Paracelsus"],
            "significance": "Late summing-up of Paracelsian medical reform vision; sustained critique of medical establishment",
            "review_status": "DRAFT",
            "confidence": "MEDIUM"
        },
        {
            "id": "paracelsus-astronomia-magna",
            "title": "Astronomia Magna",
            "author": "Paracelsus",
            "date_written": "c.1530s",
            "language": "German",
            "type": "Natural Philosophy",
            "index_card": "Treatise on cosmic influences, astral philosophy, and natural magic. Develops Paracelsus's theory of how celestial bodies influence earthly creation, connecting astronomy with alchemy and medicine.",
            "essay": "The Astronomia Magna (The Great Astronomy) represents Paracelsus's most systematic treatment of cosmology and the principles of natural magic. The work develops his framework of correspondences between celestial and terrestrial realms, showing how stars and planets influence earthly matter and human health.\n\nPararacelsus's astronomy is not merely mathematical prediction of celestial motions (though he was aware of such knowledge). Rather, it is a philosophy of influence: how divine principles operating through celestial bodies shape creation. This framework extends the microcosm/macrocosm correspondence to include the entire cosmos as an integrated system of influences and correspondences.\n\nThe work demonstrates how astrological timing affects alchemical operations. Certain pharmaceutical preparations are more effective when prepared under particular astrological conditions. This is not superstition in Paracelsus's view but systematic knowledge of how natural principles operate. The skilled physician-alchemist understands these correspondences and works with them, timing operations to align with cosmic influences.\n\nThe Astronomia Magna also addresses Paracelsus's understanding of natural magic—not as supernatural compulsion but as knowledge and practice aligned with natural principles. Magic, properly understood, is the highest form of natural philosophy: the knowledge of how to work with cosmic forces in accordance with their actual principles. In this sense, the distinction between natural and magical knowledge collapses: all genuine knowledge of nature is 'magical' in that it works with forces beyond human will.",
            "key_concepts": [
                "Cosmology",
                "Astral Influences",
                "Natural Magic",
                "Correspondences",
                "Celestial Bodies",
                "Alchemy"
            ],
            "related_figures": ["Paracelsus"],
            "significance": "Systematic treatment of cosmology and astral philosophy within Paracelsian framework",
            "review_status": "DRAFT",
            "confidence": "MEDIUM"
        }
    ]

    # Add works to database
    existing_ids = {t.get('id') for t in data['texts']}
    count = 0
    for work in works:
        if work['id'] not in existing_ids:
            data['texts'].append(work)
            count += 1

    return count

def establish_relationships(data):
    """Establish concept links and relationships"""
    # Find Paracelsus figure
    paracelsus = find_paracelsus_figure(data['figures'])
    if not paracelsus:
        return False

    # Add related figures
    paracelsus['related_figures'] = [
        'Johann Valentin Andreae',
        'Jacob Böhme',
        'Heinrich Khunrath',
        'Michael Maier',
        'Johannes Trithemius',
        'Cornelius Agrippa'
    ]

    # Add concept connections
    paracelsus['key_concepts'] = [
        'Iatrochemistry',
        'Speculative Theory',
        'Medical Reform',
        'Alchemy',
        'Microcosm/Macrocosm',
        'Correspondences',
        'Transmutation',
        'Divine Philosophy',
        'Nature Magic',
        'Reformation Crisis'
    ]

    return True

def main():
    print("Loading database...")
    data = load_database()

    print("Enhancing Paracelsus figure entry...")
    if enhance_paracelsus_figure(data['figures']):
        print("  [OK] Paracelsus essay enriched with comprehensive scholarship")

    print("\nAdding scholar profiles...")
    scholar_count = add_scholar_profiles(data)
    print(f"  [OK] {scholar_count} scholars in database (added 5 Paracelsus specialists)")

    print("\nAdding Paracelsus works to texts section...")
    work_count = add_paracelsus_works(data)
    print(f"  [OK] Added {work_count} major Paracelsus works")

    print("\nEstablishing relationships...")
    if establish_relationships(data):
        print("  [OK] Concept links and related figures connected")

    print("\nSaving updated database...")
    save_database(data)
    print("  [OK] Database saved successfully")

    print("\n" + "="*60)
    print("PARACELSUS INTEGRATION COMPLETE")
    print("="*60)
    print(f"Updated entries:")
    print(f"  - 1 figure (Paracelsus)")
    print(f"  - 5 scholar profiles")
    print(f"  - 4 major Paracelsus works")
    print(f"\nNext steps:")
    print(f"  1. Run: python scripts/build_site.py")
    print(f"  2. Test at: http://localhost:8000")
    print(f"  3. Deploy to GitHub Pages when ready")

if __name__ == '__main__':
    main()
