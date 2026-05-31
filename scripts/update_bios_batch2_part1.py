#!/usr/bin/env python3
"""
update_bios_batch2_part1.py
Handles: redirect stubs (85, 90, 92, 93, 96, 97, 86, 25), and
short new entries (94, 95, 98, 99, 100).
"""

import json, os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prototype_data.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

updates = {}

# ── REDIRECT STUBS ──────────────────────────────────────────────────────────

updates[85] = {
    'essay': (
        "This entry duplicates the main John Dee (id=2) biography. "
        "See the full entry for John Dee (1527–1608/9) covering the Monas Hieroglyphica (1564), "
        "Propaedeumata Aphoristica (1558/1568), his Enochian angelic conversations with Edward Kelley "
        "(1582–1589), and his library at Mortlake. "
        "[Duplicate stub pending deduplication]"
    ),
    'key_works': ["See id=2 (John Dee) for complete works list"]
}

updates[90] = {
    'essay': (
        "This entry duplicates the main Michael Maier (id=10) biography. "
        "See the full entry for Michael Maier (1568–1622) covering the Atalanta Fugiens (1618), "
        "Symbola Aureae Mensae (1617), Arcana Arcanissima (1614), Themis Aurea (1618), "
        "and his role as the most systematic musical-emblematic theorist of Rosicrucian alchemy. "
        "[Duplicate stub pending deduplication]"
    ),
    'key_works': ["See id=10 (Michael Maier) for complete works list"]
}

updates[92] = {
    'essay': (
        "This entry duplicates the main Gerhard Dorn (id=29) biography. "
        "See the full entry for Gerhard Dorn (c.1530–c.1584), the Flemish Paracelsian philosopher "
        "who translated and systematized Paracelsus for Latin readers and whose concept of the coniunctio "
        "was later analysed by C.G. Jung in Mysterium Coniunctionis. "
        "[Duplicate stub pending deduplication]"
    ),
    'key_works': ["See id=29 (Gerhard Dorn) for complete works list"]
}

updates[93] = {
    'essay': (
        "This entry duplicates the main Jābir ibn Ḥayyān (id=19) biography. "
        "See the full entry for Jābir ibn Ḥayyān / Geber (c.721–c.815 CE), covering the Jabirian corpus, "
        "the question of collective Ismaili authorship established by Paul Kraus (1942), "
        "and the distinct Latin pseudo-Geber tradition (Summa Perfectionis). "
        "[Duplicate stub pending deduplication]"
    ),
    'key_works': ["See id=19 (Jabir ibn Hayyan) for complete works list"]
}

updates[96] = {
    'essay': (
        "This entry duplicates the main Roger Bacon (id=22) biography. "
        "See the full entry for Roger Bacon (c.1214/1220–c.1292), the English Franciscan natural philosopher "
        "whose Opus Majus (1267) and the pseudonymous Speculum Alchimiae and Epistola de Secretis "
        "circulated widely under his name, making him one of the most invoked authorities in medieval "
        "and Renaissance alchemy. "
        "[Duplicate stub pending deduplication]"
    ),
    'key_works': ["See id=22 (Roger Bacon) for complete works list"]
}

updates[97] = {
    'essay': (
        "This entry duplicates the main Nicolas Flamel (id=18) biography. "
        "See the full entry for Nicolas Flamel (c.1330–1418), the Parisian scrivener around whom "
        "an elaborate legend of alchemical transmutation accumulated from the seventeenth century onward, "
        "centred on the Livre des figures hiéroglyphiques (published 1612, now recognized as pseudonymous). "
        "[Duplicate stub pending deduplication]"
    ),
    'key_works': ["See id=18 (Nicolas Flamel) for complete works list"]
}

updates[86] = {
    'essay': (
        "This entry duplicates the main Giambattista della Porta (id=32) biography. "
        "See the full entry for Giambattista della Porta (c.1535–1615), the Neapolitan natural philosopher "
        "whose Magia Naturalis (1558; expanded 1589) codified natural magic as systematic inquiry "
        "into hidden properties of things, and whose Accademia dei Segreti pioneered collaborative "
        "empirical investigation. "
        "[Duplicate stub pending deduplication]"
    ),
    'key_works': ["See id=32 (Giambattista della Porta) for complete works list"]
}

