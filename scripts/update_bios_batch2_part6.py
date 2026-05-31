#!/usr/bin/env python3
"""
update_bios_batch2_part6.py
Full essays for: id=9 Claude de Saint-Martin, id=44 George Cheyne,
id=46 Jane Lead, id=48 Henry More.
"""

import json, os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prototype_data.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

updates = {}

# ── id=9: Claude de Saint-Martin ────────────────────────────────────────────

updates[9] = {
    'essay': (
        "Louis-Claude de Saint-Martin (1743–1803), known as 'le Philosophe Inconnu' "
        "(the Unknown Philosopher), was a French mystic and theosophical writer whose "
        "writings synthesized the initiatic tradition of Martinez de Pasqually with the "
        "mystical theosophy of Jacob Böhme, producing a body of work that became the "
        "intellectual foundation of what would later be called 'Martinism' — the "
        "French esoteric tradition that has borne his name in initiatic lodges from "
        "the nineteenth century to the present. Born at Amboise into a minor noble "
        "family, he received a legal education and briefly served as an army officer "
        "before his encounter with Martinez de Pasqually transformed his life's direction.\n\n"

        "Saint-Martin was initiated into the Order of Élus Coëns (Elect Priests) "
        "founded by Martinez de Pasqually (c.1727–1774), a theurgist and Kabbalist "
        "who taught a system of ritual invocation aimed at the reintegration of "
        "fallen humanity into its original divine state. Pasqually's theurgy was "
        "elaborate and liturgical, involving complex rituals, passes, and the "
        "invocation of spiritual presences. Saint-Martin served as Pasqually's "
        "secretary in Bordeaux from 1768 to 1771, absorbing the Coëns system "
        "at its most intensive; after Pasqually's death in Saint-Domingue in 1774, "
        "Saint-Martin gradually moved away from the ritual emphasis toward what "
        "he called the 'inner way' — direct spiritual transformation without "
        "external ceremony.\n\n"

        "Des Erreurs et de la Vérité, ou les Hommes Rappelés au Principe Universel "
        "de la Science (On Errors and Truth, or Men Called Back to the Universal "
        "Principle of Science, 1775), published pseudonymously as by 'a Unknown "
        "Philosopher' (le Philosophe Inconnu), is Saint-Martin's first and most "
        "substantial independent work. Composed under the influence of the Pasquallian "
        "framework but already moving toward a more philosophical register, it presents "
        "a theosophical account of humanity's original dignity, its fall into material "
        "existence, and the path of restoration to divine union. The argument proceeds "
        "by way of what Saint-Martin calls 'numbers' — not mathematical quantities "
        "but symbolic principles or forces — and is notoriously obscure, a quality "
        "that Saint-Martin later acknowledged and partly regretted. The text "
        "circulated widely in French Masonic and para-Masonic circles and was "
        "translated into German, contributing to the currency of Martinist ideas "
        "in German theosophical and Pietist networks.\n\n"

        "Tableau Naturel des Rapports qui Existent entre Dieu, l'Homme, et l'Univers "
        "(Natural Table of the Relations Between God, Man, and the Universe, 1782) "
        "is a systematic expansion of the themes of Des Erreurs et de la Vérité, "
        "somewhat less obscure in presentation. It organizes Saint-Martin's "
        "theosophical cosmology — the emanation and fall of creation, the structure "
        "of the spiritual world, the nature and destiny of the human soul — into "
        "a more systematic framework.\n\n"

        "The turn to Böhme is the decisive event in Saint-Martin's intellectual "
        "development. He encountered Jacob Böhme's writings — in the Gichtel "
        "German edition — around 1788, and his subsequent works reflect a profound "
        "absorption of Böhmian theosophy. L'Homme de Désir (Man of Desire, 1790) "
        "is the first major work of Saint-Martin's Böhmian phase: a lyric- "
        "philosophical meditation on the soul's longing for its divine origin, "
        "organized around the concept of desire (désir) as the fundamental "
        "orientation of the spiritually awakened person. The prose is more "
        "lyrical and less systematic than the earlier works, closer to devotional "
        "literature than to philosophical argument.\n\n"

        "Le Ministère de l'Homme-Esprit (The Ministry of the Spirit-Man, 1802), "
        "one of his last works, develops the concept of the 'spirit-man' — the "
        "regenerated human being who has recovered the divine image — as an "
        "active mediating force between God and the fallen world. The 'ministry' "
        "of the title is the vocation of the spiritually advanced individual "
        "to serve as an instrument of divine restoration in the world. "
        "This concept connects Saint-Martin's mysticism to a tradition of "
        "theurgical or redemptive action in the world, distinct from the "
        "purely contemplative ideal.\n\n"

        "Saint-Martin translated several of Böhme's works into French, making "
        "Böhmian theosophy accessible to French readers for the first time. "
        "His French Böhme translations were the primary vehicle through which "
        "Böhmian ideas entered French Romantic and post-Revolutionary esoteric "
        "culture. The nineteenth-century Martinist tradition — organized as "
        "initiatic lodges by Gérard Encausse (Papus) in the 1880s–90s — "
        "drew on Saint-Martin's name and on the Pasquallian ritual heritage, "
        "though Saint-Martin himself had moved away from ritual initiation "
        "toward the interior path. The Martinist Society that Papus founded "
        "is thus a hybrid: Pasquallian in its ritualism, Saint-Martinian "
        "in its name and some of its theology."
    ),
    'key_works': [
        "Des Erreurs et de la Vérité (On Errors and Truth, 1775)",
        "Tableau Naturel des Rapports... (Natural Table of Relations, 1782)",
        "L'Homme de Désir (Man of Desire, 1790)",
        "Le Nouvel Homme (The New Man, 1792)",
        "Le Ministère de l'Homme-Esprit (The Ministry of the Spirit-Man, 1802)",
        "French translations of Jacob Böhme (Aurora, De Tribus Principiis, etc.)"
    ]
}

