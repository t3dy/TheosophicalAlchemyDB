"""Add timeline data and enriched map centers to prototype_data.json."""
import json, pathlib

DB = pathlib.Path("site/data/prototype_data.json")

TIMELINE = [
    # ── Precursors (1317–1499) ────────────────────────────────────────────────
    {
        "id": "tl_001", "year": 1317, "category": "historical",
        "title": "Papal Condemnation of Alchemical Fraud",
        "description": "Pope John XXII issues the decree Spondent quas non exhibent, condemning alchemists who fraudulently claim to produce gold and silver and use the proceeds for personal enrichment. The decree distinguishes fraudulent practice from legitimate philosophical inquiry but establishes a legal framework for prosecuting alchemical fraud that persists through the early modern period.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_002", "year": 1440, "category": "text",
        "title": "Nicholas of Cusa: De Docta Ignorantia",
        "description": "The German cardinal Nicholas of Cusa publishes De Docta Ignorantia (On Learned Ignorance), articulating the concept of the coincidentia oppositorum (coincidence of opposites) in which God encompasses all contradictions. Cusa's infinite God and his concept of the universe as an image of the divine infinite become foundational for Bruno, Paracelsus, and the Hermetic tradition's engagement with infinite cosmology.",
        "related_figures": ["Nicholas of Cusa"], "related_texts": ["De Docta Ignorantia"]
    },
    {
        "id": "tl_003", "year": 1453, "category": "historical",
        "title": "Fall of Constantinople",
        "description": "The Ottoman conquest of Constantinople sends Greek scholars westward, bringing Greek manuscripts—including Platonic, Neoplatonic, and Hermetic texts—to Italy. This migration of texts and scholars accelerates the recovery of ancient philosophy in the Latin West and directly enables the Florentine Platonic Renaissance that will produce the Hermetic translations of Marsilio Ficino.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_004", "year": 1460, "category": "historical",
        "title": "Corpus Hermeticum Manuscript Arrives in Florence",
        "description": "A monk named Leonardo da Pistoia brings a Greek manuscript of the Corpus Hermeticum to Cosimo de' Medici in Florence. Cosimo orders Marsilio Ficino to set aside his Plato translation and render the Hermetic texts into Latin first—a decision that marks the beginning of Renaissance Hermetism. The resulting translation (1463) will shape European intellectual culture for two centuries.",
        "related_figures": ["Marsilio Ficino"], "related_texts": ["Poemandres"]
    },
    {
        "id": "tl_005", "year": 1463, "category": "text",
        "title": "Ficino Translates the Corpus Hermeticum",
        "description": "Marsilio Ficino completes his Latin translation of the Corpus Hermeticum, presenting Hermes Trismegistus as an Egyptian prophet who foretold the coming of Christ—a prisca theologia (ancient theology) predating Plato and Moses. Ficino's translation launches Renaissance Hermetism and makes the Hermetic texts available to Latin readers across Europe, generating a tradition of philosophical and practical engagement that feeds directly into alchemy, natural magic, and the Rosicrucian movement.",
        "related_figures": ["Marsilio Ficino"], "related_texts": ["Poemandres", "Platonic Theology"]
    },
    {
        "id": "tl_006", "year": 1470, "category": "text",
        "title": "George Ripley: Compound of Alchymy",
        "description": "The English Augustinian canon George Ripley composes the Compound of Alchymy, one of the most influential vernacular alchemical texts of the late medieval period. Organized as a twelve-gate sequence, the work maps the alchemical Great Work onto a systematic philosophical and practical program. Ripley's Compound was later anthologized by Elias Ashmole in his Theatrum Chemicum Britannicum (1652) and helped establish the English alchemical poetic tradition.",
        "related_figures": ["George Ripley"], "related_texts": ["Theatrum Chemicum Britannicum"]
    },
    {
        "id": "tl_007", "year": 1486, "category": "text",
        "title": "Pico della Mirandola: Nine Hundred Theses",
        "description": "Giovanni Pico della Mirandola publishes his nine hundred philosophical theses in Rome, proposing a public disputation on all of human knowledge. The theses include the first systematic engagement with Jewish Kabbalah by a Latin Christian scholar and establish the framework for Christian Kabbalah. Pope Innocent VIII condemns thirteen theses and Pico flees Rome, but the Oration on Human Dignity—written as the planned prefatory address—becomes one of the defining texts of Renaissance humanism.",
        "related_figures": ["Giovanni Pico della Mirandola"], "related_texts": ["Kabbalistic Conclusions", "Oration on Human Dignity"]
    },
    {
        "id": "tl_008", "year": 1489, "category": "text",
        "title": "Ficino: Three Books on Life",
        "description": "Marsilio Ficino publishes De Vita Triplici (Three Books on Life), a comprehensive account of scholarly health, celestial influence, and natural magic. The third book, De Vita Coelitus Comparanda (On Drawing Down Celestial Life), elaborates a practical program of astrological medicine and talismanic magic grounded in Neoplatonic cosmology. The work becomes one of the most widely read texts of the Italian Renaissance and establishes the philosophical framework for later alchemical medicine.",
        "related_figures": ["Marsilio Ficino"], "related_texts": ["Platonic Theology"]
    },
    {
        "id": "tl_009", "year": 1493, "category": "figure",
        "title": "Birth of Paracelsus",
        "description": "Theophrastus Bombastus von Hohenheim (Paracelsus) is born in Einsiedeln, Switzerland, to a physician father who introduces him to mining, metallurgy, and medicine. He will become the most influential figure in the history of chemical medicine, reforming European medicine through the tria prima (Sulphur, Mercury, Salt), iatrochemical therapy, and a natural philosophy that fuses Neoplatonic cosmology with practical laboratory investigation.",
        "related_figures": ["Paracelsus"], "related_texts": []
    },
    {
        "id": "tl_010", "year": 1499, "category": "text",
        "title": "Trithemius Writes Steganography",
        "description": "Johannes Trithemius, abbot of Sponheim, composes his Steganographia—a manual for transmitting secret messages through the agency of spirits that is simultaneously a sophisticated cryptographic system. The work circulates in manuscript for over a century before publication (1606) due to its apparent demonism. Its concept of an invisible network of initiated communicators provides a model for the later Rosicrucian invisible brotherhood.",
        "related_figures": ["Johannes Trithemius"], "related_texts": ["Steganography"]
    },
    # ── Reformation Era (1510–1560) ────────────────────────────────────────────
    {
        "id": "tl_011", "year": 1510, "category": "text",
        "title": "Agrippa Writes De Occulta Philosophia (Manuscript)",
        "description": "Cornelius Agrippa von Nettesheim completes a first draft of De Occulta Philosophia, the most comprehensive synthesis of Renaissance natural magic, Neoplatonic cosmology, Kabbalistic symbolism, and practical magical procedure. Agrippa sends the manuscript to Trithemius for review; the work circulates privately for over two decades before publication in 1531. In its final form it will become the foundational textbook for learned magical practice.",
        "related_figures": ["Cornelius Agrippa von Nettesheim"], "related_texts": ["Three Books of Occult Philosophy"]
    },
    {
        "id": "tl_012", "year": 1517, "category": "historical",
        "title": "Luther's 95 Theses",
        "description": "Martin Luther posts his ninety-five theses against indulgences at Wittenberg, triggering the Protestant Reformation. The Reformation's critique of ecclesiastical authority, its emphasis on individual access to Scripture, and its millenarian urgency all shape the context within which Paracelsian medicine, Hermetic philosophy, and ultimately Rosicrucianism develop. The Protestant environment proves more hospitable to Hermetic reform programs than Counter-Reformation Catholicism.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_013", "year": 1527, "category": "figure",
        "title": "Birth of John Dee",
        "description": "John Dee is born in Tower Ward, London. He will become the most learned natural philosopher in Elizabethan England—mathematician, astronomer, astrologer, advocate of British imperial expansion, and author of the cryptic Monas Hieroglyphica (1564). His later Enochian workings with Edward Kelley (1582–1589) represent the most elaborate attempt to systematize angelic communication in the Western magical tradition and directly influence the Rosicrucian movement.",
        "related_figures": ["John Dee"], "related_texts": ["Monas Hieroglyphica"]
    },
    {
        "id": "tl_014", "year": 1531, "category": "text",
        "title": "Agrippa Publishes De Occulta Philosophia",
        "description": "Cornelius Agrippa publishes the complete De Occulta Philosophia in Cologne, presenting a three-book synthesis of natural magic (elemental sympathies), celestial magic (astrological talismans), and ceremonial magic (theurgy and angelic communication). The work becomes the standard reference for learned magical philosophy in the sixteenth century, influencing Marlowe, Shakespeare, and the entire Hermetic tradition through Bruno, Dee, and the Rosicrucian movement.",
        "related_figures": ["Cornelius Agrippa von Nettesheim"], "related_texts": ["Three Books of Occult Philosophy"]
    },
    {
        "id": "tl_015", "year": 1541, "category": "figure",
        "title": "Death of Paracelsus",
        "description": "Paracelsus dies in Salzburg, leaving behind an enormous corpus of unpublished manuscripts covering medicine, natural philosophy, theology, and cosmology. His posthumous publication history—initiated by Adam von Bodenstein and others from the 1560s onward—transforms him from a controversial and often-homeless itinerant into the prophet of a new medicine. Paracelsism becomes a major intellectual and institutional force in the second half of the sixteenth century.",
        "related_figures": ["Paracelsus"], "related_texts": []
    },
    {
        "id": "tl_016", "year": 1543, "category": "historical",
        "title": "Copernicus and Vesalius Publish",
        "description": "In the same year, Copernicus publishes De Revolutionibus Orbium Coelestium (placing the sun at the center of the solar system) and Andreas Vesalius publishes De Humani Corporis Fabrica (based on systematic human dissection). Both works challenge received Aristotelian and Galenic authority. The Copernican revolution, in particular, opens the question of cosmic architecture that Bruno will radicalize and that Kepler, Fludd, and Maier will engage from Hermetic perspectives.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_017", "year": 1558, "category": "text",
        "title": "Della Porta: Magia Naturalis",
        "description": "Giovanni Battista della Porta publishes the first edition of Magia Naturalis (Natural Magic), a four-book encyclopedia of natural wonders, technological secrets, and applied natural philosophy. The work defines natural magic as the mastery of hidden natural sympathies—distinguishing it from demonic magic and presenting it as legitimate natural philosophical inquiry. The expanded twenty-book edition (1589) becomes the standard reference for Renaissance natural magic.",
        "related_figures": ["Giambattista della Porta"], "related_texts": ["Magia Naturalis"]
    },
    # ── Late Renaissance Hermetism (1560–1600) ───────────────────────────────
    {
        "id": "tl_018", "year": 1560, "category": "figure",
        "title": "Birth of Heinrich Khunrath",
        "description": "Heinrich Khunrath is born in Leipzig. He will become one of the most important figures in the alchemical-Rosicrucian tradition, training as a physician in Basel (MD 1588) and producing the Amphitheatrum Sapientiae Aeternae (1595/1609)—the most visually spectacular emblem book of the alchemical tradition, combining elaborate engraved plates with polyglot philosophical texts to map the complete path from laboratory practice to divine illumination.",
        "related_figures": ["Heinrich Khunrath"], "related_texts": ["Amphitheatrum Sapientiae Aeternae"]
    },
    {
        "id": "tl_019", "year": 1564, "category": "text",
        "title": "John Dee: Monas Hieroglyphica",
        "description": "John Dee publishes the Monas Hieroglyphica in Antwerp, dedicated to Emperor Maximilian II. The work presents a single symbol—the monas, combining astronomical signs for sun, moon, elements, and Aries—that Dee claims encodes all mathematical, astronomical, alchemical, and theological knowledge. The work's twenty-four theorems develop this claim through number mysticism, Kabbalistic correspondences, and geometrical analysis. The monas becomes an emblem of unified Hermetic knowledge.",
        "related_figures": ["John Dee"], "related_texts": ["Monas Hieroglyphica"]
    },
    {
        "id": "tl_020", "year": 1574, "category": "figure",
        "title": "Birth of Robert Fludd",
        "description": "Robert Fludd is born in Bearsted, Kent. He will become the most important British representative of the Hermetic-alchemical tradition in the early seventeenth century, producing the Utriusque Cosmi Historia (1617–1621)—a massive illustrated cosmology presenting the macrocosm and microcosm through elaborate diagrams including the famous world monochord. Fludd defends the Rosicrucian brotherhood publicly and engages in controversy with Kepler and Mersenne over Hermetic natural philosophy.",
        "related_figures": ["Robert Fludd"], "related_texts": ["Utriusque Cosmi Historia"]
    },
    {
        "id": "tl_021", "year": 1583, "category": "historical",
        "title": "Giordano Bruno in London",
        "description": "Giordano Bruno arrives in London, entering the circle of Philip Sidney and Fulke Greville. During his two-year London sojourn he publishes three Italian philosophical dialogues—including De l'Infinito Universo et Mondi—and delivers lectures at Oxford. His cosmological vision of an infinite universe with infinitely many solar systems, animated by World Soul and modeled on Hermetic philosophy, influences Sidney's circle and provides the metaphysical framework for later Hermetic cosmology.",
        "related_figures": ["Giordano Bruno"], "related_texts": ["On the Infinite Universe and Worlds"]
    },
    {
        "id": "tl_022", "year": 1595, "category": "text",
        "title": "Khunrath: Amphitheatrum Sapientiae Aeternae (Hamburg)",
        "description": "Heinrich Khunrath publishes the first edition of his Amphitheatrum Sapientiae Aeternae in Hamburg, containing the famous laboratorium-oratorium plate showing the alchemical laboratory and prayer space as a unified transformative environment. The work presents the complete path from practical laboratory operations through philosophical study to divine illumination and union. An expanded edition published posthumously in Hanover (1609) adds plates and becomes the standard version.",
        "related_figures": ["Heinrich Khunrath"], "related_texts": ["Amphitheatrum Sapientiae Aeternae"]
    },
    {
        "id": "tl_023", "year": 1597, "category": "text",
        "title": "Libavius: Alchemia",
        "description": "Andreas Libavius publishes Alchemia in Frankfurt—the first systematic textbook of chemistry organized according to logical and pedagogical principles. Libavius accepts iatrochemical practice and most laboratory operations while subjecting Paracelsian cosmological theory and the mystical elaborations of Croll and Khunrath to critical scrutiny. The work represents the beginning of chemistry's institutional self-differentiation from alchemical philosophy.",
        "related_figures": ["Andreas Libavius"], "related_texts": []
    },
    {
        "id": "tl_024", "year": 1600, "category": "historical",
        "title": "Bruno Burned; Böhme's First Vision",
        "description": "Two foundational events of 1600: Giordano Bruno is burned at the stake in Rome by the Inquisition on 17 February, making him a martyr for cosmological and philosophical freedom in Protestant circles. That same year, Jacob Böhme—a shoemaker in Görlitz—experiences his first mystical vision (Blitz-Erlebnis), in which he perceives the divine ground of all being in a flash of illumination. Böhme's theosophical writings will become the foundation of spiritual alchemy.",
        "related_figures": ["Giordano Bruno", "Jacob Böhme"], "related_texts": []
    },
    # ── Rosicrucian Era (1604–1630) ───────────────────────────────────────────
    {
        "id": "tl_025", "year": 1604, "category": "text",
        "title": "Sendivogius: New Chemical Light",
        "description": "Michael Sendivogius publishes Novum Lumen Chymicum (New Chemical Light), one of the most influential alchemical texts of the seventeenth century. Sendivogius introduces the concept of the aerial niter—a universal seminal principle dissolved in air, drawn down by rain and dew, and responsible for the generation of metals in the earth and life in organisms. This concept anticipates later pneumatic chemistry and shapes both the Rosicrucian tradition and Newton's alchemical research.",
        "related_figures": ["Michael Sendivogius"], "related_texts": []
    },
    {
        "id": "tl_026", "year": 1607, "category": "text",
        "title": "Croll: Basilica Chymica",
        "description": "Oswald Croll publishes Basilica Chymica (The Chemical Palace) in Frankfurt, dedicated to Rudolf II. The work's massive Admonitory Preface provides the most eloquent defense of Paracelsian philosophy ever written, situating chemical medicine within a comprehensive Hermetic-Protestant theology. The pharmaceutical formulary that follows becomes the standard Paracelsian medical reference for the seventeenth century.",
        "related_figures": ["Oswald Croll"], "related_texts": []
    },
    {
        "id": "tl_027", "year": 1610, "category": "historical",
        "title": "Fama Fraternitatis Circulates in Manuscript",
        "description": "The Fama Fraternitatis begins circulating in manuscript in the Tübingen area, where it is associated with a circle around the lawyer Tobias Hess and the young theologian Johann Valentin Andreae. Carlos Gilly's archival research has traced multiple manuscript versions predating publication, showing that the manifesto generated intense interest among Protestant readers seeking a framework for universal reform before its official appearance in print.",
        "related_figures": ["Johann Valentin Andreae"], "related_texts": ["Fama Fraternitatis"]
    },
    {
        "id": "tl_028", "year": 1612, "category": "text",
        "title": "Böhme Writes the Aurora",
        "description": "Jacob Böhme completes the Aurora (Morgenröte im Aufgang), his first major work, recording his visionary understanding of the divine ground, the seven Quellgeister (source spirits), and the relationship between light and darkness as cosmic principles. The work is confiscated by the pastor Gregorius Richter, who prohibits Böhme from writing; Böhme keeps silent for nearly a decade before resuming with intensified productivity. The Aurora establishes all his central themes.",
        "related_figures": ["Jacob Böhme"], "related_texts": ["Aurora"]
    },
    {
        "id": "tl_029", "year": 1614, "category": "text",
        "title": "Fama Fraternitatis Published; Casaubon Dates Hermetica",
        "description": "A double turning point: the Fama Fraternitatis is published in Kassel, announcing the existence of the Rose Cross Brotherhood and calling for universal reformation. In the same year, Isaac Casaubon publishes De Rebus Sacris et Ecclesiasticis Exercitationes, demonstrating through philological analysis that the Hermetic texts are not ancient Egyptian wisdom but late antique (2nd–3rd century CE) compositions. The Rosicrucian tradition launches precisely as the historical foundations of Hermetism are undermined.",
        "related_figures": [], "related_texts": ["Fama Fraternitatis"]
    },
    {
        "id": "tl_030", "year": 1615, "category": "text",
        "title": "Confessio Fraternitatis Published",
        "description": "The Confessio Fraternitatis is published in Kassel as the second Rosicrucian manifesto, supplementing the Fama with explicit Protestant theological commitments and criteria for membership in the brotherhood. The Confessio identifies the Pope and Islam as enemies of the Rosicrucian reformation and situates the fraternity's program within Protestant eschatological expectations. Fludd, Libavius, and dozens of other writers immediately begin responding to the manifestos in print.",
        "related_figures": [], "related_texts": ["Confessio Fraternitatis"]
    },
    {
        "id": "tl_031", "year": 1616, "category": "text",
        "title": "Chymische Hochzeit Published",
        "description": "Johann Valentin Andreae's Chymische Hochzeit Christiani Rosencreütz (Chemical Wedding of Christian Rosenkreutz) is published in Strasbourg—the most literary of the three Rosicrucian manifestos. The seven-day allegorical romance encodes the alchemical Great Work within a narrative of royal wedding, initiatory trials, and the resurrection of a royal couple. The work draws on alchemical emblem traditions, chivalric romance, and Protestant mystical theology.",
        "related_figures": ["Johann Valentin Andreae"], "related_texts": ["Chymische Hochzeit"]
    },
    {
        "id": "tl_032", "year": 1617, "category": "text",
        "title": "Maier's Atalanta Fugiens Published",
        "description": "Michael Maier publishes Atalanta Fugiens in Oppenheim—the most technically complex alchemical emblem book ever produced. Its fifty emblems each combine an engraved plate, a Latin epigram, and a three-voice musical fugue encoding alchemical content through visual, verbal, and musical registers simultaneously. The work deploys the myth of Atalanta and Hippomenes to encode the sulphur-mercury coniunctio and the full sequence of the Great Work in classical allegorical form.",
        "related_figures": ["Michael Maier"], "related_texts": ["Atalanta Fugiens"]
    },
    {
        "id": "tl_033", "year": 1617, "category": "text",
        "title": "Fludd's Utriusque Cosmi Historia Begins Publication",
        "description": "The first volume of Robert Fludd's Utriusque Cosmi Maioris scilicet et Minoris Metaphysica, Physica atque Technica Historia is published by the de Bry press in Oppenheim—beginning a multi-volume illustrated cosmology presenting macrocosm and microcosm through elaborate engraved diagrams. Fludd's world monochord, depicting the cosmos as a single musical instrument, becomes one of the iconic images of Hermetic natural philosophy.",
        "related_figures": ["Robert Fludd"], "related_texts": ["Utriusque Cosmi Historia"]
    },
    {
        "id": "tl_034", "year": 1618, "category": "historical",
        "title": "Thirty Years War Begins",
        "description": "The Thirty Years War (1618–1648) begins with the Defenestration of Prague and the uprising of Bohemian Protestant estates against Habsburg authority. The war devastates Central Europe and destroys the political conditions that had supported Rosicrucian aspirations—particularly Frederick V's assumption of the Bohemian throne (1619) and his rapid defeat at the Battle of White Mountain (1620). The Rosicrucian moment of political possibility collapses with the Palatine court's exile.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_035", "year": 1620, "category": "historical",
        "title": "Battle of White Mountain",
        "description": "Frederick V, Elector Palatine—whose court at Heidelberg had been a center of alchemical and Hermetic activity associated with the Rosicrucian movement—is decisively defeated at the Battle of White Mountain near Prague. Frederick and Elizabeth Stuart flee into exile, the Palatine library is dispersed, and the political program that Frances Yates associated with Rosicrucianism is destroyed. The Thirty Years War grinds on for another twenty-eight years.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_036", "year": 1622, "category": "figure",
        "title": "Death of Michael Maier",
        "description": "Michael Maier dies in Magdeburg, having produced in the preceding decade the most impressive body of alchemical emblem literature in the tradition. His Atalanta Fugiens (1617), Symbola Aureae Mensae (1617), Arcana Arcanissima (1614), and Viatorium (1618) represent a sustained and systematic engagement with the alchemical tradition through classical mythology, emblematic philosophy, and musical counterpoint. His death coincides with the destruction of the Rosicrucian political moment.",
        "related_figures": ["Michael Maier"], "related_texts": []
    },
    {
        "id": "tl_037", "year": 1623, "category": "text",
        "title": "Böhme's Mysterium Magnum",
        "description": "Jacob Böhme completes his most ambitious systematic work, the Mysterium Magnum—a comprehensive commentary on Genesis organized around his three-principles metaphysics. The work presents the Ungrund (groundless abyss), the divine self-differentiation into light and darkness, and the seven Quellgeister as the framework within which both cosmic creation and individual spiritual regeneration must be understood. It becomes foundational for the entire Böhme tradition.",
        "related_figures": ["Jacob Böhme"], "related_texts": ["Mysterium Magnum"]
    },
    {
        "id": "tl_038", "year": 1624, "category": "figure",
        "title": "Death of Jacob Böhme",
        "description": "Jacob Böhme dies in Görlitz, having written prodigiously in the last three years of his life. The Way to Christ (published 1624) and the Mysterium Magnum represent the culmination of his theosophical program. His disciples—Abraham von Frankenberg, Johann Georg Gichtel, Dionysius Andreas Freher—will edit, publish, and elaborate his writings throughout the seventeenth century, making Böhme the foundational figure of German spiritual alchemy and the broader theosophical tradition.",
        "related_figures": ["Jacob Böhme"], "related_texts": ["The Way to Christ", "Mysterium Magnum"]
    },
    # ── Science and Mysticism (1625–1680) ────────────────────────────────────
    {
        "id": "tl_039", "year": 1627, "category": "text",
        "title": "Bacon's New Atlantis Published (Posthumous)",
        "description": "Francis Bacon's New Atlantis is published posthumously, presenting Salomon's House—a research institution on the island of Bensalem organized to investigate all natural phenomena systematically for human benefit. Frances Yates argued that Salomon's House was Bacon's secular reformulation of the Rosicrucian fraternity's program; scholars since have qualified this while acknowledging the shared milieu of universal-reform ambition.",
        "related_figures": ["Francis Bacon"], "related_texts": ["New Atlantis"]
    },
    {
        "id": "tl_040", "year": 1627, "category": "figure",
        "title": "Birth of Robert Boyle",
        "description": "Robert Boyle is born in Lismore Castle, Ireland. He will become famous as the pioneer of modern chemistry and the formulator of Boyle's Law, but Lawrence Principe's archival research has revealed that Boyle maintained a sustained private engagement with alchemical transmutation research throughout his life—corresponding with adepts, conducting laboratory experiments aimed at the philosopher's stone, and accepting claimed philosophical gold—alongside his public advocacy for mechanistic natural philosophy.",
        "related_figures": ["Robert Boyle"], "related_texts": []
    },
    {
        "id": "tl_041", "year": 1646, "category": "historical",
        "title": "Elias Ashmole Initiated into Freemasonry",
        "description": "Elias Ashmole is initiated into a Masonic lodge in Warrington, Lancashire—the earliest documented initiation of a speculative Freemason (as opposed to operative stonemason) in England. This event marks the beginning of speculative Freemasonry's institutional history and its gradual absorption of Rosicrucian, Hermetic, and alchemical themes into an initiatory fraternal structure.",
        "related_figures": ["Ashmole, Elias"], "related_texts": []
    },
    {
        "id": "tl_042", "year": 1648, "category": "historical",
        "title": "Peace of Westphalia",
        "description": "The Peace of Westphalia ends the Thirty Years War, establishing the principle of religious toleration (cuius regio, eius religio with Catholic-Protestant parity) and the modern state system in Europe. The peace allows German intellectual life to recover and Böhme's writings to circulate more freely in German Pietist and theosophical circles. The Hermetic-alchemical tradition reconstitutes itself in the post-war landscape, primarily through Pietist networks.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_043", "year": 1650, "category": "text",
        "title": "Thomas Vaughan: Anthroposophia Theomagica",
        "description": "Thomas Vaughan (Eugenius Philalethes) publishes Anthroposophia Theomagica in London, the first of a series of works advancing a Hermetic-Böhme-influenced natural philosophy in which the world is permeated by subtle vital fires and divine sparks. The work immediately provokes Henry More's hostile response, inaugurating a pamphlet debate that articulates the philosophical stakes of the confrontation between Hermetic vitalism and Cambridge Platonist mechanism.",
        "related_figures": ["Thomas Vaughan"], "related_texts": ["Anthroposophia Theomagica"]
    },
    {
        "id": "tl_044", "year": 1652, "category": "text",
        "title": "Ashmole: Theatrum Chemicum Britannicum",
        "description": "Elias Ashmole publishes the Theatrum Chemicum Britannicum—the first comprehensive anthology of English alchemical poetry, collecting works by Thomas Norton, George Ripley, John Lydgate, Thomas Charnock, and dozens of others. The work establishes the English alchemical tradition as a serious object of antiquarian study and preserves numerous texts that would otherwise have been lost.",
        "related_figures": ["Ashmole, Elias"], "related_texts": ["Theatrum Chemicum Britannicum"]
    },
    {
        "id": "tl_045", "year": 1661, "category": "text",
        "title": "Boyle's Sceptical Chymist",
        "description": "Robert Boyle publishes The Sceptical Chymist, subjecting both Aristotelian four-elements theory and Paracelsian tria prima to critical scrutiny through thought experiments and appeals to laboratory evidence. The work is often celebrated as a founding document of modern chemistry, though Principe's research shows that Boyle simultaneously maintained an active private alchemical practice—pursuing the philosopher's stone in his laboratory even as he publicly criticized alchemical theory.",
        "related_figures": ["Robert Boyle"], "related_texts": []
    },
    {
        "id": "tl_046", "year": 1660, "category": "historical",
        "title": "Royal Society Founded",
        "description": "The Royal Society of London for Improving Natural Knowledge is founded, with its motto Nullius in Verba (Take no one's word for it) expressing the empirical-experimental program that will dominate English natural philosophy. Several early Fellows—including Boyle, Kenelm Digby, and Ashmole—maintained connections with alchemical and Hermetic traditions, suggesting the complex relationship between the new science and its esoteric antecedents.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_047", "year": 1669, "category": "discovery",
        "title": "Hennig Brand Discovers Phosphorus",
        "description": "Hennig Brand, a Hamburg merchant conducting alchemical research in search of the philosopher's stone, discovers phosphorus by distilling and heating large quantities of human urine. Phosphorus—a substance that glows in the dark and ignites spontaneously in air—is the first element to be isolated through intentional alchemical investigation. The discovery exemplifies how alchemical laboratory practice generated genuine chemical knowledge as a byproduct of the search for the stone.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_048", "year": 1682, "category": "text",
        "title": "Gichtel Publishes Böhme's Complete Works",
        "description": "Johann Georg Gichtel publishes the first complete collected edition of Jacob Böhme's works in Amsterdam, making the full theosophical corpus available in a single systematic edition. Gichtel's own Theosophia Practica (1696) elaborates the physiological and psychological dimensions of Böhme's spiritual-alchemical program. His Amsterdam edition becomes the standard reference for Böhme scholarship and transmission through the eighteenth century.",
        "related_figures": ["Johann Georg Gichtel"], "related_texts": ["Mysterium Magnum"]
    },
    {
        "id": "tl_049", "year": 1687, "category": "text",
        "title": "Newton's Principia Mathematica",
        "description": "Isaac Newton publishes Philosophiae Naturalis Principia Mathematica, establishing the mathematical framework for classical mechanics and universal gravitation. Newton's published work presents a universe governed by mathematical laws, but his unpublished manuscripts—comprising over a million words on alchemy and theology—reveal that he simultaneously pursued the philosopher's stone and the restoration of ancient wisdom. Newton's alchemical practice, documented by Dobbs and Newman, shows the coexistence of mathematical physics and alchemical research.",
        "related_figures": ["Isaac Newton"], "related_texts": []
    },
    # ── Enlightenment and Persistence (1690–1780) ────────────────────────────
    {
        "id": "tl_050", "year": 1694, "category": "historical",
        "title": "Philadelphian Society Founded",
        "description": "The Philadelphian Society is founded in London around the prophetic writings of Jane Lead and the theological direction of Francis Lee, constituting the most organized form of English Behmenism. The Society published Lead's visionary writings, maintained connections with Continental Pietist and theosophical networks, and articulated a program of spiritual alchemy grounded in Böhme's theosophy and Lead's own prophetic experience.",
        "related_figures": ["Jane Lead"], "related_texts": ["An Account of the Behmenists"]
    },
    {
        "id": "tl_051", "year": 1710, "category": "historical",
        "title": "Gold- und Rosenkreuz Order Established",
        "description": "The Gold- und Rosenkreuz (Gold and Rosicrucian Cross) order is established in German-speaking territories—the first formal institutional expression of Rosicrucian ideals in an organized fraternal structure with grades, rituals, and alchemical instruction. The order, formalized into nine grades by 1757, combines Freemasonry with Kabbalistic study, alchemical laboratory work, and ceremonial initiation, attracting aristocratic and professional members across the German states.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_052", "year": 1714, "category": "text",
        "title": "Leibniz: Monadology",
        "description": "Gottfried Wilhelm Leibniz completes the Monadologie, compressing his mature metaphysics into ninety propositions. The monad—a simple, unextended substance that reflects the entire universe from its unique perspective—resonates with the Hermetic principle of macrocosm in microcosm. Leibniz's concept of pre-established harmony and his earlier engagement with alchemical research in his youth connect the Monadology to the Hermetic tradition even as it advances rationalist metaphysics.",
        "related_figures": [], "related_texts": ["Monadology"]
    },
    {
        "id": "tl_053", "year": 1717, "category": "historical",
        "title": "Premier Grand Lodge of England Founded",
        "description": "The Premier Grand Lodge of England is founded in London on 24 June 1717, establishing organized speculative Freemasonry as a formal institution. The Craft rapidly absorbs Rosicrucian themes (particularly in the higher degrees that develop through the eighteenth century) and becomes the primary institutional vehicle through which Hermetic and alchemical ideas are transmitted to the educated public in the later Enlightenment.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_054", "year": 1723, "category": "text",
        "title": "Golden Chain of Homer Published",
        "description": "The Aurea Catena Homeri (Golden Chain of Homer) is published in Frankfurt and Leipzig, presenting a comprehensive Hermetic natural philosophy organized around the concept of the generative chain connecting all levels of being from divine light to gross matter. The work's aerial niter concept—connecting Sendivogian alchemy with phlogiston theory—represents an important node in the transmission of alchemical natural philosophy into Enlightenment chemistry.",
        "related_figures": [], "related_texts": ["The Golden Chain of Homer"]
    },
    {
        "id": "tl_055", "year": 1749, "category": "text",
        "title": "Swedenborg: Arcana Coelestia Begins Publication",
        "description": "Emanuel Swedenborg begins publishing Arcana Coelestia—an eight-volume verse-by-verse commentary on Genesis and Exodus through the lens of his spiritual-world experiences. The work applies Swedenborg's systematic doctrine of correspondences (every natural thing corresponds to a spiritual reality) to biblical exegesis, producing readings in which Genesis narrates the soul's stages of regeneration—precisely the spiritual-alchemical program of the Great Work applied to scripture.",
        "related_figures": ["Emanuel Swedenborg"], "related_texts": ["Arcana Coelestia"]
    },
    {
        "id": "tl_056", "year": 1758, "category": "text",
        "title": "Swedenborg: Heaven and Hell",
        "description": "Emanuel Swedenborg publishes De Coelo et Eius Mirabilibus et de Inferno (Heaven and Hell) in London—his most widely read theological work. The systematic account of the spiritual world's geography organized by the quality of love that animates each soul, and the doctrine of correspondences that connects natural and spiritual realities, generates immediate response in both Pietist and rationalist circles. William Blake later annotates his copy with increasing hostility.",
        "related_figures": ["Emanuel Swedenborg"], "related_texts": ["Heaven and Hell"]
    },
    {
        "id": "tl_057", "year": 1775, "category": "text",
        "title": "Saint-Martin: Des Erreurs et de la Vérité",
        "description": "Louis-Claude de Saint-Martin publishes Des Erreurs et de la Vérité (On Errors and Truth) anonymously, attributed to the 'Unknown Philosopher.' The work presents a systematic critique of Enlightenment materialism and defends a spiritualist natural philosophy grounded in Kabbalistic, Martinist, and Böhme-influenced traditions. Saint-Martin's Martinism becomes the dominant form of French theosophical spirituality in the late eighteenth century.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_058", "year": 1782, "category": "historical",
        "title": "Wilhelmsbad Congress",
        "description": "The Congress of Wilhelmsbad reforms the Strict Observance system of Masonry and redefines the relationship between Freemasonry and Rosicrucianism. The Congress marks the beginning of the explicit organization of Rosicrucian degrees within Masonic structures—a process that culminates in the Scottish Rite and other high-degree systems. The Gold- und Rosenkreuz's influence on Prussian aristocracy during this period peaks as its members include Prince Frederick William (later Frederick William II of Prussia).",
        "related_figures": [], "related_texts": []
    },
    # ── Romantic and Victorian Revival (1788–1850) ───────────────────────────
    {
        "id": "tl_059", "year": 1790, "category": "text",
        "title": "Blake: Marriage of Heaven and Hell",
        "description": "William Blake composes The Marriage of Heaven and Hell—an illuminated book combining visionary narrative, satirical aphorism, and alchemical imagery to critique Swedenborg's systematic theology and Enlightenment rationalism. Blake's diabolical voice inverts conventional moral categories and his 'printing in the infernal method, by corrosives' describes his own etching technique in alchemical terms. The work represents the most radical English Romantic appropriation of alchemical imagery.",
        "related_figures": ["William Blake"], "related_texts": ["Marriage of Heaven and Hell"]
    },
    {
        "id": "tl_060", "year": 1788, "category": "historical",
        "title": "Hermetic Order of the Golden Dawn Founded",
        "description": "The Hermetic Order of the Golden Dawn is founded in London by William Wynn Westcott, Samuel Liddell MacGregor Mathers, and William Robert Woodman, combining Freemasonry, Rosicrucian symbolism, Kabbalah, Enochian magic, astrology, and tarot into a systematic initiatory curriculum organized across twelve grades. The Order becomes the most influential magical fraternity of the modern era, attracting figures including Aleister Crowley, W. B. Yeats, and Dion Fortune.",
        "related_figures": [], "related_texts": ["The Cloud upon the Sanctuary"]
    },
    {
        "id": "tl_061", "year": 1802, "category": "text",
        "title": "Eckartshausen: The Cloud upon the Sanctuary",
        "description": "Karl von Eckartshausen publishes Die Wolke über dem Heiligtum (The Cloud upon the Sanctuary), presenting the concept of the Inner Church—a spiritual community of illumined souls transcending all external religious denominations. The work directly influences the founders of the Hermetic Order of the Golden Dawn; William Wynn Westcott cites it explicitly, and A. E. Waite's 1896 English edition makes it widely available.",
        "related_figures": [], "related_texts": ["The Cloud upon the Sanctuary"]
    },
    {
        "id": "tl_062", "year": 1820, "category": "figure",
        "title": "Birth of Mary Anne Atwood",
        "description": "Mary Anne Atwood (née South) is born. She will become the most systematic theorist of spiritual alchemy in the Victorian period, producing A Suggestive Inquiry into the Hermetic Mystery (1850)—a comprehensive account of alchemy as a tradition of spiritual transformation through mesmerism and contemplative practice. Mike Zuber's Spiritual Alchemy (2021) identifies Atwood as the culmination of the Böhme-to-Atwood spiritual alchemy lineage.",
        "related_figures": [], "related_texts": []
    },
    {
        "id": "tl_063", "year": 1850, "category": "text",
        "title": "Atwood: Suggestive Inquiry into the Hermetic Mystery",
        "description": "Mary Anne Atwood publishes A Suggestive Inquiry into the Hermetic Mystery, interpreting the alchemical tradition as a systematic practice of spiritual transformation through the mesmerism-induced trance—reading the philosopher's stone as the perfected human consciousness achieved through this practice. Atwood and her father attempt to suppress the book immediately after publication, believing it reveals too much; the few copies that survive become treasured documents of the Victorian occult revival.",
        "related_figures": [], "related_texts": []
    },
]

