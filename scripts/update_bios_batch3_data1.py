"""
Batch 3 bio updates — Part 1: id=64, 20, 54, 55, 91 (redirect/stubs + ancient figures)
"""

UPDATES = {}

# id=64: Paracelsus duplicate — redirect stub
UPDATES[64] = {
    "essay": (
        "This entry is a stub duplicating the main Paracelsus (id=4) biography. "
        "See the full entry for Theophrastus Bombastus von Hohenheim (1493–1541) "
        "covering his Paragranum, Archidoxies, iatrochemistry, Reformation context, "
        "and transmission. [Pending deduplication]"
    ),
    "key_works": ["See id=4 (Paracelsus)"]
}

# id=91: Johann Arndt duplicate — redirect stub
UPDATES[91] = {
    "essay": (
        "This entry is a stub duplicating the main Johann Arndt (id=45) biography. "
        "See the full entry for Johann Arndt (1555–1621) covering his Vier Bücher vom wahren "
        "Christentum, Paradiesgärtlein, his influence on Lutheran Pietism, and his transmission "
        "of medieval mysticism into Protestant spirituality. [Pending deduplication]"
    ),
    "key_works": ["See id=45 (Johann Arndt)"]
}

# id=20: Hermes Trismegistus
UPDATES[20] = {
    "essay": (
        "Hermes Trismegistus — 'Thrice-Greatest Hermes' — is the legendary sage to whom "
        "antiquity and the Renaissance attributed a vast body of theological, philosophical, "
        "and technical wisdom. The name fuses the Greek god Hermes with the Egyptian god "
        "Thoth, both patrons of writing, measurement, and esoteric knowledge. In the "
        "Neoplatonic and early Christian milieu of the first through third centuries CE, "
        "the composite figure of Hermes Trismegistus became the supposed author of texts "
        "believed to preserve the most ancient human wisdom — a prisca theologia (ancient "
        "theology) predating even Moses and Plato.\n\n"

        "The Hermetic corpus as we have it consists of several textual clusters. The Corpus "
        "Hermeticum is a collection of seventeen Greek dialogues, the most important of which "
        "is the Poimandres (Tractate I), in which the divine Nous (Mind) appears to Hermes "
        "in a vision and reveals the creation of the cosmos, the fall of the soul into matter, "
        "and the soul's path of ascent back to the divine pleroma. The cosmogony is Platonic "
        "in structure but inflected with Gnostic themes: the soul descends through the planetary "
        "spheres, acquiring the characteristics of each, and must shed these garments on its "
        "return. The Poimandres established the template for all later hermetic soteriology — "
        "the conviction that knowledge (gnosis) of the cosmos and of the self constitutes the "
        "vehicle of spiritual liberation. Marsilio Ficino translated the Corpus Hermeticum into "
        "Latin in 1463, producing the Pimander, which circulated widely and shaped Renaissance "
        "Neoplatonism.\n\n"

        "The Asclepius (preserved in Latin, probably translated in late antiquity) is a dialogue "
        "between Hermes and his disciple Asclepius on cosmic sympathy, theurgy, and the animation "
        "of statues. Its famous passage on Egypt as the 'temple of the whole world' — and the "
        "lamentation that this wisdom will perish — became a touchstone for Renaissance thinkers "
        "who felt themselves living in a time of spiritual decline. The Asclepius's account of "
        "how priests could draw divine powers into cult statues through herbs, stones, and ritual "
        "became the basis for Renaissance discussions of natural magic and talismanic practice. "
        "Ficino's De Vita Coelitus Comparanda (1489) drew heavily on this model.\n\n"

        "The Emerald Tablet (Tabula Smaragdina) is a short, cryptic text of Arabic origin "
        "(earliest known version in an eighth- or ninth-century Arabic source, the Kitab Sirr "
        "al-Khaliqah attributed to Apollonius of Tyana), which circulated in Latin translation "
        "from the twelfth century. Its famous opening — 'As above, so below' (ut quod est "
        "inferius est sicut quod est superius) — condensed the hermetic principle of cosmic "
        "correspondence into a phrase that became the motto of alchemical philosophy. The "
        "Emerald Tablet's seven or fourteen operations were interpreted as describing both "
        "the laboratory operations of the Great Work and the soul's spiritual ascent. Every "
        "major alchemical author from Roger Bacon through Newton commented on or alluded to "
        "it. Newton's own manuscript commentary on the Emerald Tablet survives in the Keynes "
        "Collection at King's College, Cambridge.\n\n"

        "The philosophical tradition attributed to Hermes also includes the Stobaean excerpts "
        "(passages preserved by the fifth-century anthologist Stobaeus), the Definitions of "
        "Hermes Trismegistus to Asclepius (preserved in Armenian), and various technical Hermetica "
        "on astrology, alchemy, and magic. This technical material — sometimes called the 'popular' "
        "Hermetica as opposed to the 'philosophical' Hermetica of the Corpus Hermeticum — shows "
        "Hermetism as a broad intellectual culture rather than a single school.\n\n"

        "The chronological authority of the Hermetic corpus rested on the assumption, accepted "
        "from Lactantius and Augustine through the Renaissance, that Hermes Trismegistus was "
        "a real Egyptian sage who lived before Moses, and whose writings preserved primordial "
        "wisdom. Isaac Casaubon's philological analysis of 1614 (De Rebus Sacris et "
        "Ecclesiasticis Exercitationes XVI) demonstrated on the basis of linguistic and "
        "conceptual evidence that the Corpus Hermeticum was not of ancient Egyptian origin "
        "but was composed in the early centuries CE, heavily influenced by Platonism and early "
        "Christianity. This was a significant intellectual event, though its practical impact "
        "on the Hermetic tradition was slower than sometimes assumed. Robert Fludd continued "
        "to deploy Hermetic texts as ancient authority well into the 1620s; the tradition had "
        "an internal coherence that did not depend entirely on chronological priority.\n\n"

        "Modern scholarship has substantially revised the older picture — associated above all "
        "with Frances Yates's Giordano Bruno and the Hermetic Tradition (1964) — of Hermetism "
        "as a unified 'Hermetic tradition' that drove the Scientific Revolution. Brian Vickers, "
        "Wouter Hanegraaff, and Florian Ebeling have all contributed to a more nuanced account. "
        "The current consensus, represented by Hanegraaff's work and the critical edition of "
        "the Corpus Hermeticum by Nock and Festugière (1945–54), treats the Hermetic texts as "
        "a diverse body of Greco-Egyptian religious philosophy of the first through third "
        "centuries, valuable for understanding the religious pluralism of the Roman Empire "
        "and the subsequent history of esotericism, but not requiring claims about either "
        "Egyptian antiquity or proto-scientific content.\n\n"

        "Hermes Trismegistus functions in the Western esoteric tradition less as a historical "
        "individual than as an authority-figure and a symbol of the claim that esoteric wisdom "
        "is ancient, universal, and cross-cultural. His name appears on the title pages of "
        "alchemical texts from the medieval period through the eighteenth century. The "
        "Rosicrucian manifestos invoked the Hermetic tradition as background; Michael Maier's "
        "emblematic works are saturated with Hermetic reference; the Fama Fraternitatis itself "
        "describes Christian Rosenkreutz's journey to the East as a kind of Hermetic initiation. "
        "In this sense the figure of Hermes Trismegistus is constitutive of the entire tradition "
        "this database documents."
    ),
    "key_works": [
        "Corpus Hermeticum (Poimandres and sixteen further tractates, Greek, c. 1st–3rd century CE)",
        "Asclepius (Latin, probably translated late antiquity; dialogue on cosmic sympathy and theurgy)",
        "Emerald Tablet / Tabula Smaragdina (Arabic origin c. 8th–9th century CE; Latin from 12th century)",
        "Stobaean Excerpts (passages in Stobaeus's Anthologium, 5th century)",
        "Definitions of Hermes Trismegistus to Asclepius (Armenian version)"
    ]
}

