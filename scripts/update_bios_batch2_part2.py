#!/usr/bin/env python3
"""
update_bios_batch2_part2.py
Full essays for: id=29 Gerhard Dorn, id=33 Agrippa, id=19 Jabir, id=17 Pico della Mirandola.
"""

import json, os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prototype_data.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

updates = {}

# ── id=29: Gerhard Dorn ──────────────────────────────────────────────────────

updates[29] = {
    'essay': (
        "Gerhard Dorn (c.1530–c.1584) was a Flemish or German physician and philosopher who "
        "stands as the most systematic and intellectually rigorous interpreter of Paracelsian "
        "philosophy in the second half of the sixteenth century. Operating in Frankfurt and the "
        "surrounding region, Dorn made Paracelsus accessible to Latin-reading audiences through "
        "translation, commentary, and independent philosophical elaboration. His work represents "
        "the first sustained attempt to derive from Paracelsus's scattered and often opaque "
        "writings a coherent natural philosophy, and his translations shaped how Paracelsus was "
        "read by subsequent generations of physicians, chemists, and theosophers.\n\n"

        "Almost nothing is known of Dorn's life with certainty. His nationality is disputed — "
        "he has been described as both Flemish and German — and biographical details are sparse. "
        "He appears to have been medically trained and to have practised as a physician. His "
        "writings are in Latin, which was both the language of learned medicine and the vehicle "
        "through which he made Paracelsus's German writings available to European scholarship. "
        "His career falls entirely in the 1560s–1580s, a period when Paracelsianism was expanding "
        "rapidly through print and when the controversy between Galenists and Paracelsians was "
        "at its most intense.\n\n"

        "Dorn's first significant work, the Chymisticum Artificium Naturae Theoricum et Practicum "
        "(Chemical Artistry of Nature, Theoretical and Practical, 1568), established his approach: "
        "integrating Paracelsian categories with natural philosophy derived from Aristotle and "
        "Neoplatonic sources, producing a more systematic account than Paracelsus himself ever "
        "offered. The text addresses the theoretical foundations of chemical medicine — the "
        "relationship between arcana, seeds of things, and the three Paracelsian principles "
        "(sulphur, mercury, salt) — as well as practical procedures. Dorn was concerned throughout "
        "to demonstrate that Paracelsian medicine was philosophically grounded rather than merely "
        "empirical or magical, a concern driven partly by the need to defend chemical medicine "
        "against Galenic attack.\n\n"

        "His translations of Paracelsus, gathered under the title Speculativa Philosophia (and "
        "related collections), made the core Paracelsian texts available in Latin and included "
        "Dorn's own commentaries explaining and extending Paracelsus's arguments. These were not "
        "straightforward translations but interpretive interventions: Dorn systematized, clarified, "
        "and occasionally corrected Paracelsus in the process of rendering him in Latin. This "
        "editorial and philosophical work was crucial for the Latinization of Paracelsianism that "
        "made it a pan-European phenomenon rather than a German-language one.\n\n"

        "The Congeries Paracelsicae Chemiae de Transmutationibus Metallorum (A Collection of "
        "Paracelsian Chemistry on the Transmutation of Metals, 1581) addresses the relationship "
        "between Paracelsian chemistry and the older alchemical tradition of metallic transmutation. "
        "Dorn here engages with the question of whether the Great Work of transmutation was "
        "consistent with Paracelsian natural philosophy or whether the two traditions pointed in "
        "different directions. His answer is characteristically systematic: he attempts to show "
        "how Paracelsian principles can account for transmutation without reducing alchemy to "
        "the older sulphur-mercury framework.\n\n"

        "Dorn's most philosophically distinctive contribution is his elaboration of a tripartite "
        "hierarchy within the alchemical work. Drawing on Paracelsian body-soul-spirit anthropology "
        "and Neoplatonic cosmology, he distinguished between a 'somatic' or material level of "
        "the work (dealing with physical substances), a 'psychic' or soul level (dealing with "
        "the animating principles of things), and a 'pneumatic' or spirit level (dealing with "
        "the highest, divine dimension of matter and soul). This three-level analysis appears "
        "across several of his texts and represents a significant development beyond Paracelsus: "
        "where Paracelsus's three principles (sulphur, mercury, salt) are primarily applied to "
        "the material and medical domains, Dorn gives them a cosmic-hierarchical elaboration.\n\n"

        "The concept of coniunctio (conjunction) is central to Dorn's philosophical system. For "
        "Dorn, the alchemical conjunction of opposites — sulphur and mercury, fixed and volatile, "
        "male and female — was not merely a material process but a pattern operating at all three "
        "levels of his hierarchy. At the highest level, the coniunctio represented the soul's "
        "reunion with its divine source. This reading made Dorn's work particularly attractive "
        "to C.G. Jung, who analysed Dorn extensively in Mysterium Coniunctionis (1955–56), his "
        "most ambitious psychological study of alchemy. Jung treated Dorn as the clearest "
        "exemplar of the 'psychological' dimension of the alchemical tradition — not because "
        "Dorn was doing psychology in any modern sense, but because his tripartite scheme and "
        "his language of inner conjunction provided Jung with the richest material for his "
        "project of reading alchemy as symbolic individuation.\n\n"

        "Dorn's major texts were collected in Zetzner's Theatrum Chemicum (Theatre of Chemistry), "
        "the great anthology of alchemical writing first published at Ursel in 1602 and expanded "
        "in subsequent editions (Strasbourg, 1613, 1622, 1659–61). The Theatrum Chemicum was the "
        "most comprehensive Latin alchemical anthology of the early modern period, and Dorn's "
        "presence in it ensured his texts reached the broadest possible audience of learned readers. "
        "Robert Fludd, Michael Maier, and subsequent Rosicrucian-adjacent writers worked in an "
        "intellectual environment saturated with Dornian Paracelsianism, even where they did not "
        "cite him explicitly.\n\n"

        "The scholarly literature on Dorn is dominated by Jung's reading, which has shaped — and "
        "arguably distorted — subsequent engagement. Jung's Dorn is primarily a psychologist "
        "avant la lettre; historians of science and philosophy have recovered a more nuanced "
        "picture of a physician navigating the medical controversies of his time while developing "
        "a philosophically sophisticated account of Paracelsian principles. Lawrence Principe and "
        "William Newman have emphasized that Dorn's laboratory concerns were real, not merely "
        "symbolic, and that his philosophical elaborations were motivated by the need to defend "
        "chemical medicine on intellectual grounds acceptable to university-trained physicians. "
        "Dorn remains, however, genuinely unusual in the depth and systematicity of his "
        "philosophical ambition, and his tripartite scheme has no close parallel in the "
        "contemporary Paracelsian literature."
    ),
    'key_works': [
        "Chymisticum Artificium Naturae Theoricum et Practicum (1568)",
        "Speculativa Philosophia (translations of Paracelsus with commentary)",
        "Congeries Paracelsicae Chemiae de Transmutationibus Metallorum (1581)",
        "Contributions to Theatrum Chemicum (Zetzner, 1602 onward)"
    ]
}