updates[25] = {
    'essay': (
        "This entry duplicates the main Claude de Saint-Martin (id=9) biography. "
        "Louis-Claude de Saint-Martin (1743–1803) is the same person: he went by Claude de Saint-Martin "
        "and signed his works 'le Philosophe Inconnu' (the Unknown Philosopher). "
        "See the full entry at id=9 covering Des Erreurs et de la Vérité (1775), "
        "L'Homme de Désir (1790), Le Ministère de l'Homme-Esprit (1802), "
        "and the Martinist tradition. "
        "[Duplicate stub pending deduplication]"
    ),
    'key_works': ["See id=9 (Claude de Saint-Martin) for complete works list"]
}

# ── NEW SHORT ENTRIES ────────────────────────────────────────────────────────

updates[94] = {
    'essay': (
        "Muḥammad ibn Zakariyyā al-Rāzī (c.854–925 or 865–925 CE), known in Latin as Rhazes, "
        "was a Persian physician and alchemist born at Ray (near modern Tehran) who worked primarily "
        "in Ray and Baghdad. He is among the most important figures in the history of both Islamic "
        "medicine and practical alchemy, and the systematic clarity of his chemical writing ensured "
        "its wide transmission into the Latin West.\n\n"

        "Al-Rāzī's medical masterwork, the encyclopedic al-Ḥāwī fī al-ṭibb (Liber Continens in Latin "
        "translation), was a vast compilation of Greek, Syriac, and Islamic medical learning organized "
        "for clinical practice. Its Latin version, produced in the thirteenth century by Faraj ibn Sālim "
        "for Charles of Anjou, circulated as a standard medical reference throughout the later Middle Ages. "
        "The Kitāb al-Manṣūrī (Liber Almansoris) was similarly influential as a concise practical text.\n\n"

        "For the history of alchemy, his two most significant works are the Kitāb al-Asrār (Book of "
        "Secrets) and the Kitāb Sirr al-Asrār (Book of the Secret of Secrets). These texts are "
        "remarkable for their systematic, empirical approach to laboratory procedure. Al-Rāzī organized "
        "his material around a classification of substances — animal, vegetable, and mineral — and "
        "provided detailed accounts of laboratory apparatus (alembics, cucurbits, aludels, furnaces) "
        "and operations (calcination, solution, filtration, crystallization, sublimation, amalgamation). "
        "He classified mineral substances into six categories: spirits (volatile substances such as "
        "mercury, sulphur, arsenic, and sal ammoniac), bodies (the metals), stones, vitriols, boraces, "
        "and salts. This classification scheme was adapted by Latin translators and remained influential "
        "in European alchemical writing.\n\n"

        "The practical, non-speculative character of al-Rāzī's alchemy has often been contrasted with "
        "the more philosophical and cosmological orientation of the Jabirian corpus. Where the Jabir "
        "tradition elaborated complex numerical and balance theories, al-Rāzī's surviving alchemical "
        "texts are closer to a craftsman's manual: they describe what to do and what equipment to use, "
        "with less interest in cosmological justification. This pragmatic character made his work "
        "particularly useful for the Latin translators of the twelfth century, who transmitted it "
        "through the translation movement centred at Toledo. The Latin Rhazes became a standard "
        "medical and pharmaceutical authority, and his alchemical classifications fed into the "
        "systematization of European alchemy in the thirteenth and fourteenth centuries.\n\n"

        "Scholars have debated which works attributed to al-Rāzī are genuinely his and which are "
        "later pseudonymous attributions, a problem familiar from the study of Jabir. The Kitāb "
        "al-Asrār is generally regarded as authentic; other texts in the corpus are less certain. "
        "His significance for the Western tradition is clear regardless: through Latin translations "
        "he supplied a systematic vocabulary of laboratory alchemy that shaped European practice "
        "before and alongside the reception of Aristotelian natural philosophy."
    ),
    'key_works': [
        "Kitāb al-Asrār (Book of Secrets)",
        "Kitāb Sirr al-Asrār (Book of the Secret of Secrets)",
        "al-Ḥāwī fī al-ṭibb (Liber Continens)",
        "Kitāb al-Manṣūrī (Liber Almansoris)"
    ]
}