# id=54: Zosimos of Panopolis
UPDATES[54] = {
    "essay": (
        "Zosimos of Panopolis (fl. c. 300 CE) is the earliest surviving named author in the "
        "alchemical tradition, working in the city of Panopolis (modern Akhmim) in the Egyptian "
        "Thebaid. His texts, preserved in Greek manuscripts and in Syriac translation, constitute "
        "what scholars call the Zosimean Corpus — a substantial though fragmentary body of writings "
        "that combines practical laboratory instructions with philosophical and theological "
        "interpretation of unusual depth. Zosimos stands at the convergence of several intellectual "
        "traditions: Hellenistic natural philosophy, Gnostic cosmology, Egyptian priestly knowledge, "
        "and the practical craft traditions of the dyer and metalworker. His work is foundational "
        "not because he invented alchemy but because he gave it its first sustained theoretical "
        "articulation.\n\n"

        "On the Letter Omega (Peri tou omega) is his most celebrated text and one of the most "
        "remarkable documents in the history of esoteric literature. Structured as a letter to "
        "his sister or student Theosebeia, it contains an extended visionary sequence in which "
        "Zosimos dreams of a sacrificial priest who stands atop a bowl-shaped altar. The priest "
        "announces that he is undergoing a voluntary transformation: his flesh is being stripped "
        "away, his eyes gouged out, his body dissolved in boiling water — all operations that "
        "Zosimos immediately identifies with the transformations of metals in the alchemical "
        "vessel. The priest becomes in sequence each of the officiants of the rite, each "
        "suffering the same dissolution. The dream sequence has been interpreted variously as "
        "a Gnostic initiation narrative, a reflection on the violence inherent in metallurgical "
        "transformation, and a description of the spiritual death required before rebirth. "
        "Michèle Mertens's critical edition (Zosime de Panopolis: Mémoires authentiques, 1995) "
        "remains the standard scholarly resource.\n\n"

        "The Authentic Commentaries (also called the Cheirokmeta, meaning 'things made by hand') "
        "are a series of practical and philosophical notes on alchemical operations, apparatus, "
        "and the interpretation of earlier authorities. Here Zosimos criticizes what he calls "
        "'dyers' — practitioners who seek merely to deceive buyers with colored metals rather "
        "than to achieve true transformation — and draws a sharp distinction between the "
        "superficial imitation of gold and the real philosophical work. This distinction "
        "between tincturing-as-deception and transformation-as-truth runs through the entire "
        "subsequent alchemical tradition.\n\n"

        "On Apparatus and Furnaces describes the physical equipment of the alchemical laboratory "
        "in considerable detail: stills (bikos), water baths (kerotakis), distillation vessels, "
        "and the various operations of sublimation, distillation, and calcination. Zosimos is "
        "the first author to systematically describe laboratory apparatus, and his descriptions "
        "have allowed historians of chemistry to partially reconstruct the technical environment "
        "of Hellenistic alchemy. The kerotakis — a reflux device for exposing metals to sulfurous "
        "vapors — appears repeatedly in his writing and is sometimes named after him in "
        "scholarship, though the attribution is approximate.\n\n"

        "Philosophically, Zosimos operates within a broadly Gnostic framework. He refers to "
        "the Gnostic concept of the archons — planetary rulers who imprison the soul in matter — "
        "and interprets the alchemical work as a means of liberating the spiritual principle "
        "from material bondage. His distinction between the 'tinctures of the soul' and material "
        "operations — the former concerning spiritual liberation, the latter concerning metallic "
        "transformation — anticipates the entire subsequent debate in alchemy between 'spiritual' "
        "and 'material' interpretations of the Great Work. David Brakke's work on Gnostic "
        "contexts illuminates how Zosimos's demonology and cosmology fit within the broader "
        "Gnostic religious environment of Roman Egypt.\n\n"

        "Zosimos also preserves and transmits earlier material, citing and commenting on texts "
        "attributed to 'Democritus' (almost certainly the Pseudo-Democritus of the alchemical "
        "tradition rather than the Presocratic philosopher) and 'Maria the Prophetess' (Maria "
        "Hebraea), who appears in his texts as a foundational authority, famous for the "
        "dictum that 'one becomes two, two becomes three, and from the third comes the one as "
        "the fourth.' Maria is credited with the invention of the bain-marie (water bath for "
        "controlled heating) and various distillation apparatuses; Zosimos's testimony is the "
        "primary evidence for her existence and importance.\n\n"

        "The transmission of Zosimos's texts is complex. The Greek manuscripts survive primarily "
        "in Byzantine collections, most importantly the Marcianus graecus 299 (11th century). "
        "Syriac translations preserve additional material. The tenth-century Arabic encyclopedia "
        "of the Ikhwan al-Safa (Brethren of Purity) shows awareness of Zosimean-type materials, "
        "suggesting transmission into the Arabic alchemical tradition that would eventually "
        "produce Jabir ibn Hayyan and the vast corpus of Arabic alchemy. The degree of direct "
        "textual transmission versus parallel development remains a matter of scholarly debate.\n\n"

        "For the history of Western alchemy, Zosimos matters because his work established the "
        "template of the alchemical text as simultaneously practical, philosophical, and "
        "visionary. His laboratory descriptions are grounded in real materials and operations; "
        "his philosophical framework is sophisticated and internally coherent; his visionary "
        "writing anticipates the emblem tradition and the dream-vision literature of medieval "
        "alchemy. The Ripley Scrolls, the Rosarium Philosophorum, and the Mutus Liber all "
        "draw, however indirectly, on the tradition Zosimos inaugurated: that the operations "
        "performed on metals in the vessel are simultaneously, and without contradiction, "
        "operations performed on the soul of the practitioner."
    ),
    "key_works": [
        "On the Letter Omega (Peri tou omega) — visionary treatise on sacrifice, transformation, and the alchemical dream",
        "Authentic Commentaries (Cheirokmeta) — practical and philosophical notes on operations and earlier authorities",
        "On Apparatus and Furnaces — technical descriptions of laboratory equipment including the kerotakis and bikos",
        "On Virtue — philosophical treatise on the ethics of alchemical practice"
    ]
}

