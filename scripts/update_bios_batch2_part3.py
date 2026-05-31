#!/usr/bin/env python3
"""
update_bios_batch2_part3.py
Full essays for: id=23 Plotinus, id=8 Eckartshausen, id=41 Atwood, id=47 Newton.
"""

import json, os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prototype_data.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

updates = {}

# ── id=23: Plotinus ──────────────────────────────────────────────────────────

updates[23] = {
    'essay': (
        "Plotinus (204/5–270 CE) was the founder of Neoplatonism and, through his student "
        "Porphyry's editorial work, the author of the Enneads — the foundational text of the "
        "tradition that shaped late antique philosophy, Christian and Islamic theology, and "
        "the entire downstream current of Western esotericism. Born in Egypt (Lycopolis is "
        "traditionally named, though he was reluctant to discuss his origins), he studied "
        "philosophy at Alexandria under Ammonius Saccas for eleven years, participated in "
        "an expedition to Persia under Emperor Gordian III (seeking access to Persian and "
        "Indian philosophy), and then settled in Rome around 244 CE. There he taught for "
        "twenty-six years, attracting students from the Roman senatorial class and the "
        "intellectual elite, including Porphyry, Amelius, and the physician Eustochius. "
        "He reportedly delayed writing until he was fifty, and composed the treatises that "
        "Porphyry would edit into the Enneads only in the last decade and a half of his life.\n\n"

        "The Enneads (six groups of nine treatises, totaling fifty-four texts) were organized "
        "and edited by Porphyry, who published them after Plotinus's death with a biography "
        "(Vita Plotini) that provides our primary source for his life and working methods. "
        "Porphyry's arrangement is thematic rather than chronological: Ennead I covers ethics "
        "and the good; Ennead II, cosmology and the physical world; Ennead III, time, "
        "providence, and love; Ennead IV, the Soul; Ennead V, Intellect and its objects; "
        "Ennead VI, Being, the One, and the Good. This arrangement moves from the more "
        "accessible ethical and cosmological questions toward the most abstract metaphysical "
        "heights, mirroring the soul's own ascent.\n\n"

        "Plotinus's metaphysical system rests on three fundamental principles or hypostases: "
        "the One, Intellect (Nous), and Soul (Psyche). The One is the ultimate first principle, "
        "absolutely simple, beyond all predication, beyond even being and thought — it cannot "
        "be said to think (for thinking implies a duality of thinker and thought) and cannot "
        "be said to exist in any determinate way. From the One, by a process Plotinus calls "
        "procession (proodos) or emanation — not a temporal event but a logical and ontological "
        "dependence — Intellect arises. Intellect is the realm of the Platonic Forms: it thinks "
        "itself and in so doing comprehends all intelligible reality. From Intellect, Soul "
        "proceeds: Soul is both the cosmic soul (which governs the physical world) and individual "
        "human souls. Matter is at the furthest remove from the One, the bare limit of "
        "emanation — not evil in itself but the principle of privation and multiplicity.\n\n"

        "The counterpart to procession is return (epistrophe): every being that has proceeded "
        "from a higher principle naturally tends to return to it, to re-unify with its source. "
        "For the human soul, this return is the aim of philosophy and of the philosophical life. "
        "Plotinus describes the soul's ascent through stages: purification of the passions "
        "through practical virtue; the turn of attention from the physical world to the soul's "
        "own inner life; the ascent from soul to Intellect through philosophical contemplation; "
        "and finally the mystical union with the One itself, which Porphyry reports that "
        "Plotinus achieved four times in the years of their acquaintance. This union cannot "
        "be described in ordinary language, since it transcends the duality of knower and "
        "known; Plotinus calls it a 'simplification' and an 'abandonment of selfhood.'\n\n"

        "The influence of Plotinus on subsequent philosophy and esotericism is difficult to "
        "overstate. His direct students Porphyry and Iamblichus developed his system in "
        "different directions: Porphyry toward a more rationalist, less theurgical approach; "
        "Iamblichus toward a systematic integration of ritual theurgy (the performance of "
        "sacred rites to ascend through the divine hierarchies) with Plotinian metaphysics. "
        "Proclus (412–485 CE) systematized the entire tradition into a rigorous philosophical "
        "architecture that became the standard version of Neoplatonism for late antiquity and "
        "the Middle Ages. Through the pseudo-Dionysius the Areopagite (probably late fifth "
        "century), Neoplatonic language — the One beyond being, the apophatic approach to "
        "the divine, the hierarchical cosmology — entered Christian theology as if it were "
        "the work of Paul's Athenian convert, achieving canonical status.\n\n"

        "For the Renaissance hermetic tradition, Plotinus's significance was mediated primarily "
        "through Marsilio Ficino, who translated the Enneads into Latin (completed 1484–86, "
        "published 1492) alongside his translation of the Hermetic Corpus. Ficino read the "
        "Hermetic texts and the Enneads as expressions of the same prisca theologia (ancient "
        "theology), and the synthesis he produced — in the Theologia Platonica and the "
        "commentaries on Plato — shaped the intellectual vocabulary of Renaissance occult "
        "philosophy. Pico della Mirandola, Agrippa, and subsequent Hermetic-Neoplatonic "
        "writers all work within a conceptual universe in which Plotinian emanation theory, "
        "the tripartite hypostatic structure, and the soul's capacity for ascent are "
        "foundational assumptions.\n\n"

        "The relevance of Plotinus to the alchemical tradition is indirect but structural. "
        "The alchemical vocabulary of ascent (sublimation), of purification through stages, "
        "of the soul's separation from matter, and of ultimate conjunction with the divine "
        "ground is Neoplatonic in its philosophical shape even when practitioners do not "
        "cite Plotinus. The spiritual interpretation of alchemy — the reading of laboratory "
        "operations as figures for inner transformation — depends on a Neoplatonic "
        "anthropology in which the soul is imprisoned in matter and seeks return to its "
        "source. This structure pervades the allegorical alchemical tradition from the "
        "Arabic period onward, and its ultimate philosophical source is Plotinian."
    ),
    'key_works': [
        "Enneads (six groups of nine treatises, edited by Porphyry posthumously)",
        "Ennead I (Ethics, Beauty, Happiness)",
        "Ennead IV (The Soul)",
        "Ennead V (Intellect and the Intelligible World)",
        "Ennead VI (Being and the One)"
    ]
}

