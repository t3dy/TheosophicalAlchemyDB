#!/usr/bin/env python3
"""
update_bios_batch2_part4.py
Full essays for: id=71 van Helmont, id=21 Aquinas, id=22 Roger Bacon, id=26 Gichtel.
"""

import json, os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prototype_data.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

updates = {}

# ── id=71: Jan Baptist van Helmont ──────────────────────────────────────────

updates[71] = {
    'essay': (
        "Jan Baptist van Helmont (1580–1644) was a Flemish physician, natural philosopher, "
        "and chemist whose Ortus Medicinae (Origin of Medicine, 1648) placed him at the "
        "intersection of Paracelsian iatrochemistry, the new mechanical philosophy, and "
        "empirical natural inquiry in a way that made him one of the most important "
        "transitional figures in the history of chemistry. Born at Brussels into a noble "
        "family, he studied medicine at Louvain, rejected the traditional Galenic curriculum "
        "he found there as insufficiently grounded in nature, and spent decades in private "
        "research at his estate at Vilvorde before his death in 1644. His son Franciscus "
        "Mercurius van Helmont edited and published his collected works posthumously.\n\n"

        "The Ortus Medicinae (1648), assembled from manuscripts by his son, is van Helmont's "
        "principal work and one of the most important scientific texts of the seventeenth "
        "century. It encompasses natural philosophy, medical theory, experimental results, "
        "polemical exchanges with Galenists and Paracelsians, and theological reflections "
        "in an unmethodical but energetic whole. Van Helmont's prose is dense, allusive, "
        "and organized around specific experimental findings rather than systematic "
        "exposition — a feature that made his texts demanding for contemporaries and "
        "has made them rewarding for historians of science.\n\n"

        "Van Helmont's most consequential contribution to the history of science is his "
        "identification and naming of 'gas.' The word is his coinage, derived, he explains, "
        "from the Greek 'chaos' — the formless, spaceless state of matter before "
        "organization. Van Helmont recognized that certain substances, when heated or "
        "fermented, emit vapors that are not ordinary steam or air but distinct material "
        "substances with definable properties. He identified 'gas sylvestre' (wild gas, "
        "now identified as carbon dioxide) produced by the fermentation of wine and the "
        "burning of charcoal; he described it as distinguishable from air because it "
        "extinguishes flames and cannot support respiration. He also distinguished other "
        "gases by different experimental behaviors. The conceptual breakthrough — that "
        "there are multiple distinct aerial substances rather than a single 'air' — "
        "was decisive for the subsequent development of pneumatic chemistry by Boyle, "
        "Mayow, Hales, and ultimately Lavoisier.\n\n"

        "Van Helmont's natural philosophy is built on two fundamental claims derived "
        "from his Paracelsian formation but developed in distinctive directions. First, "
        "water is the universal material substrate of all natural bodies: all things "
        "are ultimately reducible to water, which is transformed by seeds (semina, "
        "the active organizing principles in things) into specific substances. This "
        "water-monism revives the ancient Thalesian position, but van Helmont supports "
        "it with his famous willow-tree experiment: he planted a willow sapling weighing "
        "five pounds in two hundred pounds of carefully dried soil, watered it only "
        "with rainwater for five years, and found that the tree had gained over one "
        "hundred and sixty pounds while the soil had lost only a tiny fraction of its "
        "weight. He concluded — incorrectly, as later chemistry would show — that "
        "the tree's mass derived entirely from the water, not from the soil. The "
        "experiment is notable as an early controlled quantitative experiment in "
        "biology, even if its interpretation was wrong.\n\n"

        "Second, van Helmont's concept of the 'Archeus' (derived from Paracelsus but "
        "significantly reinterpreted) provides the active organizing principle at "
        "work in living bodies. The Archeus is a semi-material, vital principle "
        "governing the digestion, growth, and self-repair of the body; it operates "
        "through 'ferments' (ferments in his sense are specific active principles "
        "that direct chemical transformations, not merely yeast-like agents of "
        "fermentation). His account of digestion as a series of ferment-guided "
        "chemical transformations in the stomach, liver, and other organs was "
        "influential on later iatrochemistry and on Thomas Willis's chemical "
        "physiology. Van Helmont was also among the first to identify the "
        "stomach's role in acid digestion.\n\n"

        "Van Helmont's relationship to alchemy and esotericism is complex. He "
        "accepted the reality of transmutation — he claimed in the Ortus Medicinae "
        "to have performed a transmutation experiment using a tiny quantity of "
        "philosophers' stone given to him by an anonymous stranger, obtaining "
        "a significant quantity of gold. He was also a convinced Paracelsian in "
        "his rejection of Galenism, his emphasis on chemical medicine, and his "
        "vitalist natural philosophy. At the same time, he sharply criticized "
        "what he regarded as Paracelsus's excesses, particularly the astrological "
        "elements and the magical elaborations that accompanied Paracelsian "
        "medicine in many of its proponents. Van Helmont was a Catholic who "
        "experienced a significant mystical conversion in his youth and who "
        "sought to ground his natural philosophy in a Christian understanding "
        "of creation — the seed-concept and the Archeus are for him not "
        "magical but properly natural, reflecting God's ordering of creation.\n\n"

        "The transmission from van Helmont to Robert Boyle is crucial for "
        "understanding the emergence of chemistry from iatrochemistry. Boyle read "
        "van Helmont carefully, adopted his experimental style, engaged with his "
        "concept of distinct chemical substances, and built on his gas-experiments. "
        "The Sceptical Chymist (1661) is in part a response to van Helmontian "
        "claims: Boyle argues against van Helmont's water-monism while preserving "
        "his experimental approach. Van Helmont thus stands as the figure through "
        "whom Paracelsian chemistry was filtered and partially transformed into "
        "the experimental chemistry of the Royal Society generation."
    ),
    'key_works': [
        "Ortus Medicinae (Origin of Medicine, 1648; posthumously published by Franciscus Mercurius van Helmont)",
        "Opuscula Medica Inaudita (1644; published in his lifetime)",
        "De Magnetica Vulnerum Curatione (On the Magnetic Cure of Wounds)"
    ]
}