# ── id=33: Henry Cornelius Agrippa ──────────────────────────────────────────

updates[33] = {
    'essay': (
        "Henry Cornelius Agrippa von Nettesheim (1486–1535) was a German humanist, physician, "
        "lawyer, and occult philosopher whose De Occulta Philosophia Libri Tres (Three Books of "
        "Occult Philosophy) represents the most comprehensive and systematic synthesis of "
        "Renaissance magical philosophy ever produced. Born at Cologne, he studied at the "
        "University of Cologne and subsequently at Paris, where he encountered the full range "
        "of humanist learning; he also studied law, practiced medicine, served in military "
        "campaigns, and occupied a succession of positions as court secretary, physician, and "
        "historiographer across Germany, Switzerland, France, and the Low Countries. His career "
        "was marked by repeated conflicts with ecclesiastical and civil authorities, by financial "
        "difficulty, and by a restless intellectual energy that left him no settled institutional "
        "home.\n\n"

        "The defining intellectual relationship of Agrippa's formation was his early correspondence "
        "with Johannes Trithemius (1462–1516), the Benedictine abbot and encyclopedic scholar "
        "whose Steganographia (a work on cryptography and alleged spirit communication, circulated "
        "in manuscript) had established the idea that natural magic, Kabbalistic angel-naming, "
        "and cryptographic encoding were continuous practices. Agrippa sent Trithemius an early "
        "draft of the De Occulta Philosophia around 1510, when he was approximately twenty-three; "
        "Trithemius's encouraging reply survives and provides the earliest dateable reference to "
        "the work. Between 1510 and its eventual publication in 1531–33, Agrippa extensively "
        "revised and expanded the text, and the relationship between the early draft and the "
        "published version is itself a subject of scholarly investigation.\n\n"

        "The De Occulta Philosophia Libri Tres (Three Books of Occult Philosophy, composed c.1510, "
        "extensively revised and published at Cologne and Antwerp, 1531–33) is the central document "
        "of Renaissance occult philosophy. Its organizational principle is the three-world cosmology "
        "derived from Neoplatonism: the elemental world (the physical cosmos of the four elements), "
        "the celestial world (the heavens, governed by stars, planets, and intelligences), and the "
        "supercelestial or intellectual world (the realm of angels, divine names, and pure "
        "intellect). Each world has its own mode of magic: natural magic (manipulation of elemental "
        "sympathies and antipathies), celestial magic (harnessing stellar and planetary influences "
        "through talismans, images, and suffumigations), and ceremonial or divine magic (working "
        "with angelic names, Kabbalistic divine names, and ritual prayer). The three books are "
        "organized around these three levels respectively.\n\n"

        "Book One treats natural magic: the occult properties (virtutes occultae) of simple "
        "things — plants, stones, animals — that cannot be explained by the four elementary "
        "qualities but operate through hidden sympathy with higher principles. Agrippa draws "
        "heavily on the Neoplatonic concept of the world-soul (anima mundi) as the mediating "
        "principle through which celestial influences descend into matter, and on the extensive "
        "lists of natural sympathies and antipathies found in Pliny, Dioscorides, and the "
        "Hermetic natural-magical tradition. This book is the most practically oriented and "
        "the most directly continuous with medieval natural magic.\n\n"

        "Book Two treats celestial magic: the theory of number, proportion, and harmony as keys "
        "to celestial influence; the properties of the seven planets and their relations to "
        "metals, gems, plants, and bodily organs; magic squares (cameos) attributed to each "
        "planet; the construction of talismans; and the use of music, light, and imagination "
        "to attract or repel planetary influence. This book synthesizes Pythagorean-Neoplatonic "
        "number theory with the Arabic-medieval tradition of astrological magic (particularly "
        "the Picatrix) and with Ficino's astral magic as developed in the De Vita Coelitus "
        "Comparanda. The planetary magic squares attributed to Agrippa — numerical grids whose "
        "rows, columns, and diagonals sum to the same number — became emblematic of Renaissance "
        "magical theory and were reproduced across subsequent occult literature.\n\n"

        "Book Three treats ceremonial and divine magic: the hierarchy of angels and demons "
        "(drawing on Dionysius the Areopagite and the medieval angelic hierarchies), the "
        "Kabbalistic divine names and their uses in invocation, the power of the Hebrew alphabet, "
        "and the construction of magical seals and characters. Agrippa's synthesis of Christian "
        "Kabbalah — the approach developed by Pico della Mirandola and Johannes Reuchlin that "
        "read the Kabbalistic tradition as confirming and enriching Christian theology — reaches "
        "its fullest expression here. The claim that Hebrew is the sacred language in which "
        "divine names retain their full efficacy, and that the Kabbalistic analysis of these "
        "names provides a grammar of spiritual causation, shapes the third book's entire argument.\n\n"

        "The De Incertitudine et Vanitate Scientiarum et Artium (On the Uncertainty and Vanity "
        "of the Arts and Sciences, 1530 — published just before the De Occulta Philosophia) "
        "presents what appears to be a radical contradiction. This satirical, skeptical text "
        "attacks every form of human learning — theology, law, medicine, philosophy, alchemy, "
        "astrology, magic — as vain, uncertain, and productive of more harm than good. Alchemy "
        "is dismissed as fraud; astrology as guesswork; philosophy as endless controversy. The "
        "relationship between this text and the De Occulta Philosophia has been debated by "
        "scholars since the sixteenth century. The most plausible reading, advanced by Vittoria "
        "Perrone Compagni and Charles Nauert, is that the De Vanitate does not represent a "
        "sincere recantation of the De Occulta Philosophia but rather a fideist position: "
        "human reason and human art are ultimately vain; true wisdom comes from divine revelation "
        "alone, and the magical arts are legitimate only insofar as they are ordered toward "
        "divine ends and grounded in faith. The two texts thus represent complementary rather "
        "than contradictory positions.\n\n"

        "Agrippa's De Nobilitate et Praecellentia Foeminei Sexus (On the Nobility and Excellence "
        "of the Female Sex, 1509; published 1529) is an early and sophisticated example of "
        "the Renaissance 'querelle des femmes' — the debate about women's capacities and status. "
        "Written in honour of Margaret of Austria, the text argues for women's intellectual and "
        "spiritual equality with men using humanist rhetorical strategies and scriptural citation. "
        "Whether Agrippa sincerely held the views he advances or was demonstrating rhetorical "
        "technique (declamatio) has been debated; the text's influence on later discussions of "
        "gender and the occult is nonetheless real.\n\n"

        "Agrippa's position in the history of esotericism is that of the great systematizer. "
        "He did not originate the ideas in the De Occulta Philosophia but synthesized, ordered, "
        "and transmitted the full range of Renaissance occult learning in a single accessible "
        "Latin text. His direct sources include Ficino's Theologia Platonica and De Vita, Pico's "
        "Conclusiones and Heptaplus, Reuchlin's De Arte Cabalistica, the Hermetic Corpus as "
        "translated by Ficino, the Neoplatonic tradition from Plato through Iamblichus and Proclus, "
        "and a wide range of medieval natural magic texts. His text was the primary conduit "
        "through which this synthesized tradition reached later generations: the De Occulta "
        "Philosophia was translated into English in 1651 (by James Freake) and influenced Francis "
        "Barrett's The Magus (1801), which in turn shaped nineteenth-century occultism. "
        "Christopher Marlowe's Doctor Faustus cites Agrippa by name as an exemplar of magical "
        "ambition; John Dee owned a copy of the De Occulta Philosophia annotated in his own hand. "
        "The text's influence on subsequent alchemical, Rosicrucian, and hermetic writing is "
        "pervasive if often unacknowledged."
    ),
    'key_works': [
        "De Occulta Philosophia Libri Tres (Three Books of Occult Philosophy; composed c.1510, published 1531–33)",
        "De Incertitudine et Vanitate Scientiarum et Artium (On the Uncertainty and Vanity of the Sciences and Arts, 1530)",
        "De Nobilitate et Praecellentia Foeminei Sexus (On the Nobility and Excellence of the Female Sex, 1509/1529)"
    ]
}

