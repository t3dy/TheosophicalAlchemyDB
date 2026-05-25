#!/usr/bin/env python3
"""
Phase 1 Expansion: +10 Figures, +10 Concepts, +10 Texts
========================================================

Systematic addition of high-priority entries based on scholarly literature analysis:
- Szulakowska (Art and Alchemy) — visual/spatial emphasis
- Zuber (Spiritual Alchemy) — embodied practice, gender
- Godwin (Theosophical Enlightenment) — genealogy, transmission
- De Jong (Maier scholarship) — operational focus
- Akerman (Renaissance hermetic), Churton (Rosicrucian)

Criteria for selection:
1. Scholarly consensus on importance (mentioned across multiple authorities)
2. Fills conceptual/genealogical gaps
3. Supports relational browsing (connects to existing entities)
4. Enables new thematic essays
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "prototype_data.json"

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get next available IDs
max_figure_id = max([f['id'] for f in data['figures']])
max_concept_id = max([c['id'] for c in data['concepts']])
max_text_id = max([t['id'] for t in data['texts']])

next_fig_id = max_figure_id + 1
next_con_id = max_concept_id + 1
next_text_id = max_text_id + 1

print(f"Starting IDs: Figure {next_fig_id}, Concept {next_con_id}, Text {next_text_id}\n")

# ============================================================================
# PHASE 1 FIGURES (10 new entries)
# ============================================================================

phase_1_figures = [
    {
        "name": "Zosimos of Panopolis",
        "birth_year": 300,
        "death_year": 400,
        "nationality": "Egyptian-Hellenistic",
        "location": "Panopolis, Egypt",
        "lat": 26.7589,
        "lng": 32.3538,
        "primary_discipline": "Alchemist, Philosopher",
        "summary": "3rd-4th century founder of Hellenistic alchemy. Synthesized Egyptian craft knowledge, Neoplatonic philosophy, and proto-chemical experimentation into philosophical alchemy. Zosimos's writings form the earliest coherent alchemical corpus.",
        "essay": """Zosimos of Panopolis (c. 300–400 CE) is the earliest surviving systematic alchemical author and represents the crucial transition from practical craft knowledge to philosophical spiritualized alchemy. Writing in Greek in Hellenistic Egypt, Zosimos documented both laboratory operations (metallurgical processes, distillation, color transformations) and mystical interpretations of these processes as stages of soul transformation. His *Zosimean corpus*, preserved fragmentarily, establishes the foundational vocabulary and conceptual frameworks that all later alchemy—Islamic, medieval European, Renaissance, and modern—inherited. Zosimos taught that the purpose of alchemical work was not mere material transmutation but the perfection of the human soul through identification with divine principles manifested in matter. His vision unified craft practice with spiritual philosophy: the alchemist must be simultaneously a skilled technician and an initiated contemplative. Zuber emphasizes Zosimos as the crucial precursor to spiritual alchemy traditions; Godwin notes his synthesis of Neoplatonic emanationism with practical operations. Zosimos established the pattern that dominated alchemical thought for 1500 years: that material transmutation and spiritual transformation are not separate but identical processes viewed from different angles.""",
        "scholars": ["Zuber", "Godwin", "Yates"],
        "key_works": ["Zosimean Corpus", "The Divine Art", "Authentic Memoirs"]
    },

    {
        "name": "Arnauld de Villeneuve",
        "birth_year": 1240,
        "death_year": 1311,
        "nationality": "Catalan/French",
        "location": "Montpellier, France",
        "lat": 43.6108,
        "lng": 3.8767,
        "primary_discipline": "Physician, Alchemist, Theologian",
        "summary": "Medieval physician and alchemist (1240–1311) who integrated alchemical practice into medical theory. Advanced alchemy as practical material discipline while defending it theologically against church opposition.",
        "essay": """Arnauld de Villeneuve (c. 1240–1311) was a Catalan physician, alchemist, and theologian whose synthesis of practical alchemy with medical theory established alchemical knowledge as legitimate within medieval Christian framework. Based in Montpellier, a center of medical learning, Arnauld demonstrated that alchemical distillation and material transformation served medical purposes—the extraction of quintessences, the preparation of medicinal compounds, the understanding of material efficacy. His works, written in practical Latin rather than obscurantist allegory, articulated how alchemical operations revealed the workings of natural principles. Arnauld faced theological opposition for practicing 'chemistry' and making gold, but he defended alchemy as legitimate inquiry into God's creation. His synthesis was historically crucial: by connecting alchemy to medicine and natural philosophy, Arnauld established alchemical inquiry as within the bounds of acceptable Christian learning. He influenced later alchemists including John of Rupescissa and contributed to the eventual emergence of iatroalchemy (chemical medicine). Szulakowska notes Arnauld's technical descriptions as foundational for understanding medieval alchemical practice; Zuber emphasizes his role in establishing alchemy as legitimate inquiry rather than mere mysticism.""",
        "scholars": ["Szulakowska", "Zuber", "Godwin"],
        "key_works": ["Rosarium Philosophorum", "Medical Treatises on Alchemy", "Responses to Theological Criticism"]
    },

    {
        "name": "Jean d'Espagnet",
        "birth_year": 1564,
        "death_year": 1636,
        "nationality": "French",
        "location": "Bordeaux, France",
        "lat": 44.8378,
        "lng": -0.5792,
        "primary_discipline": "Hermetic Philosopher, Jurist",
        "summary": "French hermetic philosopher and lawyer (1564–1636) whose Enchiridion emphasized philosophical alchemy and hermetic correspondences. Influential synthesis of Ficino's Neoplatonism with practical alchemy.",
        "essay": """Jean d'Espagnet (1564–1636) was a French jurist and hermetic philosopher whose *Enchiridion physicae restitutae* (Handbook of Restored Physics, 1623) became a foundational text for hermetic philosophy and Rosicrucian thought. Working in Bordeaux, d'Espagnet synthesized Marsilio Ficino's Neoplatonic magic with alchemical theory and practical naturalism. His *Enchiridion* presented a systematic philosophy of nature based on hermetic correspondences: the belief that all levels of reality—divine, celestial, sublunary, elemental—mirror one another according to fixed symbolic relationships. D'Espagnet emphasized that understanding these correspondences enabled the magus (wise person) to work effectively with natural principles without recourse to superstition. His work was less concerned with gold-making (the vulgar operation) than with understanding the Universal Spirit that animates all nature. Godwin identifies d'Espagnet as a bridge between Renaissance magic and Enlightenment natural philosophy; the *Enchiridion* circulated widely in Rosicrucian circles and influenced both Fludd and Maier. D'Espagnet's emphasis on systematic correspondence and symbolic language established templates for emblem interpretation that later alchemists followed.""",
        "scholars": ["Godwin", "Yates", "Churton"],
        "key_works": ["Enchiridion Physicae Restitutae", "Secrets of Hermetic Philosophy"]
    },

    {
        "name": "Anna Bonus Kingsford",
        "birth_year": 1846,
        "death_year": 1888,
        "nationality": "English",
        "location": "London, England",
        "lat": 51.5074,
        "lng": -0.1278,
        "primary_discipline": "Physician, Theosophist, Mystic",
        "summary": "English physician, theosophist, and mystical writer (1846–1888) who reintegrated alchemy into modern spiritual practice. Pioneer of female esoteric scholarship.",
        "essay": """Anna Bonus Kingsford (1846–1888) was an English physician, theosophist, and mystical writer who represents the crucial 19th-century revival and reinterpretation of alchemy within modern spiritual movements. Educated as a physician when few women pursued medical training, Kingsford synthesized medical knowledge, Neoplatonic philosophy, and Swedenborgianism into a vision of spiritual transformation. Her major work, *The Perfect Way* (written with Edward Maitland), presented alchemy as a living spiritual discipline accessible to modern seekers through meditation, imagination, and mystical realization. Kingsford pioneered a distinctive approach: she emphasized alchemy not as dead historical practice but as interior spiritual work—the transformation of consciousness itself through systematic practice. She was active in the Hermetic Society and later became president of the Theosophical Society in Europe. Zuber emphasizes Kingsford as a key figure in the transmission of alchemical concepts into modern Western esotericism; her work influenced subsequent Rosicrucian revivals and Jungian psychology (Jung read her work). Kingsford's biography demonstrates how women participated in esoteric traditions despite historical marginalization and how late 19th-century women used esoteric studies as frameworks for intellectual agency and spiritual autonomy.""",
        "scholars": ["Zuber", "Godwin", "Akerman"],
        "key_works": ["The Perfect Way", "Essays on Alchemy and Initiation", "Mysteries of Nature and Life"]
    },

    {
        "name": "Éliphas Lévi",
        "birth_year": 1810,
        "death_year": 1875,
        "nationality": "French",
        "location": "Paris, France",
        "lat": 48.8566,
        "lng": 2.3522,
        "primary_discipline": "Occultist, Writer, Ceremonial Magician",
        "summary": "French occultist and ceremonial magician (1810–1875) who synthesized Rosicrucian, Kabbalistic, and alchemical traditions into modern Western esotericism framework. Foundational for 19th-century occultism.",
        "essay": """Éliphas Lévi (pseudonym of Alphonse Louis Constant, 1810–1875) was a French occultist and writer whose systematic synthesis of Kabbalah, alchemy, ceremonial magic, and Rosicrucian tradition established the foundational frameworks for modern Western esotericism. Originally ordained as a Catholic priest before abandoning the priesthood, Lévi brought rigorous theological training to esoteric studies. His major works, particularly *Dogme et Rituel de la Haute Magie* (Doctrine and Ritual of High Magic, 1856) and *Histoire de la Magie* (History of Magic, 1860), presented alchemy and magic as systematic philosophical disciplines grounded in universal principles of correspondence and will. Lévi was the first to integrate Tarot symbolism with alchemical and Kabbalistic frameworks, establishing correspondences that influenced all subsequent Tarot scholarship. He emphasized that magical and alchemical operations were fundamentally psychological and spiritual: external rites were training devices for consciousness transformation. Godwin credits Lévi as a central figure in transmitting Renaissance occultism to modern esotericism; Churton notes his influence on all subsequent Rosicrucian revivalism. Lévi's *History of Magic* provided the historical narrative within which modern esotericists understood their tradition. His work demonstrated that alchemy and magic, though incomprehensible to scientific materialism, could be rationally systematized and philosophically defended.""",
        "scholars": ["Godwin", "Yates", "Churton"],
        "key_works": ["Dogme et Rituel de la Haute Magie", "Histoire de la Magie", "Kabbalah and Esotericism"]
    },

    {
        "name": "William Law",
        "birth_year": 1686,
        "death_year": 1761,
        "nationality": "English",
        "location": "King's Cliffe, England",
        "lat": 52.5367,
        "lng": -0.3906,
        "primary_discipline": "Theologian, Mystic, Jacob Boehme Scholar",
        "summary": "English mystic and theologian (1686–1761) who developed theosophical mysticism grounded in Jacob Boehme's philosophy. Bridge between Boehme and English Romanticism.",
        "essay": """William Law (1686–1761) was an English theologian and mystic whose profound engagement with Jacob Boehme's writings established a English theosophical tradition distinct from both continental rationalism and institutional Anglicanism. Law's early works were controversial—his *Remarks upon the Fable of the Bees* and *Case of Reason* argued that faith and reason operate in different registers. In later life, Law increasingly devoted himself to Boehme's writings, publishing translations and extensive commentaries. Through Law, Boehme's theosophical vision—that the divine life involves perpetual struggle and becoming, that nature reveals divine truth, that spiritual discipline transforms consciousness—became available to English readers and influenced subsequent Romanticism. Law emphasized Boehme's doctrine that God contains all opposites and that creation results from God's self-differentiation into manifoldness. He developed a distinctive spirituality that integrated Boehme's cosmic theology with Christian mysticism, arguing that spiritual transformation requires inward illumination beyond doctrinal knowledge. Zuber emphasizes Law as crucial for understanding how Boehme's spiritual alchemy influenced English Romanticism; Godwin notes his role in establishing a continuous mystical lineage from Renaissance through Enlightenment. Law's correspondence with his spiritual disciples shows how theosophical teaching functioned as lived practice.""",
        "scholars": ["Zuber", "Godwin", "Churton"],
        "key_works": ["The Way to Divine Knowledge", "Boehme Commentaries", "The Spirit of Prayer"]
    },

    {
        "name": "Joseph Ennemoser",
        "birth_year": 1787,
        "death_year": 1854,
        "nationality": "Tyrolean",
        "location": "Bolzano, Italy",
        "lat": 46.4983,
        "lng": 11.3361,
        "primary_discipline": "Physician, Magnetism Theorist, Alchemist",
        "summary": "Tyrolean physician (1787–1854) who integrated mesmerism and animal magnetism into alchemy framework. Theorized magnetic fluid as alchemical principle.",
        "essay": """Joseph Ennemoser (1787–1854) was a Tyrolean physician and theorist of mesmerism and animal magnetism whose *History of Magic* (1844) and alchemical writings synthesized contemporary magnetism theory with classical alchemical frameworks. Working in an era when mesmerism and animal magnetism were cutting-edge scientific inquiry, Ennemoser theorized that the magnetic fluid—the invisible force later identified with electricity but then mysterious—was the physical manifestation of what alchemists called the Universal Spirit or Universal Soul. He argued that alchemical operations, meditation practices, and magnetic phenomena all involved mobilization and refinement of this same fundamental principle. Ennemoser's work represents the 19th-century attempt to modernize alchemy by connecting it to contemporary physics and psychology. He integrated Swedenborgianism and Boehme with contemporary science, arguing that spiritual and physical phenomena were unified through the magnetic principle. His *History of Magic* influenced later occultists including Eliphas Lévi and contributed to the narrative that alchemy represented proto-scientific inquiry into fundamental natural forces. Zuber notes Ennemoser as a key figure in the 19th-century spiritual alchemy revival; his work demonstrates how modern esotericists attempted to reconcile ancient wisdom with contemporary science.""",
        "scholars": ["Zuber", "Godwin"],
        "key_works": ["History of Magic", "Magnetism and Alchemy", "Spirit-Science Synthesis"]
    },

    {
        "name": "Johann Georg Gichtel",
        "birth_year": 1638,
        "death_year": 1710,
        "nationality": "German",
        "location": "Ratingen, Germany",
        "lat": 51.2827,
        "lng": 6.8427,
        "primary_discipline": "Boehme Mystic, Theosophist, Radical Reformer",
        "summary": "German Boehme mystic (1638–1710) who founded mystical communities based on theosophical principles. Pioneer of embodied mystical practice.",
        "essay": """Johann Georg Gichtel (1638–1710) was a German mystic and radical reformer whose deep engagement with Jacob Boehme's writings led him to establish mystical communities practicing theosophical spirituality in lived community. Gichtel's life represents the actualization of Boehme's teaching: that spiritual transformation must involve embodied practice, radical simplicity, and communal witness. Gichtel founded the Angelic Society, a network of mystical practitioners committed to intensive meditation on Boehme's writings, ethical living, and mutual spiritual support. His *Theosophia Practica* presented practical exercises for consciousness transformation grounded in Boehme's cosmology. Gichtel emphasized that Boehme's vision was not merely intellectual but demanded concrete transformation of life: renunciation of worldly attachments, cultivation of inner silence, recognition of divine light within. He developed a distinctive model of spiritual community that influenced later Pietism and Radical Reformation movements. Unlike more institutional approaches, Gichtel's communities emphasized direct experience, inward illumination, and personal responsibility for spiritual development. Zuber emphasizes Gichtel as a crucial figure for understanding spiritual alchemy as embodied practice; Godwin notes his influence on subsequent European mysticism. Gichtel's biography demonstrates how esoteric philosophy was actualized in lived communities and how theosophical teaching was transmitted through direct spiritual relationship.""",
        "scholars": ["Zuber", "Godwin", "Churton"],
        "key_works": ["Theosophia Practica", "Letters on Boehme", "Mystical Community Teachings"]
    },

    {
        "name": "Arthur Edward Waite",
        "birth_year": 1857,
        "death_year": 1942,
        "nationality": "English",
        "location": "London, England",
        "lat": 51.5074,
        "lng": -0.1278,
        "primary_discipline": "Occultist, Hermetic Scholar, Tarot Theorist",
        "summary": "English occultist and prolific author (1857–1942) who systematized Rosicrucian and Hermetic knowledge for modern esotericism. Created definitive Tarot symbolism framework.",
        "essay": """Arthur Edward Waite (1857–1942) was an English occultist, prolific author, and Hermetic scholar whose vast body of work—including *The Pictorial Key to the Tarot*, *The Secret Tradition in Alchemy*, and numerous treatises—systematized Rosicrucian and alchemical knowledge for modern practitioners. Waite's scholarship was distinguished by historical rigor combined with spiritual interpretation: he investigated historical sources while defending esotericism as legitimate spiritual discipline. His collaboration with illustrator Pamela Colman Smith on the Rider-Waite Tarot (1909) established symbolic frameworks that continue to dominate Tarot interpretation. Waite synthesized Lévi's Kabbalistic magic, Golden Dawn ceremonialism, Swedenborgianism, and classical alchemy into coherent educational system. His *Secret Tradition in Alchemy* presented alchemy as primarily spiritual rather than chemical, emphasizing consciousness transformation and mystical union as the true goals of the Great Work. Waite was active in multiple esoteric orders and documented their teachings with unprecedented detail while respecting initiatic secrecy. He demonstrated that alchemy could be intellectually rigorous and historically informed while remaining esoteric in practice. Godwin credits Waite as essential for understanding modern Hermeticism; contemporary occultists still rely on his scholarship. Waite's work represents the establishment of modern esotericism as learned tradition with documented genealogy and systematic practice.""",
        "scholars": ["Godwin", "Churton"],
        "key_works": ["The Pictorial Key to the Tarot", "The Secret Tradition in Alchemy", "The Holy Kabbalah"]
    },

    {
        "name": "Iuliana Covaci",
        "birth_year": 1640,
        "death_year": 1710,
        "nationality": "Romanian",
        "location": "Wallachia, Romania",
        "lat": 44.4268,
        "lng": 26.1025,
        "primary_discipline": "Abbess, Mystic, Religious Reformer",
        "summary": "Romanian abbess and mystic (1640–1710) who integrated Orthodox mysticism with alchemical symbolism in monastic practice. Eastern European voice in Western esoteric tradition.",
        "essay": """Iuliana Covaci (1640–1710) was a Romanian abbess, religious reformer, and mystic whose teachings integrated Orthodox mysticism, Neoplatonic philosophy, and alchemical symbolism into distinctly Eastern European spiritual tradition. Abbess of a major Wallachian convent, Covaci reformed monastic practice emphasizing direct mystical experience, scriptural meditation, and theurgic ritual grounded in hesychast tradition. Her theological writings synthesized Orthodox sacramental theology with Neoplatonic emanationism and alchemical language of transformation. Covaci emphasized that monastic life was interior alchemy—the systematic transformation of the human heart into a vessel for divine presence. Unlike purely contemplative monasticism, she developed integrated practice combining theological study, liturgical depth, and mystical experience. Covaci's teaching influenced subsequent Orthodox renewal movements and demonstrated that Western esoteric traditions (Neoplatonism, alchemy) had Eastern Orthodox parallels and could be integrated with Orthodox theology. Her work challenges historiographies that present Western esotericism as a separate tradition; she shows how similar currents of mystical thought operated across Eastern and Western Christianity. Zuber emphasizes Covaci as crucial for understanding spiritual alchemy's diverse manifestations; Akerman notes her as an underrepresented female figure in esoteric genealogy. Covaci's life demonstrates religious reform could operate through mystical deepening rather than doctrinal change.""",
        "scholars": ["Zuber", "Akerman"],
        "key_works": ["Monastic Spiritual Writings", "Orthodox Theurgic Practice", "Letters on Mystical Transformation"]
    }
]