updates[95] = {
    'essay': (
        "Albertus Magnus (c.1200–1280), born Albert of Lauingen in Swabia, was a Dominican friar, "
        "theologian, bishop, and the most encyclopedic natural philosopher of the thirteenth century. "
        "His students at Paris and Cologne included Thomas Aquinas. He was canonized in 1931 and "
        "declared a Doctor of the Church; his epithet 'Magnus' (the Great) was applied during his "
        "own lifetime, unusually for a medieval scholar.\n\n"

        "Albert's significance for the history of alchemy derives principally from his De Mineralibus "
        "et Rebus Metallicis (On Minerals and Metallic Things), a systematic Aristotelian treatment "
        "of stones, minerals, and metals that drew on Avicenna's De Congelatione et Conglutinatione "
        "Lapidum and the Arabic mineralogical tradition. In De Mineralibus, Albert accepted the "
        "sulphur-mercury theory of metal formation (the view, derived from Arabic sources, that all "
        "metals are composed of sulphur and mercury in varying proportions) as natural philosophy, "
        "and he discussed the theoretical possibility of transmutation while remaining cautious about "
        "whether alchemical practitioners had actually achieved it. He distinguished between natural "
        "processes in the earth and artificial imitation in the laboratory, a distinction that would "
        "recur throughout later discussions of alchemy's legitimacy.\n\n"

        "The Libellus de Alchimia (Little Book on Alchemy), also called the Semita Recta (Straight "
        "Path), circulated widely under Albert's name and was taken as authoritative evidence of his "
        "endorsement of practical alchemy. Modern scholars, including Robert Halleux, have argued "
        "that this text is almost certainly pseudonymous — composed by a later author who attached "
        "Albert's name to gain authority. The attribution question matters because Albert's genuine "
        "works are notably measured in their claims about alchemy, while the Libellus is more "
        "practically oriented toward transmutation. Nevertheless, the pseudonymous text's circulation "
        "under his name made 'Albertus' one of the most cited authorities in late medieval and "
        "Renaissance alchemical literature.\n\n"

        "Albert's broader importance for the tradition lies in his role as the great legitimizer of "
        "Aristotelian natural philosophy within Christian theology — the intellectual project that his "
        "student Thomas Aquinas would complete. By demonstrating that Aristotelian science could be "
        "reconciled with Christian doctrine, Albert helped create the intellectual framework within "
        "which alchemy could be discussed as natural philosophy rather than condemned as demonic art. "
        "His authority was therefore invoked both by those who wished to defend alchemy on naturalistic "
        "grounds and by those who wished to attack it on the same grounds. The name 'Albertus Magnus' "
        "attached to alchemical texts functioned as a legitimizing signature throughout the later "
        "Middle Ages and the Renaissance."
    ),
    'key_works': [
        "De Mineralibus et Rebus Metallicis (On Minerals and Metallic Things)",
        "Libellus de Alchimia / Semita Recta (attributed; probably pseudonymous)",
        "Summa Theologiae (with Thomas Aquinas as student)",
        "De Animalibus",
        "Commentaries on Aristotle's natural works"
    ]
}