# ── id=44: George Cheyne ─────────────────────────────────────────────────────

updates[44] = {
    'essay': (
        "George Cheyne (1671–1743) was a Scottish physician and author whose writings "
        "on diet, health, and nervous disorders made him one of the most widely read "
        "medical writers of the early eighteenth century in Britain. Born in "
        "Aberdeenshire, he studied medicine at Edinburgh under the Newtonian physician "
        "Archibald Pitcairne, moved to London around 1700, and eventually settled "
        "in Bath, where he practiced medicine among the wealthy patients who came "
        "to take the waters. He was himself severely obese for much of his adult "
        "life — he reportedly reached thirty-two stone (over 200 kg) — and his "
        "dietary writings were motivated partly by his own struggles with "
        "weight, digestion, and nervous complaints.\n\n"

        "An Essay of Health and Long Life (1724) is Cheyne's most practical work: "
        "a guide to maintaining health through regulated diet, exercise, air, "
        "sleep, and the passions. The text draws on Hippocratic and Galenic "
        "regimen literature but integrates Newtonian physiological concepts "
        "— the solid fibers of the body, the fluid that circulates through them, "
        "the nervous system as a hydraulic mechanism — with practical advice on "
        "eating, drinking, and the management of daily life. Its advice was "
        "sensible enough to remain useful: moderate eating, preference for "
        "vegetables and milk over heavy meats, regular exercise, avoidance of "
        "alcohol. The text went through twelve editions in Cheyne's lifetime "
        "and was widely read by educated readers in Britain and America.\n\n"

        "The English Malady, or a Treatise of Nervous Diseases of All Kinds, as "
        "Spleen, Vapours, Lowness of Spirits, Hypochondriacal and Hysterical "
        "Distempers, &c. (1733) is his most historically important work. Cheyne "
        "argued that England was experiencing an epidemic of nervous disorders — "
        "spleen, vapors, hypochondria, melancholy — disproportionate to other "
        "nations, and explained this epidemic by reference to England's particular "
        "conditions: its damp climate, its rich and refined diet, the sedentary "
        "indoor lives of its commercial and professional classes, and the "
        "intensity of its commercial and intellectual culture. The paradox "
        "Cheyne identifies — that England's prosperity and civilization are "
        "also the sources of its characteristic disease — is a significant "
        "contribution to the emerging literature on the social causes of "
        "illness. He advocated vegetarian diet and milk as remedies for "
        "the nervous constitution, and his own experience of recovery through "
        "dietary change was offered as evidence.\n\n"

        "Cheyne's connection to esotericism and mysticism is real but indirect. "
        "He was a friend of John Wesley and moved in Methodist and proto-evangelical "
        "circles; his later writings incorporate a religious dimension, presenting "
        "spiritual discipline alongside physical regimen as necessary for health. "
        "An Essay on Regimen (1740) is the most explicitly theosophical of his "
        "works, arguing that the body is a spiritual as well as physical entity "
        "and that Newtonian natural philosophy, properly understood, confirms "
        "the Platonic and Christian account of matter and spirit. Cheyne read "
        "broadly in the mystical tradition — he was familiar with Böhme, "
        "with the Cambridge Platonists, and with the Pietist tradition — "
        "and his physiological account of the 'nervous fluid' as a subtle "
        "vehicle of spiritual influence connects to the Paracelsian-Helmontian "
        "tradition of active vital principles in the body.\n\n"

        "For the history of esotericism, Cheyne's significance lies in "
        "the intersection he inhabits between medical physiology, dietary "
        "reform, and mystical theology. His concept of the refined nervous "
        "constitution — the sensitive, spiritually inclined individual "
        "who is most prone to nervous disease but also most capable of "
        "spiritual development — participated in the construction of a "
        "cultural type that would recur in Romantic and Victorian "
        "esotericism: the spiritual seeker whose physical delicacy is "
        "a sign of spiritual refinement. His promotion of vegetarianism "
        "as a spiritual discipline connects to the vegetarian and dietary "
        "reform movements within Victorian theosophy and occultism. "
        "His patient Samuel Richardson, who corresponded with Cheyne "
        "about health and spirituality, absorbed his ideas into the "
        "emotional-physiological sensibility of the English novel."
    ),
    'key_works': [
        "An Essay of Health and Long Life (1724)",
        "The English Malady (1733)",
        "An Essay on Regimen (1740)",
        "Philosophical Principles of Religion, Natural and Revealed (1705/1715)"
    ]
}