# ── id=19: Jabir ibn Hayyan ──────────────────────────────────────────────────

updates[19] = {
    'essay': (
        "Jābir ibn Ḥayyān (c.721–c.815 CE), known in Latin Europe as Geber, is the most "
        "celebrated name in the history of Islamic alchemy — and one of the most vexed problems "
        "in the history of science. Hundreds of texts are attributed to him in Arabic; the corpus "
        "is staggeringly large, internally inconsistent, and almost certainly not the work of a "
        "single individual. The figure of Jābir has traditionally been described as an eighth-century "
        "alchemist and polymath who worked under the patronage of the Barmakid vizier Yaḥyā ibn "
        "Khālid in the Abbasid court at Baghdad; whether such a historical Jābir existed at all, "
        "and what if anything he wrote, remains genuinely uncertain.\n\n"

        "The defining scholarly intervention on the Jabirian corpus is Paul Kraus's two-volume "
        "study Jābir ibn Ḥayyān: Contribution à l'histoire des idées scientifiques dans l'Islam "
        "(1942–43). Kraus, working from a systematic analysis of the corpus's internal doctrines, "
        "terminology, and cross-references, argued that the texts were composed over an extended "
        "period by a school — most probably an Ismaili Shia intellectual circle — operating in "
        "the ninth and tenth centuries. On this reconstruction, 'Jābir' is a pseudonymous authority "
        "figure attached to a collaborative scholarly project, much as the Hermetic Corpus was "
        "attributed to the legendary Hermes Trismegistus. The Jabirian corpus is thus not the "
        "work of an eighth-century court alchemist but the product of an intellectual tradition "
        "that accumulated texts over generations, retrospectively attributed to a revered founder.\n\n"

        "The corpus is organized into several major collections. The Seventy Books (Kitāb al-Sab'īn) "
        "is the most practically oriented collection, covering laboratory operations in detail. "
        "The One Hundred and Twelve Books (al-Mi'a wa-'ithnā 'ashar) address cosmology, "
        "natural philosophy, and the theory of the elixir. The Five Hundred Books expand the "
        "philosophical and cosmological scope further. The Books of the Balances (Kutub al-Mawāzīn) "
        "represent the most distinctive and philosophically ambitious strand of the corpus: they "
        "develop a theory of quantitative balance (mīzān) according to which all natural "
        "substances can be analyzed by means of a numerical system assigning quantities to each "
        "of the four Aristotelian qualities (hot, cold, wet, dry) at four degrees of intensity. "
        "This numerological approach to natural science — the idea that hidden quantitative "
        "ratios underlie all qualitative differences — is the Jabirian corpus's most original "
        "philosophical contribution, though it remained more influential as a programmatic vision "
        "than as a practical method.\n\n"

        "The alchemical theory of the corpus develops the sulphur-mercury theory of metal "
        "formation — the idea, probably derived from earlier Greek-Arabic sources, that all "
        "metals are composed of sulphur and mercury combined in varying degrees of purity. "
        "The elixir (iksīr, from which the word 'elixir' derives) acts by correcting the "
        "imbalanced proportions in base metals and bringing them to the perfection of gold. "
        "This framework was transmitted to Latin Europe through translations and became the "
        "theoretical foundation of medieval European alchemy. The practical laboratory content "
        "of the corpus — descriptions of distillation, calcination, sublimation, crystallization, "
        "and the preparation of acids and salts — is considerable and was taken seriously as "
        "practical chemistry by historians of science from the nineteenth century onward, "
        "though modern assessment is more cautious about separating genuine experimental "
        "observation from theoretical elaboration.\n\n"

        "The Latin 'Geber' is an entirely separate tradition. A body of sophisticated Latin "
        "alchemical texts circulated in medieval Europe under the name Geber and was assumed "
        "to be a translation of the Arabic Jābir. The most important of these is the Summa "
        "Perfectionis Magisterii (Sum of Perfection of the Mastery), one of the most widely "
        "read alchemical texts of the Latin Middle Ages and early modern period. William Newman's "
        "critical study The Summa Perfectionis of Pseudo-Geber (1991) conclusively demonstrated "
        "that this text was not a translation from Arabic but was composed in Latin, most "
        "probably by an Italian Franciscan named Paul of Taranto, in the late thirteenth century. "
        "Newman's identification — based on the survival of a parallel text explicitly attributed "
        "to Paul of Taranto — resolved a question that had been debated since the seventeenth "
        "century, when some scholars had already suspected the text was not genuinely Arabic.\n\n"

        "The Summa Perfectionis is notable for the clarity and coherence of its alchemical theory: "
        "it presents a corpuscular account of metal structure — the idea that metals are composed "
        "of minute particles of sulphur and mercury — that Newman has argued is an important "
        "precursor to the corpuscular and mechanical philosophies of the seventeenth century. "
        "The pseudo-Geber's corpuscular theory influenced Roger Bacon, and through Bacon and the "
        "Latin alchemical tradition, shaped the conceptual vocabulary available to early modern "
        "chemists. The text's attribution to 'Geber' gave it the authority of the legendary "
        "Arab master and ensured its wide circulation.\n\n"

        "The historiographical significance of the Jabir/Geber problem extends beyond the "
        "specific texts. It illustrates the systematic use of pseudonymous attribution in the "
        "construction of alchemical authority: both in Arabic (where the Ismaili corpus was "
        "attributed to a legendary founder) and in Latin (where a thirteenth-century Italian "
        "attached his work to an Arabian name), the prestige of a legendary past figure was "
        "mobilized to guarantee the credibility of new claims. The Jabirian corpus also "
        "demonstrates the complexity of Arabic-Latin transmission: what Europe received as "
        "'Geber' was not what the Arabic tradition had as 'Jābir,' and neither may bear "
        "any close relation to a historical eighth-century individual."
    ),
    'key_works': [
        "The Seventy Books (Kitāb al-Sab'īn; Arabic Jabirian corpus)",
        "The One Hundred and Twelve Books (al-Mi'a wa-'ithnā 'ashar; Arabic Jabirian corpus)",
        "The Books of the Balances (Kutub al-Mawāzīn; Arabic Jabirian corpus)",
        "Summa Perfectionis Magisterii (Latin pseudo-Geber; probably Paul of Taranto, c.13th century)",
        "Liber de Investigatione Perfectionis (Latin pseudo-Geber)"
    ]
}