updates[98] = {
    'essay': (
        "Arnau de Vilanova (c.1240–1311), known in Latin as Arnaldus de Villanova, was a Catalan "
        "physician, theologian, and apocalyptic writer who taught medicine at Montpellier and served "
        "as personal physician to several Aragonese kings and to Pope Boniface VIII. His genuine "
        "medical writings — on diet, regimen, fevers, and pharmaceutical preparation — represent some "
        "of the most sophisticated medical learning of the late thirteenth century. His theological "
        "writings, which predicted an imminent Antichrist and attacked the mendicant orders, brought "
        "him repeatedly into conflict with Church authorities. He died in 1311 en route to meet Pope "
        "Clement V.\n\n"

        "The alchemical works that bear Arnau's name are, with high scholarly consensus, not by him. "
        "The 'Pseudo-Arnaldian corpus' — a substantial body of alchemical texts that circulated under "
        "his name from the fourteenth century onward — includes the Rosarius Philosophorum (Rose Garden "
        "of the Philosophers), the Novum Lumen (New Light), the Flos Florum (Flower of Flowers), "
        "and the Perfectum Magisterium, among others. These texts were composed over the course of "
        "the fourteenth and fifteenth centuries by authors who exploited the prestige of Arnau's "
        "name to authorize their claims. This strategy of pseudonymous attribution was systematic "
        "in medieval alchemical writing: Albertus Magnus, Roger Bacon, Raymond Lull, and Thomas "
        "Aquinas were all subjected to the same treatment.\n\n"

        "The Pseudo-Arnaldian Rosarius Philosophorum is the most important of these texts for the "
        "later tradition. It presents a systematic account of the Great Work in allegorical terms, "
        "using the rose as an image for the philosophers' stone, and connects alchemical language "
        "to Christian theological concepts of redemption and resurrection. It was widely copied, "
        "anthologized in major alchemical collections including the Artis Auriferae (1572), and "
        "cited as authoritative by later alchemical writers who believed it expressed Arnau's "
        "genuine teaching.\n\n"

        "The gap between Arnau's genuine and attributed works is itself historically revealing. "
        "His actual medical writings show an interest in pharmaceutical distillation — he is "
        "sometimes credited with early work on distilled spirits and aqua vitae — that may have "
        "made his name plausible as an alchemical authority. Whether Arnau personally engaged "
        "with alchemy in any way beyond pharmaceutical chemistry is uncertain; some scholars, "
        "including Michael McVaugh, have argued for a limited genuine engagement, while others "
        "treat the alchemical corpus as entirely posthumous fabrication.\n\n"

        "For the history of esotericism, the significance of the Pseudo-Arnaldian corpus lies "
        "less in its content than in its function: it demonstrates how the prestige of a known "
        "medical authority was systematically mobilized to legitimize alchemical claims, and how "
        "the boundary between genuine and attributed authorship in medieval learned culture was "
        "far more permeable than modern notions of intellectual property suggest. The corpus "
        "shaped the vocabulary and imagery of European alchemy through the sixteenth century, "
        "and its texts appear in manuscript collections alongside those attributed to Albert, "
        "Bacon, and Lull — a canon of authoritative names that together constituted alchemy's "
        "claim to ancient and authoritative intellectual tradition."
    ),
    'key_works': [
        "Rosarius Philosophorum (Rose Garden of the Philosophers; attributed, pseudonymous)",
        "Novum Lumen (New Light; attributed, pseudonymous)",
        "Flos Florum (Flower of Flowers; attributed, pseudonymous)",
        "Perfectum Magisterium (attributed, pseudonymous)",
        "Regimen Sanitatis (On the Preservation of Health; genuine)",
        "Tractatus de Aquis (genuine pharmaceutical text)"
    ]
}