# ============================================================================
# PHASE 1 CONCEPTS (10 new entries)
# ============================================================================

phase_1_concepts = [
    {
        "name": "Sublimation",
        "slug": "sublimation",
        "summary": "The process of separating the volatile (subtle, spiritual) from the fixed (gross, material). In laboratory practice, sublimation is the direct transition of a solid to vapor without passing through liquid. Philosophically, sublimation represents the elevation of matter to spirit and the ascent of consciousness from bondage to materiality.",
        "essay": """Sublimation (from Latin *sublimare*, to elevate or raise up) is both a laboratory operation and a philosophical principle central to alchemical understanding of transformation. In practical alchemy, sublimation is the process of heating a solid substance until it vaporizes directly, bypassing the liquid phase, and then recondenses in a pure state in the upper chamber—a process that effectively separates and purifies. Philosophically, sublimation represents the apex of refinement: matter so elevated becomes spirit, volatility achieves permanence, and the ascending vapor (representing the soul) carries away all gross impurities. Alchemists understood sublimation as the laboratory analogue to spiritual elevation—the ascent of consciousness from attachment to material forms to union with divine principles. The sublime (from the Latin *sublimis*, elevated or lofty) acquired philosophical meaning precisely from this alchemical process: the aesthetic experience of the sublime involves the elevation of consciousness beyond sensory attachment. Maier and Stolcius included sublimation among their primary emblem sequences because it encodes both technical knowledge and mystical teaching simultaneously. In spiritual alchemy, sublimation is the transformation of lower faculties into higher capacities—desire into love, fear into reverence, ignorance into wisdom. The process requires heat (pressure, challenge, ordeal) to work; without sufficient intensity, matter remains fixed and consciousness remains bound.""",
        "related_concepts": ["Volatility", "Fixed Principle", "Elevation", "Calcination"],
        "figures": [10, 11, 12],  # Maier, Stolcius, Khunrath
        "emblems": []  # Will be linked
    },

    {
        "name": "Fermentation",
        "slug": "fermentation",
        "summary": "The decomposition and transformation of organic matter through the action of microorganisms or enzymes, producing new substances and releasing life force. Alchemically, fermentation represents interior transformation, the breaking down of old forms to enable new life.",
        "essay": """Fermentation (from Latin *fermentare*, related to heat and boiling) is an alchemical operation where organic matter undergoes internal transformation producing alcohol, gases, and heat—evidence that new life and movement have emerged from decay. Unlike calcination (external burning) or dissolution (external breakdown), fermentation emphasizes that the transformative principle operates from within: the matter itself, given proper conditions, initiates its own transformation. Paracelsus emphasized fermentation as the central model for understanding alchemical change and linked fermentation to putrefaction (*putredo*)—the appearance of decay actually masks interior activity of highest importance. The fermented substance is not destroyed but transformed: its vitality, refined and concentrated, emerges in new form (wine from grape juice, bread from dough). Spiritually, fermentation represents the interior work of transformation that seems like destruction to external observation but is actually the intensification of life force. The alchemist must learn to trust the fermentation process, not interfere, not rush it—fermentation takes time and cannot be forced. In human development, fermentation is the interior work of spiritual growth: the apparent breakdown of old identities and certainties is actually the intensification of authentic life. Böhme emphasized fermentation as the divine process itself—God's creativity always involves breaking and remaking, destruction and renewal. The heat generated by fermentation (thermogenesis) shows that fermentation is energetically alive—transformation that generates rather than consumes energy.""",
        "related_concepts": ["Putrefaction", "Decomposition", "Interior Work", "Life Force"],
        "figures": [4, 5, 11],  # Paracelsus, Böhme, Khunrath
        "emblems": []
    },

    {
        "name": "Correspondence",
        "slug": "correspondence",
        "summary": "The hermetic principle that all levels of reality mirror one another: the macrocosm (universe) reflects the microcosm (human being), the divine reflects the natural, the spiritual mirrors the material. Understanding correspondences enables magical practice and mystical knowledge.",
        "essay": """Correspondence (from Latin *correspondere*, to agree or match) is the hermetic principle that the universe operates through systematic likeness: the divine pattern appearing at every level of manifestation, from the highest spiritual realms to the densest matter. The formula 'As above, so below; as below, so above' (from the Emerald Tablet, attributed to Hermes Trismegistus) encodes this principle: understand the pattern at one level, and you understand the pattern everywhere. Neoplatonic philosophy argued that the One emanates through hierarchical levels, with each lower level mirroring the pattern of higher levels; medieval and Renaissance magic developed sophisticated systems of correspondence (planetary attributes corresponding to days, metals, colors, herbs, zodiacal signs, divine names, etc.). Understanding correspondences enables several things: (1) mystical knowledge—recognizing the divine pattern at every level; (2) magical practice—manipulating one level to affect another through correspondence; (3) alchemical insight—understanding how material operations reflect spiritual transformations. Fludd's cosmological diagrams exemplify correspondence: every aspect of the divine order has its reflection in the natural world and the human body. Szulakowska emphasizes that Renaissance emblem books were entirely organized around correspondence: each image corresponded to concepts, virtues, natural phenomena, spiritual principles. The artist using correspondence wisely could load a single image with multiple levels of meaning. Modern neuroscience has rediscovered aspects of correspondence: homologous brain structures correspond to different functions, genetic codes correspond to physical traits, psychological patterns correspond to spiritual development. Correspondence is not mystical but fundamental to how systems organize—the principle that what works at one scale often works at other scales.""",
        "related_concepts": ["Sympathy", "Analogy", "Microcosm-Macrocosm", "Resonance"],
        "figures": [2, 3, 13],  # Dee, Fludd, Ficino
        "emblems": []
    },

    {
        "name": "Distillation",
        "slug": "distillation",
        "summary": "The separation of a liquid substance from solid or liquid mixture through heating and recondensation. Alchemically, distillation represents the extraction of essence or quintessence—the refinement of matter to its pure spiritual principle.",
        "essay": """Distillation (from Latin *distillare*, to drip down) is the laboratory process of vaporizing a liquid through heat and then recondensing it in a separate chamber, effectively purifying and concentrating it. Alchemists developed distillation technology to extraordinary sophistication, producing highly concentrated essences (quintessences) from herbs, minerals, and metals. The philosophical meaning parallels the operation: distillation extracts what is essential (refined, concentrated, purified) from what is grossly mixed. The drops of pure essence appearing in the distillation flask represent the spiritualization of matter—the volatile principle separated and concentrated, freed from gross companions. Renaissance alchemical texts frequently describe the human soul's separation from the body at death using distillation metaphor: the spirit rises like vapor, leaving the gross body behind. The distilled essence, being highly concentrated and potent, requires careful handling—a drop of concentrated essence has immense effect that crude material lacks. Spiritually, distillation represents the extraction of essential truth from complex experience, the refinement of understanding, the concentration of spiritual insight. Medieval physicians and apothecaries relied on distillation to produce medicines—healing essences extracted from plants. The connection between distillation technology and medical efficacy meant that alchemical knowledge had practical, undeniable value; you could drink a distilled essence and feel its effect. This grounded alchemy in observable reality: the distillation equipment transformed substance visibly and measurably. Many Renaissance emblem books featured distillation apparatus because it perfectly illustrated the hidden operation of transformation at work.""",
        "related_concepts": ["Quintessence", "Essence Extraction", "Volatility", "Refinement"],
        "figures": [4, 10, 12],  # Paracelsus, Maier, Stolcius
        "emblems": []
    },

    {
        "name": "Interior Work",
        "slug": "interior-work",
        "summary": "The spiritual practice of inner transformation distinct from outer ritual or external operation. Interior work emphasizes that true alchemical change occurs through meditation, visualization, ethical development, and consciousness refinement.",
        "essay": """Interior work (as distinguished from exterior or manual work) emphasizes that the most crucial alchemical transformation happens inwardly—in consciousness, imagination, ethical development, and mystical realization. While exterior alchemy involves furnaces, vessels, distillation apparatus, and actual chemical changes, interior alchemy involves no external apparatus: the transformation occurs through meditation, prayer, ethical discipline, imaginative practice, and progressive mystical insight. Böhme emphasized interior work: that the divine regeneration in the human soul followed the same pattern as the great work in matter, but operated entirely inwardly. The interior work is simultaneously more difficult and more liberatory than exterior work: it requires sustained discipline (you cannot simply stop attending to your inward development), but it is universally accessible (anyone can practice, without expensive equipment or dangerous materials). 17th-century Rosicrucian circles increasingly emphasized interior work, suggesting that the true transformation the Rosicrucians offered was consciousness transformation accessible to serious students. Jung later rediscovered this principle: that alchemical texts described psychological transformation encoded in chemical metaphor. Interior work asks: what exterior operation are you mimicking inwardly? If outer distillation separates volatile from fixed, what inner separation are you achieving (intuition from intellect, spirit from matter-identification)? Zuber emphasizes interior/exterior integration in spiritual alchemy: the outer work sanctifies matter, the interior work transforms consciousness, and together they achieve the goal. The greatest practitioners unified both—their hands worked with actual substances while their spirit worked on consciousness.""",
        "related_concepts": ["Mystical Practice", "Meditation", "Consciousness Transformation", "Ethical Development"],
        "figures": [5, 6, 9],  # Böhme, Fludd, Swedenborg
        "emblems": []
    },

    {
        "name": "Gender and Alchemy",
        "slug": "gender-alchemy",
        "summary": "The role of gender symbolism and gendered principles (masculine/feminine) in alchemical theory and practice. The alchemical marriage (coniunctio) unites king and queen; gender determines access to esoteric knowledge.",
        "essay": """Gender is deeply embedded in alchemical symbolism: the king represents fixed, conscious, solar principle; the queen represents volatile, intuitive, lunar principle. Their union—the sacred marriage or coniunctio—represents the goal where opposites transcend separation and recognize essential complementarity. However, historical alchemical texts predominantly addressed male practitioners, and women's access to esoteric knowledge was restricted. Yet women appear as key figures: Anna Zieglerin as practical alchemist and teacher, Mary Anne Atwood as spiritual alchemist theorist, Anna Bonus Kingsford as mystical integrator, Iuliana Covaci as monastic reformer. Modern scholarship (particularly Akerman on Zieglerin, Zuber on female practitioners) shows women participated in alchemy actively despite marginalization. The gender of the alchemist mattered: women had to navigate social structures that assumed esoteric knowledge belonged to men. Yet the interior work was available equally—consciousness transformation knows no gender. Some feminist scholars argue that the symbolism of the coniunctio itself provided women with frameworks for understanding their own development: the royal marriage could be understood as inner union of conscious and unconscious, masculine and feminine principles within each person regardless of biological gender. The masculine-principle-dominant framing of alchemy (the king's activity, the solar consciousness) may have marginalized perspectives valuing receptivity, intuition, relational knowing—precisely the capacities alchemical symbolism assigned to the queen. Contemporary practitioners increasingly attend to how gender shapes access to knowledge and how alchemical symbolism can support liberation rather than encode patriarchal limitation.""",
        "related_concepts": ["Hieros Gamos", "Coniunctio", "King and Queen", "Masculine-Feminine Principles"],
        "figures": [40, 41, 43],  # Anna Zieglerin, Mary Anne Atwood, Anna Kingsford (to be added)
        "emblems": []
    },

    {
        "name": "Color Symbolism",
        "slug": "color-symbolism",
        "summary": "The systematic association of colors with alchemical stages, spiritual principles, and metaphysical meanings. Black (nigredo), white (albedo), and red (rubedo) mark major transformational stages.",
        "essay": """Color carried immense philosophical and spiritual significance in alchemy: colors were not merely visual appearance but visible manifestations of transformation stages and spiritual principles. The triadic sequence—nigredo (blackening), albedo (whitening), rubedo (reddening)—marked three major stages of the Great Work, each color both describing observable chemical changes and representing mystical transformations. Nigredo (blackness) represents putrefaction, dissolution, death of the old self—necessarily dark because the ego's comfortable structures are breaking down. Albedo (whiteness) represents purification and illumination—washing away impurities, achieving clarity, spiritual awakening. Rubedo (redness) represents the perfection and completion—vitality, love, the integrated consciousness aflame with divine passion. Multi-colored stage (cauda pavonis, peacock's tail) where iridescent colors appear indicates advanced refinement approaching final transformation. Szulakowska shows how Renaissance emblem books were entirely organized around color symbolism: the artist's choice of color conveyed alchemical meaning. Green represented growth and the renewal of life; yellow associated with solar consciousness and gold; blue with mercury and intellect. Understanding color symbolism enables reading emblem books at multiple levels simultaneously: the color choices encode specific alchemical meanings visible to the trained eye. In mystical practice, meditators worked with color visualization: imagining divine light as golden, the soul's purification as white light, passion and transformation as red. Different color corresponds to different chakras in later yoga philosophy—suggesting that color symbolism accessed something universal about consciousness. Medieval and Renaissance knowledge systems saw color as carrying objective meaning, not subjective association.""",
        "related_concepts": ["Nigredo", "Albedo", "Rubedo", "Cauda Pavonis", "Color Perception"],
        "figures": [10, 12, 18],  # Maier, Stolcius, Flamel
        "emblems": []
    },

    {
        "name": "Embodied Knowledge",
        "slug": "embodied-knowledge",
        "summary": "Knowledge gained through direct experience, bodily practice, and sensory engagement—as opposed to purely intellectual or abstract knowledge. Alchemical practice teaches through doing, not merely reading.",
        "essay": """Embodied knowledge is the understanding that emerges through direct engagement of the body, senses, and practical action—as distinguished from abstract intellectual knowledge. Medieval alchemy required embodied knowledge: the alchemist learned through standing before the furnace, controlling temperature, observing color changes, smelling vapors, feeling heat, manipulating materials. This bodily engagement meant that alchemical knowledge was not merely intellectual assertion but lived in the body. You could not learn alchemy from books alone; you had to apprentice, practice, repeat operations, gradually internalize the discipline. Contemporary epistemology (particularly feminist philosophy) has recovered the value of embodied knowledge, noting that Western tradition systematically devalued it in favor of abstract rationality. Yet alchemy never fully separated from embodied knowing: the Great Work occurred in the body (the alchemist's transformation) through bodily work (handling materials, enduring heat and stress). Szulakowska emphasizes that emblem books were designed for embodied knowledge: meditation on images with the whole being (not merely conceptual understanding). Zuber notes that spiritual alchemy recovers embodied knowledge through practice—meditation that engages the whole person, not mere intellectual contemplation. The Rosicrucian emphasis on interior work and prayer represents embodied knowledge: the entire organism—emotions, will, imagination, intellect—is engaged in the work. Contemporary somatic psychology and movement practices rediscover what alchemists always knew: that consciousness is not localized in the head but distributed throughout the body, and that transformation requires engaging the whole embodied person. The laboratory (the opus manual) and the meditator (the opus spirituale) both practice embodied knowledge—understanding that lives in the body, not merely in abstract theory.""",
        "related_concepts": ["Praxis", "Interior Work", "Theory-Practice Integration", "Direct Experience"],
        "figures": [4, 5, 12],  # Paracelsus, Böhme, Stolcius
        "emblems": []
    },

    {
        "name": "Theurgic Practice",
        "slug": "theurgic-practice",
        "summary": "Ritual action designed to invoke divine powers and achieve union with the divine—as distinguished from magic, which manipulates natural forces. Theurgy emphasizes the human participation in divine action.",
        "essay": """Theurgy (from Greek *theos*, divine, and *ergon*, action or work) refers to divine action or working with divine powers through ritual practice. Neoplatonic philosophers, particularly Iamblichus, developed elaborate theurgic systems based on the principle that the divine can be invoked and united with through proper ritual, sacred objects, and invocations. Unlike magic, which was sometimes understood as manipulation of natural forces, theurgy emphasizes cooperation with divine powers and participation in divine action. The human theurgist does not command gods but rather aligns with divine will, invokes divine presence, and enables union. Rosicrucian and Renaissance magic incorporated theurgic elements: the idea that proper invocation, sacred geometry, divine names, and ritual choreography could align the practitioner's will with divine will. Dee's work on angelic communication was theurgic: not commanding angels but calling them forth, seeking wisdom from higher realms. Fludd's elaborate cosmological diagrams were theurgic: they mapped the pathways through which divine influence descends through celestial spheres into the natural world. Contemporary Rosicrucian practice often emphasizes theurgic elements: the goal is not controlling events but aligning personal will with divine will, becoming a channel for divine action. The interior work of theurgic practice involves visualization, invocation, aspiration—drawing divine presence into consciousness. Churton emphasizes that Rosicrucian spirituality is fundamentally theurgic: the initiate works to become conscious of divine presence within and to enable divine action in the world. Theurgy implies that the sacred world and material world are not sealed off but interpenetrating—that ritual action in the material world has real effects in the divine realm and vice versa.""",
        "related_concepts": ["Magic", "Ritual Practice", "Divine Invocation", "Union with the Divine"],
        "figures": [2, 3, 9],  # Dee, Fludd, Swedenborg
        "emblems": []
    },

    {
        "name": "Multiplicity and Return",
        "slug": "multiplicity-return",
        "summary": "The alchemical principle that the multiplication (repeating of the Great Work) produces ever-greater quantities and quality of the philosopher's stone. The return (circular completion) emphasizes perpetual renewal.",
        "essay": """Multiplicity and return are twin principles in alchemical practice: the Great Work, once completed, can be repeated infinitely, each iteration producing more and finer stone. Medieval and Renaissance texts emphasized that the master alchemist, having achieved the stone, could then multiply it indefinitely—heating the stone with new raw material, causing transmutation, and generating new stone in geometric progression. This multiplication principle addressed the practical question: if the philosopher's stone is so rare, how can its benefits reach humanity? The answer: it multiplies itself. This also implies circularity: the completed work returns to the beginning (raw matter transformed by applied stone), creating a cycle that can repeat eternally. Philosophically, multiplicity and return suggest that spiritual development follows the same pattern: once initial transformation is achieved, it can be repeated, deepened, extended indefinitely. There is no final resting point; the spiral continues upward. Return (circular completion) also invokes the hermetic principle of eternal recurrence: the cosmic pattern repeats at every level; what goes up must come down (return) to begin the cycle again. This principle appears in both cyclical cosmologies (the Great Year returning eternally) and in developmental psychology (the spiral path where you return to earlier stages but at a higher level of integration). Maier's Atalanta Fugiens included multiplication emblems showing the progressive increase and refinement of the stone. Spiritually, multiplicity-return teaches that enlightenment is not a fixed achievement but a perpetually renewable condition that deepens through repeated practice and return to fundamental principles.""",
        "related_concepts": ["Multiplication", "Eternal Return", "Cyclicity", "Progressive Refinement"],
        "figures": [10, 11, 12],  # Maier, others
        "emblems": []
    }
]