# ── id=21: Thomas Aquinas ────────────────────────────────────────────────────

updates[21] = {
    'essay': (
        "Thomas Aquinas (1225–1274) was an Italian Dominican friar, theologian, and "
        "philosopher whose systematic synthesis of Aristotelian natural philosophy with "
        "Christian theology established the dominant intellectual framework of Latin "
        "Scholasticism and shaped the intellectual context within which alchemy was "
        "discussed, debated, and legitimized throughout the later Middle Ages and Renaissance. "
        "Born at Roccasecca in the Kingdom of Sicily into a noble family (he was related "
        "to the Emperor Frederick II), he studied at the University of Naples, joined the "
        "Dominicans against his family's wishes, and studied under Albertus Magnus at "
        "Cologne and Paris. He taught at Paris and at several Italian studia before his "
        "death at Fossanova in 1274, called to the Council of Lyon. Canonized in 1323, "
        "declared Doctor of the Church, and made the official theologian of the Catholic "
        "Church by Leo XIII in 1879.\n\n"

        "The Summa Theologiae (Summa of Theology, begun 1265, incomplete at his death; "
        "the Third Part on the Incarnation and sacraments was left unfinished and "
        "completed by a Supplement drawn from his earlier Scriptum on the Sentences) "
        "is Thomas's greatest synthetic achievement and one of the most ambitious "
        "intellectual projects of the medieval West. Organized as a series of "
        "questions, objections, replies, and answers (the quaestio format inherited "
        "from Scholastic disputation), it covers in sequence God's existence and "
        "nature, creation and angels, human nature and ethics, law and grace, "
        "the Incarnation, and the sacraments. The text integrates Aristotelian "
        "natural philosophy at every level: Aristotle's account of matter and "
        "form (hylomorphism), his category of substance, his four causes, and "
        "his psychology of intellect and will are all absorbed and theologized "
        "within a Christian framework.\n\n"

        "The Summa contra Gentiles (Against the Pagans, 1259–65) is a philosophical- "
        "theological argument for Christian doctrine addressed, at least in its "
        "literary fiction, to non-Christians: infidels, Muslims, and pagans who "
        "do not accept scriptural revelation and must be addressed on natural "
        "rational grounds. It proceeds from what reason can establish about God "
        "and creation to the specifically Christian doctrines (Trinity, Incarnation) "
        "that surpass reason. This text gives Thomas's philosophical theology its "
        "most sustained independent expression, without the pedagogical question- "
        "and-answer structure of the Summa Theologiae.\n\n"

        "For the history of alchemy, Thomas's significance operates on two levels. "
        "First, his Aristotelian natural philosophy provided the conceptual framework "
        "within which alchemical theory was articulated and defended. The hylomorphic "
        "account of substance — matter and form as the two principles of every "
        "physical body — underpinned the alchemical question of whether artificial "
        "transmutation was possible: if the form of gold could be induced in a base "
        "metal through the right manipulation of its matter, transmutation was "
        "theoretically possible within Aristotelian natural philosophy. Thomas himself "
        "addressed this question in the Summa Theologiae (I.117.3) and in the "
        "Commentary on Aristotle's Meteorologica, concluding that while natural "
        "transmutation was philosophically coherent, he doubted whether practitioners "
        "had actually produced gold indistinguishable from the natural product. His "
        "position — theoretical possibility plus practical skepticism — was the "
        "standard Scholastic position and was cited by both defenders and critics "
        "of alchemy throughout the later Middle Ages.\n\n"

        "Second, a substantial corpus of alchemical texts circulated under Thomas's "
        "name, adding his authority to the tradition. The Aurora Consurgens, a "
        "striking allegorical text that opens with a woman speaking in the voice "
        "of Lady Wisdom from the Book of Proverbs and develops an allegorical "
        "account of the philosophers' stone, was long attributed to Thomas and "
        "believed to represent his deathbed conversion to alchemical wisdom. "
        "Marie-Louise von Franz produced an influential Jungian study of the "
        "Aurora Consurgens (1966), arguing for its attribution to Thomas and "
        "reading it as evidence of his psychology's 'alchemical' dimension. "
        "Modern scholarship has largely rejected the attribution: Barbara "
        "Obrist and others have argued that the text is a later pseudonymous "
        "composition, and there is no contemporary evidence connecting it to "
        "Thomas. Several shorter alchemical texts (De Alchimia, Thesaurus "
        "Alchimiae) also circulated under his name; these are almost "
        "certainly pseudonymous.\n\n"

        "The pattern is familiar from the study of Albertus Magnus and Roger "
        "Bacon: the most prestigious names in Scholastic natural philosophy "
        "were systematically attached to alchemical texts that those figures "
        "did not write, because their authority lent credibility to the claims "
        "being made. Thomas's name was particularly valuable because he was both "
        "the greatest Aristotelian theologian and the most orthodox of the major "
        "Schoolmen: an alchemical text attributed to him could not easily be "
        "dismissed as heretical speculation. The pseudo-Thomist alchemical corpus "
        "exploited this combination of philosophical authority and theological "
        "orthodoxy to position alchemy within the mainstream of Catholic "
        "intellectual culture."
    ),
    'key_works': [
        "Summa Theologiae (begun 1265, incomplete at death; completed by Supplement)",
        "Summa contra Gentiles (1259–65)",
        "Commentary on Aristotle's Meteorologica",
        "Aurora Consurgens (attributed; almost certainly pseudonymous)",
        "De Alchimia (attributed; pseudonymous)"
    ]
}