updates[99] = {
    'essay': (
        "Meister Eckhart (c.1260–c.1328), born Johann Eckhart at Hochheim in Thuringia, was a "
        "German Dominican friar, theologian, and preacher whose mystical philosophy represents the "
        "most intellectually ambitious expression of medieval German mysticism. He studied and "
        "taught at Paris, held the chair in theology there twice (an unusual distinction), served "
        "as Provincial Prior of Saxony and Vicar-General of Bohemia, and ended his career in "
        "Cologne, where he was tried for heresy. He died before the papal condemnation was issued; "
        "the bull In Agro Dominico (1329) condemned twenty-eight propositions drawn from his work.\n\n"

        "Eckhart wrote in both Latin and Middle High German, and the two bodies of work serve "
        "different purposes. The Latin Opus Tripartitum (Three-Part Work) was a large systematic "
        "theological project, of which the Prologues and portions of the Commentaries on Genesis, "
        "Exodus, John, and the Book of Wisdom survive. These works engage Neoplatonic metaphysics "
        "— particularly the Liber de Causis (the Arabic adaptation of Proclus) and Dionysius the "
        "Areopagite — within a rigorous scholastic framework. The German Sermons (Predigten), "
        "of which around sixty are generally considered authentic, were preached to Dominican nuns "
        "and lay audiences; they translate Eckhart's speculative theology into vernacular German, "
        "creating a new philosophical vocabulary in the process.\n\n"

        "The Talks of Instruction (Reden der Unterweisung), composed early in his career for "
        "young Dominican friars, and the Book of Divine Comfort (Buch der göttlichen Tröstung), "
        "written for Agnes of Hungary, are his major shorter German prose works. The Talks "
        "present his practical mysticism — the cultivation of Abgeschiedenheit (detachment or "
        "releasement) as the ground of spiritual transformation — in an accessible, pastoral register.\n\n"

        "Eckhart's central philosophical moves have been deeply influential on later esotericism. "
        "His concept of the Gottheit (Godhead) as distinct from the personal God of Christian "
        "theology — the Godhead as an undifferentiated ground, beyond predication, beyond the "
        "Trinity itself — pushes Neoplatonic apophatic theology to its limit. The soul, in "
        "Eckhart's account, has a 'spark' (Fünklein) or 'ground' (Grunt) that is uncreated and "
        "in permanent contact with the divine ground. The spiritual life consists in returning "
        "to this ground through detachment from all created things, including the self's attachment "
        "to its own spiritual experiences. This 'birth of the Word in the soul' (Geburt des Wortes "
        "in der Seele) is Eckhart's central image for mystical union.\n\n"

        "The transmission genealogy from Eckhart to spiritual alchemy runs through several channels. "
        "His Dominican disciple Johann Tauler (c.1300–1361) adapted Eckhart's speculative vocabulary "
        "into a more practically oriented mysticism focused on the 'ground of the soul' (Seelengrund). "
        "Heinrich Suso, another disciple, transmitted Eckhartian themes in a more affective register. "
        "The Frankfurter or Theologia Deutsch, an anonymous late-fourteenth-century text that Luther "
        "published in 1516, drew heavily on this Rhenish mystical tradition. Through Tauler and the "
        "Theologia Deutsch, Eckhart's vocabulary entered the Lutheran spiritual culture from which "
        "Jacob Böhme emerged in the early seventeenth century.\n\n"

        "Böhme's concepts of the Ungrund (unground, the divine abyss before being), the opposition "
        "of fire and light, and the soul's return through a death of self-will are saturated with "
        "Eckhartian-Taulerian language, even though Böhme had no direct access to Eckhart's Latin "
        "works and received the tradition primarily through the vernacular Tauler sermons and the "
        "Theologia Deutsch. From Böhme, this vocabulary passed into the English and Dutch Behmenist "
        "traditions (Gichtel, Jane Lead, the Philadelphians), into Pietism, and ultimately into "
        "the nineteenth-century spiritual alchemy of Mary Anne Atwood and the theosophical currents "
        "that followed. The concept of alchemical transmutation as inner detachment and divine birth "
        "in the soul is Eckhartian in its deep structure, even when the later writers do not "
        "explicitly invoke his name."
    ),
    'key_works': [
        "German Sermons (Predigten; c. 60 authentic sermons identified)",
        "Talks of Instruction (Reden der Unterweisung)",
        "Book of Divine Comfort (Buch der göttlichen Tröstung)",
        "Opus Tripartitum (Latin systematic work; fragmentary)",
        "Commentary on Genesis (Latin)",
        "Commentary on the Gospel of John (Latin)"
    ]
}