# ── id=17: Pico della Mirandola ──────────────────────────────────────────────

updates[17] = {
    'essay': (
        "Giovanni Pico della Mirandola (1463–1494) was an Italian humanist philosopher born "
        "at Mirandola in the duchy of Ferrara, youngest son of the lord of that small territory. "
        "He studied canon law at Bologna, then philosophy at Ferrara, Padua (where he encountered "
        "Averroist Aristotelianism), and Paris (the centre of scholastic philosophy). He met "
        "Marsilio Ficino and Lorenzo de' Medici in Florence in 1484, entering the Platonic "
        "Academy circle that had made Florence the centre of humanist Neoplatonism. His short "
        "life — he died at thirty-one, probably from arsenic poisoning, though the circumstances "
        "were never conclusively established — was marked by extraordinary intellectual ambition "
        "and repeated controversy.\n\n"

        "The Conclusiones Nongentae (Nine Hundred Theses, 1486) represent Pico's most audacious "
        "project: a proposal to debate nine hundred propositions drawn from the entire range of "
        "philosophical and theological traditions — Aristotelian, Platonic, Arabic, Scholastic, "
        "Hermetic, Kabbalistic, Chaldean, Orphic, and others — at Rome, at his own expense, "
        "before all comers. The project's premise was the harmony and ultimate agreement of all "
        "these traditions: diverse philosophical vocabularies were, Pico argued, different "
        "languages for the same truths. The Church condemned thirteen of the theses as heretical "
        "or suspect; the proposed debate was prohibited; and Pico was briefly imprisoned in "
        "France before being released under Medici diplomatic pressure. The Conclusiones are "
        "a remarkable document for the history of syncretism: they include the first systematic "
        "use of Kabbalistic arguments by a Christian humanist, and their treatment of Hermes "
        "Trismegistus as a prisca theologia authority established a pattern that shaped "
        "Agrippa, Ficino's later work, and the entire tradition of Renaissance Hermeticism.\n\n"

        "The Oratio de Hominis Dignitate (Oration on the Dignity of Man, 1486) was written "
        "as the opening address for the planned disputation and was never delivered as such. "
        "It is Pico's most celebrated text, often described — with some anachronism — as the "
        "'manifesto of the Renaissance.' Its central passage advances a striking account of "
        "human nature: God, having completed creation, fashioned man without a fixed nature "
        "or place in the cosmic hierarchy, giving him instead the capacity to take on any "
        "nature he chose. Man is a 'chameleon,' neither beast nor angel but capable of becoming "
        "either, through the free cultivation of his own being. This account of human "
        "self-fashioning draws on Hermetic sources — particularly the Pimander of the Corpus "
        "Hermeticum — and on Neoplatonic ideas of the soul's capacity for ascent, but Pico "
        "gives it a distinctive voluntarist inflection: it is the will, not merely the intellect, "
        "that determines the soul's rank. The Oratio frames the philosophical disputation as "
        "itself an act of dignitas — the pursuit of wisdom as the highest exercise of human "
        "freedom.\n\n"

        "The Heptaplus (1489), a seven-fold commentary on the opening verses of Genesis, is "
        "Pico's most sustained demonstration of his syncretic interpretive method. He reads "
        "the creation narrative through seven lenses — the elemental, celestial, angelic, "
        "human, temporal, and other registers — showing how each level of the cosmos is "
        "reflected in every other, and how Mosaic scripture encodes the same cosmic truths "
        "that Platonic and Hermetic philosophy express in different vocabularies. The Kabbalistic "
        "readings of Hebrew letters and words are prominent: Pico treats the Kabbalistic "
        "interpretation of the divine name and the structure of the sefirot (the divine "
        "attributes in Kabbalistic cosmology) as confirmations of Christian Trinitarian theology. "
        "This 'Christian Kabbalah' — the appropriation of Jewish esoteric tradition to "
        "demonstrate Christian doctrine — became the model for Agrippa's third book, "
        "for Johannes Reuchlin's De Arte Cabalistica (1517), and for the entire subsequent "
        "tradition of Christian Kabbalistic writing.\n\n"

        "The De Ente et Uno (On Being and the One, 1491) is Pico's most technically "
        "philosophical work, addressing the relationship between Platonic and Aristotelian "
        "accounts of being and unity. It engages specifically with the question of whether "
        "Plato and Aristotle agree on first principles — Pico argues they do — and with the "
        "Neoplatonic doctrine of the One as beyond being. This text reflects Pico's continuing "
        "engagement with the technical problems of Neoplatonic metaphysics as a philosophical "
        "discipline, not merely as esoteric framework.\n\n"

        "Pico's significance for the history of esotericism is multiple. He established "
        "Christian Kabbalah as a serious intellectual tradition, creating a model of "
        "Kabbalistic-Christian synthesis that Agrippa systematized and that Rosicrucian "
        "writers invoked throughout the seventeenth century. His prisca theologia framework "
        "— the idea that all ancient philosophical and religious traditions encode a single "
        "primordial wisdom — underwrote the syncretic aspirations of Renaissance Hermeticism "
        "and shaped the self-understanding of later esoteric movements. His account of human "
        "self-fashioning in the Oratio provided a philosophical vocabulary for the idea of "
        "spiritual transformation as the human vocation — an idea central to alchemical "
        "spirituality in its many forms.\n\n"

        "The scholarly literature on Pico has been substantially shaped by debates about "
        "the coherence and sincerity of his syncretism. Frances Yates treated him as a "
        "central figure in the 'Hermetic tradition' she was tracing; Brian Vickers and "
        "Charles Schmitt raised questions about whether the Hermetic content of his work "
        "was as central as Yates claimed. More recent scholarship by Michael Allen, Brian "
        "Copenhaver, and Chaim Wirszubski (whose Pico della Mirandola's Encounter with "
        "Jewish Mysticism, 1989, is the definitive study of his Kabbalah) has provided more "
        "nuanced accounts. Pico's Kabbalistic learning was real: he worked with Flavius "
        "Mithridates, who translated Hebrew Kabbalistic texts for him, and the Conclusiones "
        "show genuine engagement with specific Kabbalistic sources, not mere gestures "
        "toward an exotic tradition. The question of what Pico understood himself to be "
        "doing — philosophical synthesis, theological apologetics, or something else — "
        "remains productively open."
    ),
    'key_works': [
        "Conclusiones Nongentae (Nine Hundred Theses, 1486)",
        "Oratio de Hominis Dignitate (Oration on the Dignity of Man, 1486)",
        "Heptaplus (Seven-fold Commentary on Genesis, 1489)",
        "De Ente et Uno (On Being and the One, 1491)",
        "Apologia (defence of the condemned theses, 1487)"
    ]
}

# ── APPLY ────────────────────────────────────────────────────────────────────

updated_ids = []
for fig in data['figures']:
    fid = fig['id']
    if fid in updates:
        old_len = len(fig.get('essay', ''))
        fig['essay'] = updates[fid]['essay']
        if 'key_works' in updates[fid]:
            fig['key_works'] = updates[fid]['key_works']
        new_len = len(fig['essay'])
        print(f"Updated id={fid}: {fig['name']} | {old_len} → {new_len} chars")
        updated_ids.append(fid)

missed = set(updates.keys()) - set(updated_ids)
if missed:
    print(f"WARNING: IDs not found: {missed}")

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nDone. Updated {len(updated_ids)} entries.")