# ── id=22: Roger Bacon ──────────────────────────────────────────────────────

updates[22] = {
    'essay': (
        "Roger Bacon (c.1214/1220–c.1292) was an English Franciscan friar and natural "
        "philosopher whose arguments for reformed, experience-based learning made him "
        "one of the most celebrated — and most mythologized — figures in the history "
        "of medieval science. Born probably in Somerset, he studied at Oxford and Paris, "
        "where he lectured on Aristotle's natural works; he joined the Franciscans, probably "
        "in the 1250s, and spent much of his subsequent career at Oxford. His relationship "
        "with the Franciscan order was troubled: he was reportedly placed under some form "
        "of constraint in Paris, possibly for his controversial views, and he appealed "
        "directly to Pope Clement IV (1265–68), producing for him the Opus Majus and "
        "companion works. He was reportedly imprisoned again in the 1270s under the "
        "minister-general of the Franciscans for 'suspect novelties.'\n\n"

        "The Opus Majus (Greater Work, 1267) is Bacon's principal treatise and was "
        "composed as a systematic argument, addressed to Clement IV, for the reform "
        "of university learning through the recovery of mathematical and linguistic "
        "foundations and the emphasis on 'experience' (experimentum). The work is "
        "encyclopedic in scope: it covers the causes of human error (the 'four causes "
        "of error' — authority, custom, popular opinion, and false conceit of knowledge), "
        "the relations between philosophy and theology, mathematics (including optics "
        "and its theological applications), experimental science, moral philosophy, and "
        "the languages necessary for scriptural scholarship. The sections on optics "
        "(perspectiva) are among the most substantial medieval contributions to that "
        "field, drawing on Alhazen (Ibn al-Haytham) and advancing accounts of the "
        "rainbow, burning mirrors, and vision. The Opus Minus and Opus Tertium were "
        "companion texts summarizing and supplementing the Opus Majus.\n\n"

        "Bacon's concept of 'experimental science' (scientia experimentalis) in the "
        "Opus Majus has attracted sustained scholarly attention. His argument is not "
        "for experiment in the modern sense — controlled, repeatable testing of "
        "hypotheses — but for a privileged form of knowledge that supplements "
        "rational demonstration through direct acquaintance with particulars. "
        "Experience includes both ordinary sensory experience and the extraordinary "
        "experience of spiritual illumination; Bacon does not cleanly separate "
        "empirical and mystical registers. His invocation of 'experience' was "
        "nonetheless cited by later historians — particularly by Francis Bacon "
        "(no relation) and by nineteenth-century historians of science — as "
        "evidence that Roger Bacon was a precursor of the experimental method, "
        "a reading that has been contested by more recent scholarship.\n\n"

        "For the history of alchemy, Bacon's significance is primarily a matter of "
        "his reputation and the texts attributed to him rather than his own "
        "genuine alchemical writing. Several major alchemical texts circulated "
        "widely under his name. The Speculum Alchimiae (Mirror of Alchemy) is "
        "a systematic and clearly written introduction to alchemical theory — "
        "it explains the sulphur-mercury theory of metal formation, describes "
        "the nature of the philosophers' stone, and outlines the laboratory "
        "operations of the Great Work — that was widely attributed to Bacon "
        "and printed in multiple editions from the late fifteenth century onward. "
        "Modern scholarship regards it as pseudonymous; the question of when "
        "and by whom it was composed has not been definitively resolved.\n\n"

        "The Epistola de Secretis Operibus Artis et Naturae et de Nullitate Magiae "
        "(Letter on the Secret Works of Art and Nature and on the Nullity of Magic) "
        "is another widely circulated text under Bacon's name that discusses "
        "mechanical wonders (flying machines, self-propelled ships, submarines), "
        "optical illusions, and the boundary between natural magic and demonic "
        "magic. This text contributed substantially to the legend of Bacon as an "
        "arch-magician and inventor of mechanical marvels — the 'brazen head' "
        "that could answer any question was already attributed to him in the "
        "thirteenth century — and shaped his popular reputation through the "
        "early modern period. Robert Greene's play Friar Bacon and Friar Bungay "
        "(c.1589) dramatizes this legend.\n\n"

        "Bacon's genuine works do engage with alchemy. In the Opus Majus and the "
        "Opus Tertium he discusses alchemy as a legitimate branch of natural "
        "philosophy concerned with the transformation of substances, and he "
        "mentions the possibility of preparing medicines from gold. He was "
        "familiar with the major Arabic alchemical sources, including the "
        "Jabirian corpus and al-Rāzī, and his natural philosophy provided "
        "a framework within which alchemical transformation could be understood "
        "as genuinely natural rather than demonic. The distinction — crucial "
        "to the acceptability of alchemy in a Christian intellectual culture — "
        "between natural transformation (which operates through hidden but real "
        "natural causes) and demonic illusion (which produces apparent but "
        "unreal changes) is one Bacon made carefully.\n\n"

        "The myth of Bacon as magician and inventor of marvels — constructed "
        "primarily from pseudonymous texts and popular legend — was enormously "
        "influential on how early modern readers understood the relationship "
        "between natural magic, technology, and secret knowledge. The figure "
        "of 'Friar Bacon' offered a model of the scholar who, through mastery "
        "of natural causes, could produce effects indistinguishable from miracles "
        "— a model that would recur in the self-presentations of Renaissance "
        "natural magicians and in the utopian techno-scientific visions of the "
        "seventeenth century."
    ),
    'key_works': [
        "Opus Majus (Greater Work, 1267)",
        "Opus Minus (Lesser Work, 1267)",
        "Opus Tertium (Third Work, 1267)",
        "Speculum Alchimiae (Mirror of Alchemy; attributed, probably pseudonymous)",
        "Epistola de Secretis Operibus Artis et Naturae (attributed; authenticity debated)"
    ]
}