# ── id=8: Karl von Eckartshausen ────────────────────────────────────────────

updates[8] = {
    'essay': (
        "Karl von Eckartshausen (1752–1803) was a Bavarian Catholic mystic, court councillor, "
        "and prolific author whose late writings — particularly Die Wolke über dem Heiligtum "
        "(The Cloud upon the Sanctuary, 1802) — became foundational texts for nineteenth-century "
        "esotericism and theosophy. Born at Haimhausen in Bavaria, he served as a court "
        "councillor (Hofrath) to the Bavarian elector and held administrative positions "
        "throughout his career. He was a man of the Catholic Enlightenment milieu who moved "
        "progressively toward mysticism while remaining within the Roman Church, and whose "
        "hostility to both Enlightenment rationalism and to what he regarded as the external "
        "formalism of institutional religion shaped the distinctive voice of his mature work.\n\n"

        "Eckartshausen's early career produced an extensive body of practical and philosophical "
        "writing. Aufschlüsse zur Magie aus geprüften Erfahrungen über verborgene philosophische "
        "Wissenschaften und verdeckte Geheimnisse der Natur (Disclosures of Magic from Verified "
        "Experiences on Hidden Philosophical Sciences and Nature's Concealed Secrets, 4 vols, "
        "1788–91) is his most substantial earlier work. It addresses natural magic, theurgy, "
        "and the hidden properties of nature in a framework that blends natural philosophy "
        "with mystical theology. The text engages with the tradition of natural magic running "
        "from Agrippa and Porta through the seventeenth century, but increasingly frames "
        "magical efficacy as dependent on the operator's spiritual purity and inner development "
        "rather than on technical procedure alone. This shift — from technique to inner "
        "transformation as the ground of spiritual efficacy — is characteristic of the "
        "spiritualizing tendency that marks all his later work.\n\n"

        "Eckartshausen was a prolific author of devotional literature, moral tales, plays, "
        "and popular philosophical texts throughout the 1780s and 1790s. His Gott ist die "
        "reinste Liebe (God is the Purest Love) and related devotional texts aim at a "
        "popular Catholic piety deepened by mystical awareness; they circulated widely and "
        "went through multiple editions. These works are less philosophically ambitious than "
        "the Aufschlüsse but represent the devotional register within which his mystical "
        "theology was embedded.\n\n"

        "Die Wolke über dem Heiligtum (The Cloud upon the Sanctuary, 1802), published in "
        "the last year of his life, is by far his most influential text. Composed as a "
        "series of six letters addressed to 'a young man beginning his novitiate in the "
        "interior life,' it argues for the existence of an interior or invisible Church — "
        "a community of spiritually advanced individuals who, across all historical periods "
        "and external religious denominations, have shared a common inner knowledge and "
        "formed an invisible society of souls. This interior Church is not opposed to the "
        "external Roman Church but transcends and encompasses it: the visible Church is the "
        "outer court; the invisible Church is the inner sanctuary.\n\n"

        "The idea of the invisible interior Church drew on multiple traditions. The "
        "Rosicrucian manifestos of the early seventeenth century had proposed something "
        "similar — an invisible brotherhood of the learned and spiritual, transcending "
        "national and confessional boundaries. The German Pietist tradition, especially "
        "in its Böhmian-influenced strands, had developed the concept of the 'true church' "
        "as an invisible communion of regenerate souls. Eckartshausen synthesizes these "
        "Protestant currents from within a Catholic framework, which is characteristic of "
        "his position at the intersection of confessional traditions.\n\n"

        "The Cloud upon the Sanctuary was translated into English by Arthur Edward Waite "
        "(1895), the English occultist and Tarot scholar, and this translation made it "
        "widely accessible to the English-speaking esoteric milieu of the late nineteenth "
        "and early twentieth centuries. Waite's introduction framed the text as a key "
        "document of what he called 'transcendental Christianity,' and his endorsement "
        "gave it authority among the generation of occultists around the Hermetic Order "
        "of the Golden Dawn. The text was read by Aleister Crowley, influenced the "
        "young Dion Fortune, and was cited by Papus (Gérard Encausse) in the French "
        "Martinist tradition. In the Russian esoteric milieu, it influenced the early "
        "discussions of an 'inner church' that would recur in Steiner-influenced theosophy.\n\n"

        "For the history of spiritual alchemy, Eckartshausen occupies the position Mike "
        "Zuber identifies as a crucial transitional node. The genealogy Zuber traces in "
        "Spiritual Alchemy: Reinventing a Tradition (2017) runs from Böhme through "
        "Eckartshausen to Atwood and Blavatsky: where Böhme provides the original "
        "vocabulary of inner transformation and the soul's alchemical rebirth, "
        "Eckartshausen translates this into the language of an interior church and "
        "invisible tradition that Atwood and the theosophists will convert into "
        "the claim that all historical alchemy was always a spiritual practice. "
        "Eckartshausen's position within the Catholic Church made this transmission "
        "paradoxical — a Catholic mystic whose ideas fertilized Protestant, "
        "Martinist, and ultimately theosophical esotericism — but it reflects the "
        "genuine cross-confessional character of the mystical tradition he inhabited."
    ),
    'key_works': [
        "Aufschlüsse zur Magie aus geprüften Erfahrungen (Disclosures of Magic, 4 vols, 1788–91)",
        "Die Wolke über dem Heiligtum (The Cloud upon the Sanctuary, 1802)",
        "Gott ist die reinste Liebe (God is the Purest Love; devotional writings)",
        "Zahlenlehre der Natur (Number-theory of Nature)"
    ]
}