# ── id=46: Jane Lead ─────────────────────────────────────────────────────────

updates[46] = {
    'essay': (
        "Jane Lead (1624–1704) was an English visionary, mystic, and writer whose "
        "accounts of spiritual visions and her interpretation of Jacob Böhme's "
        "theosophy made her one of the most significant transmitters of Behmenism "
        "to English and Continental audiences in the late seventeenth century. "
        "Born Jane Ward at Letheringsett in Norfolk, she married William Lead in "
        "1644; after his death in 1670 she entered the circle of John Pordage "
        "(1607–1681), an Anglican clergyman who had been ejected from his "
        "living in 1655 for his Böhmian mystical practices and who maintained "
        "a community of Behmenist spirituality in London. Pordage became her "
        "spiritual father and intellectual guide; his influence is pervasive "
        "in her early writings.\n\n"

        "Lead's visionary life began in earnest in 1670 after her husband's "
        "death, and she maintained detailed journals of her spiritual experiences "
        "over decades. Her vision of the divine Sophia — the heavenly wisdom "
        "figure whom she encountered repeatedly in trance states — is the "
        "central event of her spiritual autobiography. Sophia, in Lead's "
        "accounts, appears as a celestial woman who reveals the secrets of "
        "divine regeneration, the fall and restoration of humanity, and the "
        "coming of a new spiritual age. The Sophia figure draws on Böhme's "
        "concept of the divine wisdom as the Virgin-Sophia, but Lead develops "
        "her into a more personal and visionary presence than Böhme's "
        "theological concept.\n\n"

        "The Heavenly Cloud Now Breaking (1681) is Lead's first published work, "
        "an account of her vision of the celestial world and the beginning of "
        "her dialogue with Sophia. The Revelation of Revelations (1683) develops "
        "the Johannine theme of the Apocalypse in Böhmian terms: the revelation "
        "of the divine mysteries is an inner event, the opening of the spiritual "
        "senses, rather than an external historical catastrophe. These early "
        "texts established Lead's distinctive voice: lyrical, visionary, "
        "grounded in a specific experiential record rather than systematic "
        "theology.\n\n"

        "The Enochian Walks with God (1694) recounts Lead's visionary "
        "encounters with the figure of Enoch — the biblical patriarch "
        "who 'walked with God' and was translated to heaven — as a type "
        "of the spiritually advanced soul who walks with God in the "
        "present inner life. The title evokes both the biblical Enoch "
        "and the Enochian tradition of angelic communication associated "
        "with John Dee, though Lead does not explicitly reference Dee; "
        "the angelic communications she receives are Böhmian in their "
        "theological content.\n\n"

        "A Fountain of Gardens (4 vols, 1696–1701) is Lead's most substantial "
        "work and her spiritual diary in its most extended form: four volumes "
        "of dated journal entries recording visions, dialogues with Sophia "
        "and other heavenly figures, and reflections on the Böhmian theosophy. "
        "The work is remarkable as a sustained personal spiritual record; "
        "few comparable documents exist from the period. The garden imagery "
        "of the title — the fountain as the divine source, the garden as "
        "the cultivated interior life — connects to the alchemical hortus "
        "philosophicus (philosophical garden) tradition and to the Böhmian "
        "imagery of seeds and growth.\n\n"

        "In 1694 Lead and her supporters founded the Philadelphian Society "
        "(named after the Philadelphian church of Revelation 3, the church "
        "that keeps the faith in the last age) in London. The Society — "
        "which included the physician Francis Lee, who became Lead's "
        "amanuensis and editor — aimed to gather those who had the "
        "'inner church' experience across confessional boundaries: "
        "Anglicans, Quakers, and Continental Protestants were all welcome. "
        "It published a journal, Theosophical Transactions, in 1697, "
        "making it one of the earliest theosophical periodicals.\n\n"

        "Lead's texts were translated into German and Dutch and circulated "
        "widely in the Continental Böhmist networks centered in Amsterdam "
        "(where Johann Georg Gichtel presided over the Böhmist community) "
        "and in German Pietist circles. Her influence on German Pietism "
        "has been documented by Rufus Jones and more recently by scholars "
        "of Württemberg Pietism; her concept of the millennial spiritual "
        "church and the inner rebirth fed into the radical Pietist "
        "tradition of Johann Wilhelm Petersen and his wife Johanna Eleonora. "
        "Lead represents a convergence of English Behmenism with "
        "Continental Pietist millenarianism that was influential "
        "through the early decades of the eighteenth century and "
        "that fed ultimately into the theosophical currents of the "
        "nineteenth century."
    ),
    'key_works': [
        "The Heavenly Cloud Now Breaking (1681)",
        "The Revelation of Revelations (1683)",
        "The Enochian Walks with God (1694)",
        "A Fountain of Gardens (4 vols, 1696–1701)",
        "The Wonders of God's Creation Manifested in the Variety of Eight Worlds (1695)"
    ]
}

