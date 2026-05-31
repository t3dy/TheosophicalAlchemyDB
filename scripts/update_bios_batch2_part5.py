#!/usr/bin/env python3
"""
update_bios_batch2_part5.py
Full essays for: id=24 Blake, id=88 Boyle, id=83 Libavius, id=73 Croll.
"""

import json, os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prototype_data.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

updates = {}

# ── id=24: William Blake ─────────────────────────────────────────────────────

updates[24] = {
    'essay': (
        "William Blake (1757–1827) was an English poet, painter, and printmaker whose "
        "visionary prophetic books constitute one of the most original literary achievements "
        "of the Romantic period and one of the densest engagements with esoteric traditions "
        "in English literature. Born in Soho, London, to a family of dissenters, he was "
        "apprenticed to an engraver at fourteen and developed the illuminated printing "
        "technique — combining etched text and image in a single plate, printed and "
        "then hand-coloured — that gave his major works their distinctive visual-verbal "
        "character. He worked as a commercial engraver throughout his life and never "
        "achieved mainstream recognition; his visionary poetry was largely unread in his "
        "lifetime and recovered only through the efforts of Alexander Gilchrist's "
        "biography (1863) and the subsequent Pre-Raphaelite and Symbolist interest.\n\n"

        "The Marriage of Heaven and Hell (1790) is Blake's most accessible esoteric "
        "text and his most direct engagement with the tradition he was inheriting and "
        "subverting. Written in response to Swedenborg's Heaven and Hell (1758) — "
        "Blake had initially admired Swedenborg but turned against him, annotating "
        "his works with increasing hostility — it inverts Swedenborg's moral "
        "cosmology: the 'Devils' (energy, desire, the body, excess) are revalued "
        "as creative and divine; the 'Angels' (reason, restraint, the law) are "
        "exposed as repressive and false. The 'Proverbs of Hell' ('The road of excess "
        "leads to the palace of wisdom'; 'Energy is Eternal Delight') are Blake's "
        "most quoted lines and his most direct formulation of what he calls the "
        "'active' as against the 'passive' life. The Marriage's account of the "
        "'Contraries' — without Contraries is no progression; Attraction and "
        "Repulsion, Reason and Energy, Love and Hate are necessary to Human "
        "existence — encodes an alchemical logic of conjunction: it is the "
        "tension and union of opposites, not their separation, that produces "
        "life and progress.\n\n"

        "The 'Lambeth Books' of the 1790s — The Book of Urizen (1794), The Book "
        "of Los (1795), The Book of Ahania (1795), and Europe: A Prophecy (1794) "
        "— develop Blake's private mythological cosmos. Urizen is the deity of "
        "reason, law, and restriction, who 'divides' and 'measures' and creates "
        "the fallen material world by the very act of mental contraction. Los is "
        "the spirit of prophecy and imagination, the eternal poet who forges "
        "forms in the furnace of time. The furnace and the forge are explicitly "
        "alchemical images in Blake: Los works with hammer and anvil in a "
        "smithy that is both actual metal-working and a figure for the "
        "imaginative labor of transforming the fallen world into the living "
        "body of vision.\n\n"

        "Milton: A Poem (1804–1811) is Blake's meditation on poetic tradition "
        "and spiritual authority. The historical John Milton descends from "
        "eternity to correct the errors of his Puritanism and reunite with "
        "his 'emanation' (his female counterpart or projected selfhood) — "
        "a psychomachic drama that Blake understood as the necessary prior "
        "act before prophetic vision could be recovered in his own time. "
        "The concept of the 'emanation' — the female aspect projected outward "
        "from the male spiritual self — has structural parallels to the "
        "alchemical soror mystica (the mystical sister) and to the "
        "Böhmian concept of the divine Sophia.\n\n"

        "Jerusalem: The Emanation of the Giant Albion (1804–1820), Blake's "
        "longest and most complex prophetic book, narrates the fall and "
        "redemption of Albion — a giant figure embodying both England and "
        "universal humanity — through the separation and reunification of "
        "his spiritual components. The four 'Zoas' (Urizen, Luvah, Tharmas, "
        "Urthona/Los) represent faculties of the cosmic human that have fallen "
        "into mutual conflict; their reintegration into the unified fourfold "
        "humanity is the book's telos. This fourfold scheme has been traced "
        "to Böhme's four 'properties of nature' (fire, light, sound, matter) "
        "and to the alchemical four elements; the redemptive process moves "
        "through stages analogous to the alchemical nigredo, albedo, citrinitas, "
        "and rubedo.\n\n"

        "Blake's debts to esoteric tradition are documented most systematically "
        "by Kathleen Raine in Blake and Tradition (2 vols, 1969). Raine argued "
        "that Blake's mythology is comprehensible only when read against Thomas "
        "Taylor's translations of Neoplatonic texts (Taylor was Blake's "
        "contemporary, and Blake knew him personally), against the Hermetic "
        "tradition mediated through Agrippa and Paracelsus, against Böhme "
        "(whose Aurora and other works Blake read), and against Swedenborg "
        "(whom he read, annotated, and satirized). The influence of Böhme "
        "is particularly important: Blake's concept of the Contraries, his "
        "account of the fall as a contraction of vision rather than a moral "
        "transgression, his emphasis on the 'fire' of imagination and the "
        "'light' of vision, and his language of 'the Abyss' and 'Eternity' "
        "are all saturated with Böhmian vocabulary.\n\n"

        "Blake also knew Paracelsus: his concept of the 'Spectre' — the "
        "rational, mechanical aspect of the self that has separated from "
        "the imaginative core — has been compared to the Paracelsian concept "
        "of the astral body that persists after death as a 'specter.' His "
        "insistence that the imagination transforms the material world, that "
        "vision is not a passive reception of external reality but an active "
        "creation, resonates with Paracelsian and Hermetic ideas of the "
        "imagination as a formative power. Raine's reading has been criticized "
        "for making Blake too systematically 'Neoplatonic' and for underplaying "
        "the originality of his mythological invention; subsequent scholars "
        "including Jon Mee and E.P. Thompson have emphasized the Dissenting "
        "Protestant and radical political dimensions of his work alongside "
        "the esoteric. Blake is most accurately seen as a figure who absorbed "
        "esoteric traditions deeply and transformed them into something "
        "unmistakably his own."
    ),
    'key_works': [
        "The Marriage of Heaven and Hell (1790)",
        "The Book of Urizen (1794)",
        "The Book of Los (1795)",
        "Milton: A Poem (1804–1811)",
        "Jerusalem: The Emanation of the Giant Albion (1804–1820)",
        "Annotations to Swedenborg, Lavater, and other authors"
    ]
}