# ── id=41: Mary Anne Atwood ──────────────────────────────────────────────────

updates[41] = {
    'essay': (
        "Mary Anne Atwood (1817–1910), born Mary Anne South, was an English occult author "
        "whose A Suggestive Inquiry into the Hermetic Mystery (1850) is the most important "
        "single work in the tradition of spiritual alchemy — and one of the strangest "
        "publication histories in the history of esotericism. Atwood was the daughter of "
        "Thomas South, an amateur scholar and Mesmerist with deep interests in occult "
        "philosophy; she spent much of her life in Gosport and later in Clifton and "
        "Malvern, moving in the circles of Victorian occultism and spiritualism without "
        "seeking public prominence. She married the clergyman Alban Thomas Atwood in 1859.\n\n"

        "A Suggestive Inquiry into the Hermetic Mystery with a Dissertation on the More "
        "Celebrated of the Alchemical Philosophers Being an Attempt towards the Recovery "
        "of the Ancient Experiment of Nature (London, 1850) was published in a small "
        "edition that Atwood, reportedly seized by the conviction that she had revealed "
        "too much, recalled and had most copies burned within months of publication. "
        "The surviving copies circulated in restricted form for decades; the book was "
        "finally reissued in 1918, by which time it had already achieved legendary status "
        "in esoteric circles through manuscript copies, private circulation, and the "
        "testimony of those who had read it. The burning of the edition is itself a "
        "significant gesture in the esoteric tradition of concealment and selective "
        "disclosure — Atwood enacted, in the physical destruction of her book, "
        "the very concern with restricted transmission that her text theorizes.\n\n"

        "The Suggestive Inquiry argues a single central thesis: that alchemy is, and "
        "always was, fundamentally a practice of spiritual transformation, not of "
        "material chemistry. The philosophers' stone is not a chemical substance but "
        "a state of the soul; the Great Work is the work of inner regeneration; "
        "the alchemical operations (calcination, dissolution, coagulation, and so on) "
        "are symbolic descriptions of spiritual processes. This argument is not, "
        "in Atwood's presentation, a merely allegorical reading imposed on texts "
        "that are 'really' about chemistry — she argues that the alchemists "
        "themselves knew the true meaning of their operations and deliberately "
        "encoded it in chemical language to protect it from the profane.\n\n"

        "What is distinctive about Atwood's version of this argument — which had "
        "predecessors in the theological-alchemical tradition and in early "
        "eighteenth-century spiritualizing readings — is her specific mechanism "
        "for the spiritual work. She argues that the alchemical practice involved "
        "a form of magnetic or Mesmeric induction: the alchemist, having "
        "prepared himself through moral and spiritual discipline, induced in "
        "himself and his 'subject' (a passive partner in a trance state) a "
        "condition of heightened spiritual receptivity analogous to Mesmeric "
        "somnambulism. In this trance state, the soul could be 'volatilized' — "
        "separated from its ordinary material attachments — and brought into "
        "direct contact with the divine light at the centre of being. The "
        "philosopher's stone was the capacity to induce and guide this process. "
        "The alchemical apparatus — furnace, alembic, vessel, fire — were "
        "symbolic descriptions of the Mesmerist's procedures and the magnetized "
        "subject's inner experience.\n\n"

        "This interpretation is audacious and historically untestable in the "
        "sense that Atwood provides: there is no evidence that alchemists "
        "practiced Mesmerism or used magnetic induction, and the Mesmeric "
        "framework was available to Atwood from late-eighteenth-century "
        "sources rather than from the alchemical tradition itself. But the "
        "book's influence was enormous precisely because it gave intellectual "
        "coherence and emotional force to the spiritual-alchemical reading. "
        "By claiming that alchemy was always inwardly psychological and "
        "spiritual, Atwood provided Victorian esotericists with a framework "
        "for appropriating the entire alchemical tradition without being "
        "committed to the literal possibility of transmuting metals.\n\n"

        "The genealogy of spiritual alchemy that Mike Zuber traces in Spiritual "
        "Alchemy: Reinventing a Tradition (2017) places Atwood at a decisive "
        "pivot. The chain runs: Meister Eckhart and Johann Tauler → Jacob Böhme "
        "→ Karl von Eckartshausen → Mary Anne Atwood → Helena Blavatsky → "
        "twentieth-century 'spiritual alchemy.' Böhme provided the vocabulary "
        "of inner transformation and the soul's alchemical rebirth; Eckartshausen "
        "translated this into the language of an invisible interior church and "
        "hidden tradition; Atwood made the explicit claim that this inner "
        "tradition was identical with the hidden meaning of all historical alchemy. "
        "Once Atwood made this identification, the path was open for Blavatsky "
        "to incorporate alchemy into her Theosophical synthesis as spiritual "
        "technology, and for subsequent writers to read every alchemical text "
        "as a coded description of inner experience.\n\n"

        "The Suggestive Inquiry also contains substantial historical scholarship: "
        "extended discussions of Paracelsus, van Helmont, Böhme, the Cambridge "
        "Platonists, Thomas Vaughan, and other figures, which are not negligible "
        "as historical writing even if their interpretive framework is Atwood's "
        "own. Her treatment of these sources reveals genuine familiarity with "
        "primary texts and with the scholarly literature available to her. "
        "The book deserves to be read not only as an esoteric classic but as "
        "a document in the intellectual history of Victorian occultism and "
        "as the founding text of the spiritual-alchemical tradition that "
        "dominated twentieth-century popular alchemy."
    ),
    'key_works': [
        "A Suggestive Inquiry into the Hermetic Mystery (1850; reissued 1918)"
    ]
}

