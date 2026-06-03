#!/usr/bin/env python3
"""Generate the technical alchemical and Rosicrucian glossary (dictionary) for prototype_data.json."""
import json
from pathlib import Path

glossary = [

# ─── Alchemical Stages & Operations ──────────────────────────────────────────

{"id":"nigredo","term":"Nigredo","latin":"nigredo","also_known_as":["blackening","putrefactio","melanosis"],
"category":"alchemical_stage","period":"12th–18th c.",
"definition":"The first and most fearful stage of the alchemical opus, nigredo designates the blackening and putrefaction of the prima materia. In laboratory alchemy it corresponds to calcination or dissolution processes that break down the starting material into an undifferentiated black mass. In the spiritual tradition codified by Jung's interpreters and anticipated in Böhme, it signifies a dark night of the soul — the mortification of ego-consciousness preceding regeneration. Michael Maier's Atalanta Fugiens and Daniel Cramer's Rosicrucian emblems both visualize it as a black sun (sol niger) or a raven. For Paracelsus the stage involved separating the impure from the pure through fire; for later spiritual alchemists it became the necessary precondition for enlightenment.",
"etymology":"Latin niger (black) + -edo (state or condition).","related_concept_id":None,"related_terms":["albedo","rubedo","calcinatio","putrefactio","prima-materia"]},

{"id":"albedo","term":"Albedo","latin":"albedo","also_known_as":["whitening","leucosis","ablutio"],
"category":"alchemical_stage","period":"12th–18th c.",
"definition":"The second major stage of the opus alchymicum, albedo follows nigredo through washing or 'ablution' of the blackened matter. It produces a brilliant white substance associated with the lunar principle, silver, and purified consciousness. In Paracelsian medicine it signified the purification of the body's vital spirits. The emblem tradition — notably Maier's Atalanta Fugiens emblem XIV — depicts a white queen or white swan emerging from darkness. Spiritual alchemists (Zuber's analysis) read albedo as the stage of soul-purification in which dross desires are eliminated and the practitioner attains clarity. Some traditions insert a transitional citrinitas (yellowing) between albedo and the final rubedo.",
"etymology":"Latin albus (white) + -edo.","related_concept_id":None,"related_terms":["nigredo","citrinitas","rubedo","ablutio","luna"]},

{"id":"citrinitas","term":"Citrinitas","latin":"citrinitas","also_known_as":["yellowing","xanthosis"],
"category":"alchemical_stage","period":"12th–17th c.",
"definition":"A transitional stage between albedo and rubedo, citrinitas (yellowing) appears in many medieval alchemical texts but was progressively dropped by 17th-century authors who compressed the opus into three primary stages. The yellow colour was associated with the solar principle and with gold approaching its final perfection. In the Arabic-influenced tradition (Jabir, pseudo-Geber) all four stages were retained. The emblem of the peacock's tail (cauda pavonis) sometimes represents citrinitas because the peacock's iridescent feathers display yellow alongside other colours. Modern Jungian commentary associates it with an intuitive rather than fully realised consciousness.",
"etymology":"Latin citrinus (lemon-yellow).","related_concept_id":None,"related_terms":["nigredo","albedo","rubedo","cauda-pavonis"]},

{"id":"rubedo","term":"Rubedo","latin":"rubedo","also_known_as":["reddening","iosis"],
"category":"alchemical_stage","period":"12th–18th c.",
"definition":"The culminating stage of the opus alchymicum, rubedo signifies the final reddening that produces the philosophers' stone (lapis philosophorum). In the laboratory it corresponds to the projection of a red tincture or powder onto base metals. The colour red is associated with Sol (the sun), with sulphur in its most exalted state, and with the union of masculine and feminine principles. In spiritual alchemy, rubedo represents the final integration of the alchemist's personality — the wedding of soul and spirit, analogous to the hieros gamos. Daniel Cramer's emblem 22 depicts a red king crowned and enthroned. Maier's Atalanta Fugiens mottos address the red stage as the perfection of the Work.",
"etymology":"Latin rubeus (red) + -edo.","related_concept_id":None,"related_terms":["nigredo","albedo","lapis-philosophorum","hieros-gamos","sol"]},

{"id":"calcinatio","term":"Calcinatio","latin":"calcinatio","also_known_as":["calcination","incineration"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The reduction of a substance to its calx (ash or powder) by sustained heat; often the first operative procedure in the opus. Practically, calcination destroys the structural integrity of metals and organic materials, reducing them to powder and initiating the putrefaction associated with nigredo. Paracelsus elevated calcination to a medical procedure — calxes of metals were used therapeutically in his system. Symbolically the operation corresponded to the annihilation of the false self. The calcinated substance was called the 'dead body' awaiting resurrection through solution and cohobation. George Starkey's laboratory notebooks (studied by Principe and Newman) show systematic calcination records.",
"etymology":"Medieval Latin calcinare, from calx (lime, chalk, burnt stone).","related_concept_id":None,"related_terms":["solutio","nigredo","prima-materia","paracelsian-medicine"]},

{"id":"solutio","term":"Solutio","latin":"solutio","also_known_as":["dissolution","solve"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The dissolution of a solid into a liquid — the operatic inverse of coagulatio. In practice, solutio involved acid dissolution, water digestion, or amalgamation with mercury. The axiom 'solve et coagula' (dissolve and coagulate) encapsulates the rhythmic tension of the entire opus: the material must be dissolved back to prime matter before it can be reconfigured into a higher form. Philosophically, solutio represented the loosening of fixed forms, the liquefaction of the rigid ego, and the opening to transformation. The emblem of the king drowning in the sea — as in Rosarium Philosophorum (1550) — images the solar principle undergoing solutio.",
"etymology":"Latin solvere (to loosen, dissolve).","related_concept_id":None,"related_terms":["coagulatio","calcinatio","solve-et-coagula","prima-materia"]},

{"id":"coagulatio","term":"Coagulatio","latin":"coagulatio","also_known_as":["coagulation","fixation","solidification"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The congealing or solidification of a dissolved substance — the operative complement of solutio. In laboratory practice, coagulatio produced the crystalline or solid product from a solution, often achieved by cooling, evaporation, or the addition of a coagulating agent. The process gave philosophical form to the materia prima: what had been fluid and formless was fixed into a definite, stable substance. The aphorism 'solve et coagula' (dissolve and coagulate) defined the dual motion of the Work. Spiritually, coagulatio represented the crystallisation of purified consciousness into a permanent disposition — the establishment of the 'stone' in the alchemist's own being.",
"etymology":"Latin coagulare (to curdle, congeal).","related_concept_id":None,"related_terms":["solutio","fixatio","solve-et-coagula"]},

{"id":"sublimatio","term":"Sublimatio","latin":"sublimatio","also_known_as":["sublimation","elevation"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The conversion of a solid directly into vapour by heat, bypassing the liquid state; the condensed vapour deposits as a pure sublimate. Practically, sublimation was used to purify mercury, arsenic, and sulphur compounds. In symbolic terms it was the most 'spiritualizing' of operations, associated with the elevation of crude matter to a higher state. Paracelsus used sublimation in preparing arcana. The image of a flying eagle often represented sublimation in emblem literature — the heavy made light, the terrestrial made aerial. The procedure was central to the preparation of the philosophical mercury in the dry-path and wet-path traditions.",
"etymology":"Latin sublimare (to elevate, exalt), from sublimis (raised aloft).","related_concept_id":None,"related_terms":["distillatio","philosophical-mercury","arcanum","paracelsian"]},

{"id":"putrefactio","term":"Putrefactio","latin":"putrefactio","also_known_as":["putrefaction","corruption","mortificatio"],
"category":"alchemical_stage","period":"12th–18th c.",
"definition":"The decomposition or rotting of the prima materia, typically identified with the nigredo stage. In laboratory terms, putrefactio involved the digestion of matter in a sealed vessel ('philosophic egg') at gentle heat — the 'dung-heat' of the Athanor furnace — over an extended period (sometimes weeks). The resulting black, stinking mass was understood as the death of the old form, necessary precondition for rebirth. Paracelsus distinguished putrefaction from calcination: the former required moisture and gentleness, the latter fire and violence. The image of a king decomposing in the earth — or of a black crow perched on a skull — emblematized putrefactio.",
"etymology":"Latin putrefacere (to make rotten), from putere (to stink).","related_concept_id":None,"related_terms":["nigredo","calcinatio","athanor","mortificatio"]},

{"id":"fermentatio","term":"Fermentatio","latin":"fermentatio","also_known_as":["fermentation","impregnation"],
"category":"alchemical_stage","period":"15th–18th c.",
"definition":"The introduction of a small quantity of the philosophical stone or a prepared tincture into the work to catalyse its transformation — by analogy with bread-leaven or wine yeast. Fermentatio is often distinguished from projection (the final act of transmutation) as the preparatory stage in which the stone is 'opened' and activated. In Paracelsian medicine, fermentation explained the action of arcana: a tiny quantity could transform a large amount of diseased matter. Symbolically fermentatio represented the infusion of spiritual principle into dense matter, analogous to grace entering the soul. The number and ratio of ferment to matter was a closely guarded procedural secret.",
"etymology":"Latin fermentum (leaven, yeast).","related_concept_id":None,"related_terms":["projectio","multiplicatio","lapis-philosophorum","arcanum"]},

{"id":"distillatio","term":"Distillatio","latin":"distillatio","also_known_as":["distillation","rectification"],
"category":"alchemical_stage","period":"12th–18th c.",
"definition":"The separation of a volatile component from a mixture by heating and condensing the vapour — one of the oldest and most practically useful alchemical operations. Distillation was central to Paracelsian medicine for preparing quintessences and spirituous medicaments. Alambics (stills) and Pelican flasks for circulation-distillation were standard equipment. Multiple redistillations ('cohobation') were believed to increase purity and potency. Spiritually, distillation was associated with the refinement of the soul's subtler aspects: the practical and metaphorical dimensions were kept in productive tension by 17th-century practitioners.",
"etymology":"Latin destillare (to drip, trickle down), from de- (down) + stillare (to drip).","related_concept_id":None,"related_terms":["sublimatio","cohobation","quinta-essentia","alambic"]},

{"id":"separatio","term":"Separatio","latin":"separatio","also_known_as":["separation","analysis","diairesis"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The division of a mixed substance into its constituent principles — earth, water, air, fire, or sulphur, mercury, and salt. Separatio was often the first analytical step after putrefaction, dividing the blackened mass into its gross and subtle parts. In Paracelsian theory, the archei (formative forces) in the body carried out an internal separatio, sorting nourishment from waste. The emblematic image was of a sword or scalpel dividing the living from the dead. Some traditions placed separatio near the beginning of the opus; others made it a continuous discipline alternating with coniunctio throughout the work.",
"etymology":"Latin separare (to put apart, divide).","related_concept_id":None,"related_terms":["coniunctio","calcinatio","tria-prima","archeus"]},

{"id":"coniunctio","term":"Coniunctio","latin":"coniunctio","also_known_as":["conjunction","union","chymical wedding","syzygy"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The union of opposing principles — typically Sol and Luna (gold and silver, sulphur and mercury, king and queen, fixed and volatile) — to produce a higher synthesis. Coniunctio is at once an operative procedure (the mixing of two prepared substances), an emblematic motif (the sacred marriage depicted in Rosarium Philosophorum woodcuts), and a philosophical principle (the reconciliation of opposites at the heart of Hermetic cosmology). The Chymische Hochzeit Christiani Rosencreutz (1616) allegorizes an entire Rosicrucian initiation as a chymical wedding. C.G. Jung devoted major analysis to coniunctio as a symbol of psychological integration.",
"etymology":"Latin coniungere (to yoke together, unite).","related_concept_id":None,"related_terms":["hieros-gamos","separatio","rubedo","sol","luna"]},

{"id":"multiplicatio","term":"Multiplicatio","latin":"multiplicatio","also_known_as":["multiplication","augmentation"],
"category":"alchemical_stage","period":"15th–18th c.",
"definition":"The increase in both quantity and power of the philosophers' stone through repeated cycles of fermentation and projection. A stone capable of transmuting one part of base metal to gold could, through multiplication, be empowered to transmute a thousand parts, then a million. This exponential amplification distinguished the true stone from mere transmuting agents. Medieval authors such as pseudo-Geber (Summa Perfectionis) specified three degrees of multiplication. In spiritual alchemy, multiplicatio corresponded to the increasing illuminative capacity of the purified practitioner.",
"etymology":"Latin multiplicare (to multiply, increase manifold).","related_concept_id":None,"related_terms":["projectio","fermentatio","lapis-philosophorum"]},

{"id":"projectio","term":"Projectio","latin":"projectio","also_known_as":["projection","transmutation","tincture casting"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The final operative act: casting a small quantity of the perfected stone or tincture onto molten base metal to effect transmutation to gold or silver. Authors specify elaborate protocols — the stone must be wrapped in wax or gold foil, then cast onto the crucible. The ratio of stone to metal transformed was called the 'grade' of the stone; a stone of the seventh grade might transmute a thousandfold its weight. Accounts of projection are numerous in alchemical literature, from historical figures such as Johann Friedrich Schweitzer (Helvetius) to likely fabrications. Lawrence Principe has examined projectio claims with unusual rigor.",
"etymology":"Latin proicere (to throw forward).","related_concept_id":None,"related_terms":["multiplicatio","lapis-philosophorum","fermentatio","tinctura"]},

{"id":"fixatio","term":"Fixatio","latin":"fixatio","also_known_as":["fixation","coagulatio","making fast"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The conversion of a volatile substance into a fixed (non-volatile) form by sustained heat or combination with an earthly principle. Fixation was intimately related to coagulation and was a key step in the preparation of the philosophers' stone, which had to be fixed sufficiently to withstand the extreme heat of projection without subliming away. The volatile-fixed axis was one of the fundamental polarities of alchemical theory: sulphur was typically fixed, mercury volatile; the Work aimed to fix the volatile while volatilizing the fixed. George Starkey's laboratory notebooks document numerous fixation procedures.",
"etymology":"Latin figere (to fasten, fix).","related_concept_id":None,"related_terms":["coagulatio","sublimatio","projectio","philosophical-mercury"]},

{"id":"mortificatio","term":"Mortificatio","latin":"mortificatio","also_known_as":["mortification","killing","death of metals"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The 'death' of a metal or substance — its reduction to a state of apparent inactivity, loss of metallic properties, and readiness for rebirth. Mortificatio overlaps with nigredo and putrefactio but carries a specifically active sense: the alchemist kills the metal deliberately through a chemical agent. In the spiritual reading, mortificatio is the voluntary submission to an ego-death that precedes higher rebirth. Emblem books routinely depict a king killed or buried, a skeleton, or a crowned corpse to represent mortificatio. The motif connects alchemical initiation to Christian death-and-resurrection theology.",
"etymology":"Latin mortificare (to put to death), from mors (death) + facere (to make).","related_concept_id":None,"related_terms":["nigredo","putrefactio","calcinatio","coniunctio"]},

{"id":"circulatio","term":"Circulatio","latin":"circulatio","also_known_as":["circulation","pelican operation"],
"category":"alchemical_stage","period":"15th–18th c.",
"definition":"A continuous distillation in which the condensed vapour is returned to the flask for repeated redistillation — performed in a pelican vessel (a flask with side arms that loop back to the body). Circulatio was believed to produce a substance of supreme purity and potency by subjecting it to an endless cycle. The circular vessel became an emblem of perfection, self-reference, and the eternal return. The ouroboros serpent devouring its own tail is both an image of circulatio and a broader cosmological symbol. Paracelsus valued circulatio for preparing quintessences; Rosicrucian authors used circular imagery to describe spiritual renewal.",
"etymology":"Latin circulare (to move in a circle).","related_concept_id":None,"related_terms":["distillatio","ouroboros","quinta-essentia","athanor"]},

{"id":"cohobation","term":"Cohobation","latin":"cohobatio","also_known_as":["repeated distillation","imbibition and distillation"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The repeated distillation of a liquid over its own residue — the condensed distillate is poured back onto the remaining matter and distilled again, often many times. Cohobation was used to concentrate virtues and to ensure thorough impregnation. It appears in Paracelsian pharmaceutical preparation and in the philosophical work for perfecting the mercury. Some texts specified seven cohobations (the sacred number), others three, others as many as required. The operation required patient, methodical labour — a virtue consistently praised in alchemical literature as necessary for success.",
"etymology":"From Arabic (via Medieval Latin); possibly from Arabic kahaba (to refine).","related_concept_id":None,"related_terms":["distillatio","circulatio","fermentatio"]},

{"id":"ablutio","term":"Ablutio","latin":"ablutio","also_known_as":["ablution","washing","whitening wash"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The washing of the calcined or putrefied matter to remove impurities — a stage bridging nigredo and albedo. Practically, ablutio involved repeated washing with distilled water or with a purified menstruum. Symbolically it carried baptismal resonances: the black, dead matter was washed clean in preparation for its resurrection as white, purified substance. Rosicrucianism picked up these baptismal overtones explicitly: the Fama Fraternitatis describes the opening of the vault of Christian Rosencreutz as revealing an incorruptible, washed body. Several emblem-book images depict a figure being washed or bathed.",
"etymology":"Latin abluere (to wash away, cleanse).","related_concept_id":None,"related_terms":["nigredo","albedo","baptism","putrefactio"]},

{"id":"exaltatio","term":"Exaltatio","latin":"exaltatio","also_known_as":["exaltation","elevation","sublimation of virtues"],
"category":"alchemical_stage","period":"14th–18th c.",
"definition":"The increase in nobility or virtue of a prepared substance through repetition of the opus, or the production of a highly refined sublimate. Exaltatio referred both to the quantitative multiplication of the stone's power and to a qualitative elevation in its nature — the difference between a crude and a perfected medicine. In astrology, exaltatio designated the sign in which a planet exercised its maximum power; alchemists borrowed the term to describe analogous peak-states in materials. The exalted stone was considered the apex of the Work, capable of transforming both metals and the practitioner who possessed it.",
"etymology":"Latin exaltare (to raise up, elevate).","related_concept_id":None,"related_terms":["multiplicatio","lapis-philosophorum","projectio","sublimatio"]},

# ─── The Three Principles / Tria Prima ───────────────────────────────────────

{"id":"tria-prima","term":"Tria Prima","latin":"tria prima","also_known_as":["the three principles","sulphur-mercury-salt"],
"category":"paracelsian","period":"16th–17th c.",
"definition":"Paracelsus's reformulation of the Arabic two-principle theory (sulphur and mercury) into a three-principle system by adding salt. These were not ordinary chemical substances but philosophical principles present in all matter: sulphur = combustibility, soul, and spiritual nature; mercury = volatility, spirit, and mediating principle; salt = solidity, body, and fixity. Together they replaced the four Aristotelian elements as the primary analytical framework of Paracelsian chemistry and medicine. Disease arose from imbalance among the three; health and perfection from their proper proportion and harmony. The tria prima influenced all subsequent alchemical theory, including Rosicrucian philosophy.",
"etymology":"Latin tria (three) + prima (first, primary).","related_concept_id":None,"related_terms":["philosophical-sulphur","philosophical-mercury","philosophical-salt","paracelsian"]},

{"id":"philosophical-sulphur","term":"Philosophical Sulphur","latin":"sulphur philosophorum","also_known_as":["sulphur of the philosophers","coagulating principle"],
"category":"paracelsian","period":"14th–18th c.",
"definition":"In alchemical theory, sulphur (not the common mineral) designates the active, fiery, coagulating principle that gives matter its colour and combustibility. As one of the tria prima, philosophical sulphur corresponds to the soul (anima), the masculine active force, and the principle of colour in metals (red in gold, white in silver). In the binary system predating Paracelsus, sulphur and mercury generated all metals through their proportional combination in the earth. Rosicrucian authors used sulphur as a symbol of the divine masculine principle active in nature. George Starkey's 'sophic sulphur' was a specific philosophical preparation integral to his path to the stone.",
"etymology":"Latin sulphur (brimstone, native sulphur mineral).","related_concept_id":None,"related_terms":["philosophical-mercury","philosophical-salt","tria-prima","prima-materia"]},

{"id":"philosophical-mercury","term":"Philosophical Mercury","latin":"Mercurius philosophorum","also_known_as":["sophic mercury","mercury of the philosophers","divine water"],
"category":"paracelsian","period":"12th–18th c.",
"definition":"The subtle, volatile, mediating principle in alchemical theory — not ordinary quicksilver but its spiritual essence or a specially prepared analogue. Philosophical mercury was the key to the Work because it could dissolve gold without destroying it ('our mercury dissolves gold philosophically'). Authors described elaborate preparations: the mercury must be 'animated,' 'philosophically opened,' and sometimes fused with specific metals before it could serve as the prime solvent. Starkey and Philalethes (Eirenaeus Philalethes, i.e., Starkey) devoted extensive writing to its preparation. In Jungian interpretation, philosophical mercury = the unconscious as transformative medium.",
"etymology":"Latin Mercurius (the planet Mercury; also, quicksilver).","related_concept_id":None,"related_terms":["tria-prima","azoth","prima-materia","philosophical-sulphur","george-starkey"]},

{"id":"philosophical-salt","term":"Philosophical Salt","latin":"sal philosophorum","also_known_as":["salt of the philosophers","sal centrale","body principle"],
"category":"paracelsian","period":"16th–18th c.",
"definition":"The third and often least-discussed of the Paracelsian tria prima, salt designates the fixed, corporeal, and preservative principle in matter. Where sulphur is soul and mercury is spirit, salt is body — the principle that resists decomposition and gives substances their characteristic form and solidity. In medicine, Paracelsus used salts therapeutically and saw disease sometimes as a salt imbalance (notably calculus/stone formations = excess salt). Symbolically, salt was associated with wisdom (sapientia, also sapiens = one who tastes/discerns) and with resurrection — the incorruptible body preserved, like salted meat, for its final transformation.",
"etymology":"Latin sal (salt), from Proto-Indo-European *sal-.","related_concept_id":None,"related_terms":["tria-prima","philosophical-sulphur","philosophical-mercury","paracelsian"]},

{"id":"prima-materia","term":"Prima Materia","latin":"prima materia","also_known_as":["first matter","prime matter","chaos","hyle"],
"category":"alchemical_stage","period":"12th–18th c.",
"definition":"The undifferentiated first matter from which all things are derived and to which the alchemical opus must reduce the starting material before reconstruction. In Aristotelian cosmology, prima materia was pure potentiality without form; alchemy adopted and radicalised this concept, seeking the actual substance underlying all metals. Authors disagreed radically on its identity: it was variously identified as common mercury, dew, antimony, vitriol, salt-peter, the 'black earth,' or a special preparation. The philosopher's stone itself was made from the prima materia by subjecting it to the stages of the opus. The search for the prima materia drove centuries of experimentation.",
"etymology":"Latin prima (first, primary) + materia (matter, substance, timber).","related_concept_id":None,"related_terms":["lapis-philosophorum","philosophical-mercury","nigredo","tria-prima"]},

# ─── Key Substances ────────────────────────────────────────────────────────────

{"id":"lapis-philosophorum","term":"Lapis Philosophorum","latin":"lapis philosophorum","also_known_as":["philosopher's stone","philosophers' stone","the Stone","Rebis"],
"category":"substance","period":"10th–18th c.",
"definition":"The ultimate product and goal of the alchemical opus: a substance (variously described as a red powder, a stone, or a wax-like material) capable of transmuting base metals to gold, preparing a universal medicine (Elixir), and conferring longevity or immortality. The stone was not a fixed chemical formula but a contested theoretical object. Lawrence Principe and William Newman have shown that 17th-century chymists like George Starkey made genuine laboratory attempts to prepare it using well-defined procedures. Spiritual alchemists (Zuber) read the stone as a symbol of the transformed self. The stone's dual action — on metals and on the human body — made it a uniquely powerful symbol bridging material and spiritual ambitions.",
"etymology":"Latin lapis (stone) + philosophorum (of the philosophers; genitive plural of philosophus).","related_concept_id":None,"related_terms":["elixir","projectio","prima-materia","philosophical-mercury","rubedo"]},

{"id":"azoth","term":"Azoth","latin":"azoth","also_known_as":["universal mercury","al-zā'būq","the radical moisture"],
"category":"substance","period":"14th–18th c.",
"definition":"A term with two distinct but related senses: (1) in medieval Arabic-influenced alchemy, a synonym for philosophical mercury or the universal solvent; (2) in later Paracelsian and Rosicrucian usage, the supreme and universal animating principle of nature, identified with the spiritus mundi or with a perfected philosophical agent. Paracelsus placed AZOTH prominently (reportedly had it inscribed on his sword-pommel), using it for the quintessential animating principle of life. The word is sometimes parsed as A-Z-O-TH, combining the first and last letters of the Latin, Greek, and Hebrew alphabets (A/Z, alpha/omega, aleph/tav), signifying universal completeness. Böhme and later theosophists used azoth as a metaphor for divine life-force.",
"etymology":"From Arabic al-zā'būq (mercury/quicksilver), entering Latin as azote/azoth; later reinterpreted as multi-alphabetical.","related_concept_id":None,"related_terms":["philosophical-mercury","prima-materia","spiritus-mundi","paracelsian"]},

{"id":"vitriol","term":"Vitriol","latin":"vitriolum","also_known_as":["green vitriol","blue vitriol","VITRIOL acrostic","sulphate of iron/copper"],
"category":"substance","period":"15th–18th c.",
"definition":"Metal sulphates (ferrous sulphate = green vitriol; copper sulphate = blue vitriol; zinc sulphate = white vitriol) used practically in dyeing and medicine, but also made emblematically prominent by the acronym VITRIOL: Visita Interiora Terrae Rectificando Invenies Occultum Lapidem (Visit the interior of the earth; by rectifying you will find the hidden stone). This alchemical motto appears prominently in Basil Valentine's writings and became a widely-repeated formula. The emblem of a figure descending into the earth represented the VITRIOL program of interior self-examination leading to the discovery of the hidden stone within.",
"etymology":"Medieval Latin vitriolum (glassy stone), from vitrum (glass) due to its crystalline appearance.","related_concept_id":None,"related_terms":["lapis-philosophorum","prima-materia","separatio","basil-valentine"]},

{"id":"alkahest","term":"Alkahest","latin":"alkahest","also_known_as":["universal solvent","menstruum universale","ignis Gehennae"],
"category":"substance","period":"16th–17th c.",
"definition":"A hypothetical universal solvent capable of dissolving any substance without itself being altered — proposed by Paracelsus and developed by Jan Baptist van Helmont. The alkahest, if real, would dissolve gold itself (which aqua regia cannot do without changing), reduce all bodies to their prima materia, and possibly serve as a universal medicine. Van Helmont believed he possessed a preparation called the alkahest and described experiments with it. His claims were controversial and influential. Robert Boyle examined and critiqued the alkahest concept, noting logical difficulties with a solvent that dissolves all things while remaining itself unchanged.",
"etymology":"Origin obscure; possibly Paracelsus's coinage from German 'all-Geist' (all-spirit) or a cipher.","related_concept_id":None,"related_terms":["prima-materia","elixir","van-helmont","menstruum","iatrochemistry"]},

{"id":"elixir","term":"Elixir","latin":"elixir","also_known_as":["elixir of life","elixir vitae","red elixir","white elixir"],
"category":"substance","period":"10th–18th c.",
"definition":"A perfected medicine or quintessence derived from (or identical with) the philosophers' stone, capable of curing all disease and prolonging life indefinitely. The elixir of life entered European alchemy from Arabic sources (al-iksīr) in the 12th–13th centuries. The 'red elixir' transmuted metals to gold; the 'white elixir' produced silver. For Paracelsus, the true arcana were elixirs in this sense — concentrated, spiritualized preparations. The quest for the elixir drove Paracelsian iatrochemistry and contributed to the development of pharmaceutical distillation. Later theosophists (Godwin, Churton) associated the elixir with spiritual immortality.",
"etymology":"From Arabic al-iksīr, perhaps from Greek xēron (dry powder used in medicine).","related_concept_id":None,"related_terms":["lapis-philosophorum","arcanum","quinta-essentia","aurum-potabile","iatrochemistry"]},

{"id":"quinta-essentia","term":"Quinta Essentia","latin":"quinta essentia","also_known_as":["quintessence","fifth element","aether","celestial substance"],
"category":"substance","period":"14th–18th c.",
"definition":"The 'fifth essence' beyond the four Aristotelian elements (earth, water, fire, air), associated with the celestial substance of which the stars were made and, in alchemical usage, the purified spiritual core of any material substance. Distillation could extract the quintessence from wine (producing alcohol, which was the quintessence of the grape), from plants, and from metals. Paracelsus's pharmaceuticals were often quintessences: the most spiritualized, potent, and rapidly effective forms of medicines. Circulatio (repeated distillation) was the preferred method. The concept bridges cosmology, chemistry, and medicine.",
"etymology":"Medieval Latin quinta (fifth) + essentia (essence, being).","related_concept_id":None,"related_terms":["elixir","distillatio","circulatio","arcanum","aether"]},

{"id":"aurum-potabile","term":"Aurum Potabile","latin":"aurum potabile","also_known_as":["drinkable gold","potable gold","soluble gold"],
"category":"substance","period":"14th–17th c.",
"definition":"A preparation of gold dissolved in a solvent (often the philosophers' mercury or a specially prepared menstruum) to produce a drinkable, medicinally active golden solution. Aurum potabile was one of the great objects of iatrochemical medicine, promised as a cure for incurable diseases, a restorative for vital spirits, and an agent of longevity. Various preparations were sold under this name, often with little actual gold. Paracelsus and his followers claimed to have prepared genuine aurum potabile. Michael Maier's Atalanta Fugiens and numerous 17th-century medical texts discuss it. Lawrence Principe notes that some preparations may have been genuine colloidal gold suspensions.",
"etymology":"Latin aurum (gold) + potabilis (drinkable), from potare (to drink).","related_concept_id":None,"related_terms":["elixir","lapis-philosophorum","iatrochemistry","arcanum","aurum"]},

{"id":"red-tincture","term":"Red Tincture","latin":"tinctura rubea","also_known_as":["tincture of the sun","great tincture","red lion"],
"category":"substance","period":"14th–18th c.",
"definition":"The perfected philosophers' stone in its red form, specifically capable of transmuting base metals to gold. The 'white tincture' (luna) transmuted to silver; the 'red tincture' (sol) to gold. The red tincture represented the highest achievement of the opus and its maximum power. In emblems, it was represented by a red or gold-crowned king or a red lion devouring the sun. The distinction between white and red tinctures mapped onto lunar/feminine and solar/masculine principles. Some traditions described a further 'exaltation' of the red tincture beyond both, corresponding to a state beyond gold.",
"etymology":"Latin tinctura (a dyeing, tincture), from tingere (to dye, colour).","related_concept_id":None,"related_terms":["lapis-philosophorum","projectio","rubedo","sol","multiplicatio"]},

# ─── Hermetic / Neoplatonic ────────────────────────────────────────────────────

{"id":"hermetism","term":"Hermetism","latin":"hermetismus","also_known_as":["Hermeticism","Hermetism","Hermetic philosophy"],
"category":"hermetic","period":"3rd c. CE – 18th c.",
"definition":"A religious-philosophical current claiming the authority of Hermes Trismegistus, the supposed Egyptian sage identified with the god Thoth. The Hermetic Corpus (collected Greek-language texts, probably 2nd–3rd century CE) presents a theology of cosmic ascent, the divine mind (nous), and the soul's fall into and return from matter. Frances Yates argued that Hermetic philosophy provided crucial stimulus to the Scientific Revolution; Brian Vickers contested this. Lawrence Principe and William Newman have argued for a more modest assessment of Hermetism's role in practical alchemy. Hermetism in the Renaissance was inseparable from Neoplatonism, Kabbalah, and natural magic.",
"etymology":"From Hermes Trismegistus (Greek Hermēs trismegistos, 'thrice-great Hermes').","related_concept_id":None,"related_terms":["prisca-theologia","hermes-trismegistus","neoplatonism","kabbalah","ficino"]},

{"id":"prisca-theologia","term":"Prisca Theologia","latin":"prisca theologia","also_known_as":["ancient theology","perennial philosophy","philosophia perennis"],
"category":"hermetic","period":"15th–18th c.",
"definition":"The doctrine that a single divine wisdom underlies all ancient philosophical and religious traditions — revealed to a chain of sages beginning with Hermes Trismegistus or Zoroaster and transmitted through Moses, Plato, the Neoplatonists, and ultimately to the Renaissance magus. Marsilio Ficino, who translated the Hermetic Corpus (1463–71), championed prisca theologia as evidence that all wisdom converged on Christian truth. Pico della Mirandola extended it to include Kabbalah. The doctrine was central to the intellectual project of figures like Agrippa, Fludd, and the Rosicrucians. Brian Vickers criticized the prisca theologia tradition as incoherent and historically implausible.",
"etymology":"Latin prisca (ancient, old) + theologia (theology, discourse about god/s).","related_concept_id":None,"related_terms":["hermetism","philosophia-perennis","ficino","kabbalah","agrippa"]},

{"id":"philosophia-perennis","term":"Philosophia Perennis","latin":"philosophia perennis","also_known_as":["perennial philosophy","perennialism","sophia perennis"],
"category":"hermetic","period":"15th c. – present",
"definition":"The idea that certain fundamental truths about reality, consciousness, and the divine are universal and recurrent across all authentic religious and philosophical traditions. Coined by Agostino Steuco (1540), it was later associated with Leibniz and, in the 20th century, with Aldous Huxley's book of the same name. In the context of this portal, it describes the interpretive principle linking Hermetism, Kabbalah, Neoplatonism, and spiritual alchemy as expressions of a shared esoteric wisdom. Hanegraaff has subjected the perennialist assumption to sharp criticism, arguing that it projects modern comparativist assumptions onto historically distinct traditions.",
"etymology":"Latin philosophia (love of wisdom) + perennis (perennial, enduring through the year).","related_concept_id":None,"related_terms":["prisca-theologia","hermetism","sophia-perennis","hanegraaff"]},

{"id":"theurgy","term":"Theurgy","latin":"theurgia","also_known_as":["divine operation","ritual magic","theurgic ascent"],
"category":"hermetic","period":"3rd c. CE – 18th c.",
"definition":"A ritual practice aiming to draw the divine down into matter or the practitioner upward into unity with the divine — distinguished by its proponents from mere 'goety' (necromancy and demonic magic) by its operations' cosmic scope and purificatory intent. Developed in late Neoplatonic philosophy (Iamblichus, Proclus), theurgy was adopted by Renaissance Hermetists as a framework for understanding magic as a legitimate philosophical practice. D.P. Walker's Spiritual and Demonic Magic (1958) remains the standard study of how Ficino and his circle distinguished permissible theurgic operations from demonic manipulation.",
"etymology":"From Greek theourgía (divine work), from theos (god) + ergon (work).","related_concept_id":None,"related_terms":["hermetism","ficino","agrippa","walker-dp","magic-natural"]},

{"id":"anima-mundi","term":"Anima Mundi","latin":"anima mundi","also_known_as":["world soul","soul of the world","spiritus mundi"],
"category":"hermetic","period":"5th c. BCE – 18th c.",
"definition":"The animating soul of the entire cosmos — a Platonic (Timaeus) and Neoplatonic concept holding that the world is a living organism with a soul analogous to the human soul. Ficino's influential reading of the Timaeus and the Hermetic Corpus made the anima mundi central to Renaissance natural philosophy: it mediated between the divine ideas and the material world, and operated through the vehicles of light and celestial spiritus. Alchemists, including Fludd and the Rosicrucian emblematists, invoked the anima mundi to explain sympathetic correspondences, the growth of metals in the earth, and the philosopher's stone as a microcosmic embodiment of the world soul.",
"etymology":"Latin anima (soul, breath) + mundi (of the world; genitive of mundus).","related_concept_id":None,"related_terms":["spiritus","neoplatonism","ficino","correspondentia","hermetism"]},

{"id":"spiritus","term":"Spiritus","latin":"spiritus","also_known_as":["spirit","pneuma","spiritus mundi","spiritus vitalis"],
"category":"hermetic","period":"3rd c. BCE – 18th c.",
"definition":"In Neoplatonic and alchemical cosmology, a subtle, semi-material intermediary substance between the immaterial soul and gross matter — often described as a very fine vapour or luminous ether. Ficino's spiritus mediated stellar influences to the human body and soul; controlling one's spiritus through music, diet, and philosophical activity was the heart of his talismanic magic. In Paracelsian medicine, the spiritus vitalis (vital spirit) animated the body. Alchemical mercury was often identified with spiritus: volatile, mercurial, penetrating. D.P. Walker devoted his major study to the role of spiritus in Renaissance natural magic.",
"etymology":"Latin spiritus (breath, spirit), from spirare (to breathe).","related_concept_id":None,"related_terms":["anima-mundi","ficino","philosophical-mercury","theurgy","walker-dp"]},

{"id":"ouroboros","term":"Ouroboros","latin":"ouroboros","also_known_as":["uroboros","tail-eater","serpent circle"],
"category":"hermetic","period":"14th c. BCE – 18th c.",
"definition":"The serpent (or dragon) devouring its own tail — one of the oldest continuous symbols in alchemical iconography, appearing in Egyptian texts, Gnostic manuscripts, and throughout European alchemical emblem books. The ouroboros images cyclical recurrence, the unity of beginning and end, the circulatio of the alchemical work (in which vapours return to their source), and the self-contained, self-sustaining nature of the prima materia or the completed stone. In Rosicrucian emblems and Maier's Atalanta Fugiens, the ouroboros is prominently deployed. C.G. Jung read it as a mandala symbol of the Self.",
"etymology":"Greek oura (tail) + boros (devouring), from bora (food).","related_concept_id":None,"related_terms":["circulatio","prima-materia","emblems","hermetism","maier-michael"]},

{"id":"unus-mundus","term":"Unus Mundus","latin":"unus mundus","also_known_as":["one world","unified world","undivided reality"],
"category":"hermetic","period":"16th–20th c.",
"definition":"A concept associated with Gerhard Dorn (16th century) and later with C.G. Jung and Wolfgang Pauli: the idea that there exists a single underlying reality from which both psyche and matter emerge as differentiations. Dorn, in his Physica Trismegisti and other writings, described the third and final stage of the alchemical opus as a unification with the unus mundus — beyond both the inner (psychological) and the outer (material) opposites. In Jungian psychology, the unus mundus became the theoretical ground for synchronicity. For Rosicrucian authors, it resonated with Hermetic ideas of cosmic sympathy and macrocosm-microcosm unity.",
"etymology":"Latin unus (one) + mundus (world).","related_concept_id":None,"related_terms":["correspondentia","macrocosm-microcosm","hermetism","jung"]},

{"id":"henosis","term":"Henosis","latin":"henosis","also_known_as":["union with the One","mystical union","deification"],
"category":"hermetic","period":"3rd c. CE – 18th c.",
"definition":"In Neoplatonic philosophy (Plotinus, Porphyry, Iamblichus), henosis designates the soul's ultimate union with the ineffable One — a state beyond intellect, beyond being, accessible only through ecstatic ascent. The Hermetic Corpus adopted similar language for the soul's return to the divine Father after death. For Renaissance Hermetists, henosis (or its approximate equivalent, unio mystica) was the telos of philosophical and theurgic activity. Alchemical texts used the language of henosis for the philosopher's stone and the completed opus — the 'chemical wedding' achieved when all opposites were resolved into unity.",
"etymology":"Greek henōsis (unification, union), from hen (one) + -ōsis (process).","related_concept_id":None,"related_terms":["theurgy","hermetism","theosis","neoplatonism","coniunctio"]},

{"id":"theosis","term":"Theosis","latin":"theosis","also_known_as":["deification","divinisation","deiformity"],
"category":"hermetic","period":"3rd c. CE – 17th c.",
"definition":"The process by which a human being becomes divine or participates in the divine nature — a concept shared by Neoplatonic philosophy and Orthodox Christian theology. In alchemical spirituality (Zuber's analysis), theosis described the ultimate goal of the Great Work: not merely the transmutation of metals but the divinisation of the practitioner. Jacob Böhme's theosophical writings placed theosis at the centre of spiritual development. This gave Rosicrucian spiritual alchemy — which claimed to perfect both matter and the self — a theological warrant for its most ambitious claims.",
"etymology":"Greek theōsis (divinisation, deification), from theos (god).","related_concept_id":None,"related_terms":["henosis","hermetism","bohme-jakob","zuber","spiritual-alchemy"]},

# ─── Rosicrucian / Esoteric ────────────────────────────────────────────────────

{"id":"fama-fraternitatis","term":"Fama Fraternitatis","latin":"Fama Fraternitatis R.C.","also_known_as":["Fama","Fame of the Fraternity"],
"category":"rosicrucian","period":"1614 (circulated c. 1610)",
"definition":"The first of the three Rosicrucian manifestos, published in Kassel in 1614, announcing the existence of the Fraternity of the Rosy Cross (Rosenkreuzer), calling upon learned men to reform philosophy and religion, and narrating the legend of Christian Rosencreutz (C.R.C.). The Fama describes C.R.C.'s journey to the East, his acquisition of secret wisdom, his return to Europe, and the later discovery of his perfectly preserved tomb. It circulated in manuscript before print and provoked hundreds of responses. Carlos Gilly has identified key manuscript versions and linked it to the Tübingen circle around Andreae. The Fama's call for universal reform (Reformation Generale) situates it within Lutheran millenarianism.",
"etymology":"Latin fama (fame, reputation, report) + fraternitatis (of the brotherhood; genitive of fraternitas).","related_concept_id":None,"related_terms":["confessio-fraternitatis","chymische-hochzeit","andreae","christian-rosencreutz","rosy-cross"]},

{"id":"confessio-fraternitatis","term":"Confessio Fraternitatis","latin":"Confessio Fraternitatis R.C.","also_known_as":["Confessio","Confession of the Fraternity"],
"category":"rosicrucian","period":"1615",
"definition":"The second Rosicrucian manifesto, published in Kassel in 1615, expanding on the Fama with a more explicitly theological and millenarian tone. The Confessio defends the Fraternity against accusations of diabolism, affirms Lutheran Protestant orthodoxy, attacks the Pope and Mahomet as enemies of truth, and promises tremendous rewards to those who join the Brotherhood. It is shorter and more polemical than the Fama. Carlos Gilly and Roland Edighoffer have debated its precise authorship and relationship to the Tübingen circle. The Confessio's apocalyptic urgency — pointing to imminent cosmic transformation — shaped how contemporaries read the Rosicrucian call to reform.",
"etymology":"Latin confessio (confession, declaration), from confiteri (to declare, acknowledge).","related_concept_id":None,"related_terms":["fama-fraternitatis","chymische-hochzeit","andreae","rosicrucian-fraternity"]},

{"id":"chymische-hochzeit","term":"Chymische Hochzeit","latin":"Nuptiae Chymicae","also_known_as":["Chemical Wedding","Chymical Wedding of Christian Rosencreutz"],
"category":"rosicrucian","period":"1616",
"definition":"The third Rosicrucian manifesto, published in 1616, attributed to Johann Valentin Andreae. An allegorical romance in seven days recounting how Christian Rosencreutz is invited to a royal wedding and undergoes a series of initiatory trials and transformations. The narrative draws on theatrical court entertainment, alchemical symbolism (the seven stages of the opus), and Renaissance romance conventions. Andreae later claimed it was a 'youthful jest' (ludibrium), which has prompted extensive debate about the sincerity of the Rosicrucian project. The Chymische Hochzeit is a masterpiece of early modern allegory and remains central to understanding Rosicrucian spirituality.",
"etymology":"German chymisch (chymical, alchemical) + Hochzeit (wedding, marriage).","related_concept_id":None,"related_terms":["fama-fraternitatis","andreae","ludibrium","coniunctio","christian-rosencreutz"]},

{"id":"ludibrium","term":"Ludibrium","latin":"ludibrium","also_known_as":["jest","play","fiction","game"],
"category":"rosicrucian","period":"17th c.",
"definition":"Latin for a jest, plaything, or object of ridicule — the word Andreae used in his later autobiography (Vita, 1642) to describe the Rosicrucian manifestos and particularly the Chymische Hochzeit. Scholars disagree sharply about how to read this self-description: John Warwick Montgomery and Carlos Gilly interpret it as false modesty and evidence of later political caution (Andreae needed to distance himself from the Rosicrucian controversy after the Thirty Years War); Roland Edighoffer and Adam McLean argue the manifestos were genuinely programmatic. The ludibrium question remains one of the central interpretive cruxes of Rosicrucian studies.",
"etymology":"Latin ludibrium, from ludere (to play, jest).","related_concept_id":None,"related_terms":["chymische-hochzeit","andreae","fama-fraternitatis","andreae-ludibrium-debate"]},

{"id":"invisible-college","term":"Invisible College","latin":"Collegium Invisibile","also_known_as":["invisible brotherhood","secret society","collegium"],
"category":"rosicrucian","period":"17th c.",
"definition":"The Rosicrucian Fraternity's self-description as an 'invisible' society of adepts whose members never reveal themselves but perform their work secretly for the benefit of humanity — a claim that defined the movement and generated both imitations (real and fictitious secret societies) and parodies. The Fama promises that brothers will recognise each other by secret signs and will never charge for their services. The 'invisible' quality is both practically protective (avoiding persecution) and philosophically significant (the true philosopher works unseen). Robert Boyle's reference to an 'invisible college' in 1646–47 letters has been taken as a reference to an informal scientific circle.",
"etymology":"Latin invisibilis (unseen) + collegium (college, association).","related_concept_id":None,"related_terms":["fama-fraternitatis","rosicrucian-fraternity","adept","pansophia"]},

{"id":"pansophia","term":"Pansophia","latin":"pansophia","also_known_as":["universal wisdom","all-wisdom","encyclopaedic knowledge"],
"category":"rosicrucian","period":"17th c.",
"definition":"The Rosicrucian and Comenius-inspired vision of a universal, comprehensive reform of knowledge: a system that would unify all sciences, arts, and philosophies in a single, transparent, divinely-ordered encyclopedia. Pansophia was at once an educational ideal (John Amos Comenius devoted his life to it) and a spiritual one (the adept who possessed pansophia would know all of nature's secrets). The Fama Fraternitatis invokes a related ideal through the figure of the Book M and the universal reformation. Samuel Hartlib's mid-17th-century correspondence circle in London was partly organized around pansophic aspirations.",
"etymology":"Greek pan (all) + sophia (wisdom).","related_concept_id":None,"related_terms":["fama-fraternitatis","comenius","hartlib","invisible-college","andreae"]},

{"id":"adept","term":"Adept","latin":"adeptus","also_known_as":["the adept","philosopher","perfected practitioner"],
"category":"rosicrucian","period":"17th–18th c.",
"definition":"In alchemical and Rosicrucian usage, one who has 'obtained' (adeptus) the philosophers' stone or its spiritual equivalent — a practitioner who has completed the Great Work in both its material and spiritual dimensions. The adept was distinguished from the mere practitioner or 'puffer' (who worked blindly with bellows) by philosophical understanding and spiritual initiation. Rosicrucian texts present the Fraternity's members as adepts: possessors of secret knowledge, healers, natural philosophers, and spiritual guides. The concept of the hidden adept — working quietly for humanity's benefit — became central to 18th-century Freemasonic and theosophical imaginaries.",
"etymology":"Latin adeptus, past participle of adipisci (to reach, obtain, gain).","related_concept_id":None,"related_terms":["lapis-philosophorum","invisible-college","rosicrucian-fraternity","theosophia","pansophia"]},

{"id":"theosophia","term":"Theosophia","latin":"theosophia","also_known_as":["theosophy","divine wisdom","God-wisdom"],
"category":"rosicrucian","period":"16th–19th c.",
"definition":"Divine wisdom or knowledge of God derived not from rational theology but from direct illumination — a term that covers several historically distinct phenomena: (1) the 17th-century German mystical tradition associated with Paracelsus, Weigel, and above all Jacob Böhme; (2) the 18th-century illuminist movement; (3) the 19th-century Theosophical Society of Blavatsky and Olcott. This portal focuses on senses (1) and (2). For Böhme, theosophia was the direct contemplative knowledge of God's own nature and the principles operating in creation — inseparable from alchemy and natural philosophy. Mike Zuber's Spiritual Alchemy (2021) is the definitive study of this tradition.",
"etymology":"Greek theos (God) + sophia (wisdom).","related_concept_id":None,"related_terms":["bohme-jakob","zuber","spiritual-alchemy","sophia","paracelsian"]},

{"id":"sophia-perennis","term":"Sophia Perennis","latin":"sophia perennis","also_known_as":["perennial wisdom","eternal wisdom","sacred science"],
"category":"rosicrucian","period":"17th c. – present",
"definition":"The eternal or perennial wisdom underlying all authentic religious traditions — a concept closely related to prisca theologia but emphasizing wisdom (sophia) rather than theological content. In 17th-century usage, it named the divine wisdom available to the illuminated adept through study of scripture, nature, and alchemical-theosophical tradition. In 20th-century traditionalist philosophy (René Guénon, Frithjof Schuon), sophia perennis became the master-concept of a metaphysical and initiatic project. Hanegraaff has critiqued the sophia perennis concept as a modern construction projecting unity onto historically diverse traditions.",
"etymology":"Latin sophia (wisdom, from Greek) + perennis (perennial, everlasting).","related_concept_id":None,"related_terms":["philosophia-perennis","prisca-theologia","hermetism","hanegraaff","zuber"]},

# ─── Kabbalistic ──────────────────────────────────────────────────────────────

{"id":"kabbalah","term":"Kabbalah","latin":"Cabala","also_known_as":["Cabala","Kabbalah","Qabbalah","Jewish mysticism"],
"category":"kabbalistic","period":"12th–18th c.",
"definition":"A Jewish esoteric tradition concerned with the nature of the divine, the structure of reality as expressed through the ten sefirot, and the practice of contemplation, prayer, and sometimes theurgy to achieve mystical union. Gershom Scholem's Major Trends in Jewish Mysticism (1941) defined the academic field; Moshe Idel subsequently challenged Scholem's historicism. Renaissance Christian Kabbalah (Pico, Reuchlin, Agrippa, Fludd) adapted kabbalistic symbols and methods for Christian theological purposes. For Rosicrucian authors the Kabbalah — especially the Zohar and the system of the sefirot — provided a framework for understanding divine emanation and the structure of the cosmos.",
"etymology":"Hebrew qabalah (tradition, reception), from qabal (to receive).","related_concept_id":None,"related_terms":["sefirot","ein-sof","adam-kadmon","christian-kabbalah","gematria"]},

{"id":"sefirot","term":"Sefirot","latin":"sephiroth","also_known_as":["sephiroth","the ten","divine attributes","emanations"],
"category":"kabbalistic","period":"12th–18th c.",
"definition":"The ten attributes or emanations through which Ein Sof (the infinite divine) manifests in the world, according to Kabbalistic teaching. They are arranged on the Tree of Life (Etz Chayyim) in a specific pattern: Keter (Crown), Chokhmah (Wisdom), Binah (Understanding), Chesed (Loving-kindness), Gevurah (Strength), Tiferet (Beauty), Netzach (Victory), Hod (Splendour), Yesod (Foundation), and Malkuth (Kingdom). Each sefirah has associated divine names, angelic orders, and correspondences. Christian Kabbalists such as Pico and Agrippa mapped the sefirot onto Christian theological categories. Rosicrucian emblems occasionally incorporated sefirotic symbolism.",
"etymology":"Hebrew sefiroth, plural of sefirah (counting, numeration, sapphire).","related_concept_id":None,"related_terms":["kabbalah","ein-sof","adam-kadmon","christian-kabbalah","agrippa"]},

{"id":"ein-sof","term":"Ein Sof","latin":"En Soph","also_known_as":["Ain Soph","the Infinite","the boundless","divine ground"],
"category":"kabbalistic","period":"13th–18th c.",
"definition":"The infinite, unknowable divine ground in Kabbalistic theology — literally 'without end' (Ein = no/without, Sof = end). Ein Sof is beyond all attributes, beyond being and non-being, beyond any positive characterization. The sefirot are its emanations — the ways in which the Infinite makes itself known in finite reality without itself becoming finite. For Christian Kabbalists, Ein Sof corresponded to the apophatic Godhead of Pseudo-Dionysius (the Deus absconditus) or to Böhme's Ungrund (groundless ground). This parallel made Kabbalah attractive to speculative mystical theologies seeking a concept of the absolute divine that transcended philosophical predication.",
"etymology":"Hebrew ein (no, without) + sof (end, limit).","related_concept_id":None,"related_terms":["kabbalah","sefirot","adam-kadmon","bohme-jakob","neoplatonism"]},

{"id":"gematria","term":"Gematria","latin":"gematria","also_known_as":["numerology","sacred numerology","letter-number calculation"],
"category":"kabbalistic","period":"2nd c. CE – 18th c.",
"definition":"A hermeneutic practice that assigns numerical values to Hebrew letters and interprets words or phrases through the relationships between their numerical equivalents. If two words have the same numerical value, they are held to share a deeper connection. Gematria was a standard tool of Kabbalistic biblical interpretation and was adapted by Christian Kabbalists (Agrippa, Dee) for magical and philosophical purposes. John Dee's Monas Hieroglyphica (1564) uses gematria-like numerical symbolism extensively. In alchemical contexts, gematria was used to encode and decode the names of substances and operations.",
"etymology":"From Greek geometria (geometry), possibly influenced by the Greek letter gamma (third letter, = 3).","related_concept_id":None,"related_terms":["kabbalah","notarikon","tetragrammaton","dee-john","agrippa"]},

{"id":"notarikon","term":"Notarikon","latin":"notarikon","also_known_as":["acrostical reading","initial-letter method","shorthand reading"],
"category":"kabbalistic","period":"2nd c. CE – 18th c.",
"definition":"A Kabbalistic hermeneutic technique interpreting each letter of a word as the initial of another word, thereby expanding a term into a sentence or phrase, or conversely compressing a phrase to an acronym. The VITRIOL acrostic (Visita Interiora Terrae Rectificando Invenies Occultum Lapidem) is a notarikon-style expansion applied to an alchemical substance name. Notarikon appears in the Talmud and was extensively developed in Kabbalistic literature. Christian Kabbalists employed it in biblical interpretation and in magical operations involving divine names. It illustrates the general Kabbalistic assumption that scripture is inexhaustibly dense with layered meanings.",
"etymology":"From Greek notarikon (shorthand writing), from notarios (shorthand writer).","related_concept_id":None,"related_terms":["kabbalah","gematria","vitriol","tetragrammaton"]},

{"id":"tetragrammaton","term":"Tetragrammaton","latin":"tetragrammaton","also_known_as":["YHWH","YHVH","the divine name","the ineffable name"],
"category":"kabbalistic","period":"Biblical – 18th c.",
"definition":"The four-letter Hebrew divine name (yod-heh-vav-heh = YHWH) held in Jewish tradition to be the personal name of God, too sacred to be pronounced. In Kabbalistic analysis, each letter of the Tetragrammaton corresponded to a level of divine reality and the cosmos (the letter yod = Chokhmah; the first heh = Binah; the vav = Tiferet; the second heh = Malkuth). Pico's 900 Theses proposed adding a shin to produce Yehoshua (Jesus) as a Kabbalistic proof of the Incarnation. Agrippa and John Dee used the Tetragrammaton in magical practice. It featured in Rosicrucian emblems as an emblem of divine unity.",
"etymology":"Greek tetra (four) + gramma (letter) + -ton (neuter noun ending).","related_concept_id":None,"related_terms":["kabbalah","gematria","notarikon","adam-kadmon","dee-john"]},

{"id":"adam-kadmon","term":"Adam Kadmon","latin":"Adam Kadmon","also_known_as":["primordial Adam","heavenly Adam","archetypal man"],
"category":"kabbalistic","period":"13th–18th c.",
"definition":"The primordial or heavenly Adam in Lurianic Kabbalah (16th century) — the first configuration of divine light after the tzimtzum (contraction), preceding the creation of the material world. Adam Kadmon is not the Adam of Genesis but a cosmic, divine template for all of creation; the sefirot are arrayed as parts of his body. For Christian Kabbalists and alchemists, Adam Kadmon was associated with the Anthropos of Gnostic and Hermetic texts, the Cosmic Man of whom each human being is an image. Böhme used the concept of the heavenly Adam extensively. In Jungian psychology, Adam Kadmon = the archetype of the Self.",
"etymology":"Hebrew adam (man; also, red earth) + qadmon (primordial, ancient).","related_concept_id":None,"related_terms":["kabbalah","sefirot","ein-sof","bohme-jakob","hermetism"]},

{"id":"golem","term":"Golem","latin":"golem","also_known_as":["artificial man","homunculus (Kabbalistic)","created being"],
"category":"kabbalistic","period":"Medieval – 18th c.",
"definition":"An artificial anthropomorphic creature created by a Kabbalistic adept through manipulation of Hebrew letters and divine names — the most dramatic expression of the creative power attributed to sacred language. The classical golem legend involves shaping a clay figure and animating it with the divine name EMET (truth) inscribed on its forehead. Moshe Idel's Golem (1990) provides the definitive scholarly study. The golem legend intersects with alchemical accounts of the homunculus (Paracelsus) and with broader Renaissance debates about whether humans could create artificial life. Both traditions raised questions about the boundaries of natural and divine creativity.",
"etymology":"Hebrew golem (unformed mass, embryo), from galam (to fold, wrap).","related_concept_id":None,"related_terms":["kabbalah","tetragrammaton","adam-kadmon","homunculus","paracelsian"]},

# ─── Paracelsian ─────────────────────────────────────────────────────────────

{"id":"spagyria","term":"Spagyria","latin":"spagyria","also_known_as":["spagyric art","spagyria","Paracelsian pharmacy"],
"category":"paracelsian","period":"16th–18th c.",
"definition":"Paracelsus's term for his own alchemical-pharmaceutical practice, from Greek spao (to draw out) and ageiro (to gather together) — to separate and recombine. Spagyric preparations involved extracting the active principle of a substance (through distillation, fermentation, or dissolution), purifying it, then recombining it with its salt and residue in enhanced form. This distinguished Paracelsian pharmacy from Galenic herbalism (which used raw or cooked plant materials) and from purely transmutational alchemy. Spagyric medicines were believed to preserve the quintessential virtue of the plant or mineral while removing poisonous impurities — the tinctura rather than the crude whole.",
"etymology":"Greek spao (to draw, separate) + ageiro (to gather, combine).","related_concept_id":None,"related_terms":["iatrochemistry","tria-prima","arcanum","quinta-essentia","distillatio"]},

{"id":"iatrochemistry","term":"Iatrochemistry","latin":"iatrochemia","also_known_as":["chemical medicine","Paracelsian medicine","chymical medicine"],
"category":"paracelsian","period":"16th–18th c.",
"definition":"The application of alchemical theory and procedures to medicine — the programme associated above all with Paracelsus, developed by his followers including Johannes Hartmann, Oswald Croll, and Jan Baptist van Helmont, and ultimately feeding into the Chemical Revolution of the 17th century. Iatrochemists replaced (or supplemented) Galenic humoral medicine with a chemistry of arcana, tinctures, and mineral medicines. Debus and Webster showed how Paracelsian iatrochemistry constituted a genuine intellectual revolution in medical practice. Principe and Newman have critiqued overly sharp demarcations between iatrochemistry and transmutational alchemy ('chymistry' is their preferred umbrella term).",
"etymology":"Greek iatros (physician, healer) + chemistry.","related_concept_id":None,"related_terms":["spagyria","arcanum","tria-prima","alkahest","paracelsus","debus","principe"]},

{"id":"arcanum","term":"Arcanum","latin":"arcanum","also_known_as":["arcana","secret medicine","specific remedy"],
"category":"paracelsian","period":"16th–18th c.",
"definition":"In Paracelsian medicine, a highly potent and specifically targeted remedy — more refined and effective than ordinary medicines because it had been alchemically concentrated and its virtue extracted as a quinta essentia. Unlike Galenic compound medicines (acting through qualities like warmth or moisture), arcana acted specifically and powerfully against specific diseases. Paracelsus claimed to possess arcana against plague, epilepsy, and madness. The term implies both secrecy (the recipe hidden from unauthorized practitioners) and potency (the concentrated 'secret virtue' of the substance). Arcana were the commercial and intellectual currency of Paracelsian medicine.",
"etymology":"Latin arcanum, neuter of arcanus (secret, hidden), from arca (box, chest).","related_concept_id":None,"related_terms":["spagyria","iatrochemistry","elixir","tinctura","quinta-essentia"]},

{"id":"archeus","term":"Archei","latin":"archeus","also_known_as":["archeus","formative force","vital principle","internal alchemist"],
"category":"paracelsian","period":"16th–17th c.",
"definition":"In Paracelsian natural philosophy, the vital, alchemical force that governs the growth, nutrition, and healing of living bodies — a kind of internal physician and craftsman at work within every organism. Every living thing has its own archeus which separates nourishment from waste (analogous to digestion), maintains the body's integrity, and resists disease. Van Helmont developed the concept extensively, arguing for multiple archei in the body corresponding to different organs. The archeus of the stomach was responsible for digestion; the archeus of the seed for plant growth. The concept bridged alchemy, medicine, and vitalist biology.",
"etymology":"From Greek arkhē (beginning, rule, first principle).","related_concept_id":None,"related_terms":["spagyria","iatrochemistry","separatio","van-helmont","paracelsus"]},

{"id":"mumia","term":"Mumia","latin":"mumia","also_known_as":["mummy substance","vital balsam","corporeal spirit"],
"category":"paracelsian","period":"16th–17th c.",
"definition":"A Paracelsian concept designating the vital balsam or spirit permeating living bodies — the subtle material force that preserved the body's life and could be used medicinally, sympathetically, or magically when extracted from a living or recently dead person. The term relates to actual mummy preparations (Egyptian and otherwise) used in Renaissance medicine, but Paracelsus expanded it into a theoretical principle: the mumia of a living person could heal wounds at a distance through sympathetic action, could influence their health, and could be directed to harm through maleficium. The concept sat uneasily between natural magic, medicine, and witchcraft.",
"etymology":"From Arabic mūmiyā (bitumen, mummy resin), perhaps from Persian mūm (wax).","related_concept_id":None,"related_terms":["paracelsian","arcanum","spiritus","sympathetic-magic","weapon-salve"]},

{"id":"tartarus","term":"Tartarus","latin":"Tartarus","also_known_as":["tartar","Tartarean principle","stone-forming substance"],
"category":"paracelsian","period":"16th–17th c.",
"definition":"In Paracelsian medicine, a disease-principle associated with the formation of concretions, crystalline deposits, and calculi (stones) in the body — named from the sediment deposited in wine casks. Diseases like gout, kidney stones, arteriosclerosis, and certain forms of arthritis were attributed to a tartar excess in the body: an over-coagulating, stone-forming force that exceeded the archei's capacity to dissolve and eliminate it. The treatment involved arcana designed to dissolve these tartarean deposits chemically. Paracelsus wrote an entire treatise On Tartar Diseases (Tartarische Krankheiten). The concept contributed to early thinking about crystallization and sediment in chemistry.",
"etymology":"Latin Tartarus (the underworld in classical mythology; also tartarum, wine-stone sediment), from Greek.","related_concept_id":None,"related_terms":["iatrochemistry","arcanus","archeus","paracelsus"]},

{"id":"menstruum","term":"Menstruum","latin":"menstruum","also_known_as":["solvent","universal menstruum","dissolving medium"],
"category":"paracelsian","period":"14th–18th c.",
"definition":"A solvent used in alchemical operations to dissolve a substance, particularly the philosophical mercury in its role as the medium for dissolving gold and bringing it into the opus. The term 'menstruum' was applied both to practical solvents (acids, water, alcohol) and to the philosophical universal solvent or alkahest. The analogy with the uterine menstrual fluid was deliberate: the menstruum nourished and transformed the dissolved substance just as the womb nourished and transformed the embryo. This gendered language of dissolution was common in alchemical writing and was analysed by Stanton Linden and other scholars of the rhetoric of alchemy.",
"etymology":"Medieval Latin menstruum (monthly discharge), from mensis (month).","related_concept_id":None,"related_terms":["alkahest","solutio","philosophical-mercury","prima-materia","tinctura"]},

{"id":"magistery","term":"Magistery","latin":"magisterium","also_known_as":["magistery","masterpiece","perfected preparation"],
"category":"paracelsian","period":"15th–18th c.",
"definition":"The highest and most perfect form of an alchemical preparation — a 'masterwork' achieved by taking a substance through the complete cycle of the opus to its most refined state. The magistery (magisterium) of a metal was its quintessential, most spiritualized preparation; the Lapis Philosophorum was the supreme magistery. In Paracelsian medicine, the magisteries of specific plants, minerals, and animals were highly concentrated arcana. The term distinguishes a philosophically complete work from mere technical competence ('art') — only one who truly understood the opus could produce a true magisterium.",
"etymology":"Latin magisterium (authority, office of master), from magister (master).","related_concept_id":None,"related_terms":["arcanum","lapis-philosophorum","quinta-essentia","spagyria"]},

{"id":"tinctura","term":"Tinctura","latin":"tinctura","also_known_as":["tincture","dyeing quality","colouring power"],
"category":"paracelsian","period":"14th–18th c.",
"definition":"In alchemy, a tincture is the essential colouring or transforming quality of a substance — what can be transmitted from one material to another to change it fundamentally. The philosophers' stone operated as a tincture: a minute quantity could transmute a large quantity of base metal by 'dyeing' it with the quality of gold. In medicine, tinctures were prepared by macerating or distilling plant or mineral materials in alcohol to extract their active virtue. The tincture concept bridges transmutation and medicine, suggesting that transformation (of metals or bodies) is fundamentally a communication of qualities rather than a material transfer.",
"etymology":"Latin tinctura (a dyeing, staining), from tingere (to dye, colour).","related_concept_id":None,"related_terms":["red-tincture","lapis-philosophorum","arcanum","projectio","elixir"]},

{"id":"homunculus","term":"Homunculus","latin":"homunculus","also_known_as":["homuncle","artificial man","little man"],
"category":"paracelsian","period":"16th–17th c.",
"definition":"A miniature artificial human being, allegedly producible by alchemical means — described in a text attributed to Paracelsus (De natura rerum) involving the putrefaction of human semen in a sealed flask at body heat for forty days. The homunculus would be transparent and could serve as a prophetic oracle. William Newman showed that the Paracelsian homunculus was part of a larger debate about whether art could imitate nature in producing life, countering the Aristotelian view that spontaneous generation was impossible without natural heat. The concept intersects with Kabbalistic golem traditions and with 17th-century mechanist debates about the boundaries of artificial life.",
"etymology":"Latin homo (man) + -unculus (diminutive suffix = little).","related_concept_id":None,"related_terms":["golem","spagyria","paracelsus","newman","prima-materia"]},
]

out = Path(__file__).parent / "glossary_patch.json"
with open(out, 'w', encoding='utf-8') as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)
print(f"Saved {len(glossary)} glossary entries to {out}")