# ── id=88: Robert Boyle ──────────────────────────────────────────────────────

updates[88] = {
    'essay': (
        "Robert Boyle (1627–1691) was an Anglo-Irish natural philosopher and chemist "
        "whose experimental program and corpuscular philosophy were foundational for "
        "the emerging discipline of chemistry and for the institutional culture of "
        "the Royal Society. Born at Lismore Castle in County Waterford as the "
        "fourteenth child of the first Earl of Cork, he was educated at Eton "
        "and through private tutors in England and on the Continent, where he "
        "encountered Galileo's mechanics and the new mechanical philosophy. He "
        "settled in Oxford in 1655, where he worked with Robert Hooke on the "
        "air pump, and moved to London in 1668. He never married and declined "
        "the presidency of the Royal Society and a bishopric.\n\n"

        "The Sceptical Chymist, or Chymico-Physical Doubts and Paradoxes (1661) "
        "is Boyle's most celebrated work and a foundational text of modern chemistry. "
        "Cast as a dialogue among several speakers — a Peripatetic Aristotelian, "
        "a Paracelsian, and the Sceptick Carneades (Boyle's mouthpiece) — it "
        "argues against both the Aristotelian four-element theory and the "
        "Paracelsian three-principle theory (sulphur, mercury, salt) as "
        "adequate accounts of the material composition of chemical substances. "
        "Carneades argues that neither set of principles can be recovered "
        "unaltered from all chemical analysis — some substances yield more "
        "or fewer than three or four components — and that the terms 'element' "
        "and 'principle' need to be defined empirically rather than assumed "
        "philosophically. Boyle's positive proposal — that matter consists of "
        "minute corpuscles that group into clusters with specific sizes, shapes, "
        "and motions — provided a mechanical framework for chemical explanation "
        "that did not depend on the contested theoretical categories of either "
        "tradition. The Sceptical Chymist did not, as was long assumed, "
        "definitively establish the modern definition of 'element'; its "
        "argument is primarily negative and critical, clearing ground rather "
        "than building a systematic chemistry.\n\n"

        "Boyle's alchemical engagement is one of the most important and "
        "least-known aspects of his career, and its recovery by historians "
        "since the 1990s has substantially altered the picture of the "
        "Scientific Revolution. Boyle believed in the philosophical "
        "possibility — and was persuaded of the practical achievability — "
        "of metallic transmutation. He corresponded with Isaac Newton on "
        "alchemical matters in 1676; the correspondence, which survives "
        "only partially, concerned a 'mercury' that could be 'excited' "
        "to multiply in a manner associated with the philosophers' stone, "
        "and both men were sufficiently cautious about the implications "
        "to communicate obliquely. Lawrence Principe's The Aspiring Adept: "
        "Robert Boyle and His Alchemical Quest (1998) is the definitive "
        "study: Principe worked through Boyle's manuscript alchemical "
        "notebooks and demonstrated that Boyle spent decades in laboratory "
        "pursuit of the philosophers' stone, that he believed he had "
        "witnessed a transmutation, and that his experimental chemistry "
        "and his alchemical research were not compartmentalized but deeply "
        "intertwined.\n\n"

        "In 1689, Boyle lobbied successfully for the repeal of the English "
        "statute of 1404 against 'multiplying gold and silver' — the law "
        "that had made alchemical practice legally risky in England. The "
        "repeal, engineered through Boyle's connections, reflected his "
        "genuine conviction that transmutation was possible and that the "
        "law was an obstacle to legitimate inquiry. Newton supported the "
        "repeal and shared Boyle's concern that if transmutation became "
        "publicly known and practiced, the destabilization of the monetary "
        "system would result — a concern that assumes the practice was real.\n\n"

        "Boyle's theological writings complement his natural philosophy. "
        "His Occasional Reflections (1665), The Excellence of Theology (1674), "
        "and The Christian Virtuoso (1690–91) argue that the study of nature "
        "is a form of religious devotion, that the 'book of nature' reveals "
        "God's wisdom alongside the book of scripture, and that the natural "
        "philosopher's work is inherently pious. This 'physico-theology' "
        "provided a framework within which alchemy — understood as the "
        "investigation of God's created natural powers — could be pursued "
        "as a religious as well as a scientific activity.\n\n"

        "Boyle's case is exemplary of the entanglement of what later "
        "historiography would separate as 'science' and 'occult.' The man "
        "who argued against Paracelsian three-principles in the Sceptical "
        "Chymist simultaneously pursued the Paracelsian philosophers' stone "
        "in his laboratory. His corpuscular philosophy, often cited as a "
        "founding document of mechanical chemistry, was developed alongside "
        "an alchemical research program in which active, vital principles "
        "in matter played a central role. The categories of 'mechanical' "
        "and 'occult' were not yet the clean opposites they would become "
        "in later historiography; Boyle worked in a world where the "
        "boundaries had not been drawn."
    ),
    'key_works': [
        "The Sceptical Chymist (1661)",
        "The Origin of Forms and Qualities (1666)",
        "Some Considerations Touching the Usefulness of Experimental Natural Philosophy (1663)",
        "The Christian Virtuoso (1690–91)",
        "Alchemical manuscripts (unpublished laboratory notebooks)"
    ]
}