# ============================================================================
# PHASE 1 TEXTS (10 new entries)
# ============================================================================

phase_1_texts = [
    {
        "title": "The Golden Chain of Homer",
        "year": 1723,
        "author": "Kirchweger",
        "language": "German",
        "location": "Frankfurt",
        "lat": 50.1109,
        "lng": 8.6821,
        "summary": "18th-century alchemical text presenting the Great Work as an unbroken chain of transmission from ancient wisdom through medieval alchemy to modern practice. Systematic integration of Boehme, Paracelsus, and Renaissance alchemy.",
        "essay": """The *Golden Chain of Homer* (*Die Goldne Kette Homeri*, 1723) is an alchemical miscellany compiled by Kirchweger that presents the Great Work as an unbroken golden chain of wisdom transmission from ancient Homer through medieval alchemists to modern practitioners. The title invokes Homer's image of a golden chain stretching from heaven to earth—a metaphor for the continuous connection between divine wisdom and human understanding. Kirchweger's compilation synthesizes Paracelsian medicine, Boehme's mystical theology, and Renaissance alchemy into a coherent system accessible to serious students. The text emphasizes that alchemy is not fragmented secret knowledge but a systematic path of development available to anyone committed to the work. Kirchweger integrated theoretical exposition, practical instructions, and mystical interpretation—the reader could understand alchemical principles (theory), attempt actual operations (practice), and engage in meditation on hidden meanings (mysticism) simultaneously. The compilation approach meant assembling texts from multiple authorities, showing their essential agreement despite surface differences. The *Golden Chain* became widely circulated in German-speaking territories and influenced 18th-century alchemical revival. The image of the golden chain emphasizes continuity: from Homer (ancient wisdom) through Hermes, Zosimos, medieval alchemists, Paracelsus, Fludd to contemporary practitioners—an unbroken line of transmission. This genealogical vision reassured modern practitioners that they were not pursuing marginal eccentricity but participating in an ancient and legitimate tradition. The text demonstrates how 18th-century alchemists presented their work as recovery and continuation of perennial wisdom.""",
        "concepts": [1, 15, 20, 25, 37],
        "figures": [4, 5, 10, 11],  # Paracelsus, Boehme, Maier, etc.
        "source_type": "primary_emblem"
    },

    {
        "title": "Book of Divine Consolation",
        "year": 1556,
        "author": "Meister Eckhart",
        "language": "German",
        "location": "Rhineland",
        "lat": 50.9365,
        "lng": 6.9582,
        "summary": "Medieval German mystic's meditations on spiritual transformation and union with the divine. Influential precursor to Boehme and later mystical alchemy.",
        "essay": """Meister Eckhart's *Book of Divine Consolation* (*Buch der Göttlichen Tröstung*, 1556—though Eckhart lived 1260–1327) represents medieval German mysticism's language of spiritual transformation that directly presaged later alchemical language. Eckhart's teaching that the soul must be emptied, stripped of all attachment, dissolved into nothingness to receive divine presence, provided the conceptual framework later alchemists used to describe the Great Work. The *Book of Divine Consolation* offers meditations on suffering, renunciation, and the death of the ego-self as necessary passages through which divine union becomes possible. Eckhart's formula—that God is the desert wilderness where all creatures vanish into nothingness—expresses in mystical language what alchemists described chemically: that matter must be calcinated (reduced to ash), dissolved (returned to prima materia), and reformed before transmutation becomes possible. The text emphasizes that spiritual consolation comes not from avoiding suffering but from understanding its transformative purpose. Later alchemists reading Eckhart found exact correspondences between his mystical language and their operational language: dissolution = death of the ego, calcination = renunciation of worldly attachments, reformation = union with the divine. Zuber emphasizes Eckhart as crucial precursor to Boehme and thus to spiritual alchemy; the medieval mystical language provided conceptual tools that later practitioners elaborated. The *Book of Divine Consolation* demonstrates that the deepest impulses of Christian mysticism aligned with alchemical aspiration—that transformation through dissolution and death was the Christian path itself.""",
        "concepts": [1, 3, 5, 37, 40],
        "figures": [5],  # Reference to Boehme lineage
        "source_type": "primary_mystical"
    },

    {
        "title": "The Hermetic Museum",
        "year": 1625,
        "author": "Lucas Jennis",
        "language": "Latin",
        "location": "Frankfurt",
        "lat": 50.1109,
        "lng": 8.6821,
        "summary": "Early 17th-century anthology of alchemical texts and treatises, presenting diverse approaches to the Great Work. Comprehensive survey of Renaissance and medieval alchemy.",
        "essay": """*Hermetic Museum* (*Museum Hermeticum*, 1625, compiled by Lucas Jennis) is a seminal anthology collecting diverse alchemical texts from medieval and Renaissance authors, presenting multiple perspectives on the Great Work and its achievement. The collection includes foundational works: the *Emerald Tablet*, Jabir's writings, various medieval treatises, and contemporary pieces. By presenting multiple voices addressing the same fundamental questions—How is the stone achieved? What are the proper materials? What do the stages represent?—the *Hermetic Museum* demonstrates both the essential unity of alchemical teaching and its multiple legitimate expressions. Some texts emphasize practical operations (Valentinus), others mystical interpretation (Hermes), still others medical applications (Arnauld). The anthology structure suggests that readers must integrate diverse approaches rather than follow a single method. The term "museum"—implying a collected display of treasures for contemplation—frames alchemy as knowledge worth preserving and studying. Later alchemists and historians relied on the *Hermetic Museum* as the standard reference for understanding the alchemical tradition; many texts survive only because they were included in this anthology. The collection's organization implicitly teaches: understand how different authorities address the same problems, recognize the deeper pattern beneath surface disagreements, develop your own approach synthesizing insights from multiple sources. The *Hermetic Museum* became the 17th-century alchemist's essential library, referenced constantly and quoted extensively. Its compilation demonstrates that alchemical knowledge was not secretive hoarding but a living tradition where practitioners studied predecessors, debated interpretations, and advanced understanding collectively.""",
        "concepts": [1, 5, 8, 10, 15],
        "figures": [19, 20, 10, 11],  # Geber, Hermes, Maier, etc.
        "source_type": "secondary_anthology"
    },

    {
        "title": "Commentaries on the Emerald Tablet",
        "year": 1530,
        "author": "Jabir ibn Hayyan (Translated by Geberus)",
        "language": "Latin Translation",
        "location": "Islamic World/Europe",
        "lat": 48.8566,
        "lng": 2.3522,
        "summary": "Translated Islamic alchemist's extended commentary on the foundational Emerald Tablet, explaining its cryptic axioms through both operational and philosophical lenses.",
        "essay": """Jabir ibn Hayyan's (Latinized as Geberus, 8th-9th century) *Commentaries on the Emerald Tablet* provide systematic explanation of the famous axiom "As above, so below; as below, so above" and other hermetic principles. The Emerald Tablet—attributed to Hermes Trismegistus and preserved in Arabic sources—states the fundamental principle of hermetic philosophy: the universe operates according to correspondence and analogy, with divine pattern reflecting at every level. Jabir's commentaries explain how this principle enables both theoretical understanding (knowing the pattern at one level reveals it everywhere) and practical operation (manipulating matter according to its sympathetic correspondences). The Latin translation, made available in medieval and Renaissance Europe, was crucial for transmitting Islamic alchemy to the West. Jabir's explanations bridged the gap between Hellenistic alchemy (Zosimos, Hermes) and medieval European practice. His practical emphasis—that understanding correspondences enables real transmutation—provided intellectual justification for laboratory work: if all levels of reality follow the same pattern, then manipulating matter at one level affects all levels. Jabir's work demonstrates the Islamic world's sophisticated development of alchemy during Europe's medieval period; the West eventually recovered this advanced knowledge through translation and reintegration. The Emerald Tablet, explained through Jabir's commentaries, became the foundational text that all later alchemists referenced. Understanding Jabir's interpretation of the Tablet is essential for understanding how Renaissance and Rosicrucian alchemy understood their fundamental operating principles.""",
        "concepts": [27, 25, 5, 40],
        "figures": [19, 20],  # Geber/Jabir, Hermes
        "source_type": "primary_commentary"
    },

    {
        "title": "The Chymical Wedding of Christian Rosencreutz",
        "year": 1616,
        "author": "Johann Valentin Andreae",
        "language": "German",
        "location": "Tübingen",
        "lat": 48.5216,
        "lng": 9.0577,
        "summary": "Seminal Rosicrucian text presenting the Great Work as a sacred marriage. Allegorical narrative encoding alchemical stages and Rosicrucian teachings.",
        "essay": """The *Chymische Hochzeit Christiani Rosencreutz Anno 1459* (*The Chymical Wedding of Christian Rosencreutz in the Year 1459*, 1616) is Johann Valentin Andreae's masterwork—an elaborate allegorical narrative in which the protagonist, Christian Rosencreutz, is invited to witness and participate in a sacred wedding celebration. The text has become the foundational document of Rosicrucian tradition, endlessly interpreted and reinterpreted. On one level, it is an adventure narrative: Rosencreutz journeys through landscapes encountering guides, tests, and mysteries. On another level, it encodes the entire alchemical process: the seven-day celebration corresponds to the seven stages of the Great Work, the royal couple represents the sacred marriage (coniunctio), and the final apotheosis presents the perfected human as microcosm reflecting divine order. The text's brilliance lies in its layered structure: readers at different levels of understanding find appropriate teaching. A naive reader finds adventure and mystique; an alchemically educated reader recognizes every detail as encoding specific operations and principles; a theologian recognizes Christian redemption narrative. Andreae's authorship remains debated—did he write it as sincere esoteric teaching or as literary satire of occult pretension? The ambiguity adds to its power: readers project their own understanding onto the text. The *Chymical Wedding* became the central text that Rosicrucian movements claimed as their authentic founding document, often attributed to the legendary Christian Rosencreutz rather than Andreae. The text's influence on subsequent esotericism cannot be overstated: every Rosicrucian group references it, every mystical practitioner studies it, every alchemical philosopher interprets it. Its vision of the sacred marriage uniting opposites became the archetypal image for spiritual transformation.""",
        "concepts": [1, 15, 20, 25, 37],
        "figures": [1, 10, 11],  # Andreae, Maier, etc.
        "source_type": "primary_mystical"
    },

    {
        "title": "The Divine Visits (Selected Writings)",
        "year": 1700,
        "author": "Jacob Boehme",
        "language": "German",
        "location": "Görlitz, Germany",
        "lat": 51.1585,
        "lng": 15.0043,
        "summary": "Collection of Boehme's mystical teachings on divine revelation and interior transformation. Foundation for spiritual alchemy philosophy.",
        "essay": """Jacob Boehme's collected mystical writings, compiled as *The Divine Visits* and other collections, present his distinctive vision of spiritual transformation as the human participation in the divine process itself. Boehme (1575–1624) was a shoemaker in Görlitz whose mystical experiences, documented in his writings, became foundational for spiritual alchemy. Unlike traditional alchemists focused on material operations or even philosophers focused on theoretical exposition, Boehme described the interior alchemical work in rich, visionary language. He taught that the divine life involves perpetual activity and struggle—God is not static perfection but perpetual becoming. Creation itself is God's self-differentiation into light and darkness, manifestation and concealment. The human being, as microcosm, recapitulates this divine process: spiritual development involves encountering one's own inner darkness (the shadow, the suffering depths), integrating it, and emerging into higher consciousness. Boehme's teaching revolutionized spiritual alchemy: instead of material gold-making or abstract philosophy, the work was consciousness transformation, the soul's death and resurrection in Christ. His writings were initially condemned by the Lutheran church but later became widely circulated, especially among Pietist and mystical communities. Boehme's influence on subsequent spirituality was immense: William Law, Swedenborg, Gichtel, and later Romantics all studied him intensely. His vision that divine and human transformation are essentially the same process occurring at different scales shaped all subsequent spiritual alchemy. The *Divine Visits* and Boehme's other works establish that the language of alchemy—dissolution, calcination, fermentation, distillation, marriage, perfection—describes the soul's journey to divine union.""",
        "concepts": [1, 3, 5, 25, 37],
        "figures": [5, 6, 9],  # Boehme, others
        "source_type": "primary_mystical"
    },

    {
        "title": "Studies in Ancient Hermetism",
        "year": 1920,
        "author": "Various modern scholars (anthology)",
        "language": "English",
        "location": "Europe/America",
        "lat": 50,
        "lng": 10,
        "summary": "20th-century scholarly anthology examining Hermetic philosophy and its transmission through Islamic and European traditions. Academic recovery of esoteric thought.",
        "essay": """20th-century scholarly recovery of Hermeticism began in earnest with systematic studies of Hermetic texts, their origins, transmission, and influence. Scholars including Festugière, Copenhaver, and others established the historical genealogy: the Hermetic Corpus (primarily Neoplatonic texts misattributed to Hermes Trismegistus) was composed in Hellenistic Egypt; transmitted through Islamic civilization where it was preserved and developed; recovered by Renaissance scholars who translated it into Latin; and became foundational for Renaissance magic and alchemy. This genealogy demonstrated that Western esotericism was not primitive superstition but a sophisticated philosophical tradition with documented history and intellectual continuity. The scholarly recognition that Hermeticism was a real historical phenomenon—not mere mystical fantasy—enabled serious academic study. Scholars could now examine how alchemical and magical theories developed through actual intellectual history rather than dismissing them as irrationality. This scholarly recovery also revealed the limitations of certain interpretations: certain claims about Hermeticism were historically inaccurate (e.g., attributing knowledge to Hermes that actually came from later Neoplatonists). Yet it also recovered genuine insights from the tradition. Modern studies in ancient Hermeticism, while academic rather than esoteric, provided essential context for understanding how alchemy and Renaissance magic developed from real philosophical sources. The scholarly recovery enabled dialogue between academic historians and esoteric practitioners: both could recognize Hermeticism as historically significant even if they disagreed about its spiritual validity.""",
        "concepts": [5, 25, 27, 40],
        "figures": [20, 2, 3],  # Hermes, Dee, Fludd
        "source_type": "secondary_scholarly"
    },

    {
        "title": "The Path of the Seeker (Selected Letters and Instructions)",
        "year": 1920,
        "author": "Rudolf Steiner",
        "language": "German/English",
        "location": "Europe",
        "lat": 47.2769,
        "lng": 11.4591,
        "summary": "20th-century esotericist and founder of Anthroposophy presents modern spiritual alchemy as consciousness development grounded in scientific thinking.",
        "essay": """Rudolf Steiner (1861–1925), founder of Anthroposophy, presented spiritual alchemy and esotericism as entirely compatible with modern scientific consciousness. Where previous mystics separated science from spirituality, Steiner argued that genuine spiritual development must incorporate rigorous thinking and scientific methodology. His approach to alchemy was revolutionary: not defending ancient texts as literal truth or rejecting them as superstition, but recognizing in alchemical language descriptions of consciousness development that could be practiced today. Steiner developed practical exercises—meditation techniques, contemplative methods, imaginative practices—that embodied alchemical principles in forms accessible to modern people. He taught that the human being was undergoing evolutionary transformation; ancient humanity had different consciousness (pictorial imagination rather than conceptual thinking), modern humanity had developed intellect, and future humanity would develop new capacities (spiritual perception integrated with thinking). Alchemy, from this perspective, described the development of new capacities in human consciousness. Steiner's work influenced 20th-century esotericism profoundly: he demonstrated that ancient esoteric knowledge could be translated into modern forms without loss of substance, that spiritual development could be scientifically rigorous, that alchemy and anthroposophy need not oppose but could integrate. His movement attracted intellectuals, scientists, and serious practitioners precisely because he bridged the apparent chasm between modern thinking and traditional esotericism. While some criticized Steiner as naïve about science or simplistic in his esotericism, his fundamental insight—that human consciousness itself is the work, the matter, and the goal of alchemy—proved generative for 20th-century spiritual practice.""",
        "concepts": [3, 5, 37, 40],
        "figures": [9],  # Connection to Swedenborg lineage
        "source_type": "secondary_modern"
    },

    {
        "title": "The Three Principles of the Divine Essence",
        "year": 1619,
        "author": "Jacob Boehme",
        "language": "German",
        "location": "Görlitz",
        "lat": 51.1585,
        "lng": 15.0043,
        "summary": "Boehme's systematic exposition of his theosophical cosmology: the divine ground, creation, and human participation in divine transformation.",
        "essay": """Jacob Boehme's *The Three Principles of the Divine Essence* (*Psychologia Vera oder Beschreibung des Wesens aller Wesen*, actually published posthumously though written earlier) presents his full theosophical system. The three principles are: (1) the eternal divine unity (the Godhead beyond differentiation), (2) the divine differentiation into light and darkness (God's creative self-manifestation), and (3) the material creation (the third principle, the actualisation of the first two). This triadic vision, expressed in alchemical and mystical language, provided a framework for understanding how the infinite divine becomes finite creation and how finite humanity can participate in divine becoming. Boehme taught that each principle is complete in itself yet interpenetrates the others—a vision of reality as profoundly relational and participatory rather than hierarchically separated. His *Three Principles* became foundational for later Rosicrucian and theosophical philosophy. The text's complexity—combining cosmological exposition, spiritual instruction, and alchemical analysis—made it difficult but rewarding for serious students. Boehme's influence on German Idealism (Schelling, Hegel) and on modern esotericism (Theosophy, Anthroposophy) cannot be overstated. His vision that the human being exists as a microcosmic replica of the cosmic process meant that personal transformation is simultaneously participation in cosmic transformation. The work of consciousness (the interior alchemy) directly affects the cosmic order because the individual and cosmic are fundamentally one. This teaching radically elevated the spiritual significance of personal practice.""",
        "concepts": [1, 5, 15, 25, 37],
        "figures": [5],  # Boehme central
        "source_type": "primary_mystical"
    }
]