# ── id=26: Johann Georg Gichtel ─────────────────────────────────────────────

updates[26] = {
    'essay': (
        "Johann Georg Gichtel (1638–1710) was a German Protestant mystic, Böhmist "
        "theologian, and the most important early editor of Jacob Böhme's writings. "
        "Born at Regensburg into a Lutheran family, he studied law, but an intense "
        "religious crisis in the 1660s led him to abandon his legal career and seek "
        "a more radical spiritual life. After contact with the Labadist movement and "
        "the beginnings of his engagement with Böhme's writings, he settled permanently "
        "in Amsterdam in 1668, where he spent the rest of his long life in voluntary "
        "poverty, celibacy, and intensive spiritual practice.\n\n"

        "Gichtel's most consequential contribution to the history of esotericism is "
        "his editorial work on Jacob Böhme. The collected works of Böhme had "
        "circulated in manuscript and in scattered publications since the 1620s, "
        "but they lacked a systematic, comprehensive edition. Gichtel produced the "
        "first major collected edition of Böhme's works in Amsterdam in 1682 "
        "(under the title Theosophia Revelata or similar), and an expanded second "
        "edition in 1715, which is generally referred to as the 'Gichtel edition' "
        "and remained the standard edition of Böhme into the nineteenth century. "
        "This editorial work was not merely bibliographic: Gichtel brought to it "
        "a deep personal familiarity with Böhme's thought, and the edition shaped "
        "how subsequent generations read Böhme — in Germany, England, and the "
        "Netherlands. The English translations of Böhme from the 1640s–1660s "
        "had made him known in Britain; the Gichtel edition provided the "
        "authoritative German text from which later translations proceeded.\n\n"

        "Gichtel's own primary work, Theosophia Practica (1696; expanded posthumous "
        "edition, 1722), is a collection of spiritual letters addressed to his "
        "correspondents and disciples across Germany and the Netherlands. It is "
        "organized as a practical guide to Böhmian inner Christianity: the soul's "
        "fall into the material world, the stages of purification through spiritual "
        "combat, the regeneration of the inner image of God, and the final "
        "transformation of the earthly into the celestial body. The letters are "
        "characterized by intense personal engagement — Gichtel describes his own "
        "spiritual struggles and experiences with unusual directness — and by a "
        "practical, non-academic register quite different from Böhme's speculative "
        "theosophy.\n\n"

        "The Theosophia Practica is most famous for its anatomical diagrams: "
        "remarkable images showing the human body with the seven planetary centers "
        "(Seelencentra or Geistescentra) marked at specific locations — from the "
        "crown of the head (Saturn) through the brow (Jupiter), throat (Mars), "
        "heart (Sun), solar plexus (Venus), spleen or genitals (Mercury), and "
        "base (Moon). These diagrams provide a visual map of Böhme's theosophy: "
        "the seven planets correspond to the seven properties of divine nature "
        "(the 'seven spirits of God') that Böhme identified in his cosmological "
        "works, and each planetary center in the body is associated with a "
        "spiritual quality that must be purified in the course of inner "
        "transformation. The diagrams are among the earliest examples of a "
        "systematic chakra-like mapping of spiritual centers onto the human body "
        "in the Western esoteric tradition, though they derive from Böhmian "
        "planetary theology rather than from any Hindu or Buddhist source.\n\n"

        "Gichtel founded the community known as the 'Angel Brethren' (Engelsbrüder) "
        "in Amsterdam — a small circle of men and women committed to Böhmian "
        "theosophy and to celibacy as a spiritual discipline. Gichtel's insistence "
        "on celibacy was total: he regarded marriage as a sign of the fallen, "
        "material condition and saw sexual abstinence as a precondition for the "
        "regeneration of the spiritual body. This position put him at odds with "
        "most Protestant theology, which regarded marriage as honorable and "
        "celibacy as a Catholic deviation; Gichtel defended his position through "
        "a Böhmian anthropology in which the original Adam was androgynous and "
        "the division into sexes was itself a mark of the Fall.\n\n"

        "Gichtel's network extended beyond Amsterdam through an extensive "
        "correspondence — the Theosophia Practica preserves hundreds of letters "
        "— that connected him to Böhmists in Germany, Switzerland, and England. "
        "His influence on the English transmission is significant: the Philadelphian "
        "Society of Jane Lead and John Pordage, founded in London in 1694, was "
        "in contact with Gichtel's circle, and the cross-fertilization between "
        "Dutch Böhmism and English Behmenism shaped both traditions. Gichtel's "
        "edition of Böhme's works was the primary text used by English readers "
        "who did not have access to the earlier English translations. Through "
        "Gichtel, Böhmian theosophy entered the Dutch Collegiant and Mennonite "
        "milieu and fed into the Pietist currents of the late seventeenth and "
        "early eighteenth centuries in Germany and Scandinavia.\n\n"

        "For the history of spiritual alchemy, Gichtel represents the first "
        "systematic attempt to map Böhme's vocabulary onto the human body as "
        "a site of spiritual transformation. The planetary centers in the "
        "Theosophia Practica diagrams connect to the alchemical planetary "
        "symbolism (each planet associated with a metal, a bodily organ, and "
        "a spiritual quality) in ways that subsequent readers — including "
        "the nineteenth-century theosophists — would develop into more "
        "explicit spiritual alchemy. The Gichtel edition of Böhme, by making "
        "his works systematically accessible, also made available the "
        "vocabulary of the nigredo (the dark night of the soul), the "
        "albedo (illumination), and the rubedo (union) that alchemical "
        "readers found in Böhme's accounts of spiritual transformation."
    ),
    'key_works': [
        "Theosophia Practica (1696; expanded posthumous edition 1722)",
        "Edition of Jacob Böhme's collected works (Amsterdam, 1682; second edition 1715)",
        "Extensive correspondence (preserved in Theosophia Practica)"
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