updates[100] = {
    'essay': (
        "Johann Tauler (c.1300–1361) was a German Dominican friar and preacher, born at Strasbourg "
        "and active in the Rhenish mystical circle that included Meister Eckhart, Heinrich Suso, "
        "and the lay 'Friends of God' (Gottesfreunde) movement. He spent most of his life in "
        "Strasbourg, with periods in Basel during the Black Death (1348–1349), when he ministered "
        "to the sick and dying. He died at Strasbourg in 1361.\n\n"

        "Tauler's surviving works consist almost entirely of German sermons — over eighty of which "
        "are accepted as genuine, with a larger corpus of doubtful or pseudonymous texts also "
        "circulating under his name. Unlike his teacher Eckhart, Tauler was never tried for heresy; "
        "his mystical theology is more guarded in its speculative reach and consistently more "
        "practical in its orientation. Where Eckhart pressed Neoplatonic concepts toward their "
        "logical extreme (the soul's identity with the Godhead, the uncreated spark), Tauler "
        "emphasized the experiential and ethical dimensions of mystical life — the long, difficult "
        "work of self-mortification, inner suffering, and gradual transformation of the will.\n\n"

        "The central concept in Tauler's preaching is the Seelengrund (ground of the soul), "
        "inherited from Eckhart but given a more pastoral inflection. The Seelengrund is the "
        "deepest part of the soul, where the human person is in immediate contact with the divine. "
        "To enter this ground requires Abgeschiedenheit (detachment) from all created things and "
        "from the ego's will — a process Tauler describes as a kind of death and rebirth. "
        "The metaphors of putrefaction, dissolution, and new birth that pervade Tauler's sermons "
        "connect structurally to alchemical language, though Tauler himself makes no explicit "
        "alchemical references. The parallel was noticed by later readers who brought Tauler "
        "into conversation with Paracelsian and Böhmian alchemy.\n\n"

        "Martin Luther's engagement with Tauler was decisive for the transmission of Rhenish "
        "mysticism into Protestant culture. Luther read Tauler's sermons with enthusiasm around "
        "1515–1516 and found in them a model of experiential, grace-centered piety that resonated "
        "with his developing theology of justification by faith. In 1516 he published an edition "
        "of the Theologia Deutsch (Frankfurter), an anonymous text closely related to Tauler's "
        "circle. Luther's endorsement gave Tauler wide readership in Lutheran Germany and beyond: "
        "the sermons were frequently reprinted throughout the sixteenth century and were well "
        "known to educated Protestants.\n\n"

        "The connection to Jacob Böhme is the most important transmission link for the history "
        "of spiritual alchemy. Böhme, the Görlitz shoemaker who produced the most systematic "
        "Protestant mystical theosophy of the early seventeenth century, drew on the Taulerian "
        "tradition (mediated through the Theologia Deutsch and Lutheran devotional literature) "
        "for his concepts of the soul's ground, the death of self-will as the gateway to divine "
        "birth, and the transformation of darkness into light. Böhme's vocabulary is structurally "
        "Taulerian even where it adopts alchemical and astrological terminology from Paracelsus.\n\n"

        "From Böhme, Tauler's themes passed into the English Behmenist tradition through figures "
        "such as Johann Georg Gichtel (who edited Böhme's works) and Jane Lead (whose Philadelphian "
        "Society brought Behmenism to England and translated it for Dutch and German audiences). "
        "The spiritual alchemy of the nineteenth century — Mary Anne Atwood's Suggestive Inquiry "
        "(1850), with its argument that alchemy is fundamentally about inner transformation through "
        "a kind of magnetic or mesmeric rebirth — inherits, through these transmission chains, "
        "the Taulerian insistence that the real transformation is of the soul, not of metals. "
        "Mike Zuber's Spiritual Alchemy (2017) maps this genealogy explicitly, placing Tauler "
        "at the beginning of a chain that runs through Böhme, Eckartshausen, Atwood, and "
        "Blavatsky to contemporary 'spiritual alchemy.'"
    ),
    'key_works': [
        "Sermons (Predigten; c. 80+ authentic sermons in German)",
        "Letters and shorter spiritual texts (some authentic, many attributed)"
    ]
}

# ── APPLY UPDATES ────────────────────────────────────────────────────────────

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

# Confirm all target IDs were found
missed = set(updates.keys()) - set(updated_ids)
if missed:
    print(f"WARNING: IDs not found in data: {missed}")

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nDone. Updated {len(updated_ids)} entries.")