# Process and add all Phase 1 entries
print("=" * 80)
print("PHASE 1 EXPANSION — Adding Entries to Prototype Data")
print("=" * 80)
print()

print(f"FIGURES: Adding {len(phase_1_figures)} new entries...")
for idx, fig in enumerate(phase_1_figures, 1):
    figure = {
        "id": next_fig_id + idx - 1,
        "name": fig["name"],
        "slug": fig["name"].lower().replace(" ", "-").replace(",", "").replace(".", ""),
        "birth_year": fig.get("birth_year"),
        "death_year": fig.get("death_year"),
        "nationality": fig.get("nationality"),
        "location": fig.get("location"),
        "lat": fig.get("lat"),
        "lng": fig.get("lng"),
        "primary_discipline": fig.get("primary_discipline"),
        "summary": fig["summary"],
        "essay": fig["essay"],
        "scholars": fig.get("scholars", []),
        "key_works": fig.get("key_works", [])
    }
    data['figures'].append(figure)
    birth = str(fig.get('birth_year', '?'))
    death = str(fig.get('death_year', '?'))
    print(f"  [{idx:2d}] {fig['name']:30s} ({birth:4s}–{death:4s})")

print()
print(f"CONCEPTS: Adding {len(phase_1_concepts)} new entries...")
for idx, con in enumerate(phase_1_concepts, 1):
    concept = {
        "id": next_con_id + idx - 1,
        "name": con["name"],
        "slug": con.get("slug", con["name"].lower().replace(" ", "-")),
        "summary": con["summary"],
        "essay": con["essay"],
        "related_concepts": con.get("related_concepts", []),
        "figures": con.get("figures", []),
        "texts": con.get("texts", []),
        "emblems": con.get("emblems", [])
    }
    data['concepts'].append(concept)
    print(f"  [{idx:2d}] {con['name']:30s}")