MAP_CENTERS = [
    { "name": "Prague", "lat": 50.0755, "lng": 14.4378,
      "role": "Alchemical center under Rudolf II (r. 1576–1612)",
      "description": "Rudolf II's Prague court was the preeminent center of alchemical patronage in Europe at the turn of the seventeenth century, attracting Michael Maier, John Dee, Edward Kelley, Oswald Croll, and dozens of lesser-known practitioners. Rudolf's collections of art, naturalia, and scientific instruments made the Hradcany Castle the most concentrated site of Hermetic intellectual activity in the period. The de Bry press in nearby Oppenheim published Maier's Atalanta Fugiens and Fludd's Utriusque Cosmi under Rudolf's cultural umbrella." },
    { "name": "Florence", "lat": 43.7696, "lng": 11.2558,
      "role": "Birthplace of Renaissance Neoplatonism and Hermetism",
      "description": "Cosimo de' Medici's Platonic Academy, directed by Marsilio Ficino, was the site of the first Latin translation of the Corpus Hermeticum (1463) and the systematic development of Renaissance Neoplatonism. Ficino's Three Books on Life and Platonic Theology established the philosophical framework within which alchemy, astrology, and natural magic could be pursued as legitimate philosophical activities. Giovanni Pico della Mirandola's Kabbalistic Conclusions emerged from the same Florentine humanist circle." },
    { "name": "Tübingen", "lat": 48.5216, "lng": 9.0577,
      "role": "Rosicrucian theological reform circle",
      "description": "The circle around the Tübingen lawyer Tobias Hess and the theologian Johann Valentin Andreae is now identified as the probable origin of all three Rosicrucian manifestos. Carlos Gilly's archival research has traced the Fama Fraternitatis manuscripts through this circle, demonstrating that the manifesto emerged from Protestant Pietist-reform networks in Württemberg rather than from a formal organization. Andreae's chemical wedding was also composed during his Tübingen years." },
    { "name": "London", "lat": 51.5074, "lng": -0.1278,
      "role": "English Rosicrucian, Masonic, and Hermetic synthesis",
      "description": "London was the center of English engagement with Hermetic, Rosicrucian, and alchemical traditions from John Dee's Elizabethan court to the founding of the Hermetic Order of the Golden Dawn (1888). Robert Fludd defended Rosicrucianism here; Elias Ashmole collected alchemical manuscripts and was initiated into Freemasonry; Isaac Newton conducted his private alchemical research; Jane Lead's Philadelphian Society disseminated Böhme's spiritual alchemy. The Royal Society's founding (1660) did not displace but coexisted with alchemical practice." },
    { "name": "Amsterdam", "lat": 52.3676, "lng": 4.9041,
      "role": "Böhme edition center and theosophical publishing hub",
      "description": "Amsterdam's press freedom made it the primary publishing center for heterodox religious and philosophical texts in the seventeenth century. Johann Georg Gichtel published the complete Böhme edition here in 1682; Descartes, Spinoza, and the Rosicrucian sympathizer Comenius all published in Amsterdam. The city's mercantile cosmopolitanism and religious tolerance made it a crossroads for Hermetic, theosophical, and Martinist networks across Europe." },
    { "name": "Paris", "lat": 48.8566, "lng": 2.3522,
      "role": "French illuminism, alchemy, and the Martinist tradition",
      "description": "Paris hosted some of the most important French alchemical and theosophical networks, from the Paracelsian controversies at the medical faculty (Duchesne vs. Galenists, 1560s–1660s) through Saint-Martin's Martinism in the 1770s–1780s and the revolutionary-era persistence of Rosicrucian-Masonic fraternities. The Strict Observance and Rite of Memphis-Misraim both maintained Hermetic traditions in Parisian Masonic lodges through the late eighteenth and early nineteenth centuries." },
    { "name": "Basel", "lat": 47.5596, "lng": 7.5886,
      "role": "Paracelsian medicine and German humanism",
      "description": "Basel was central to both Paracelsus's career and the transmission of Hermetic humanism north of the Alps. Paracelsus lectured at the University of Basel in 1527, briefly holding the municipal physician's post before his controversial departure. The Froben press in Basel had published Erasmus and would publish major Paracelsian editions. Heinrich Khunrath received his medical degree here in 1588, and the city remained a center of medical humanism and reformed natural philosophy through the seventeenth century." },
    { "name": "Görlitz", "lat": 51.1558, "lng": 15.0055,
      "role": "Jacob Böhme's workshop and the birth of theosophy",
      "description": "Jacob Böhme lived and worked in Görlitz his entire adult life, practicing as a shoemaker while producing the theosophical writings that made him the foundational figure of the German mystical-alchemical tradition. His circle of friends and supporters in Görlitz—including the nobleman Karl von Ender—enabled him to write and circulate his manuscripts despite the hostility of the city pastor Gregorius Richter. The Görlitz circle represents the communal dimension of early modern spiritual alchemy." },
    { "name": "Hamburg", "lat": 53.5753, "lng": 10.0153,
      "role": "Khunrath's Amphitheatrum and Northern German Hermetism",
      "description": "Hamburg was the site of Heinrich Khunrath's practice and the publication of the first edition of his Amphitheatrum Sapientiae Aeternae (1595)—the most visually spectacular emblem book of the alchemical tradition. Northern German cities like Hamburg, Lübeck, and Danzig maintained active Hermetic and Rosicrucian networks through the seventeenth century, connecting the Böhme circle in Görlitz with the broader European esoteric landscape through trade and correspondence routes." },
    { "name": "Oppenheim", "lat": 49.8612, "lng": 8.3699,
      "role": "De Bry press: Maier, Fludd, and Rosicrucian publishing",
      "description": "The de Bry printing house in Oppenheim—operated by Johann Theodor de Bry—was the most important publisher of alchemical and Rosicrucian emblem books in the early seventeenth century. Maier's Atalanta Fugiens (1617), Fludd's Utriusque Cosmi Historia (from 1617), and several other key texts were produced here. The de Bry family's artistic excellence in engraving made Oppenheim the visual epicenter of the Rosicrucian emblem tradition." },
    { "name": "Frankfurt am Main", "lat": 50.1109, "lng": 8.6821,
      "role": "Book fair and Paracelsian publishing hub",
      "description": "Frankfurt's annual book fair was the most important marketplace for learned publications in Europe, and the city's printing houses produced key alchemical texts including Croll's Basilica Chymica (1609) and Libavius's Alchemia (1597). The Frankfurt fair enabled rapid dissemination of Rosicrucian and alchemical texts across European learned networks. The de Bry family had connections to Frankfurt before their Oppenheim operations, and Frankfurt remained central to alchemical publishing throughout the seventeenth century." },
    { "name": "Leiden", "lat": 52.1601, "lng": 4.4970,
      "role": "Iatrochemistry enters the academy",
      "description": "The University of Leiden was the most prestigious Protestant university in Europe in the seventeenth century and the site where iatrochemistry first entered academic medical teaching. Franciscus Sylvius de le Boë occupied the chair of medicine from 1658 and systematically taught acid-alkali chemistry as the foundation of physiology—transforming Paracelsian iatrochemistry into a form acceptable to university medicine. Thomas Willis's work on fermentation was also associated with the Leiden circle." },
    { "name": "Heidelberg", "lat": 49.3988, "lng": 8.6724,
      "role": "Palatine court and Rosicrucian milieu",
      "description": "The Palatinate court at Heidelberg under Elector Frederick V (1610–1620) was the most important Protestant princely court in Germany and the center that Frances Yates associated with the Rosicrucian movement. Frederick V's marriage to Elizabeth Stuart (daughter of James I) linked Heidelberg to the English court; his court library, his botanical garden, and his circle of learned advisors made Heidelberg a center of Hermetic humanism before his defeat at the Battle of White Mountain (1620) destroyed the Palatine project." },
    { "name": "Wittenberg", "lat": 51.8667, "lng": 12.6458,
      "role": "Reformation heartland and Protestant millenarianism",
      "description": "Luther's Wittenberg was the originating site of the Protestant Reformation that shaped the theological context of the Rosicrucian manifestos. Protestant millenarianism—the expectation of an imminent eschatological transformation—was cultivated in Wittenberg and its successor institutions, providing the apocalyptic framework within which the Rosicrucian call for universal reform was articulated. The Rosicrucian manifestos' Protestant identity—anti-papal, anti-Islamic, Luther-affirming—derives directly from the Wittenberg theological tradition." },
    { "name": "Strasbourg", "lat": 48.5734, "lng": 7.7521,
      "role": "Chemical Wedding publication and Protestant reform printing",
      "description": "Andreae's Chymische Hochzeit (Chemical Wedding) was published in Strasbourg in 1616, and the city's printing industry had deep connections with Protestant reform movements across the Rhine region. Strasbourg's Reformed intellectual culture—combining humanist scholarship with Pietist spirituality—was sympathetic to the Rosicrucian reform program, and the city served as a conduit between the Tübingen manifesto circle and wider European Protestant networks." },
]

with open(DB, encoding='utf-8') as f:
    db = json.load(f)

db['timeline'] = TIMELINE
db['map_centers'] = MAP_CENTERS

with open(DB, 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"Added {len(TIMELINE)} timeline events")
print(f"Added {len(MAP_CENTERS)} map learning centers")
