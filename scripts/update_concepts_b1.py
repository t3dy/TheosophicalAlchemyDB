#!/usr/bin/env python3
"""
update_concepts_b1.py
Expand 8 concept entries (ids 41-48) with full scholarly apparatus:
essay (800-1100 words), summary (2-3 sentences), operational_meaning,
philosophical_meaning, spiritual_meaning, transmission_genealogy.
"""

import json, sys, os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prototype_data.json')

UPDATES = {
    41: {
        "summary": (
            "Inner Transformation is the alchemical conviction that the Great Work enacts genuine change in the practitioner — not merely symbolic, moral, or metaphorical change, but an ontological shift in consciousness, soul, and embodied selfhood. "
            "The central tension in the tradition runs between three positions: whether practitioner transformation is a prerequisite for transmuting metals, a parallel process unfolding alongside laboratory operations, or in fact the primary goal to which metal-transmutation is instrumental or allegorical. "
            "From Böhme's 'birth of Christ in the soul' to Atwood's mesmeric induction and Jung's individuation, the concept anchors both the spiritual alchemical tradition and modern scholarly debates about alchemy's ultimate aims."
        ),
        "essay": (
            "Inner Transformation is the foundational claim that the alchemical Great Work enacts genuine, irreversible change in the practitioner — not merely edifying symbolism, moral improvement, or intellectual illumination, but an actual ontological shift in consciousness, soul, and embodied self. "
            "The concept sits at the interpretive heart of the entire tradition and generates its most persistent scholarly dispute: is practitioner transformation a prerequisite for transmuting metals, a parallel process developing alongside laboratory operations, or the primary goal to which physical transmutation is instrumental or simply allegorical?\n\n"
            "The earliest stratum of this idea appears in the Greek alchemical papyri and the writings attributed to Zosimos of Panopolis (fl. c. 300 CE), whose visions of a priest undergoing dismemberment and distillation encode an explicit parallel between laboratory processing and the suffering, death, and rebirth of the operator's own pneuma. "
            "Zosimos drew on the Hermetic texts, particularly Poimandres (Corpus Hermeticum I), which narrate the soul's original descent through the planetary spheres — accumulating material characteristics — and its potential return by stripping those accretions away. "
            "For Zosimos, the alchemical vessel was not merely a container of matter but a site of the operator's own transformation; the operations performed on copper or sulfur were simultaneously and inseparably operations on the soul.\n\n"
            "This pneumatic dimension was substantially developed in the late medieval and early modern period through the Christian theological elaboration of alchemy. "
            "The thirteenth-century Rosarium Philosophorum explicitly maps the stages of the opus — nigredo, albedo, rubedo — onto spiritual states: despair and ego dissolution, purification and illumination, reintegration and sanctification. "
            "Benedictus Figulus and later Johann Daniel Mylius radicalized this parallel, insisting that without inner purity the laboratory work could not succeed: the operator's moral and spiritual state was not incidental but causally efficacious. "
            "This position — that transformation is a prerequisite — created an ethical-spiritual framework for laboratory work that distinguished the adept from the merely technically competent 'puffer.'\n\n"
            "Jacob Böhme (1575–1624) gave the concept its most theologically precise articulation in the German Protestant tradition. "
            "For Böhme, the 'birth of Christ in the soul' — the Wiedergeburt or new birth — was the inner Great Work: the divine fire of the Holy Spirit operated on the soul as calcination, dissolution, and coagulation operated on metals, burning away the old Adam and precipitating the new being. "
            "This was not metaphor for Böhme but ontological description: the sulfur, mercury, and salt of his cosmological chemistry were cosmic-spiritual forces operative in the soul itself, and the alchemical stages were actual phases of spiritual regeneration. "
            "His influence on subsequent spiritual alchemy was enormous: Gottfried Arnold, Johann Georg Gichtel, Jane Lead, and the entire Philadelphian movement developed variations on the Böhmean schema.\n\n"
            "The eighteenth century saw a divergence of emphasis. "
            "Martinist and Gold- und Rosenkreutz traditions maintained the operative dimension — the practitioner actually worked, in laboratory or theurgic ritual, to effect real inner change. "
            "Emanuel Swedenborg's correspondences provided a parallel but distinct framework: chemical and natural processes directly corresponded to spiritual realities not as allegory but as structural mirroring, so that understanding chemistry was simultaneously spiritual understanding. "
            "Swedenborg himself claimed his inner senses were permanently opened by a divine illumination in 1745, an event he understood as precisely such an inner transformation.\n\n"
            "Mary Anne Atwood's Suggestive Inquiry into the Hermetic Mystery (1850) — the text that most completely systematized the spiritual alchemical interpretation in the nineteenth century — argued that the Great Work was a mesmeric-magnetic process: the skilled adept induced in a subject (or in themselves through self-directed concentration) an altered state of consciousness that dissolved ordinary selfhood and opened access to deeper spiritual reality. "
            "Atwood's model positioned inner transformation as operative rather than merely symbolic: the mesmeric trance was the solvent, the operator's directed will the fire, and the transformed, illumined consciousness the philosopher's stone. "
            "Her father, Thomas South, famously burned all copies of the first edition immediately after publication, fearing it revealed too much.\n\n"
            "C. G. Jung's psychological interpretation (Psychology and Alchemy, 1944; Mysterium Coniunctionis, 1955–56) transformed the concept's cultural reach. "
            "Jung argued that the alchemists had projected unconscious psychological contents onto matter: the stages of the opus mapped the individuation process, the integration of shadow, anima/animus, and Self that constituted psychological wholeness. "
            "The philosopher's stone was the Self as such — the centre and totality of the psyche. "
            "Although many historians of alchemy (Lawrence Principe, William Newman) have challenged Jung's reading as anachronistic and have demonstrated that many alchemists were primarily laboratory practitioners with no interest in psychological development, Jung's interpretation has proven extraordinarily generative for twentieth-century esoteric traditions and psychological culture.\n\n"
            "The scholarly consensus emerging from Principe, Newman, Zuber, and Hanegraaff distinguishes carefully between historical positions. "
            "Some alchemists (Zosimos, the spiritual alchemical tradition from Böhme through Atwood) genuinely understood their work as primarily transformative of the practitioner. "
            "Others (most laboratory practitioners from Jabir through the seventeenth century) were principally interested in material results, with spiritual or moral language serving rhetorical or protective functions. "
            "The concept of inner transformation must therefore be traced as a living tradition with specific proponents and textual genealogy, not universalized as the hidden meaning of all alchemy.\n\n"
            "What practitioners actually did varied accordingly. Böhmean practitioners engaged in prolonged meditation on sacred texts and the seven qualities of eternal nature. "
            "Atwood's subjects entered mesmeric trance under skilled induction. "
            "Rosicrucian adepts combined prayer, laboratory work, and moral discipline in a unified practice. "
            "In each case, the claim was not symbolic but operational: specific practices, properly performed, genuinely transformed the practitioner's consciousness and soul."
        ),
        "operational_meaning": (
            "Operationally, inner transformation is enacted through specific disciplines: Böhmean practitioners meditated on the seven qualities of eternal nature and submitted to the divine fire's action in prayer and contemplative reading. "
            "Atwood's operators induced mesmeric trance states through concentrated will and directed imagination, treating the dissociation of ordinary consciousness as the solvent phase of the opus. "
            "Rosicrucian and Gold- und Rosenkreutz practitioners combined laboratory operations, theurgic invocation, moral examination, and graduated initiation as a unified transformative program. "
            "The key operational claim across all variants is that transformation is not merely conceptual: it requires specific acts — performed with specific attention, discipline, and orientation — that genuinely alter the practitioner's interior state."
        ),
        "philosophical_meaning": (
            "Philosophically, inner transformation rests on the Hermetic participatory ontology: the practitioner who fully understands and enacts the Great Work does not merely observe a process from without but enters into it, becoming part of the operation. "
            "This has roots in Neoplatonic epistemology (knowledge is assimilation, not mere representation) and in the alchemical principle that only like can work on like: the operator's soul must resemble the stone it seeks to produce. "
            "The deepest philosophical question is whether transformation is a prerequisite, parallel, or goal — a debate that maps onto broader questions about the relationship between moral purity and natural efficacy in Renaissance natural philosophy."
        ),
        "spiritual_meaning": (
            "Spiritually, inner transformation is the Great Work itself, understood as the opus of the soul: the practitioner undergoes the same death and resurrection as the metals, traversing nigredo (ego-death, despair, dissolution of false selfhood), albedo (purification, illumination, the emergence of the silver consciousness), and rubedo (integration, divine union, the birth of the new being). "
            "Böhme named this the 'birth of Christ in the soul'; the Corpus Hermeticum called it the return of the mind (Nous) to its divine source; Jung named it individuation. "
            "Despite these different frameworks, all share the claim that transformation is not moral improvement but ontological rebirth — a qualitative change in the very substance of the soul."
        ),
        "transmission_genealogy": (
            "The concept flows from Zosimos of Panopolis (c. 300 CE), who first explicitly linked laboratory operations to the transformation of the pneuma, through the Hermetic Corpus (Poimandres's soul-ascent narrative), medieval Christian alchemical allegory (Rosarium Philosophorum, thirteenth century), and the Paracelsian tradition's integration of laboratory and spiritual work. "
            "Jacob Böhme (1575–1624) gave it systematic Protestant theological form, transmitted through the Philadelphian movement (Jane Lead, John Pordage) to English spiritual alchemy. "
            "The Martinist tradition (Martinez de Pasqually, Louis-Claude de Saint-Martin) carried it into French esotericism. "
            "Mary Anne Atwood's Suggestive Inquiry (1850) provided the fullest systematic treatment. "
            "C. G. Jung's psychological reinterpretation (1944–56) gave the concept twentieth-century cultural reach while generating significant scholarly controversy about its historical accuracy."
        )
    },
    42: {
        "summary": (
            "Hermetic Spirituality designates the broader tradition of spiritual practice grounded in Hermetic philosophy: the soul's ascent through the planetary spheres, the cultivation of divine intellect (Nous), theurgic ritual, and the understanding of correspondences as a path to wisdom and divine union. "
            "It is distinguished from dogmatic religion by the absence of fixed creed, from philosophy alone by the insistence that practice is essential, and from magic alone by the emphasis on spiritual development as the ultimate goal. "
            "Transmitted from ancient Alexandria through Byzantine and Arabic intermediaries, Italian Renaissance humanism, and northern European esotericism, it provided the intellectual and practical matrix within which Rosicrucian spirituality, spiritual alchemy, and Christian Kabbalah all developed."
        ),
        "essay": (
            "Hermetic Spirituality designates the broad tradition of spiritual practice grounded in the philosophical framework of the Corpus Hermeticum and related Hermetic writings — texts produced in Greek-speaking Egypt in the first through third centuries CE, attributed to the legendary sage Hermes Trismegistus ('thrice-greatest Hermes'), and understood for over a millennium as prisca sapientia, the wisdom of primordial antiquity. "
            "The tradition is distinguished from dogmatic religion by the absence of fixed creed or ecclesiastical institution, from philosophy alone by the insistence that knowledge of divine realities requires practice and inner transformation, not merely argument, and from operative magic alone by the emphasis on spiritual development — the soul's ascent toward divine union — as the goal to which all techniques are instrumental.\n\n"
            "The foundational Hermetic texts, particularly Poimandres (Corpus Hermeticum I) and the Asclepius, narrate the soul's original divine nature, its descent through the planetary spheres at birth (acquiring the passions and characteristic qualities of each sphere), its life in matter under those acquisitions, and the possibility of its return by recognizing its true nature and progressively shedding the planetary accretions. "
            "The Nous — divine mind or intellect — is both the human soul's deepest nature and the cosmic principle through which the Demiurge created the world; the practitioner who cultivates Nous aligns with this creative intelligence and ascends toward union with it. "
            "This framework is simultaneously cosmological (a theory of how the universe is structured) and soteriological (a path of liberation from material bondage).\n\n"
            "The Greek Neoplatonists, particularly Plotinus (c. 205–270 CE) and Iamblichus (c. 245–325 CE), integrated Hermetic themes with their own systematic metaphysics. "
            "Plotinus's Enneads describe the soul's return to its source through philosophical contemplation — the successive inward turns by which the soul recognizes itself as Intelligence (Nous) and then as unified with the One. "
            "Iamblichus, by contrast, insisted that human souls had fallen too far for philosophy alone to accomplish the return: theurgic ritual — the use of divine tokens (symbola), sacred sounds, ritual fire, and divine images — was necessary to draw down divine power and lift the soul beyond its own capacity. "
            "This debate between philosophy and theurgy as the supreme spiritual path remained live throughout the Hermetic tradition and its later revivals.\n\n"
            "The Hermetic texts were largely unknown in the Latin West through the medieval period, preserved in Byzantine and Arabic manuscript traditions. "
            "Marsilio Ficino's Latin translation of the Corpus Hermeticum (1463–1471), commissioned by Cosimo de' Medici who ordered it prioritized over Plato, brought Hermetic Spirituality into the center of Italian Renaissance thought. "
            "Ficino read the Hermetica as anticipating Christian revelation, fitting them into the schema of prisca theologia — the ancient theology of which Christianity was the culmination. "
            "His De Vita Libri Tres (Three Books on Life, 1489), especially Book III ('De Vita Coelitus Comparanda,' On Obtaining Life from the Heavens), translated Hermetic spirituality into practical guidance: the scholar who wished to maintain spiritual vitality cultivated solar foods, music attuned to celestial harmonies, and astrological timing, capturing beneficent planetary influences through systematic correspondences.\n\n"
            "Heinrich Cornelius Agrippa von Nettesheim's De Occulta Philosophia (1531) systematized the Hermetic-Neoplatonic-Kabbalistic synthesis into the most comprehensive Renaissance treatment of spiritual practice. "
            "Agrippa's three books organize operations by the three worlds: the elemental world (natural magic, working through elemental correspondences), the celestial world (mathematical magic, working through astrological influences), and the intellectual world (ceremonial magic, working through divine names and intelligences). "
            "Book III is explicitly theurgic, drawing on Iamblichus, the Chaldaean Oracles, and Kabbalah to describe the ascent of the mind to divine intellect. "
            "For Agrippa, Hermetic Spirituality was not a medieval 'superstition' but the highest form of natural philosophy: understanding correspondences in their deepest ontological dimension was simultaneously the path to natural knowledge and to divine union.\n\n"
            "John Dee (1527–1608/9) represents perhaps the most dramatic instantiation of Hermetic Spirituality in the late Renaissance. "
            "His Monas Hieroglyphica (1564) compressed the entire Hermetic-Neoplatonic-mathematical synthesis into a single hieroglyphic symbol; his angelic conversations with the medium Edward Kelley (1582–1589), conducted in what Dee understood as the original Adamic language of creation (later called Enochian), were explicitly theurgic — attempts to engage divine intelligence directly and receive the unified key to all knowledge. "
            "Whether Dee achieved his goal remains beside the point: his work embodies the Hermetic Spirituality framework completely, treating cosmological knowledge, linguistic analysis, mathematical investigation, and direct divine contact as aspects of a single spiritual practice.\n\n"
            "The northern European reception of Hermetic Spirituality after Agrippa and Dee ran through several channels: the Rosicrucian manifestos (1614–1615), which explicitly promised a 'general reformation of the whole wide world' grounded in Hermetic and Paracelsian knowledge; the spiritual alchemy tradition from Böhme through the Philadelphian movement; and the Masonic and Martinist initiatory traditions of the eighteenth century. "
            "The Rosicrucian synthesis was distinctive in combining Hermetic philosophy, Paracelsian chemistry, Protestant theology, and social reform aspiration — a constellation that gave Hermetic Spirituality a new institutional and political dimension it had not possessed in the Florentine academy.\n\n"
            "Antoine Faivre's foundational scholarship (Access to Western Esotericism, 1994) identified four intrinsic characteristics of Hermetic Spirituality as a tradition: the theory of correspondences, the idea of living nature, imagination and mediations as instruments of knowledge, and the experience of transmutation (of the self as well as matter). "
            "These characteristics, Faivre argued, constitute a recognizable 'form of thought' across the tradition's many variations — not a fixed doctrine but a characteristic way of approaching knowledge, cosmos, and self that unifies figures as different as Ficino, Böhme, and Swedenborg."
        ),
        "operational_meaning": (
            "Practitioners of Hermetic Spirituality cultivated the soul's ascent through disciplined practices: Ficino prescribed astrologically timed music, solar foods, and contemplation of celestial images to attract beneficent planetary influence. "
            "Iamblichan theurgists used synthemata — divine tokens including specific stones, plants, animals, and sounds — as vehicles through which divine power descended. "
            "Dee sought direct angelic communication through scrying, understood as theurgic contact with intelligences superior to the planetary rulers. "
            "In each case, Hermetic Spirituality is not a set of beliefs but a set of practices: specific disciplines, performed with specific understanding of correspondences and with the appropriate interior orientation, through which the practitioner cultivates Nous and moves toward divine union."
        ),
        "philosophical_meaning": (
            "Philosophically, Hermetic Spirituality rests on a participatory Neoplatonic ontology in which knowledge is assimilation: to know a thing truly is to become like it, to participate in its being. "
            "The soul can ascend to Nous because it is itself Nous in its deepest nature; it can attain union with the One because it flows from the One and carries that origin within itself. "
            "The doctrine of correspondences is not arbitrary symbolism but a claim about the structure of reality: because all things emanate from a single source, they retain structural kinship — the practitioner who understands these correspondences can work with them, and in doing so enters more deeply into the fabric of being."
        ),
        "spiritual_meaning": (
            "Spiritually, Hermetic Spirituality offers the soul a complete itinerary from material bondage to divine union: the practitioner recognizes the Nous within, cultivates it through correspondence-work and contemplation, sheds the planetary accretions accumulated in descent, and achieves henosis — the experience of unity with the divine source described in Poimandres as the final liberation. "
            "This is not mystical quietism but active spiritual work requiring knowledge, discipline, and courage. "
            "The goal, as the Asclepius puts it, is to become a 'second god' — not to deny creation but to understand and participate in its divine ground so completely that the soul becomes a transparent instrument of divine creativity."
        ),
        "transmission_genealogy": (
            "The Hermetic Corpus was composed in Alexandria (first–third centuries CE) drawing on Egyptian temple tradition, Middle Platonic philosophy, Jewish wisdom literature, and early Stoic cosmology. "
            "It passed into Byzantine scholarship and Arabic translation (the Sabi'an community of Harran preserved and transmitted key texts), then into Latin Europe through twelfth-century translations. "
            "Ficino's complete Latin translation (1463–71) inaugurated the Renaissance revival. "
            "The genealogy then runs through Pico della Mirandola's Oratio and Kabbalistic synthesis, Agrippa's De Occulta Philosophia (1531), Dee's Monas Hieroglyphica (1564), the Rosicrucian manifestos (1614–15), Böhme's theosophical elaboration, the Philadelphian and Martinist traditions, and into nineteenth-century Theosophy and twentieth-century Western esotericism."
        )
    },
    43: {
        "summary": (
            "The Alchemical Hermaphrodite — named Rebis, from the Latin res bina ('double thing') — is the hermaphroditic figure representing the coniunctio of male and female, sulfur and mercury, sun and moon, that produces the Philosopher's Stone. "
            "The Rosarium Philosophorum traces the union of king and queen through death and resurrection to their emergence as a single hermaphroditic being; Maier's Atalanta Fugiens emblem 38 depicts the completed Stone as androgyne. "
            "As both the goal of the opus and an image of wholeness transcending binary opposition, the Rebis became a touchstone for Jungian psychological interpretation, feminist scholarship on alchemical gender, and ongoing debates about whether alchemical sexual symbolism describes laboratory operations, cosmological principles, or practitioner psychology."
        ),
        "essay": (
            "The Alchemical Hermaphrodite — most often named Rebis, from the Latin res bina, 'double thing' — is among the most visually arresting and philosophically productive symbols in the alchemical tradition: a hermaphroditic figure, male on one side and female on the other, combining the solar and lunar, active and passive, fixed and volatile into a single body that represents the perfected Philosopher's Stone. "
            "It appears across the full range of alchemical literature from the fourteenth century onward, achieving canonical status in the Rosarium Philosophorum (early fifteenth century), the Splendor Solis (c. 1531–1532), and Michael Maier's Atalanta Fugiens (1617).\n\n"
            "The foundational narrative of the Alchemical Hermaphrodite is given in the Rosarium Philosophorum, a compilation of alchemical texts with accompanying woodcuts that was printed in Frankfurt in 1550. "
            "The twenty woodcuts trace the full opus: king and queen (sun and moon, sulfur and mercury, gold and silver) meet, bathe together, engage in hieros gamos (the sacred marriage), undergo death together and are depicted as a conjoined corpse, receive the dew of divine animation, and finally resurrect as the Rebis — a single winged hermaphroditic figure standing on the moon with a solar crown. "
            "The Latin texts accompanying these images draw on multiple alchemical authorities to interpret each stage, creating a rich textual-visual synthesis. "
            "C. G. Jung's Mysterium Coniunctionis (1955–56) provided the most detailed psychological commentary on this sequence, reading the stages as phases of the individuation process in which the unconscious contents of the psyche are progressively integrated.\n\n"
            "In the language of alchemical principles, the hermaphrodite unites the masculine principle (sulfur: hot, dry, active, solar, gold) with the feminine principle (mercury: cold, wet, passive, lunar, silver). "
            "The specific combination varied by author and school: in Arabic alchemy (Jabir ibn Hayyan), sulfur and mercury were the two principles of all metals, and their combination in varying proportions produced the full range of metallic substances; the perfected stone was their ideally balanced union. "
            "In Paracelsian chemistry, tria prima (sulfur, mercury, salt) supplemented the dyadic pair with a third term, but the masculine-feminine dynamic remained operative. "
            "The hermaphroditic stone, in laboratory terms, was understood as a substance that had achieved the perfect equilibrium of these principles, thereby possessing the transforming power of both.\n\n"
            "The visual genealogy of the Rebis is extensive and iconographically rich. "
            "Aurora Consurgens (fifteenth century) depicts the soul of alchemy as a feminine wisdom figure (Sapientia) in a tradition linking the alchemical art to the biblical Wisdom literature. "
            "The Splendor Solis (attributed to Salomon Trismosin) presents seventeen illuminated paintings including hermaphroditic figures in cosmological frames. "
            "Maier's Atalanta Fugiens emblem 38 depicts the androgyne standing on a globe, with the Latin motto 'Hermaphroditus est opus nostrum perfectum' ('The Hermaphrodite is our perfect work'). "
            "Heinrich Khunrath's Amphitheatrum Sapientiae Aeternae (1595, 1609) integrates Rosicrucian, Kabbalistic, and alchemical symbolism with hermaphroditic imagery in its central oratory engraving.\n\n"
            "The philosophical background reaches beyond alchemy into broader Renaissance thought. "
            "Plato's Symposium, in Aristophanes' speech, narrates the myth of the spherical hermaphroditic primordial humans split by Zeus — a myth of lost wholeness whose recovery through love is a persistent cultural theme. "
            "The Neoplatonists, especially Plotinus and Proclus, read the androgyne as a symbol of the One's self-sufficiency and undifferentiated unity, from which sexual differentiation proceeded as a consequence of the soul's descent into matter. "
            "Ficino's commentary on the Symposium incorporated these themes into Renaissance love philosophy. "
            "For alchemists reading within this tradition, the Rebis was not a curiosity but a cosmological statement: the perfected stone recovered the primordial wholeness that material existence had divided.\n\n"
            "Gender scholarship has significantly complicated understanding of the Alchemical Hermaphrodite. "
            "Leah DeVun's Prophecy, Alchemy, and the End of Time (2009) and Patricia Fara's work on women in early science have examined how alchemical sexual symbolism constructed gender categories while simultaneously transgressing them: the hermaphrodite models the overcoming of gender distinction even as the gendering of sulfur as masculine and mercury as feminine reinforces conventional hierarchies. "
            "Barbara Obrist and Stanton Linden have analyzed the visual traditions through which these constructions were transmitted. "
            "Lawrence Principe and William Newman have cautioned against over-reading sexual symbolism at the expense of understanding the actual laboratory content: the 'marriage' of sulfur and mercury was, in many texts, a description of chemical combination rather than a cosmological myth.\n\n"
            "The Rebis's afterlife in Western esotericism has been extensive. "
            "Rosicrucianism incorporated hermaphroditic symbolism in its alchemical-initiatory framework; the Chemical Wedding of Christian Rosencreutz (1616) culminates in the resurrection of hermaphroditic royal figures as symbolic of the completion of the Rosicrucian Work. "
            "Nineteenth-century Theosophical and occultist traditions (Blavatsky, Papus) read the hermaphrodite as encoding the doctrine of the androgynous divine and the androgynous original human. "
            "Jung's reading — that the Rebis images the psyche's integration of its contrasexual elements (anima/animus) into the unified Self — has proven the most culturally influential modern interpretation, though it has been challenged as anachronistic by historians of alchemy."
        ),
        "operational_meaning": (
            "In the laboratory, the conjunction (coniunctio) that produced the hermaphroditic stone involved the combination of sulfur-bearing and mercury-bearing substances in a sealed vessel, subjected to sustained heat in a graduated sequence. "
            "The signs of successful conjunction included color changes through black, white, yellow, and finally red; the appearance of peacock's tail colors (cauda pavonis) was taken as evidence that the marriage was proceeding. "
            "The Rebis as final product was identified with the red stone or elixir that could transmute base metals into gold in ratios of one part stone to thousands of parts base metal — a projection (projectio) understood as the tincturing or dyeing of metal with the stone's perfected nature."
        ),
        "philosophical_meaning": (
            "Philosophically, the Alchemical Hermaphrodite embodies the coincidentia oppositorum — Nicholas of Cusa's principle that perfection consists in the reconciliation and transcendence of contrary principles rather than the dominance of one over the other. "
            "The stone is neither pure sulfur nor pure mercury but their dynamic, stable unity; neither masculine nor feminine but both. "
            "This has ontological implications: matter at its most perfect is not simple but complexly unified; being at its fullest is not undifferentiated unity but integrated multiplicity. "
            "The hermaphrodite thus models a philosophy of wholeness through integration rather than through reduction."
        ),
        "spiritual_meaning": (
            "Spiritually, the Rebis figures the transformed practitioner: the soul that has undergone the full opus — nigredo's death, albedo's purification, rubedo's apotheosis — has integrated the opposing principles within itself and no longer experiences the fundamental dividedness of ordinary consciousness. "
            "In Jung's reading, this is the individuated Self, which contains and reconciles the conscious and unconscious, masculine and feminine, light and shadow. "
            "In Böhmean terms, the hermaphrodite images the new being in whom the tincture of divine love has overcome the fire-darkness of self-will, producing a stable union of contrary principles in a single spiritual being."
        ),
        "transmission_genealogy": (
            "The dyadic sulfur-mercury theory of metallic composition entered Latin alchemy from Arabic sources (Jabir ibn Hayyan, al-Razi) in the twelfth century, providing the chemical basis for hermaphroditic symbolism. "
            "The Rosarium Philosophorum (compiled c. 1400–1550, printed 1550) established the visual narrative of royal conjunction and hermaphroditic resurrection. "
            "Maier's Atalanta Fugiens (1617) and Khunrath's Amphitheatrum (1595, 1609) gave the Rebis its most elaborate Renaissance artistic treatment. "
            "The Rosicrucian Chemical Wedding (1616) incorporated hermaphroditic imagery into initiatory narrative. "
            "C. G. Jung's psychological commentary (Mysterium Coniunctionis, 1955–56) gave the symbol its twentieth-century cultural centrality. "
            "Contemporary scholarship (DeVun, Principe, Newman, Obrist) has examined the gender politics and laboratory meanings of the tradition with increasing precision."
        )
    },
    44: {
        "summary": (
            "Theurgic Practice designates the systematic use of ritual operations — synthemata (divine tokens: specific stones, plants, animals, sounds), sacred fire, invocation, and graduated initiation — to attract divine power into the practitioner's soul and accomplish spiritual ascent beyond what unaided philosophical contemplation can achieve. "
            "Iamblichus articulated the classic defense of theurgy against Porphyry's purely philosophical approach, arguing that the gods must draw the soul upward through rites that the gods themselves have established. "
            "In the Renaissance, Ficino, Agrippa, and Dee translated this framework into a Christian context, and in the seventeenth century John Dee's Enochian conversations and the Gold- und Rosenkreutz initiatory system represented its most elaborate institutionalized forms."
        ),
        "essay": (
            "Theurgic Practice designates the systematic ritual engagement with divine powers through specific material and sensory operations — not worship, prayer, or philosophical argument, but the skilled manipulation of what Iamblichus called synthemata and symbola: objects, sounds, gestures, and substances that participate in divine realities and can therefore serve as vehicles through which divine power descends into the practitioner and the practitioner's soul ascends toward the divine. "
            "The term derives from Greek theourgia, 'the work of gods in humans,' and was first used by the Chaldaean Oracles (late second century CE) to describe rites through which the soul could be liberated from material bondage by the fiery Hecate and the other theurgic deities.\n\n"
            "The philosophical justification for theurgy over philosophy alone was given most forcefully by Iamblichus of Chalcis (c. 245–325 CE) in his De Mysteriis Aegyptiorum, a response to the questions of his teacher Porphyry. "
            "Porphyry had argued that the soul could achieve union with the divine through philosophical contemplation alone — the Plotinian ascent through self-reflection to the One. "
            "Iamblichus countered that human souls had descended too far into matter for philosophy to accomplish their return: they required the assistance of the gods themselves, made available through rites the gods had established precisely for this purpose. "
            "The synthemata — specific minerals, plants, animals, colours, and sounds that each god had embedded in the material world as tokens of his own presence — served as channels through which divine power could flow when properly engaged. "
            "This was not the practitioner commanding divine power but the practitioner creating the conditions under which divine power, of its own generosity, descended.\n\n"
            "The Chaldaean Oracles, the primary scriptural text of theurgic practice, describe rites involving sacred fire, the whirling of the iynx (a ritual object creating a vortex of divine attraction), and the animation of statues through divine invocation. "
            "The Oracles insist on the importance of the practitioner's purity — not moral purity in a conventional ethical sense but a specific orientation of the entire person toward divine fire, involving dietary discipline, ritual preparation, and sustained contemplative attention. "
            "The Oracles also describe the 'pneumatic vehicle' of the soul — a subtle body that must be refined and purified before the soul can ascend without being consumed by the divine fire it encounters.\n\n"
            "Marsilio Ficino's De Vita Coelitus Comparanda (Book III of De Vita, 1489) translated theurgic practice into Renaissance natural philosophy. "
            "Ficino's framework replaced the Neoplatonic hierarchy of gods with the planetary intelligences of astrological tradition, and the theurgic synthemata became planetary correspondences: solar herbs (celandine, bay laurel, gold) used in astrologically timed preparations to attract solar virtue into the practitioner's constitution. "
            "Music attuned to planetary harmonics, fragrances corresponding to specific planets, and the material composition of talismans were all instruments for drawing down celestial influence. "
            "Ficino was careful to frame this as natural rather than demonic magic — working within the created order through its own structural correspondences — but the theurgic logic was intact: specific material operations, properly understood and executed, opened channels for divine power.\n\n"
            "Heinrich Cornelius Agrippa's De Occulta Philosophia (1531) extended Ficino's framework systematically. "
            "Agrippa's Book III addresses the 'intellectual world' and describes the highest form of magic as Kabbalistic and theurgic: the skilled practitioner, having purified his intellect and received divine inspiration, can invoke divine names and call down angelic intelligences as assistants. "
            "Agrippa drew extensively on Iamblichus, the Chaldaean Oracles, and the Pseudo-Dionysian celestial hierarchy to describe the graduated system through which human souls could ascend — and divine power could descend — through the angelic orders.\n\n"
            "John Dee's conversations with angels (1582–1589), conducted through the medium Edward Kelley using a crystal globe and a scrying mirror, represent the most ambitious Renaissance attempt at theurgic dialogue. "
            "Dee understood these sessions as the reception of the original Adamic language — the language in which God created the world and in which Adam named the animals — which he called Enochian (after the patriarch Enoch who walked with God). "
            "The Enochian system included a complete angelic hierarchy, a system of calls or keys for invoking successive orders of angels, and a geographical-cosmological map of the angelic government of the world. "
            "Whether Dee achieved authentic angelic contact, was deceived by Kelley, or was himself engaging in a complex imaginative-spiritual practice remains debated; what is clear is that his framework was explicitly theurgic — he sought to draw divine intelligences into communicative contact through ritual preparations, prayer, and sustained contemplative attention.\n\n"
            "In the Rosicrucian and esoteric Masonic traditions of the seventeenth and eighteenth centuries, theurgic practice was institutionalized in graduated initiation systems. "
            "The Gold- und Rosenkreutz order (eighteenth century) organized its degrees around increasingly intimate contact with spiritual powers, with each degree conferring new operative capacities as the initiate's own purification advanced. "
            "Martinez de Pasqually's Élus Coëns (Elus Cohen or 'elected priests') practiced complex ceremonial operations (the 'magic circle' work) aimed at the 'reintegration' of the fallen human being into its original divine condition through ritual contact with divine agents.\n\n"
            "The debate between Iamblichus and Porphyry about whether theurgy or philosophy is the higher path was not resolved in antiquity and recurs in every generation of the tradition. "
            "Some Renaissance Hermetists (Pico della Mirandola, the later Ficino) emphasized interior contemplation over ritual manipulation. "
            "Others (Agrippa, Dee) invested heavily in operative ritual. "
            "The modern esoteric tradition (Martinism, Rosicrucianism, Golden Dawn, contemporary ceremonial magic) largely follows the Iamblichan position: ritual is necessary because the soul cannot lift itself by its own efforts but requires the descending grace of divine operation, mediated through the ritual vehicles the gods themselves have established."
        ),
        "operational_meaning": (
            "What theurgists actually do: prepare a sacred space through fumigations, purifications, and the establishment of protective circles; select synthemata appropriate to the divine power being invoked (specific stones, plants, animals, colors, and geometric figures associated with that power through the table of correspondences); invoke through specific divine names and formulae; attend to the signs of divine presence (heat, light, fragrance, interior illumination); and perform the concluding rites that properly close the operation and ground the energies invoked. "
            "Ficino's practical instructions include the timing of operations by planetary hour and lunar phase, the composition of specific fumigations, and the use of music in specific modes. "
            "Dee's operations required a consecrated crystal, specific prayers, the construction of the 'holy table' with its complex geometric sigils, and weeks of preparatory fasting and prayer."
        ),
        "philosophical_meaning": (
            "Philosophically, theurgic practice rests on the Neoplatonic doctrine of sympatheia — the universal sympathy connecting all levels of the cosmos through their common origin in the One — combined with the Iamblichan claim that the soul's return requires divine assistance because the fall into matter has disabled the soul's capacity for self-directed ascent. "
            "This is not a pessimistic anthropology but a precise claim about the mechanics of divine-human interaction: the gods are supremely generous and have established the conditions of their own accessibility; the practitioner's task is to understand and fulfil those conditions. "
            "The logic distinguishes theurgy sharply from both philosophy (insufficient) and coercive magic (inappropriate): theurgic practice cooperates with divine generosity, neither substituting its own effort for divine grace nor compelling divine power against its will."
        ),
        "spiritual_meaning": (
            "Spiritually, theurgic practice accomplishes the progressive illumination and elevation of the soul's pneumatic vehicle — the subtle body through which divine fire and divine light are received and retained. "
            "Each successful theurgic operation leaves a deposit of divine influence in the pneumatic vehicle that slightly raises the soul's inherent luminosity and receptivity; the cumulative effect, over a sustained practice, is a genuine transformation of the soul's constitution. "
            "The goal — as the Chaldaean Oracles describe it — is the soul's liberation from material bondage and its ascent through the divine fire to unity with the highest divine principle, an ascent that theurgy makes possible by providing the divine assistance that unaided human effort cannot achieve."
        ),
        "transmission_genealogy": (
            "Theurgic practice originates in the Chaldaean Oracles (late second century CE), elaborated by Iamblichus (De Mysteriis, c. 310 CE) and Proclus (fifth century). "
            "The tradition passed into Byzantine scholarship and through Arabic intermediaries. "
            "Ficino's De Vita (1489) and Agrippa's De Occulta Philosophia (1531) gave it Renaissance Latin form. "
            "Dee's Enochian system (1582–89) represents its most elaborate Renaissance instantiation. "
            "The Rosicrucian tradition incorporated theurgic operative dimensions; the Gold- und Rosenkreutz and Élus Coëns institutionalized it in graduated initiation. "
            "The Hermetic Order of the Golden Dawn (1888) systematized the full range of theurgic techniques for the modern esoteric tradition."
        )
    },
    45: {
        "summary": (
            "Spiritual Chemistry designates the use of chemical language, concepts, and operations as a framework for spiritual transformation — distinct from spiritual alchemy (which interprets traditional alchemical symbolism) in that it engages directly with seventeenth- and eighteenth-century chemistry, including van Helmont's archeus, Böhme's tria prima as cosmic-spiritual forces, and the Romantic Naturphilosophie of Schelling and Ritter. "
            "Rather than reading old alchemical symbols spiritually, spiritual chemistry finds in the new empirical chemistry its own cosmological and spiritual depth, treating the laboratory as a site where spiritual realities are disclosed through material operations. "
            "The tradition marks the transition point at which chemical metaphor began replacing alchemical metaphor in spiritual discourse, a shift whose full consequences are still being assessed by scholars of science and esotericism."
        ),
        "essay": (
            "Spiritual Chemistry designates a distinct tradition within the broader range of alchemical and chemical spirituality: not the spiritual interpretation of traditional alchemical symbolism (spiritual alchemy proper), but the deployment of chemical language, concepts, and laboratory operations drawn from seventeenth- and eighteenth-century chemistry as a framework for understanding spiritual transformation, cosmic structure, and divine creativity. "
            "The distinction matters because spiritual chemistry engages with the new chemistry — from van Helmont through Stahl and Lavoisier — rather than rehearsing the medieval and Renaissance alchemical inheritance, finding in the empirically oriented chemistry of the Scientific Revolution its own spiritual depth and cosmological implication.\n\n"
            "Joan Baptista van Helmont (1580–1644) is the pivotal figure in the genesis of spiritual chemistry. "
            "Van Helmont rejected the four-element theory and the Paracelsian tria prima as inadequate to account for chemical phenomena, developing instead a chemical philosophy centered on the concept of the archeus — a semi-material, semi-spiritual principle operative at the level of individual substances and organisms. "
            "For van Helmont, the archeus was not a poetic metaphor but a genuine explanatory entity: each substance possessed its own archeus that governed its specific operations, and the human body was governed by the archeus of the stomach (archaeus stomachi) as the chief organizer of digestive and vital processes. "
            "This framework was simultaneously chemical and spiritual: the archeus was the meeting point of matter and spirit, the principle through which divine creative activity operated in the material world. "
            "Van Helmont's concept of gas (a term he coined from the Greek chaos) was similarly charged: gas was the spiritual vehicle through which matter's vital and chemical operations were mediated.\n\n"
            "Jacob Böhme (1575–1624), though not himself a chemist in the laboratory sense, provided spiritual chemistry's most theologically developed framework. "
            "Böhme used the Paracelsian tria prima (sulfur, mercury, salt) not as descriptions of physical substances but as names for cosmic-spiritual principles operative throughout creation: sulfur was the principle of desire and wrath, the fiery self-assertion of being; mercury was the principle of understanding and revelation, the luminous self-manifestation of being; salt was the principle of body and fixity, the crystallization of being into determinate form. "
            "These were not merely metaphors but — for Böhme — actual forces operating in both matter and soul. "
            "The alchemical process was not allegory but genuine description of how divine creativity worked in nature: the nigredo of Böhme's primal abyss, the albedo of divine light, the rubedo of divine love's triumph over wrath were cosmic events, chemical events, and psychological events simultaneously. "
            "Böhme's influence on spiritual chemistry was enormous: his frameworks shaped the Romantic reception of chemistry throughout the eighteenth and nineteenth centuries.\n\n"
            "The Romantic Naturphilosophie of Friedrich Wilhelm Joseph Schelling (1775–1854) represents spiritual chemistry's most philosophically ambitious elaboration. "
            "Schelling's Ideen zu einer Philosophie der Natur (1797) and his subsequent Naturphilosophie developed a speculative natural science in which chemical processes disclosed the structure of the Absolute's self-revelation: the polarity of acid and alkali, the dynamics of combustion, the chemistry of organic life were not merely empirical facts but manifestations of the same fundamental structure that appeared in consciousness as the subject-object relation. "
            "Johann Wilhelm Ritter (1776–1810), the experimental physicist and Naturphilosoph, carried this program into the laboratory: his electrochemical experiments were conducted within a framework in which electricity was understood as the most subtle form of the vital force animating both matter and soul. "
            "Ritter's own spiritual and mystical interests led him to connect his chemical work to the tradition of spiritual alchemy and to investigate phenomena (galvanism, dowsing, animal magnetism) on the border between the material and spiritual.\n\n"
            "Emanuel Swedenborg (1688–1772) occupies a unique position in the history of spiritual chemistry. "
            "As a mining engineer and metallurgist before his spiritual illumination in 1745, Swedenborg had deep practical knowledge of smelting, assaying, and mineralogy. "
            "His doctrine of correspondences — that natural things correspond structurally to spiritual realities — applied directly to chemical phenomena: gold corresponded to celestial love, silver to spiritual truth, iron to natural truth, lead to cupidity. "
            "These were not arbitrary assignments but structural correspondences grounded in the properties of the metals as Swedenborg understood them from his metallurgical experience. "
            "Swedenborg's theological works — Heaven and Hell, Arcana Coelestia — applied this chemical-spiritual correspondence system throughout, treating the entire created order as a system of spiritual meaning disclosed through careful empirical observation.\n\n"
            "The transition from alchemical to chemical metaphor in spiritual discourse occurred gradually through the seventeenth and eighteenth centuries. "
            "As the credibility of traditional alchemical claims to transmutation declined under the pressure of the new chemistry, spiritual writers who wished to use chemical language had to engage with the new framework. "
            "Böhme's tria prima was ancient but his framework was productive because it could be read in terms of the new chemistry's basic categories. "
            "Van Helmont's archeus concept influenced generations of vitalist and pneumatist physicians who maintained the spiritual dimension of chemical processes within a broadly empirical framework. "
            "By the early nineteenth century, spiritual chemistry had become the language of Naturphilosophie, animal magnetism, and the flourishing tradition of alchemical revival.\n\n"
            "Wouter Hanegraaff's scholarship (Esotericism and the Academy, 2012) has traced how the intersection of spiritual and chemical frameworks was negotiated through the period, showing that the 'rejection' of alchemy by the new chemistry was more complex than a simple supersession: many figures who accepted the new chemistry also maintained spiritual-chemical frameworks, and the idea that chemistry discloses spiritual realities persisted in various forms throughout the nineteenth century. "
            "The distinction Hanegraaff draws between rejected knowledge and esoteric knowledge as forms of self-definition for the alternative tradition illuminates why spiritual chemistry has remained generative even as laboratory chemistry has become entirely secular."
        ),
        "operational_meaning": (
            "Practitioners of spiritual chemistry brought specific spiritual orientation to laboratory work: van Helmont's investigations of gas and the archeus were conducted with the conviction that chemical phenomena disclosed the action of semi-spiritual principles. "
            "Ritter's electrochemical experiments were interpreted within a framework of vital polarity that connected galvanic phenomena to the structure of living matter and ultimately to cosmic life. "
            "Böhmean practitioners who engaged with chemical ideas (Georg von Welling's Opus Mago-Cabbalisticum, 1735) treated laboratory operations as disclosures of spiritual forces, observing chemical phenomena with the expectation that the spiritual dimensions would be visible to the appropriately prepared observer. "
            "The key operational claim is that chemical phenomena mean something beyond their material surface: understanding that meaning is simultaneously scientific and spiritual."
        ),
        "philosophical_meaning": (
            "Philosophically, spiritual chemistry rests on a non-reductive philosophy of nature: matter is not inert and mechanical but inherently animated by spiritual forces that chemical operations disclose and engage. "
            "Van Helmont's archeus, Böhme's tria prima, and Schelling's Naturphilosophie all articulate versions of the claim that chemistry is not merely the rearrangement of inert particles but the disclosure of living, spiritually charged processes. "
            "This philosophy stands against Cartesian mechanism and its successors, maintaining that the natural sciences, properly understood, lead toward rather than away from recognition of the spiritual structure of reality."
        ),
        "spiritual_meaning": (
            "Spiritually, spiritual chemistry offers a path to divine knowledge through the careful study of natural processes: because the chemical operations of nature disclose the creative activity of divine principles (Böhme's tria prima, van Helmont's archeus, Swedenborg's correspondences), the chemist who understands what she observes is simultaneously understanding divine creativity. "
            "Laboratory work becomes a form of contemplation, the test-tube a site of theological disclosure. "
            "This gives spiritual chemistry a distinctive relationship to the natural sciences: it does not reject chemistry in favor of mysticism but insists that chemistry, pursued with appropriate attention and understanding, discloses spiritual realities that purely secular chemistry ignores."
        ),
        "transmission_genealogy": (
            "Van Helmont's archeus and gas concepts (1648, posthumous) established the framework for seventeenth-century spiritual chemistry. "
            "Böhme's tria prima cosmology (Aurora, 1612; subsequent works) gave it theological depth. "
            "Georg von Welling's Opus Mago-Cabbalisticum (1735) synthesized Böhmean and chemical frameworks for German esotericism. "
            "Swedenborg's correspondences (1749–71) applied chemical metaphor systematically to spiritual description. "
            "Schelling's Naturphilosophie (1797 onward) and Ritter's experimental work brought spiritual chemistry into Romantic natural science. "
            "The tradition feeds into nineteenth-century Theosophy (Blavatsky's scientific-spiritual synthesis) and twentieth-century integrative approaches to chemistry and spirituality."
        )
    },
    46: {
        "summary": (
            "Divine Names designates the doctrine that names of God — Hebrew divine names from the Tetragrammaton (YHWH) through the seventy-two names of the Shemhamphorash — are not merely labels but participations in divine reality, possessing operative power through their structural correspondence to the divine being they name. "
            "Kabbalistic practice developed specific techniques for working with divine names: meditation (hitbonenut), vocalization, inscription on talismans, and gematria (numerical analysis). "
            "Christian Kabbalists from Pico della Mirandola through Agrippa and Dee incorporated divine name practice into natural magic and theurgic operation, and the Abramelin operation and Enochian system represent its most elaborate Renaissance-period instantiations."
        ),
        "essay": (
            "Divine Names designates the doctrine that the names by which the divine is addressed — pre-eminently the Hebrew names of God but also Greek and Coptic divine names in various traditions — are not merely conventional labels pointing to a referent but genuine participations in the divine reality they name, possessing operative power proportional to that participation. "
            "A divine name, properly understood, invoked, and used, is not a symbol of God's power but an expression of it: to speak the name correctly, with correct preparation and understanding, is to be in real contact with what the name names. "
            "This doctrine, developed with greatest precision in Jewish Kabbalah and transmitted into Renaissance Christian Kabbalah, provides the linguistic-metaphysical foundation for a wide range of ritual and operative practices from the medieval period through the present.\n\n"
            "The Kabbalistic framework for divine names begins with the Tetragrammaton — the four-letter name YHWH, the primary name of God in the Hebrew Bible — which rabbinic tradition treated with extraordinary reverence, prohibiting its ordinary pronunciation and substituting Adonai (Lord) or HaShem (The Name) in reading. "
            "This prohibition itself signals the name's power: if the name were merely a label, there would be no reason to withhold it. "
            "The prohibition reflects the conviction that the Tetragrammaton participates structurally in divine reality — it is not a name for God but in some sense a form of God's self-expression in language. "
            "Medieval Kabbalists developed this intuition systematically: the Sefer Yetzirah (Book of Formation, composed perhaps in the third to sixth centuries) described the divine creative act as proceeding through combinations of the twenty-two Hebrew letters, treating language as the medium of creation rather than its description. "
            "The Tetragrammaton, on this reading, is not a word God uses but the word God is — or at least, the word closest to that identity.\n\n"
            "The tradition of the seventy-two names of God (the Shemhamphorash) developed from Exodus 14:19–21, three verses of seventy-two letters each, which medieval interpreters combined boustrophedon to yield seventy-two three-letter divine names. "
            "Each of these names was identified with an angel who was the specific expression of that divine attribute in the angelic world, and practical manuals (such as those in the grimoire tradition) provided techniques for invoking each of the seventy-two through their specific divine names, sigils, and associated planetary correspondences. "
            "Abraham Abulafia (c. 1240–c. 1291) developed a sophisticated meditation system centered on the combination and permutation of divine names — the technique of tzeruf ha-otiot (letter combination) — as a path to prophetic illumination and unio mystica with the divine source.\n\n"
            "Pico della Mirandola's Conclusiones (1486) introduced Kabbalistic divine name doctrine to the Latin Christian world with the claim that no magic is more effective than magic worked through the names of God, and that Kabbalah was the most reliable key to natural magic. "
            "Pico's defense of this position in his Apologia (1487) — that Christian Kabbalah provided the most secure foundation for Christian theology because it demonstrated the doctrine of the Trinity from Hebrew divine names — shows how completely the doctrine of divine names had been assimilated into Christian theological argument. "
            "Johannes Reuchlin's De Arte Cabalistica (1517) developed the specific claim that the name Yeshua (Jesus) was the Tetragrammaton augmented by the letter shin, making the Christian divine name a literally new divine name of five letters containing and surpassing the four-letter name of the Hebrew Bible.\n\n"
            "Agrippa's De Occulta Philosophia (1531) provided the fullest systematic treatment of divine name practice in the Renaissance. "
            "Book III, drawing on Reuchlin and Iamblichus, describes the method of working through the angelic hierarchy using divine names as keys: each angelic order is governed by specific divine names whose correct invocation opens access to that order's powers. "
            "Agrippa provides detailed tables of divine names, angelic names, planetary names, and their correspondences, organized as a practical handbook for the learned magus who has been properly prepared through moral and intellectual discipline.\n\n"
            "John Dee's Enochian system (1582–1589) represents the most ambitious Renaissance attempt to receive a complete divine name system directly from angelic sources. "
            "The angels communicating through Edward Kelley provided Dee with an entirely new language — Enochian — which they described as the original Adamic language in which God had created the world and in which He had spoken to Adam before the Fall. "
            "The Enochian system included forty-nine divine names organized in the 'Forty-Nine Tables of Loagaeth,' nineteen 'Enochian Keys' or calls for invoking successive orders of angels, and a complex system of angelic governors organized by geographical region and astrological correspondence. "
            "Whether the Enochian language was genuine divine revelation, a product of Kelley's creative mediumship, or the result of some collaborative unconscious process between Dee and Kelley remains debated; Dee believed absolutely in its divine origin and in the operative power of the divine names it contained.\n\n"
            "The Abramelin operation, described in Abraham of Worms's Book of the Sacred Magic of Abramelin the Mage (probably late fifteenth century, published in French translation 1898), involves an eighteen-month preparatory discipline of prayer, fasting, and moral purification culminating in direct contact with one's Holy Guardian Angel — understood as one's higher spiritual self or personal divine messenger — who then reveals the true divine names and teaches the magician to compel demons by those names. "
            "The operation exemplifies the theological structure of divine name practice: the names do not coerce divine power but are received as divine gifts, which the practitioner may then use with authority.\n\n"
            "The operative methods by which divine names are actually used vary by tradition. "
            "Kabbalistic meditation involves slow, rhythmic vocalization of divine names while attending to their Hebrew letters as visual objects for contemplation, working through systematic permutations. "
            "Talismanic practice inscribes divine names on specific materials (gold for solar names, silver for lunar, etc.) in astrologically timed operations. "
            "Ceremonial invocation speaks divine names aloud in consecrated ritual space as part of a structured sequence. "
            "Gematria analyzes divine names through their numerical equivalents, discovering hidden structural connections between divine names and words of equivalent numerical value in scripture."
        ),
        "operational_meaning": (
            "Practitioners used divine names through four main operations: vocalization (pronouncing the name correctly, with proper intention, breath control, and internal orientation — Abulafia's technique involved rhythmic permutation of letters while monitoring the practitioner's interior state); inscription (writing divine names on talismans in astrologically timed conditions using appropriate materials — parchment from specific animals, inks prepared with corresponding ingredients); ceremonial invocation (speaking divine names as part of a structured ritual that creates the conditions for angelic or divine response); and gematria (analyzing the numerical structure of divine names to reveal hidden correspondences, used both for contemplation and for constructing new operative formulae). "
            "Each method rests on the conviction that the name participates in the divine reality it names: proper engagement with the name is real engagement with that reality."
        ),
        "philosophical_meaning": (
            "Philosophically, divine name doctrine rests on a realist theory of language derived from the Platonic Cratylus (in which Socrates argues for the natural fitness of names to things) and from the Neoplatonic doctrine that the divine names are not human conventions but emanations from the divine principle itself. "
            "On this view, language is not primarily a human tool for communication but a cosmic phenomenon: the universe was spoken into existence by divine names, and the divine names in human language participate — however distantly — in that original creative speech. "
            "The practitioner who correctly uses a divine name is not speaking about divine reality but speaking from within it, participating in the creative speech through which that reality maintains itself."
        ),
        "spiritual_meaning": (
            "Spiritually, divine name practice aims at the progressive assimilation of the practitioner's consciousness to the divine reality expressed in the names. "
            "Abulafia's meditation system sought prophetic illumination and mystical union through sustained engagement with the divine name: the practitioner's ordinary mental activity gradually dissolved in the luminous clarity of the name's own reality. "
            "Christian Kabbalists sought through divine name practice the experience of divine sonship — the assimilation of the practitioner to the divine Son whose name (Yeshua) was the Tetragrammaton's perfection. "
            "In each case, divine name practice is not merely instrumental (aimed at producing effects in the world) but transformative: the practitioner who sustains it is genuinely changed by the encounter with what the names express."
        ),
        "transmission_genealogy": (
            "Biblical divine name traditions (Exodus, Psalms) and early rabbinic reverence for the Tetragrammaton provided the foundation. "
            "Sefer Yetzirah (third–sixth century CE) developed the creative power of Hebrew letters. "
            "Medieval German Hasidism (Eleazar of Worms) and Spanish Kabbalah (Zohar, late thirteenth century) systematized divine name practice. "
            "Abraham Abulafia (c. 1240–c. 1291) developed prophetic meditation on divine names. "
            "Pico della Mirandola (Conclusiones, 1486) introduced Christian Kabbalah; Reuchlin's De Arte Cabalistica (1517) developed the Yeshua doctrine; Agrippa's De Occulta Philosophia (1531) systematized the full framework. "
            "Dee's Enochian system (1582–89) represented the tradition's most ambitious Renaissance expansion. "
            "The Abramelin operation, Rosicrucian Kabbalah, and the Golden Dawn's systematic use of divine names in ceremonial magic carry the tradition into the modern period."
        )
    },
    47: {
        "summary": (
            "Mystical Union — Greek henosis, Latin unio mystica — designates the direct experiential contact with or absorption into the divine that constitutes the culminating goal of both Neoplatonic contemplative philosophy and the Christian mystical tradition. "
            "The central theological tension runs between two models: union as absorption (the soul loses its individual identity in the divine, as a drop in the ocean), associated with Plotinus and Eckhart's Durchbruch, and union as marriage (the soul retains its identity in intimate relationship with the divine, as bride and bridegroom), associated with Bernard of Clairvaux and the Flemish beguine mysticism. "
            "Alchemical imagery — coniunctio, the Rebis, the completion of the opus — provided the most influential visual and conceptual vocabulary for mystical union in the Renaissance, and the debate about whether union is temporary experience or permanent transformation remains unresolved in the tradition."
        ),
        "essay": (
            "Mystical Union — called henosis in Greek, unio mystica in Latin — designates the direct experiential contact with the divine that both Neoplatonic contemplative philosophy and Christian mystical theology identify as the highest goal of the spiritual life: not knowledge about the divine, not moral conformity to divine will, not even sustained loving attention to divine presence, but an experiential state in which the ordinary distinction between the knowing self and the known divine is surpassed, suspended, or transformed. "
            "The nature of that surpassal — whether the self is temporarily absorbed, permanently transformed, or mysteriously united while remaining distinct — has generated the most searching and theologically consequential debates in the mystical tradition.\n\n"
            "The Neoplatonic foundation is Plotinus's account of henosis in the Enneads (especially VI.9 and V.1). "
            "For Plotinus, the highest hypostasis — the One — is absolutely simple, beyond being, beyond thought, beyond all determination. "
            "The soul that ascends through the contemplation of Intelligence (Nous) and then abandons even that contemplation in a final, thought-free receptivity achieves momentary union with the One: a condition Plotinus describes as a 'falling asleep of the ordinary faculty of knowing' and an awakening to a purer state that is beyond ordinary knowing and being known. "
            "This union is not absorption in the sense of annihilation: the soul returns from it to ordinary consciousness, retaining only the memory and the orientation produced by the encounter. "
            "Plotinus is notably reticent about specifying the mechanism of this union, describing it in terms of receptivity, simplicity, and the stripping of all determination rather than in terms of any positive content.\n\n"
            "Meister Eckhart (c. 1260–1328) gave mystical union its most theologically radical Christian articulation. "
            "Eckhart's Middle High German sermons develop the concept of the Durchbruch — the 'breakthrough' — in which the soul passes through the personal God (Gott) of Christian devotion into the Godhead (Gottheit) that underlies and surpasses it: a nameless, formless abyss of pure being identical with the soul's own ground (Seelengrund). "
            "In the Durchbruch, Eckhart asserts, the soul is not merely united with God but is God — not in terms of the hypostatic union of Christ's two natures, but in terms of the structural identity of the soul's ground with the divine ground. "
            "This claim brought Eckhart before inquisitorial investigation; twenty-eight propositions from his works were condemned in the papal bull In agro dominico (1329), one year after his death. "
            "His Rhineland Dominican disciples Johannes Tauler and Heinrich Suso preserved his themes in somewhat more cautious formulation, and the entire stream of German mysticism that led through the Theologia Germanica (c. 1350) to Luther's early reading was shaped by Eckhartian union mysticism.\n\n"
            "The alternative model — union as marriage rather than absorption — is associated most powerfully with Bernard of Clairvaux (1090–1153) and his commentaries on the Song of Songs, which read the bridal mysticism of the Hebrew poem as describing the soul's loving union with the divine Word. "
            "In Bernard's framework, the union of bride and bridegroom maintains the distinction of persons: the soul and Christ remain themselves even in their most intimate embrace. "
            "This model was developed by Flemish beguine mystics (Hadewijch, Mechthild of Magdeburg) and by the Flemish Augustinian Jan van Ruusbroec (1293–1381), whose distinction between union (the soul flowing into God) and the return from union (the soul's activity in the world) provided a dynamic model of the mystical life that avoided both annihilationist extremes and the reduction of union to mere devotional feeling.\n\n"
            "Jacob Böhme (1575–1624) provided spiritual alchemy's most theologically precise account of mystical union. "
            "For Böhme, union with the divine was not an immediate simplicity but a complex dynamic event in which the soul's fire-will was overcome by divine love and transformed into the luminous consciousness of the new being. "
            "The 'eternal birth' of divine wisdom (Sophia) in the soul was not a single experience but an ongoing process in which the soul's dark wrath-principle was progressively converted into divine love-light. "
            "Böhme's account insisted on the embodied dimension of this process: the soul's transformation was simultaneously a transformation of its relationship to its body and to the material world, not a flight into pure interiority.\n\n"
            "In alchemical discourse, mystical union was figured as the coniunctio — the conjunction of sun and moon, king and queen, sulfur and mercury — that produced the philosopher's stone. "
            "The Rosarium Philosophorum sequence (hieros gamos, death, resurrection, hermaphrodite) provided the most influential visual narrative of union through death and resurrection. "
            "The coniunctio is not a simple merging but a complex operation involving differentiation, conflict, dissolution, and reintegration: the parties to the union must first be clearly distinguished and then brought into the specific combination that produces the stone. "
            "Jung's Mysterium Coniunctionis (1955–56) read the alchemical coniunctio as a projection of the psyche's individuation process — the integration of conscious and unconscious, masculine and feminine, ego and shadow — and treated mystical union and psychological wholeness as variant descriptions of the same process.\n\n"
            "The temporal structure of mystical union is a persistent point of debate: is union a temporary experience that the soul 'returns from,' or is it a permanent transformation? "
            "Plotinus describes it as occasional and brief. "
            "Eckhart's language in the Durchbruch suggests a permanent structural transformation — the soul that breaks through into the Godhead never entirely loses its ground there. "
            "The eighteenth-century Quietist controversy (centered on Fénelon and Madame Guyon) turned precisely on this question: whether the permanent 'state' of pure love (in which the soul loves God without any admixture of self-interest, including the interest in its own salvation) was spiritually legitimate or amounted to Quietist passivity incompatible with Christian virtue.\n\n"
            "What practices lead to mystical union? "
            "The traditions are broadly consistent: sustained contemplative attention (lectio divina, hesychast prayer, Ignatian meditation); progressive stripping of concepts, images, and desires (the apophatic way); moral purification understood as the removal of the obstacles to divine presence rather than the production of virtue; and — in the theurgic and spiritual alchemical traditions — specific ritual operations or laboratory disciplines that open the practitioner to dimensions of reality inaccessible through ordinary consciousness."
        ),
        "operational_meaning": (
            "Practices directed toward mystical union are organized around three overlapping approaches: the cataphatic (working through specific images, texts, and devotional practices to bring the practitioner into sustained divine presence), the apophatic (systematic negation of all concepts and images, leaving the practitioner in a receptive emptiness), and the operative (theurgic ritual, alchemical laboratory work, or mesmeric induction understood as opening channels for divine power). "
            "Hesychast practice (from Evagrius through Gregory Palamas) involves the repetition of the Jesus Prayer coordinated with breath and heartbeat until the prayer becomes continuous and the practitioner experiences the uncreated divine light. "
            "Eckhart's practice involves the radical 'letting go' (Gelassenheit) of all possessions, desires, and even spiritual consolations until the ground is cleared for the Durchbruch. "
            "Böhmean practice involves meditation on the seven qualities of eternal nature while submitting the fire-will to the action of divine love."
        ),
        "philosophical_meaning": (
            "Philosophically, mystical union raises the question of participation: can a finite being genuinely share in infinite divine reality without either being absorbed (ceasing to be finite) or remaining entirely external (sharing nothing)? "
            "The Neoplatonic doctrine of methexis (participation) and the Christian theological doctrine of theosis (deification) both articulate versions of the answer that genuine participation is possible without identity: the soul shares in divine life analogically, becoming more fully what it is by participating in what it is not. "
            "Eckhart's Durchbruch pushes against this limit toward identity, as does Plotinus's henosis; the mystical marriage tradition preserves the distinction. "
            "The deepest philosophical question is whether union preserves or abolishes the self — and whether the self that is preserved after union is the same self that entered it."
        ),
        "spiritual_meaning": (
            "Spiritually, mystical union is the telos of the entire contemplative and alchemical tradition: the point at which the soul achieves its deepest nature, which is divine. "
            "Whether described as absorption (Plotinus, Eckhart), marriage (Bernard, Ruusbroec), the birth of the new being (Böhme), or the completion of the Great Work (alchemical rubedo), it designates the condition in which the soul is no longer in conflict with itself or its divine ground — in which the friction that generates the heat of spiritual development has been transformed into the light of settled divine presence. "
            "It is simultaneously the goal of the journey and the discovery that the journey's end was always already the journey's beginning — that what was sought was the nature of what sought it."
        ),
        "transmission_genealogy": (
            "Plotinus (Enneads, c. 250–270 CE) provided the classical Neoplatonic formulation. "
            "The Pseudo-Dionysius (c. 500 CE) Christianized it as the mystical theology of apophatic ascent. "
            "Meister Eckhart (c. 1260–1328) radicalized it in the German Dominican tradition. "
            "The Flemish mystical tradition (Ruusbroec, Hadewijch) developed the marriage model. "
            "Ficino's Platonic Theology (1469–74) recovered the Plotinian framework for the Renaissance. "
            "Böhme (1575–1624) gave it spiritual-alchemical theological form. "
            "The Philadelphian movement (Jane Lead, John Pordage) transmitted the Böhmean account to England. "
            "The Quietist controversy (Fénelon, Madame Guyon) engaged the permanent-union question. "
            "Jung's Mysterium Coniunctionis (1955–56) provided the twentieth-century psychological reading."
        )
    },
    48: {
        "summary": (
            "Regeneration designates the spiritual and alchemical concept of genuine rebirth — not moral improvement or intellectual development but an ontological change in the very substance of the soul, producing a qualitatively new being. "
            "The concept connects John 3's baptismal new birth, the Corpus Hermeticum Tractate XIII's account of Tat's regeneration through the replacement of material demons by divine powers, Böhme's Wiedergeburt as the birth of Christ in the soul, and the phoenix image of alchemy — death by fire and rebirth from ashes. "
            "Paracelsus extended the concept to metals regenerated in the earth and to medicinal preparations that restored bodies to primal vitality, grounding regeneration in actual natural process rather than metaphor alone."
        ),
        "essay": (
            "Regeneration — from the Latin regeneratio, new birth — designates the spiritual and alchemical conviction that the goal of the Work is not gradual moral improvement, intellectual development, or even mystical experience, but a genuine ontological change in the very substance of the soul: the production of a qualitatively new being in whom the old nature has been genuinely superseded and a new, divine-participatory nature has been established. "
            "This distinguishes regeneration from reform (which changes behavior while leaving nature intact), from illumination (which changes knowledge while leaving substance intact), and from moral growth (which strengthens existing capacities rather than creating new ones). "
            "Regeneration claims that what is produced is literally a new kind of being — not the old being improved but a different being born.\n\n"
            "The foundational Christian text is the third chapter of the Gospel of John, in which Jesus tells Nicodemus that unless a person is 'born again' (or 'born from above,' Greek anothen, deliberately ambiguous) he cannot enter the Kingdom of God. "
            "Nicodemus's literalist response — 'How can a man be born when he is old? Can he enter a second time into his mother's womb and be born?' — provides the occasion for Jesus's clarification that the new birth is 'of water and Spirit' — a spiritual birth requiring divine agency, not human effort. "
            "This text established regeneration as a central Christian theological category and generated enormous commentary on its precise meaning: Is regeneration accomplished at baptism? Through faith? Through a combination of divine grace and human cooperation? "
            "These controversies, active from the early Church through the Reformation and beyond, provided the theological framework within which spiritual alchemists worked when they used regeneration language.\n\n"
            "The Corpus Hermeticum Tractate XIII, 'On Regeneration,' provides the most developed ancient Hermetic account. "
            "The dialogue between Hermes Trismegistus and his son Tat describes regeneration as a transformation through which the twelve tormentors — material vices corresponding to the signs of the zodiac (ignorance, grief, incontinence, desire, injustice, avarice, deceit, envy, treachery, anger, rashness, malice) — are replaced by their corresponding divine powers (knowledge, joy, self-control, fortitude, justice, generosity, truth, goodness, life, light, beatitude, and love). "
            "This is not metaphor in the Hermetic understanding: the tormentors and divine powers are actual entities operative in the soul, and regeneration is their actual replacement. "
            "Tat at the conclusion of the dialogue reports a genuinely altered state: he perceives differently, experiences differently, and understands himself as a new being. "
            "This framework — regeneration as the replacement of material principles by divine ones in the soul's actual constitution — deeply influenced the spiritual alchemical tradition.\n\n"
            "Jacob Böhme (1575–1624) gave regeneration its most systematic Protestant theological elaboration and its most direct connection to alchemical conceptuality. "
            "Böhme's concept of Wiedergeburt ('rebirth' or 'new birth') was central to his entire theological vision: the fallen human being, dominated by the fire-wrath principle inherited from Adam's self-assertion, must undergo a genuine interior death and birth through which the fire-principle is converted into the love-light of divine Sophia. "
            "For Böhme this was not an experience but an event: a real change in the soul's substantial constitution, not merely in its states of consciousness. "
            "The process was explicitly alchemical: the seven qualities of eternal nature — Böhme's alchemical-cosmological principles — were operative in the soul, and their transformation followed the same dynamics as the opus in the laboratory. "
            "Nigredo in the soul was the dark night of the self-will's confrontation with its own wrathfulness; albedo was the dawning of divine light as the fire-will surrendered; rubedo was the establishment of the new being in whom divine love had permanently overcome the fire-principle.\n\n"
            "Johann Arndt's Vier Bücher vom wahren Christentum (Four Books of True Christianity, 1605–10) was the most widely read Protestant devotional text of the seventeenth century and the primary vehicle through which the regeneration concept entered popular Protestant spirituality. "
            "Arndt, drawing on medieval mysticism (Tauler, Ruusbroec, Thomas à Kempis), Paracelsian natural philosophy, and Böhmean theosophy, presented regeneration as the entire substance of Christian life: the Christian was one undergoing regeneration, progressively brought from the old nature of sin into the new nature of divine love. "
            "Arndt's extensive use of alchemical and natural philosophical imagery — distillation, putrefaction, the phoenix — made him a crucial bridge between devotional Protestantism and the spiritual alchemy tradition.\n\n"
            "The phoenix is the alchemical emblem most directly associated with regeneration: the bird that ages, piles the spices of its own funeral pyre, is consumed by fire, and rises renewed from the ashes. "
            "Michael Maier's Atalanta Fugiens (1617) includes the phoenix in its emblem series; the bird appears in Rosicrucian symbolism, in Böhmean imagery, and in the entire spiritual alchemical tradition as the image of radical renewal through radical destruction. "
            "The phoenix is not reformed — it does not gradually improve; it must die completely before the new being can emerge from the ashes. "
            "This insistence on the necessity of death — real spiritual death, not merely ascetic discipline — distinguishes the regeneration concept from all ameliorative spiritual programs.\n\n"
            "Paracelsus (1493/4–1541) extended regeneration into the domain of natural philosophy and medicine. "
            "For Paracelsus, the physician's task was not merely to suppress symptoms but to assist the vis medicatrix naturae — the healing power of nature — in restoring the body's archeus (its governing vital principle) to its original, pristine constitution. "
            "This was a form of bodily regeneration: not merely repair but renewal, the restoration of the body's primal vitality that illness had corrupted. "
            "Paracelsus also wrote of the regeneration of metals in the earth: just as a seed planted in the earth dies and regenerates into a new plant, so metallic seeds planted in the appropriate geological matrix could regenerate into higher metals over geological time. "
            "The alchemist who understood this process could accelerate it in the laboratory.\n\n"
            "Mary Anne Atwood's Suggestive Inquiry (1850) brought together the Hermetic, Böhmean, and mesmeric traditions of regeneration into a single systematic account. "
            "Atwood argued that the Great Work was the mesmeric induction of regeneration: the skilled operator, working on a subject in mesmeric trance, assisted the dissolution of the old material consciousness and the emergence of the new spiritual consciousness — a process she read as the fulfilment of the Hermetic Tractate XIII's promise, the actual replacement of the tormentors by the divine powers. "
            "This was operative regeneration: specific techniques, properly applied, producing genuine ontological change.\n\n"
            "The distinction that regeneration insists upon — between genuine ontological change and mere moral or psychological improvement — remains theologically and philosophically contested. "
            "Reformed Protestant theology (drawing on Luther's simul justus et peccator — simultaneously just and sinner) tends to locate regeneration in divine declaration rather than ontological transformation. "
            "Catholic and Orthodox theology (theosis, divinization) insists on real ontological participation in divine nature. "
            "Spiritual alchemy, following the Hermetic Tractate XIII and Böhme, takes the most radical position: regeneration is real, substantial, and operative — producing a being that literally participates in divine nature in ways the unregenerate being does not."
        ),
        "operational_meaning": (
            "What does regeneration require in practice? "
            "The traditions converge on several operational elements: sustained discipline that breaks the dominance of the old nature's habitual patterns (ascetic practice, moral examination, the via purgativa); specific positive practices that cultivate the new nature's faculties (prayer without ceasing, meditation on divine wisdom, laboratory work understood as cooperation with divine creative process); willingness to undergo the death-phase — the genuine surrender of the old self's identity and control — that the tradition figures as nigredo, the dark night, or the phoenix's consumption; and receptivity to the grace or divine power that alone can accomplish the actual substitution of old nature for new. "
            "Böhme's practical guidance centers on the 'yielding' of the fire-will to divine love; Atwood's on the mesmeric operator's skilled assistance of this yielding through induced trance."
        ),
        "philosophical_meaning": (
            "Philosophically, regeneration requires a participatory ontology: the claim that a finite being can genuinely receive a new ontological constitution through participation in divine being, becoming a different kind of being without ceasing to be itself. "
            "This stands against both purely immanent accounts of spiritual development (in which the soul develops only capacities already latent in itself) and purely transcendent accounts (in which divine action is wholly external and leaves the creature's nature unchanged). "
            "Regeneration claims that divine nature can become constitutive of created nature in a genuinely new way — that the creature born again is neither the same creature improved nor a new creature replacing the old, but the same creature transformed through real ontological participation in what it was not before."
        ),
        "spiritual_meaning": (
            "Spiritually, regeneration is the Great Work's ultimate claim: that genuine transformation of the soul's nature — not mere purification or illumination but actual new birth — is possible, achievable, and constitutes the proper telos of human existence. "
            "The alchemist who completes the Work does not merely understand gold or produce gold: she is gold — her soul has been transformed into the incorruptible, projective, luminous nature that the philosopher's stone represents. "
            "This is the 'glorious body' of Pauline theology (Philippians 3:21), the 'spiritual body' of 1 Corinthians 15, the 'new creature' of 2 Corinthians 5:17, and the Böhmean 'new being born from divine love' — all different expressions of the single conviction that regeneration produces a genuinely different, genuinely new mode of being."
        ),
        "transmission_genealogy": (
            "The Johannine new birth theology (Gospel of John 3, c. 90–100 CE) and the Hermetic Tractate XIII on regeneration (second–third century CE) are the foundational texts. "
            "The medieval mystical tradition (Tauler's Seelengrund, the Theologia Germanica) carried the concept through the late medieval period. "
            "Johann Arndt's Wahres Christentum (1605–10) made it central to Protestant devotional spirituality. "
            "Böhme (1575–1624) gave it systematic alchemical-theological form. "
            "The Philadelphian movement (Jane Lead, John Pordage), the Pietist tradition (Francke, Zinzendorf), and the Swedenborgian New Church all transmitted Böhmean regeneration themes. "
            "Atwood's Suggestive Inquiry (1850) synthesized the mesmeric-alchemical account. "
            "The concept remains active in contemporary Western esotericism, transpersonal psychology, and integrative spiritual traditions."
        )
    }
}

def main():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    concepts = data.get('concepts', [])
    updated = []

    for concept in concepts:
        cid = concept['id']
        if cid not in UPDATES:
            continue
        before_len = len(concept.get('essay', '') or '')
        upd = UPDATES[cid]
        concept['essay'] = upd['essay']
        concept['summary'] = upd['summary']
        concept['operational_meaning'] = upd['operational_meaning']
        concept['philosophical_meaning'] = upd['philosophical_meaning']
        concept['spiritual_meaning'] = upd['spiritual_meaning']
        concept['transmission_genealogy'] = upd['transmission_genealogy']
        after_len = len(concept['essay'])
        updated.append((cid, concept['name'], before_len, after_len))

    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Done. Results:")
    for cid, name, before, after in updated:
        print(f"  id={cid} {name}: {before} → {after} chars")

    # Verify JSON
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        json.load(f)
    print("JSON valid.")

if __name__ == '__main__':
    main()