# id=55: Arnau de Vilanova
UPDATES[55] = {
    "essay": (
        "Arnau de Vilanova (c.1240–1311) — also written Arnauld de Villeneuve in French, "
        "Arnaldus de Villanova in Latin — was a Catalan physician, theologian, and court "
        "advisor whose prolific career at the intersection of medicine, eschatology, and "
        "natural philosophy made him one of the most controversial intellectuals of the "
        "medieval Mediterranean. He served as physician to kings of Aragon and to several "
        "popes, taught medicine at Montpellier, and wrote theological treatises so radical "
        "that he was condemned by the Paris theology faculty and narrowly escaped Inquisitorial "
        "proceedings. After his death, his name was attached to a vast body of alchemical "
        "pseudepigrapha that profoundly shaped the late medieval and Renaissance alchemical "
        "tradition — though almost none of this material is genuinely his.\n\n"

        "This entry concerns the historical Arnau and should be distinguished from id=98 "
        "(the Pseudo-Arnaldian alchemical corpus), which treats the extensive body of texts "
        "written under his name.\n\n"

        "Arnau's genuine medical works are substantial and significant. The Speculum Medicinae "
        "(Mirror of Medicine) is a systematic medical compendium organized according to Galenic "
        "principles, covering physiology, pathology, and therapeutics; it was a standard "
        "teaching text at Montpellier for generations. The Regimen Sanitatis ad Regem Aragonum "
        "(Regiment of Health for the King of Aragon, written c.1305–08 for James II) is a "
        "practical health guide addressing diet, sleep, exercise, and seasonal regimen; it "
        "circulated enormously and was translated into Catalan, French, Hebrew, and other "
        "languages. The Aphorismi de Gradibus (Aphorisms on Degrees) is a technical work on "
        "pharmaceutical compounding that applied mathematical reasoning to the question of how "
        "the qualities (hot, cold, wet, dry) of medicines compound when ingredients are mixed "
        "— a sophisticated attempt to rationalize pharmacy within the Galenic framework. Michael "
        "McVaugh's studies of Arnau's medical work within the broader context of Montpellier "
        "medicine in the thirteenth century are the standard modern resource.\n\n"

        "Arnau's theological writings were inflammatory. De Adventu Antichristi (On the Coming "
        "of Antichrist, c.1297–1300) predicted the end of the world and the coming of Antichrist "
        "within a specific timeframe based on numerological analysis of the Book of Daniel; it "
        "was condemned by the Paris theology faculty in 1300. Arnau appealed to Pope Boniface "
        "VIII, who — perhaps aware of the political usefulness of having the physician of the "
        "Crown of Aragon in his debt — treated him leniently. His subsequent theological "
        "treatises, written under the influence of the Franciscan Spiritual wing and their "
        "Joachimite apocalypticism, continued to generate controversy. He identified with "
        "persecuted poverty-advocates and wrote against Dominican theological hegemony.\n\n"

        "Arnau's documented interest in alchemy is genuine but limited. A letter attributed "
        "to him on the philosopher's stone, addressed to Pope Boniface VIII, circulated widely "
        "and helped anchor the association of his name with alchemical authority. His Epistola "
        "de Sanguine Humano and several medical works show familiarity with distillation and "
        "with the preparation of medicinal compounds using processes that overlap with alchemical "
        "technique. However, the claim that Arnau was a practicing transmutational alchemist "
        "rests almost entirely on the pseudepigraphical corpus rather than on documented evidence "
        "about his actual practice.\n\n"

        "The confusion between the historical Arnau and the Pseudo-Arnaldian corpus is itself "
        "historically significant. From the fourteenth century onward, Arnau's name was attached "
        "to texts including the Rosarium Philosophorum (Rose Garden of the Philosophers), one "
        "of the most important alchemical texts of the late medieval period, and numerous other "
        "treatises on the philosopher's stone, the quintessence, and vegetable and mineral "
        "remedies. The sheer volume of this pseudepigraphical production testifies to the "
        "authority his name carried: a physician of known brilliance, theological boldness, "
        "and royal connection made an ideal patron for texts that needed to claim learned "
        "medical-philosophical credentials. The Pseudo-Arnaldian corpus was still being printed "
        "and cited as authoritative in the sixteenth and seventeenth centuries."
    ),
    "key_works": [
        "Speculum Medicinae — systematic Galenic medical compendium, standard Montpellier teaching text",
        "Regimen Sanitatis ad Regem Aragonum (c.1305–08) — practical health guide for James II of Aragon; widely translated",
        "Aphorismi de Gradibus — mathematical treatment of pharmaceutical compounding and degree theory",
        "De Adventu Antichristi (c.1297–1300) — eschatological treatise predicting Antichrist's coming; condemned in Paris",
        "Epistola de Sanguine Humano — letter on human blood with alchemical-medical implications"
    ]
}