# ── id=83: Andreas Libavius ──────────────────────────────────────────────────

updates[83] = {
    'essay': (
        "Andreas Libavius (c.1555–1616) was a German physician, teacher, and "
        "iatrochemist whose Alchymia (1597; expanded edition 1606) is generally "
        "regarded as the first systematic textbook of chemistry — a work that "
        "organized the discipline's operations, equipment, and theory in a "
        "methodical sequence accessible to university-trained readers. Born "
        "probably at Halle in Saxony, he studied medicine and worked as a "
        "physician and schoolmaster in Rothenburg ob der Tauber and then "
        "Coburg, where he directed a gymnasium. His career was defined by "
        "his simultaneously embracing chemical medicine and attacking "
        "Paracelsian mysticism — a position that required careful navigation "
        "of the polemical landscape of late-sixteenth-century German learned culture.\n\n"

        "The Alchymia (full title: Alchymia, Recognita, Emendata, et Aucta, tum "
        "Dogmatibus et Experimentis Nonnullis, 1597; expanded 1606) proceeds in "
        "two parts. The first part, treating the instruments and spaces of "
        "chemical work (what we might call laboratory design), describes in "
        "systematic detail the furnaces, vessels, and apparatus required for "
        "each class of operation. Libavius's vision of an ideal chemical "
        "laboratory — with separate rooms for distillation, calcination, "
        "and other operations, organized for efficient work — was the first "
        "systematic architectural treatment of the laboratory as a specialized "
        "space. The second part covers chemical operations and substances: "
        "distillation, extraction, calcination, cementation, and the "
        "preparation of specific substances including acids, salts, and "
        "metallic compounds. The text is organized as a reference work: "
        "practical, clear, and designed for a reader who already has some "
        "familiarity with chemical procedures.\n\n"

        "Libavius's relationship to Paracelsianism defines his intellectual "
        "position. He accepted the legitimacy of chemical medicine — the "
        "use of distilled and chemically prepared remedies — and engaged "
        "seriously with the theoretical framework of Paracelsian chemistry. "
        "But he rejected what he saw as Paracelsus's obscurantism, mystical "
        "excess, and hostility to classical learning. Where Paracelsus "
        "had attacked Galenic medicine wholesale and replaced it with a "
        "new cosmological-theological system, Libavius sought to integrate "
        "chemical medicine into the existing framework of university-trained "
        "natural philosophy. His Paracelsian polemics — particularly in "
        "his Defensio et Declaratio Perspicua Alchymiae Transmutatoriae (1604) "
        "and in extended exchanges with the Paracelsian school — attacked "
        "Oswald Croll, Joseph Duchesne (Quercetanus), and others for "
        "precisely the mystical and anti-rational tendencies he found "
        "in Paracelsus himself.\n\n"

        "This position — defending chemical medicine while attacking Paracelsian "
        "mysticism — made Libavius a crucial figure in the institutionalization "
        "of chemistry. By presenting chemical operations in the organized, "
        "methodical format familiar from university natural philosophy, and by "
        "grounding chemical medicine in Aristotelian natural philosophy rather "
        "than Paracelsian cosmological speculation, he made iatrochemistry "
        "more respectable to the Galenic medical establishment without abandoning "
        "the chemical procedures that made it therapeutically distinctive. His "
        "Lutheran confessional identity reinforced this approach: he associated "
        "Paracelsian mysticism with religious heterodoxy and his own reformed "
        "chemistry with Protestant orthodoxy and rational discipline.\n\n"

        "Libavius also wrote extensively on the Rosicrucian manifestos when "
        "they appeared: his Analysis Confessionis Fraternitatis de Rosea Cruce "
        "(1615) is an early critical engagement that combines genuine interest "
        "in the manifestos' reform program with deep suspicion of their mystical "
        "and cryptic elements. His response typifies the reaction of "
        "academically trained chemical physicians: attracted by the promise "
        "of a reformed medicine and a community of learned reformers, "
        "repelled by the obscurity and occultism that he associated with "
        "Paracelsian excess and that the manifestos seemed to promote."
    ),
    'key_works': [
        "Alchymia (1597; expanded edition 1606)",
        "Defensio et Declaratio Perspicua Alchymiae Transmutatoriae (1604)",
        "Analysis Confessionis Fraternitatis de Rosea Cruce (1615)",
        "Commentariorum Alchymiae (1606)"
    ]
}