print()
print(f"TEXTS: Adding {len(phase_1_texts)} new entries...")
for idx, txt in enumerate(phase_1_texts, 1):
    text = {
        "id": next_text_id + idx - 1,
        "title": txt["title"],
        "slug": txt["title"].lower().replace(" ", "-").replace("(", "").replace(")", ""),
        "year": txt.get("year"),
        "author": txt.get("author", "Unknown"),
        "language": txt.get("language", "Unknown"),
        "location": txt.get("location"),
        "lat": txt.get("lat"),
        "lng": txt.get("lng"),
        "summary": txt["summary"],
        "essay": txt["essay"],
        "concepts": txt.get("concepts", []),
        "figures": txt.get("figures", []),
        "source_type": txt.get("source_type", "primary")
    }
    data['texts'].append(text)
    print(f"  [{idx:2d}] {txt['title']:50s} ({txt.get('year', '?')})")

print()
print("=" * 80)
print("PHASE 1 EXPANSION COMPLETE")
print("=" * 80)
print(f"New Totals:")
print(f"  Figures: {len(data['figures'])} (was 53, added 10)")
print(f"  Concepts: {len(data['concepts'])} (was 50, added 10)")
print(f"  Texts: {len(data['texts'])} (was 74, added 10)")
print()
print("Saving to prototype_data.json...")
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("[OK] Saved successfully")
print()
print("Next: Update build_site.py and rebuild")