# ── id=47: Isaac Newton ──────────────────────────────────────────────────────

updates[47] = {
    'essay': (
        "Isaac Newton (1643–1727) was an English mathematician, natural philosopher, and "
        "theologian whose Principia Mathematica (1687) and Opticks (1704) established the "
        "foundations of classical mechanics and corpuscular optics. He is also the most "
        "celebrated practitioner of alchemy among major figures of early modern natural "
        "philosophy: his alchemical manuscripts run to over a million words, representing "
        "more of his intellectual labour than either the Principia or the Opticks. This "
        "fact, suppressed or minimized for two centuries after his death, has fundamentally "
        "altered the historiography of the Scientific Revolution since the 1970s.\n\n"

        "Newton's alchemical manuscripts were purchased at the 1936 Sotheby's auction of "
        "his papers by John Maynard Keynes, who described Newton as 'the last of the "
        "magicians.' Keynes recognized that the alchemical papers represented a "
        "substantial and sustained engagement, not an embarrassing sideline. The "
        "manuscripts are now held primarily at King's College Cambridge, the Jewish "
        "National and University Library in Jerusalem, and various other institutions. "
        "Betty Jo Teeter Dobbs was the first historian to work through them systematically; "
        "her two studies — The Foundations of Newton's Alchemy (1975) and The Janus Faces "
        "of Genius (1991) — established that Newton's alchemy was neither a youthful "
        "enthusiasm nor a late irrationalism but a lifelong engagement spanning from the "
        "1660s to the first decade of the eighteenth century.\n\n"

        "Newton's alchemical manuscripts include extensive reading notes from the major "
        "alchemical literature — Paracelsus, Ripley, Flamel, van Helmont, Sendivogius, "
        "the Rosarium Philosophorum, and many others — alongside his own experimental "
        "records and synthetic texts. Several of Newton's own alchemical writings have "
        "been identified and studied. 'Of Natures obvious laws and processes in vegetation' "
        "(c.1672) sets out Newton's view that there are two kinds of natural process: "
        "mechanical (explicable by contact and collision) and vegetable or vital (involving "
        "active, animating principles that cannot be reduced to mechanism). The 'Praxis' "
        "manuscript and the 'Clavis' (Key) record experimental work aimed at identifying "
        "the 'vegetable spirit' — Newton's term for the active principle he believed "
        "operated in the growth and transformation of metals. He also composed 'Index "
        "Chemicus,' a vast concordance of alchemical terms and concepts drawn from his reading.\n\n"

        "Newton's relationship to the figure of George Starkey (1628–1665) has been "
        "illuminated by William Newman's research. Starkey, an American alchemist and "
        "chemist who worked in London, was a major transmitter of Helmontian chemical "
        "medicine and a prolific author of alchemical texts published under the pseudonym "
        "'Eirenaeus Philalethes.' Newman demonstrated that Newton's alchemical reading "
        "and experimentation was substantially shaped by the Philalethes texts, "
        "particularly the Secrets Reveal'd (1669) and the Introitus Apertus ad Occlusum "
        "Regis Palatium (Open Entrance to the Closed Palace of the King), and that Newton "
        "copied long passages from Starkey's unpublished laboratory notebooks alongside "
        "Starkey's published works. Newton the Alchemist: Science, Enigma, and the Quest "
        "for Nature's 'Secret Fire' (2019), Newman's monograph on this subject, is the "
        "most rigorously documented account of Newton's laboratory alchemy.\n\n"

        "Newton's alchemical goal can be reconstructed from his manuscripts with reasonable "
        "confidence: he sought the 'vegetable spirit,' an active animating principle "
        "embedded in matter that was responsible for growth, fermentation, and vital "
        "processes, and that was distinct from the passive mechanical properties of "
        "inert matter. This active principle was not identical with the theological "
        "soul but was a natural power — Newton sometimes calls it the 'spirit of "
        "nature' or the 'fermental virtue' — that operated below the level of ordinary "
        "mechanical causation. His conviction that nature contained such active principles "
        "alongside mechanical ones is reflected in the famous General Scholium of the "
        "Principia (1713 edition), with its reference to a 'certain most subtle spirit' "
        "pervading gross bodies, and in the Queries appended to later editions of the "
        "Opticks, where Newton speculates about active principles in nature.\n\n"

        "Newton also engaged seriously with the transmutation claim. He corresponded with "
        "Robert Boyle on alchemical matters and shared Boyle's concern that knowledge of "
        "the philosophers' stone should be kept from the public lest it destabilize "
        "the monetary system. He was present when Boyle lobbied for — and achieved — "
        "the repeal of the English statute against multiplying gold (1689), suggesting "
        "that Newton, like Boyle, believed transmutation to be genuinely possible in "
        "principle. His laboratory records show active chemical experimentation on "
        "antimony regulus preparations (following Starkey's procedures), on the "
        "purification of mercury, and on the 'net' (a reticulated crystalline "
        "pattern he observed in certain preparations) that he associated with the "
        "vegetable spirit's operation.\n\n"

        "The historiographical significance of Newton's alchemy extends beyond "
        "biography. It challenges the standard narrative of the Scientific Revolution "
        "as a clean break from Renaissance occultism toward mechanical philosophy. "
        "Newton operated simultaneously in both registers: developing the mathematical "
        "mechanics of the Principia and experimenting with alchemical procedures "
        "that presupposed active, vital principles in matter. Dobbs argued that "
        "these were parts of a unified research program rather than compartmentalized "
        "activities. Newman is more cautious about inferring systematic unity, "
        "but shares the conclusion that the alchemy was genuine intellectual "
        "engagement rather than entertainment or eccentricity. The Newton who "
        "emerges from this scholarship is not a precursor of modern science who "
        "unfortunately dabbled in alchemy but a natural philosopher for whom the "
        "boundary between chemical philosophy and mathematical mechanics had not "
        "yet been drawn."
    ),
    'key_works': [
        "'Of Natures obvious laws and processes in vegetation' (c.1672; manuscript)",
        "'Praxis' and 'Clavis' (alchemical manuscripts)",
        "'Index Chemicus' (alchemical concordance; manuscript)",
        "Principia Mathematica (1687; natural philosophy)",
        "Opticks (1704; with alchemically relevant Queries in later editions)",
        "Extensive reading notes and laboratory records on Starkey, Ripley, Sendivogius (manuscripts)"
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