# ── id=73: Oswald Croll ──────────────────────────────────────────────────────

updates[73] = {
    'essay': (
        "Oswald Croll (c.1563–1609) was a German physician and Paracelsian whose "
        "Basilica Chemica (Chemical Palace, 1609), published posthumously, became "
        "the most comprehensive and widely distributed compendium of Paracelsian "
        "pharmaceutical medicine of the early seventeenth century. Born probably "
        "at Wetter in Hesse, he studied at Marburg, and subsequently traveled "
        "and studied across Germany, France, Italy, Hungary, and Bohemia, acquiring "
        "Paracelsian medical learning wherever he could find it. He came eventually "
        "into the service of Christian I of Anhalt-Bernburg, one of the most "
        "important Calvinist princes of the Holy Roman Empire and the political "
        "patron who organized the Protestant alliance that would lead, after "
        "Croll's death, to the Bohemian revolt of 1618 and the opening of the "
        "Thirty Years' War.\n\n"

        "The Basilica Chemica (full title: Basilica Chymica, Continens Philosophicam "
        "Propria Laborum Experientia Confirmatam Descriptionem et Usum Remediorum "
        "Chymicorum ...) was dedicated to Rudolf II, the Habsburg emperor at Prague "
        "whose court was the great centre of Paracelsian natural philosophy, alchemy, "
        "and esoteric learning in the late sixteenth and early seventeenth centuries. "
        "The dedication to Rudolf — by a Protestant physician in the service of "
        "a Calvinist prince — reflects both the cross-confessional character of "
        "Paracelsian medical culture and the magnetic attraction of Rudolf's Prague "
        "for anyone seeking patronage in the hermetic-chemical arts.\n\n"

        "The text opens with an extended Prooemium (Preface) — longer than most "
        "contemporary prefaces and essentially a manifesto for Paracelsian medicine "
        "— that is partly Croll's own work and partly dependent on Petrus Severinus's "
        "Idea Medicinae Philosophicae (1571), the most systematic earlier defense "
        "of Paracelsian natural philosophy. The Prooemium argues for the superiority "
        "of Paracelsian over Galenic medicine on both philosophical and empirical "
        "grounds, positions chemical medicine within a providential Christian "
        "framework (God has inscribed remedies in nature through signatures and "
        "correspondences for the benefit of humanity), and develops the doctrine "
        "of signatures — the idea that the outer appearance of plants, minerals, "
        "and other natural things reveals their therapeutic uses — in considerable "
        "detail. The doctrine of signatures was not new, but Croll's elaboration "
        "of it was the most systematic and influential early seventeenth-century "
        "statement, and the Prooemium became the locus classicus for subsequent "
        "discussions of the theory.\n\n"

        "The main body of the Basilica Chemica provides practical formulas for "
        "the preparation of hermetic remedies: specifics for each disease, "
        "organized by the affected organ or bodily system. Each remedy is "
        "prepared by chemical means — distillation, calcination, extraction, "
        "or other Paracelsian operations — rather than by the Galenic methods "
        "of decoction and compounding. The remedies include antimony preparations "
        "(strongly endorsed by Croll, as by most Paracelsians), aurum potabile "
        "(drinkable gold), vitriol preparations, and many others. The practical "
        "pharmaceutical detail is considerable: Croll provides temperatures, "
        "durations, proportions, and procedures with a specificity that made "
        "the text genuinely useful for practitioners.\n\n"

        "The Basilica Chemica went through numerous editions and translations "
        "within decades of its publication: it appeared in Latin, German, French, "
        "and English (The Royal and Practical Chymist, 1670), becoming one of "
        "the most widely distributed medical-chemical texts of the seventeenth "
        "century. It was the standard reference work for Paracelsian pharmaceutics "
        "throughout the period when iatrochemistry was the major alternative to "
        "Galenic medicine — from roughly 1609 to the Boylean revolution of the "
        "1660s–1680s — and its influence is visible in the prescribing practices "
        "of physicians across Europe who never read Paracelsus directly but "
        "worked from Croll's systematization. The text's relationship to the "
        "Rosicrucian milieu is significant: Croll's patron Christian of Anhalt "
        "was deeply involved in the political and intellectual networks that "
        "produced the Rosicrucian manifestos in 1614–15, and the Basilica "
        "Chemica circulated in the same milieu of Protestant Paracelsian "
        "reform that the manifestos addressed."
    ),
    'key_works': [
        "Basilica Chemica (Chemical Palace, 1609; posthumously published)",
        "Treatises on Paracelsian medicine (incorporated in Basilica)"
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