# ── id=48: Henry More ────────────────────────────────────────────────────────

updates[48] = {
    'essay': (
        "Henry More (1614–1687) was an English philosopher and theologian, one of "
        "the central figures of the Cambridge Platonists — the group of mid-seventeenth- "
        "century philosophers at Emmanuel College, Cambridge who sought to reconcile "
        "Neoplatonic metaphysics with Protestant Christianity and with the new "
        "natural philosophy. Born at Grantham in Lincolnshire into a Calvinist "
        "family, he rejected Calvinist predestination as a student at Cambridge, "
        "finding it incompatible with the goodness of God and with his own "
        "experience of divine benevolence; he remained at Emmanuel College "
        "as a Fellow for the rest of his life, declining preferment in order "
        "to pursue philosophy and spiritual reflection.\n\n"

        "More's early philosophical poetry — Psychodia Platonica (1642), a set "
        "of philosophical poems on the soul's nature and ascent, followed by "
        "Antipsychopannychia (1642) — established his Neoplatonic commitments: "
        "the soul as preexistent, divine in origin, capable of progressive "
        "purification and ascent toward God. The tone is elevated and "
        "devotional, presenting philosophical argument through lyric verse "
        "in the tradition of Spenser. More's verse was admired in his "
        "lifetime and was reprinted in his Philosophical Poems (1647) "
        "alongside longer philosophical poems on the soul and the divine.\n\n"

        "An Antidote Against Atheism (1653) is More's first systematic "
        "philosophical argument for the existence of God and spiritual "
        "reality, directed against the perceived atheistic implications "
        "of materialist natural philosophy (he had Thomas Hobbes's "
        "materialism particularly in mind). The text argues from the "
        "concept of God as the most perfect being, from the innate idea "
        "of God in the human mind, and from the evidence of divine "
        "providence in nature. More also adduces cases of witchcraft, "
        "apparitions, and spirit communication as evidence for the "
        "reality of an immaterial world — a move that has struck later "
        "readers as odd but reflects his conviction that dismissing "
        "reported spirit phenomena was precisely the kind of dogmatic "
        "materialist reductionism he was fighting.\n\n"

        "The Immortality of the Soul (1659) is More's most systematic "
        "treatment of the soul's nature, arguing for its immateriality, "
        "preexistence, and survival of death. He develops a sophisticated "
        "account of the soul's relationship to matter through his concept "
        "of the 'Spirit of Nature' (also called the Hylarchic Principle "
        "or Anima Mundi): a subtle immaterial substance intermediate "
        "between soul and matter that serves as the vehicle through which "
        "souls act on bodies and through which divine providence governs "
        "the physical world. This concept, elaborated in the Enchiridion "
        "Metaphysicum (1671), is More's most distinctive philosophical "
        "contribution and his most important for the history of natural "
        "philosophy.\n\n"

        "The Enchiridion Metaphysicum (Metaphysical Handbook, 1671) is More's "
        "most technically philosophical work: a systematic metaphysics of "
        "space, matter, soul, and divine action. More argues for the "
        "existence of absolute space as a divine attribute — space is the "
        "divine extension, the infinite presence of God in the world — "
        "a concept that Isaac Newton absorbed and transformed into the "
        "absolute space of the Principia. The Spirit of Nature is here "
        "developed as the principle through which God acts in the physical "
        "world without immediate miraculous intervention: it is the "
        "immaterial ordering principle that explains the organized "
        "regularity of natural phenomena without reducing nature to "
        "mere mechanical causation. More was arguing against Descartes's "
        "mechanism, which he saw as leaving no room for spirit or "
        "providence in nature.\n\n"

        "More's relationship to esotericism is significant and underappreciated. "
        "He was a close friend of Anne Conway (1631–1679), the philosopher "
        "whose Principles of the Most Ancient and Modern Philosophy (written "
        "c.1671–76, published 1690) developed a vitalist metaphysics deeply "
        "indebted to Kabbalah and to the Quaker-Behmenist tradition; "
        "Conway's correspondence with More was extensive and philosophically "
        "serious. More introduced Conway to Francis Mercury van Helmont "
        "(son of the iatrochemist Jan Baptist van Helmont and himself "
        "a wandering Kabbalist and theosopher), and van Helmont became "
        "Conway's philosophical companion in her last years. Through "
        "these personal connections, More was embedded in a network "
        "that included Kabbalistic, Böhmian, and alchemical currents "
        "alongside the academic Cambridge Platonism for which he is "
        "primarily remembered.\n\n"

        "More's engagement with Henry Vaughan (the poet and alchemist) "
        "and his broader awareness of Hermetic and alchemical traditions "
        "is visible in his discussions of the anima mundi and active "
        "principles in nature. His concept of the Spirit of Nature "
        "provided a philosophical vocabulary within which alchemical "
        "active principles — the archeus, the seminal reasons, the "
        "vegetable spirit — could be articulated without the mystical "
        "and astrological elaborations of Paracelsian alchemy. "
        "Newton's engagement with More's metaphysics, and Newton's "
        "own alchemical research, suggests that the Cambridge Platonist "
        "tradition provided one of the frameworks within which "
        "alchemical ideas survived and developed in the late "
        "seventeenth century."
    ),
    'key_works': [
        "Psychodia Platonica (1642; philosophical poems on the soul)",
        "An Antidote Against Atheism (1653)",
        "The Immortality of the Soul (1659)",
        "Enchiridion Ethicum (1667)",
        "Enchiridion Metaphysicum (1671)",
        "Divine Dialogues (1668)"
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
