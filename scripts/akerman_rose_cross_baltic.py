"""
Akerman Rose Cross over the Baltic — Database Ingestion Script
Susanna Åkerman, Rose Cross over the Baltic: The Spread of Rosicrucianism in Northern Europe
(Leiden: Brill, 1998), 270 pp.

Adds: 9 figures, 6 concepts, 7 texts, 1 scholar entry, 25 timeline events
Updates: existing entries for Andreae, Tycho Brahe, Michael Maier, Jacob Böhme
"""

import json
import copy

DATA_FILE = "data/prototype_data.json"

with open(DATA_FILE) as f:
    data = json.load(f)

def safe_int(v):
    try: return int(v)
    except: return 0

max_fig = max(safe_int(f["id"]) for f in data["figures"])
max_con = max(safe_int(c["id"]) for c in data["concepts"])
max_txt = max(safe_int(t.get("id", 0)) for t in data["texts"])

# ─────────────────────────────────────────────────────────────────────────────
# NEW FIGURES  (IDs 101–109)
# ─────────────────────────────────────────────────────────────────────────────
NEW_FIGURES = [
    {
        "id": 101,
        "name": "Johannes Bureus",
        "slug": "johannes-bureus",
        "birth_year": 1568,
        "death_year": 1652,
        "nationality": "Swedish",
        "location": "Stockholm / Uppsala",
        "lat": 59.3293,
        "lng": 18.0686,
        "primary_discipline": "Runic Theosophy / Court Antiquarianism",
        "summary": "Johannes Bureus (1568–1652) was Sweden's royal antiquary, the architect of a unique 'Adulrunic' theosophy that fused Norse runic lore with Kabbalistic Hermetism, and the central figure in the reception of Rosicrucian ideas in Scandinavia. Trained in Latin, Hebrew, and the runic traditions preserved in Swedish archives, Bureus presented the Gothic-runic heritage of the North as a primordial divine alphabet whose hidden combinations unlocked universal reform. Susanna Åkerman's archival research identifies him as the pivotal transmitter of Rosicrucian millenarianism in the Baltic world.",
        "essay": "Johannes Bureus (1568–1652) occupies a singular place in the history of European esotericism as the principal conduit through which Rosicrucian ideas entered Swedish court culture. Born in Åkerby, Uppsala province, he rose to become royal antiquary under King Carl IX and later King Gustavus II Adolphus, a position that gave him both access to manuscript archives and the ear of power.\n\nBureus's intellectual project centred on what he called the *Adulruna*—a system of runic combinatorics in which each of the sixteen Gothic runes was divided into component shapes (*stavar*), each carrying numerical and alphabetical equivalences derived from Hebrew Kabbalah and Hermetic number theory. Bureus believed he had recovered a primordial divine alphabet that antedated the Hebrew tradition and was uniquely preserved in Scandinavia. His major work, *Adulruna Rediviva* (composed over decades, c. 1611–1647), presents an elaborate theosophical system in which runic combinations reveal the names of angels, the structure of the cosmos, and the pathway to spiritual regeneration.\n\nÅkerman's research (1998) demonstrates that Bureus encountered Rosicrucian pamphlets—including the *Fama Fraternitatis* (1614) and *Confessio* (1615)—through the Hanseatic trade networks linking Stockholm to Hamburg, Lübeck, and Danzig. He read them through his existing Adulrunic framework, finding in the brotherhoods' claims of universal reform a confirmation of his own millenarian expectations. The Rosicrucian figure of the 'Temple of the Holy Spirit' resonated with Bureus's interest in the Temple at Damar, which he connected to runic inscriptions at Swedish burial sites.\n\nBureus circulated his ideas through an informal network of Swedish court officials, clergymen, and later Georg Stiernhielm, the Baroque poet who transmitted Hermetic-runic thought into the later seventeenth century. His influence on Swedenborgianism—traced by Åkerman through the specific vocabulary of 'divine influx' and regeneration—represents the longest arc of his intellectual legacy, connecting Baltic Rosicrucianism to eighteenth-century theosophy.\n\nScholars have debated the relationship between Bureus's runic nationalism and the political appropriations of his work. Johan Nordström (1934) first noted that Paracelsian-Hermetic prophecy served as psychological preparation for Sweden's entry into the Thirty Years' War, but Nils Ahnlund (1939) countered that the 'Lion of the North' prophecy had negligible direct influence on royal decision-making. Åkerman's more nuanced position holds that while direct political causation cannot be demonstrated, Bureus's theosophical circle created a cultural atmosphere receptive to eschatological justifications for Swedish imperial expansion.\n\nBureus's significance lies not in military history but in intellectual genealogy: he is the point at which Norse antiquarianism, Kabbalistic Hermetism, and Rosicrucian universalism fused into a distinctively northern tradition that would persist well into the Enlightenment.",
        "scholars": ["Susanna Åkerman", "Johan Nordström", "Nils Ahnlund", "Sten Lindroth"],
        "key_works": [],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapters 1, 5. Nordström, Johan. 'Lejonet från Norden,' *De Yverbornes Ö* (Uppsala, 1934). Lindroth, Sten. *Paracelsismen i Sverige* (Uppsala, 1943).",
        "scholarly_debates": "Whether Bureus's runic-Rosicrucian circle had genuine political influence (Nordström vs. Ahnlund debate); whether his tradition represents an authentic Scandinavian variant of Hermetism or a derivative appropriation.",
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 8,
        "image_url": "",
        "genealogical_position": "Swedish Rosicrucian reception; Adulrunic theosophy; Swedenborg precursor",
        "influenced_by_figures": [4, 2, 33],
        "influenced_figures": [7]
    },
    {
        "id": 102,
        "name": "Helisaeus Roeslin",
        "slug": "helisaeus-roeslin",
        "birth_year": 1544,
        "death_year": 1616,
        "nationality": "German (Alsatian)",
        "location": "Ensisheim / Frankfurt",
        "lat": 47.8660,
        "lng": 7.3570,
        "primary_discipline": "Astrology / Cosmology / Millenarian Prophecy",
        "summary": "Helisaeus Roeslin (1544–1616) was an Alsatian physician, astrologer, and millenarian cosmologist whose apocalyptic manuscripts, circulated under the pseudonym 'Lampertus Floridus,' shaped the prophetic atmosphere in which Rosicrucianism emerged. Writing on the new star of 1572 (Tycho Brahe's nova), comets, celestial geometry, and the coming transformation of Europe, Roeslin provided the eschatological framework that Rosicrucian writers would amplify. Åkerman identifies him as a crucial link between late-sixteenth-century astrological prophecy and the Rosicrucian manifestoes.",
        "essay": "Helisaeus Roeslin (1544–1616) represents a type of early modern intellectual that resists easy categorisation: a trained physician, practising astrologer, millenarian prophet, and participant in the learned manuscript culture of the upper Rhine. Born near Saarbrücken in Alsace, he spent much of his career at Ensisheim, the Habsburg administrative centre in Alsace, where he served as court physician while maintaining an extensive correspondence with astronomers, theologians, and esoteric writers across the German lands.\n\nRoeslin's intellectual significance lies chiefly in his role as a propagator of 'celestial wheel' cosmology—a system in which the movements of the outer planets, combined with the observation of celestial prodigies (comets, novae, eclipses), permitted the calculation of world-historical epochs. His treatise *De Opere Dei Creationis* (1597) presents a cosmological schema in which history unfolds through divinely ordered planetary cycles culminating in an imminent world transformation. The nova of 1572, which both Tycho Brahe and Roeslin observed, became for him a pivotal sign of approaching universal change.\n\nÅkerman's research reveals that Roeslin circulated a series of apocalyptic manuscripts under the pseudonym 'Lampertus Floridus'—an allusion to the twelfth-century chronicle *Liber Floridus* by Lambert of Saint-Omer, which Roeslin associated with the Frankish-Scandinavian genealogy of the coming universal monarch. These manuscripts, listed in 1638 by the Rosicrucian author Karl Wideman at Augsburg, indicate that Roeslin occupied a central node in the network of esoteric manuscript exchange through which Rosicrucian ideas would later travel.\n\nThe relationship between Roeslin and Simon Studion is of particular importance. Both were active in the Württemberg-Alsace region; both drew on the same astronomical and prophetic sources; and both fed into the millenarian expectation that the early Rosicrucian manifestoes both expressed and exploited. Åkerman demonstrates that the 'celestial wheel' motif in Studion's *Naometria* (1604) derives from Roeslin's cosmological system.\n\nRoeslin's connection to Rosicrucian writers was thus primarily structural rather than personal: he provided the eschatological vocabulary—universal reform, celestial signs, imminent transformation—that the *Fama Fraternitatis* and *Confessio* would deploy for their own purposes. His death in 1616, the same year as the *Chymische Hochzeit*, marks the end of the generation that incubated Rosicrucianism before placing it before the European public.",
        "scholars": ["Susanna Åkerman", "Carlos Gilly", "Wilhelm Schmidt-Biggemann"],
        "key_works": [],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 2, pp. 97–110. Gilly, Carlos. 'Cimelia Rhodostaurotica' (Amsterdam, 1995).",
        "scholarly_debates": "Roeslin's precise relationship to early Rosicrucian circles; whether his pseudonymous manuscripts directly influenced the Rosicrucian manifestoes or represent parallel development in the same eschatological milieu.",
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 5,
        "image_url": "",
        "genealogical_position": "Late Paracelsian millenarianism; pre-Rosicrucian prophecy tradition",
        "influenced_by_figures": [84],
        "influenced_figures": [1]
    },
    {
        "id": 103,
        "name": "Simon Studion",
        "slug": "simon-studion",
        "birth_year": 1543,
        "death_year": 1605,
        "nationality": "German (Württemberg)",
        "location": "Marbach am Neckar",
        "lat": 48.9369,
        "lng": 9.2581,
        "primary_discipline": "Millenarian Mysticism / Proto-Rosicrucianism",
        "summary": "Simon Studion (c. 1543–1605) was a Württemberg schoolmaster and millenarian mystic whose enormous unpublished manuscript *Naometria* (1604) constitutes one of the most important pre-Rosicrucian documents in European esoteric history. Combining numerological analysis of the Temple of Solomon with astrological prediction and Paracelsian prophecy, Studion constructed an elaborate timetable for the imminent universal reform that would directly shape the Rosicrucian manifestoes. Åkerman's work places him at the centre of the Württemberg esoteric circle from which Rosicrucianism emerged.",
        "essay": "Simon Studion (c. 1543–1605) is one of the great uncelebrated architects of early modern esotericism. A schoolmaster at Marbach on the Neckar in Württemberg, he devoted decades to composing *Naometria*—a title meaning 'temple-measurement'—a vast manuscript treatise completed around 1604 that attempted to calculate the precise timing of the coming reformation of all things through numerological analysis of the biblical Temple of Solomon.\n\n*Naometria* represents the convergence of three streams: the Paracelsian prophetic tradition (centred on the figure of 'Elias Artista,' the coming reformer of medicine and philosophy), the astrological chronology of Helisaeus Roeslin's 'celestial wheel,' and the kabbalistic numerology transmitted through Protestant biblical scholarship. Studion calculated that the year 1604—marked by a conjunction of Saturn and Jupiter—would initiate a definitive historical turning point. The text, never printed in Studion's lifetime, circulated in manuscript among the Württemberg-Kassel esoteric circle that included figures close to the later Rosicrucian publication project.\n\nÅkerman's analysis (1998) establishes the relationship between *Naometria* and the *Confessio Fraternitatis* (1615) at the level of specific numerical schemes and prophetic vocabulary. The Rosicrucian promise of 'universal reform of the whole world' (*Generalreformation*) echoes Studion's own formulation of *Naometria*'s purpose. The symbol of the 'Celestial Wheel' and the association of the reforming fraternity with the Temple were standard topoi in *Naometria* before they appeared in print in 1614–15.\n\nStudion's *Naometria* also deployed the imagery of the Rosy Cross itself—the symbol appears in the manuscript in an ecclesiastical-heraldic context—suggesting that it formed part of the shared visual-symbolic vocabulary of the Württemberg circle before the manifestoes made it famous. Carlos Gilly's archival work has confirmed that the manuscript was known to figures connected to Johann Valentin Andreae.\n\nStudion represents the moment at which Protestant prophecy, Paracelsian medicine, and Kabbalistic numerology fused into an anticipatory Rosicrucianism that was waiting to become a public movement. His death in 1605, before the manifestoes appeared, means that he belongs to the generative prehistory of the movement rather than its public history.",
        "scholars": ["Susanna Åkerman", "Carlos Gilly", "Roland Edighoffer"],
        "key_works": [],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 2, pp. 97–104. Gilly, Carlos. 'Iter Rosicrucianum,' in *Das Erbe des Christian Rosenkreuz* (Amsterdam, 1988).",
        "scholarly_debates": "Whether Studion belongs to the same circle as Andreae or represents a parallel development; the extent of *Naometria*'s manuscript circulation; its direct influence on the *Confessio Fraternitatis*.",
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 6,
        "image_url": "",
        "genealogical_position": "Württemberg proto-Rosicrucian circle; Naometria → Fama/Confessio lineage",
        "influenced_by_figures": [102, 4],
        "influenced_figures": [1]
    },
    {
        "id": 104,
        "name": "Paul Grebner",
        "slug": "paul-grebner",
        "birth_year": 1543,
        "death_year": 1604,
        "nationality": "German / Bohemian",
        "location": "Prague / Saxony",
        "lat": 50.0755,
        "lng": 14.4378,
        "primary_discipline": "Prophetic Vision / Millenarian Writing",
        "summary": "Paul Grebner (1543–1604) was a Bohemian prophet and visionary whose manuscript prophecies, circulated in German, Latin, and eventually Danish and English translations, became central texts in the network of esoteric millenarianism that fed into Rosicrucianism and the 'Lion of the North' tradition. His visions—presented as divinely revealed knowledge of imminent world transformation—were transmitted through the Baltic networks studied by Åkerman, eventually reaching the Danish and English courts.",
        "essay": "Paul Grebner (1543–1604) belongs to the tradition of 'prophetic manuscripts' that flourished in the German lands during the late sixteenth century—texts claiming divine revelation of imminent world transformation, circulated in manuscript rather than print, and treated as esoteric knowledge by recipients who used them to interpret political events. His *Prophetische Beschreibung*—a vision of a great northern king who would reform the world under the sign of the lion—became one of the central documents in the construction of the 'Lion of the North' tradition that would eventually be applied to Gustavus Adolphus of Sweden.\n\nGrebner's visions are notable for their geographic specificity: the prophesied reformer comes from the North, crosses the Baltic, conquers southward, and restores the true church before dying in Germany. This narrative template resonated powerfully with Baltic Rosicrucian readers because it appeared to provide divine sanction for precisely the kind of northward-originating reformation that figures like Johannes Bureus had been anticipating through their own theosophical calculations.\n\nÅkerman's research (1998) traces the manuscript transmission of Grebner's prophecies through a Danish-Dutch network active between 1622 and 1625—precisely the years when the Rosicrucian movement in Northern Europe was at its height and when the candidacy of various Protestant princes for the role of reforming 'lion' was being actively debated. The prophecies passed through Hesse-Kassel, Hamburg, Amsterdam, Copenhagen, and Stockholm, acquiring new annotations and translations at each node.\n\nThe relationship between Grebner's prophecies and the 'Leo ex Silva' tradition—the image of a lion emerging from a forest in the North, used in prophetic pamphlets from the 1620s—is direct. Åkerman shows how the Rosicrucian printing network at Hesse-Kassel served as an amplifier for this tradition, producing and distributing pamphlets that combined Grebner's visionary material with the Rosicrucian promise of universal reform.\n\nGrebner died in 1604, before the Rosicrucian manifestoes appeared, but his prophecies outlived him in remarkable ways: an English translation of his visions was presented to Queen Elizabeth I in 1582, and later copies reached the Swedish court through precisely the intellectual networks that Bureus inhabited.",
        "scholars": ["Susanna Åkerman", "Hartmut Lehmann", "Robin Barnes"],
        "key_works": [],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 3, pp. 171–172. Concerning prophetic manuscript traditions: Barnes, Robin. *Prophecy and Gnosis* (Stanford, 1988).",
        "scholarly_debates": "The relationship between Grebner's tradition and classical millenarianism; the extent of his actual manuscript distribution; whether the later application to Gustavus Adolphus was politically organised or organic.",
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 4,
        "image_url": "",
        "genealogical_position": "Bohemian-Saxon prophetic tradition; Lion of the North typology",
        "influenced_by_figures": [],
        "influenced_figures": [101]
    },
    {
        "id": 105,
        "name": "Raphael Eglinus",
        "slug": "raphael-eglinus",
        "birth_year": 1559,
        "death_year": 1622,
        "nationality": "Swiss",
        "location": "Marburg",
        "lat": 50.8021,
        "lng": 8.7711,
        "primary_discipline": "Paracelsian Medicine / Rosicrucian Sympathy",
        "summary": "Raphael Eglinus (1559–1622) was a Swiss physician trained in Paracelsian medicine who became one of the earliest and most engaged respondents to the Rosicrucian manifestoes. A professor at Marburg, he published *Disquisitio de Helia Artista* (1606)—predating the public manifestoes—and subsequently *Assertio Fraternitatis RC* (1616), contributing to the Rosicrucian debate from a position of genuine sympathy and sophisticated Hermetic learning. Åkerman identifies his work on 'Elias Artista' as crucial to the millenarian framework within which the manifestoes were received.",
        "essay": "Raphael Eglinus (1559–1622) represents the educated Paracelsian physician who formed the most receptive audience for the Rosicrucian manifestoes. Born in Switzerland and trained in medicine, he rose to a professorship at the Gymnasium in Marburg in Hesse—a city whose Landgrave Moritz was among the most active patrons of Rosicrucian culture in the German lands.\n\nEglinus's 1606 publication *Disquisitio de Helia Artista* is remarkable in predating the public Rosicrucian manifestoes: it shows that the tradition of the 'Elias Artista'—the Paracelsian prophecy of a coming reformer of natural philosophy and medicine—was already circulating in print as an expectation before the *Fama Fraternitatis* (1614) gave it its most famous expression. Eglinus understood the 'Artista' figure through the lens of Paracelsian medical eschatology: a philosopher-physician who would reveal the hidden secrets of nature and inaugurate a reformed era of healing.\n\nAfter the manifestoes appeared, Eglinus became one of their most sophisticated commentators. His *Assertio Fraternitatis RC* (1616) defends the reality of the brotherhood against sceptics while interpreting its goals in terms of Paracelsian-Hermetic natural philosophy. He distinguishes carefully between the genuine esoteric wisdom claimed by the brotherhood and the fraudulent impostors who had begun to exploit the Rosicrucian name for charlatanism.\n\nÅkerman's analysis places Eglinus in the context of the Marburg-Hesse network: the same intellectual environment that included the Landgrave's patronage of alchemical laboratory work, the Rosicrucian printing press activities documented at Kassel, and the circulation of Paracelsian manuscripts in the region. His references to 'the signifying fish'—a symbol drawn from Hermetic number theory—indicate familiarity with the same iconographic vocabulary that Studion and Bureus deployed.\n\nThe significance of Eglinus for the broader story is his demonstration that Rosicrucianism had genuine intellectual substance for educated Paracelsians, not merely millennial excitement. His sophisticated engagement with the movement's claims represents the tradition at its most rigorous.",
        "scholars": ["Susanna Åkerman", "Carlos Gilly", "Bruce Moran"],
        "key_works": [],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 2, pp. 116–119. Moran, Bruce. *The Alchemical World of the German Court* (Stuttgart, 1991).",
        "scholarly_debates": "Whether Eglinus had direct contact with the Rosicrucian authorship circle; the relationship between *Disquisitio de Helia Artista* and the *Fama Fraternitatis*.",
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 4,
        "image_url": "",
        "genealogical_position": "Paracelsian Marburg network; Elias Artista tradition",
        "influenced_by_figures": [4, 1],
        "influenced_figures": []
    },
    {
        "id": 106,
        "name": "Julius Sperber",
        "slug": "julius-sperber",
        "birth_year": 1560,
        "death_year": 1621,
        "nationality": "German (Anhalt)",
        "location": "Zerbst / Anhalt",
        "lat": 51.9636,
        "lng": 12.0836,
        "primary_discipline": "Gnostic Rosicrucianism / Theosophical Astronomy",
        "summary": "Julius Sperber (c. 1560–1621) was a German courtier and Rosicrucian writer active in the Anhalt region whose *Echo der von Gott hocherleuchteten Fraternität* (1615) was among the earliest and most theosophically sophisticated responses to the Rosicrucian manifestoes. Sperber's work is distinguished by its explicitly Gnostic-theosophical framework, its integration of astronomical observation with spiritual transformation, and its emphasis on the interior illumination (*Erleuchtung*) that qualifies one for genuine brotherhood. Åkerman identifies a 'Sperber circle' of Gnostic Rosicrucians distinct from the more institutionally oriented Kassel network.",
        "essay": "Julius Sperber (c. 1560–1621) occupies a distinctive niche in the Rosicrucian movement as the representative of what Åkerman calls its 'Gnostic' wing—a strand of the tradition that emphasised interior illumination, cosmological speculation, and the direct reception of divine light rather than the institutional reform of learning and medicine that other Rosicrucian writers foregrounded.\n\nSperber served as a courtier in the small Protestant principality of Anhalt, whose ruling family had connections to both the Reformed church and to Paracelsian-Hermetic culture. His *Echo der von Gott hocherleuchteten Fraternität des löblichen Ordens R.C.* (1615) is structured as a response to the *Confessio Fraternitatis*—an 'echo' that amplifies and comments on the manifesto's themes while giving them a distinctly theosophical colouring. The title's resonance between 'Echo' and the manifesto's call for public 'announcement' reveals Sperber's literary sophistication.\n\nThe most distinctive aspect of Sperber's Rosicrucianism is its astronomy. Åkerman's analysis of Chapter 5 of *Rose Cross over the Baltic* shows that Sperber was deeply engaged with the post-Tychonic debate about the structure of the cosmos—whether the earth moved (Copernican), whether the planets orbited the sun which orbited the earth (Tychonic), or whether some combination applied. Sperber's position was that astronomical truth and spiritual illumination were intimately connected: only the genuinely illumined could perceive the true structure of the heavens. This 'theosophy and science' intersection anticipates later developments in Swedenborgian and theosophical natural philosophy.\n\nSperber's emphasis on 'Phosphoric Lights'—luminescent phenomena including bioluminescence, ignes fatui, and optical effects in glass—as signs of the spirit's presence in matter connects his work to what Åkerman calls the 'roses and phosphoric lights' dimension of Rosicrucian science: the conviction that natural phenomena of light and luminescence were material manifestations of the divine influx that would be fully revealed in the coming transformation.\n\nHis *Kabbalah Denudatam* connections and his engagement with the Tychonic model at Danzig (the *Oculus Sidereus* group) indicate that Sperber's network extended from Anhalt across the Baltic world.",
        "scholars": ["Susanna Åkerman", "Wouter Hanegraaff", "Antoine Faivre"],
        "key_works": [],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 5, pp. 208–215. Faivre, Antoine. *Access to Western Esotericism* (Albany, 1994).",
        "scholarly_debates": "Sperber's relationship to the primary Rosicrucian authorship circle; the 'Gnostic' vs. 'reform' wings of Rosicrucianism; the extent of his Baltic network.",
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 4,
        "image_url": "",
        "genealogical_position": "Gnostic Rosicrucianism; theosophical astronomy; Anhalt esoteric circle",
        "influenced_by_figures": [1, 3],
        "influenced_figures": []
    },
    {
        "id": 107,
        "name": "Guillaume Postel",
        "slug": "guillaume-postel",
        "birth_year": 1510,
        "death_year": 1581,
        "nationality": "French",
        "location": "Paris",
        "lat": 48.8566,
        "lng": 2.3522,
        "primary_discipline": "Christian Kabbalah / Universal Language / Millenarian Reform",
        "summary": "Guillaume Postel (1510–1581) was a French Hebraist, Kabbalist, and visionary who anticipated many of the central themes of Rosicrucianism decades before the manifestoes appeared. His projects for a universal language, a reconciliation of religions, and the imminent installation of a French universal monarch over a reformed Christendom created a template for Rosicrucian universalism. Åkerman's analysis of Chapter 4 traces how Postel's *Candelabri Typici* (c. 1548) and his concept of the *Cain Renatus* ('renewed Cain') fed directly into the millenarian framework of the *Confessio Fraternitatis*.",
        "essay": "Guillaume Postel (1510–1581) is one of the most extraordinary figures of sixteenth-century European intellectual history: a royal professor of Oriental languages, an early Kabbalist in a Christian idiom, a would-be universal reformer, and a visionary who spent years under investigation by the Inquisition for his prophetic claims. His influence on the Rosicrucian movement, identified and documented by Åkerman, represents a crucial genealogical link between Renaissance Christian Kabbalah and seventeenth-century Rosicrucianism.\n\nPostel's scholarly career at the Collège Royal in Paris gave him access to Greek, Hebrew, Arabic, and Aramaic manuscripts unavailable to most European scholars. His study of the Kabbalistic *Sefer ha-Bahir* and *Zohar* led him to the conviction that the Hebrew tradition contained the primordial divine wisdom that would, when properly understood and propagated, enable the reconciliation of Christianity, Judaism, and Islam under a single universal monarchy—which Postel initially envisioned as a restored French empire.\n\nThe text that most directly connects Postel to Rosicrucianism is his *Candelabri Typici* (c. 1548), an extended meditation on the seven-branched candelabrum of the Temple of Solomon as a universal symbol of divine knowledge. Åkerman's close reading (Chapter 4, *Rose Cross over the Baltic*) demonstrates that the *Confessio Fraternitatis*'s imagery of the fraternity as custodians of a revealed 'light' draws on precisely the candelabrum symbolism that Postel had elaborated—the seven branches representing the seven liberal arts transformed and perfected by divine illumination.\n\nEqually significant is Postel's concept of *Cain Renatus*—the 'renewed Cain' who, through spiritual transformation, transcends the curse of the first murderer and becomes a new kind of human being. Åkerman traces this concept into the Rosicrucian tradition through the figure of Christian Rosencreutz himself, who in the *Fama* narrative undergoes precisely this kind of spiritual rebirth and return.\n\nPostel spent his last years in the monastery of Saint-Martin-des-Champs in Paris, under a form of 'gentle' ecclesiastical custody that permitted him to write and receive visitors while preventing further public prophesying. The manuscripts he produced in this period—including elaborations of his universal language project—circulated through the scholarly networks that would eventually connect to the Rosicrucian milieu.",
        "scholars": ["Susanna Åkerman", "William Bouwsma", "Marion Leathers Kuntz"],
        "key_works": [],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 4, pp. 173–195. Bouwsma, William. *Concordia Mundi: The Career and Thought of Guillaume Postel* (Cambridge MA, 1957). Kuntz, Marion Leathers. *Guillaume Postel, Prophet of the Restitution of All Things* (The Hague, 1981).",
        "scholarly_debates": "The channels through which Postel's ideas reached the Rosicrucian writers; whether the connection is direct influence or structural parallel; Postel's own religious status (visionary? heretic? eccentric?).",
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 5,
        "image_url": "",
        "genealogical_position": "Christian Kabbalism → Rosicrucian universalism; candelabrum symbolism; Cain Renatus tradition",
        "influenced_by_figures": [17, 16],
        "influenced_figures": [1, 103]
    },
    {
        "id": 108,
        "name": "Georg Stiernhielm",
        "slug": "georg-stiernhielm",
        "birth_year": 1598,
        "death_year": 1672,
        "nationality": "Swedish",
        "location": "Stockholm",
        "lat": 59.3293,
        "lng": 18.0686,
        "primary_discipline": "Baroque Poetry / Hermetic Philosophy / Runic Studies",
        "summary": "Georg Stiernhielm (1598–1672), known as the 'father of Swedish poetry,' was a baroque poet, mathematician, philologist, and Hermetic philosopher who transmitted the runic-theosophical tradition of Johannes Bureus into the mid-seventeenth century. His long philosophical poem *Hercules* (1658) encodes Hermetic principles within classical allegory, and his philological studies pursued the thesis that Gothic was the mother of all languages—a thesis with esoteric as well as nationalistic implications. Åkerman demonstrates his role as the key link between Bureus's Adulrunic theosophy and the later reception of Hermetism in Sweden.",
        "essay": "Georg Stiernhielm (1598–1672) is one of the most intellectually complex figures of seventeenth-century Sweden: simultaneously a court official, a mathematician, a poet of genuine distinction, a comparative philologist, and a transmitter of esoteric tradition. His significance for the history of northern Rosicrucianism lies in his role as the inheritor and adaptor of Johannes Bureus's Adulrunic theosophy—the system that had fused Norse runic lore with Kabbalistic Hermetism in the early decades of the century.\n\nStiernhielm's career began under the patronage of the same court circles that had supported Bureus, and the two men were in direct contact during Stiernhielm's formative intellectual years. Where Bureus had worked in an essentially manuscript culture, Stiernhielm operated in the transformed print culture of mid-century Sweden, adapting the Adulrunic synthesis for a more public audience without abandoning its esoteric core.\n\nHis major literary work *Hercules* (1658) deploys the classical hero's choice between Virtue and Pleasure as an allegory of interior alchemical and theosophical transformation. The poem's elaborate mythological apparatus encodes Hermetic cosmological principles—the tripartite structure of matter, the role of elemental transformation in spiritual regeneration, the cosmic significance of heroic choice—in forms accessible to courtly readers while preserving their deeper esoteric meanings for the initiated.\n\nStiernhielm's philological work pursued the thesis that Gothic (the Germanic languages including Swedish) was the original language of humanity, prior even to Hebrew. This 'Gothicism' had a double dimension: on one level it served Swedish national mythology, supporting the empire's cultural pretensions; on another level it connected to Bureus's runic theosophy, in which the Gothic runes preserved primordial divine knowledge. Åkerman's reading of Johan Nordström's 1924 dissertation on Stiernhielm identifies him as the crucial intellectual link between Burean theosophy and the later Hermetic culture of the Swedish Enlightenment.\n\nThe path from Stiernhielm to Swedenborg—traced by Åkerman through the vocabulary of divine influx, the nature of light, and the structure of the human soul—represents the longest genealogical arc of Baltic Rosicrucianism, running from the 1614 manifestoes to the theological visions of the eighteenth century.",
        "scholars": ["Susanna Åkerman", "Johan Nordström", "Gunnar Eriksson"],
        "key_works": [],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), pp. 14, 236–240. Nordström, Johan. *Moralisten Stiernhielm* (Uppsala, 1924).",
        "scholarly_debates": "The relationship between Stiernhielm's Gothicism and his Hermetism; whether his transmission of Burean theosophy was conscious or structural; his place in the genealogy of Swedish Enlightenment thought.",
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 4,
        "image_url": "",
        "genealogical_position": "Bureus transmission chain; Swedish Baroque Hermetism; Swedenborg precursor",
        "influenced_by_figures": [101],
        "influenced_figures": [7]
    },
    {
        "id": 109,
        "name": "Susanna Åkerman",
        "slug": "susanna-akerman",
        "birth_year": 1952,
        "death_year": None,
        "nationality": "Swedish",
        "location": "Stockholm",
        "lat": 59.3293,
        "lng": 18.0686,
        "primary_discipline": "History of Esotericism / Rosicrucian Studies / Nordic Intellectual History",
        "summary": "Susanna Åkerman (b. 1952) is a Swedish historian of ideas whose *Rose Cross over the Baltic: The Spread of Rosicrucianism in Northern Europe* (Brill, 1998) is the definitive study of Rosicrucian transmission through Scandinavian and Baltic networks. Drawing on Swedish, Danish, and German archives, she displaces the southern-German bias of Frances Yates's foundational study, demonstrating that the millenarian and theosophical dimensions of the movement had a distinctive and historically important development in the North. Her work integrates manuscript history, political history, and intellectual biography in exemplary fashion.",
        "essay": "Susanna Åkerman (b. 1952) is among the most important historians of Northern European esotericism working in the post-Yates generation, and her methodological contributions are as significant as her substantive findings. Her career represents an ongoing project to write the history of the Rosicrucian movement from primary archival sources rather than secondary interpretation, and to correct the geographical distortions that had privileged southern Germany and England at the expense of the Baltic and Nordic worlds.\n\n*Rose Cross over the Baltic: The Spread of Rosicrucianism in Northern Europe* (Brill, 1998) is her central achievement. The work's five chapters trace the reception of Rosicrucian ideas from Sweden (Johannes Bureus, Georg Stiernhielm), through the origins of the manifestoes in Württemberg (Simon Studion, Helisaeus Roeslin, Johann Valentin Andreae), through the political turbulence of the 1620s (the 'Lion of the North' typology, the Danish-Dutch networks), and into the astronomy and natural philosophy of the later Rosicrucian tradition (Julius Sperber, the *Oculus Sidereus* group at Danzig). The conclusion traces the path from Bureus's Adulrunic theosophy through Georg Stiernhielm to Swedenborg.\n\nÅkerman's methodological stance is notable for three features. First, she foregrounds *millenarianism*—the expectation of imminent world transformation—as the organizing category of Rosicrucian culture, rather than the occult revival (Yates) or the early scientific movement (McGuire). This allows her to connect the religious, political, and natural-philosophical dimensions of the movement without reducing any to a mere epiphenomenon of the others.\n\nSecond, she takes *transmission networks* seriously as objects of historical analysis: the Hanseatic trade routes, the court patronage networks, the manuscript circulation systems, and the print networks are all traced as specific historical channels rather than vague 'influences.' Her reconstruction of the Danish-Dutch network for Rosicrucian material between 1622 and 1625 is a model of this approach.\n\nThird, she insists on the *northern perspective* as both a historiographical corrective and a substantive claim: the Baltic reception of Rosicrucianism was not merely derivative but generative, producing distinctively new syntheses (Adulrunic theosophy, Gnostic astronomical theosophy, the Lion of the North typology) that fed back into the broader movement.\n\nÅkerman's work builds on and critiques both Frances Yates's *Rosicrucian Enlightenment* (1972) and Brian Vickers's methodological objections to Yates. She accepts Vickers's demand for documentary rigour but rejects his dismissal of the movement's significance, demonstrating through careful archival work that Rosicrucianism had real intellectual substance and real political effects in the Baltic world.",
        "scholars": ["Frances Yates", "Brian Vickers", "Carlos Gilly"],
        "key_works": [],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998). Åkerman, Susanna. *Queen Christina of Sweden and Her Circle* (Brill, 1991).",
        "scholarly_debates": "Åkerman's relationship to the Yates thesis; her position on millenarianism as the organizing category; her treatment of Swedenborg as culmination of Baltic Rosicrucian tradition.",
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 12,
        "image_url": "",
        "genealogical_position": "Post-Yates Rosicrucian scholarship; Nordic intellectual history",
        "influenced_by_figures": [51],
        "influenced_figures": []
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# NEW CONCEPTS (IDs 75–80)
# ─────────────────────────────────────────────────────────────────────────────
NEW_CONCEPTS = [
    {
        "id": 75,
        "name": "Adulruna",
        "slug": "adulruna",
        "category": "Esoteric System / Nordic Theosophy",
        "summary": "Adulruna is the theosophical-runic system developed by Johannes Bureus (1568–1652) in which the sixteen Gothic runes are analysed into component shapes, each carrying numerical, alphabetical, and divine-name equivalences derived from Hebrew Kabbalah and Christian Hermetism. Bureus regarded the Adulrunic combinations as encoding the primordial language of creation, antedating Hebrew, and uniquely preserved in Scandinavian runic monuments. The system represents the most sustained synthesis of Norse antiquarianism and Kabbalistic esotericism in European intellectual history.",
        "essay": "The word *Adulruna* appears to combine the Swedish *adel* (noble) with *runa* (rune, secret), signifying something like 'noble secret' or 'the noble rune'—a name that encodes Bureus's conviction that the runic tradition preserved knowledge of supreme dignity and antiquity.\n\nThe system works by decomposing each of the sixteen Younger Futhark runes into simpler graphic elements (*stavar*), which Bureus aligns with the consonants of the Hebrew alphabet. Each component shape carries a numerical value derived from both its Hebrew equivalent and its geometric properties. When combined according to systematic rules, these components generate the names of angels, the divine attributes of Kabbalistic tradition, and the structural principles of the cosmos.\n\nThe intellectual genealogy of Adulruna runs through several streams. From Agrippa's *Occult Philosophy* (1531), Bureus inherited the association of letters with numbers, angelic names, and cosmological principles. From the work of Johannes Reuchlin on Christian Kabbalah, he took the method of letter-combination as a path to divine names. From Johannes Trithemius's *Steganographia* he took the angelic communication system. Into these he integrated the specifically Norse material: the sixteen-rune Younger Futhark, Swedish runestone inscriptions, and the mythological associations of individual runes preserved in the Icelandic *Eddas*.\n\nÅkerman's analysis demonstrates that Bureus encountered the Rosicrucian manifestoes through precisely these Hermetic-Kabbalistic frameworks. He read the *Fama Fraternitatis* as confirming what the Adulruna had revealed: that a primordial divine knowledge existed in hidden form in the world, awaiting recovery by those with the necessary preparation. The Rosicrucian 'temple of the Holy Spirit' resonated with his own Temple at Damar project, in which specific runic inscriptions at Swedish burial sites were identified as Adulrunic encodings of sacred geometry.\n\nThe Adulruna project represents one of the earliest and most sophisticated attempts to integrate indigenous Northern European symbolic traditions with the mainstream of Kabbalistic Hermetism. Its significance for the history of ideas lies both in its intrinsic intellectual ambition and in its demonstration that the 'universal reform' promised by Rosicrucianism could be received and reformulated in genuinely local terms.",
        "operational_meaning": "In practice: the system involves decomposing runic characters into component shapes, assigning them Hebrew letter equivalences, and combining them according to Kabbalistic number-letter rules to generate divine names and angelic invocations.",
        "philosophical_meaning": "Philosophically: the Adulruna is premised on the claim that primordial divine knowledge was encoded in the runic tradition and that this Nordic heritage is continuous with—and perhaps prior to—the Hebrew Kabbalistic tradition.",
        "spiritual_meaning": "Spiritually: mastery of Adulrunic combinations opens access to angelic realms and enables the practitioner to participate in the coming universal reform promised by Rosicrucian millenarianism.",
        "transmission_genealogy": "Agrippa → Reuchlin → Bureus (synthesis with Norse runic tradition) → Stiernhielm → Swedish Hermetism → Swedenborg precursors",
        "emblem_count": 0,
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 6,
        "related_concepts": [7, 29, 36],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 1, pp. 29–67.",
        "image_url": "",
        "emblem_links": []
    },
    {
        "id": 76,
        "name": "Millenarianism (Rosicrucian)",
        "slug": "millenarianism-rosicrucian",
        "category": "Eschatology / Historical Philosophy",
        "summary": "Rosicrucian millenarianism is the expectation, central to the early Rosicrucian manifestoes and their reception, that the present age was approaching its end and a universal transformation—spiritual, political, and intellectual—was imminent. Drawing on Protestant apocalypticism, Paracelsian prophecy (especially the 'Elias Artista' tradition), and astrological calculation, Rosicrucian millenarians identified specific signs—celestial events, political crises, the circulation of new knowledge—as harbingers of the coming universal reform. Åkerman argues that millenarianism, rather than occult philosophy or proto-science, is the organizing category for understanding the Rosicrucian movement.",
        "essay": "Rosicrucian millenarianism is distinctive in combining three strands of expectation that elsewhere remained separate: Protestant eschatology (the expectation of Christ's return and the millennium of Revelation 20), Paracelsian natural-philosophical prophecy (the coming of an 'Elias Artista' who would reform medicine and natural knowledge), and astrological periodisation (the calculation of world-historical epochs from planetary conjunctions).\n\nThe Protestant eschatological stream contributed the urgency of expectation—the conviction that present history was the last age and that global transformation was not merely possible but scripturally guaranteed. The Paracelsian stream contributed specific content: the reform would be led by an adept physician-philosopher who would reveal hidden natural knowledge. The astrological stream contributed timing: the conjunction of Saturn and Jupiter in 1603–04, observed by Johannes Kepler among others, was widely interpreted as marking the transition to a new planetary epoch.\n\nSimon Studion's *Naometria* (1604) represents the most elaborate synthesis of these three streams before the manifestoes. His numerological analysis of the Temple of Solomon, combined with Roeslin's celestial calculations and the Paracelsian prophecy tradition, produced a timetable for the coming transformation that gave the Rosicrucian project its sense of world-historical timeliness.\n\nThe *Fama Fraternitatis* (1614) deploys millenarian expectation with remarkable literary sophistication: the story of Christian Rosencreutz's travels, his founding of the fraternity, his death and entombment, and the discovery of his incorruptible tomb 120 years later is structured as a salvation narrative. The fraternity's call for all 'learned men' to join them is explicitly framed as preparation for the 'morning redness' (*Morgenröte*) of a new age.\n\nÅkerman's key contribution is to show that millenarianism explains the movement's geographic spread better than either the occult-revival thesis (Yates) or the proto-science thesis. The Baltic networks through which Rosicrucian ideas spread were already structured by millenarian expectations—the 'Lion of the North' prophecy, the Paracelsian tradition in Scandinavia, the apocalyptic readings of the Thirty Years' War—and the manifestoes resonated precisely because they appeared to confirm what recipients already anticipated.\n\nThe millenarian dimension also explains the rapid disillusionment that followed: when the universal reform failed to materialise, when the Thirty Years' War destroyed rather than renewed, the Rosicrucian movement could not maintain its momentum, and its energies dispersed into the various streams—Pietism, natural philosophy, court alchemy, political mysticism—that had been its tributaries.",
        "operational_meaning": "Historically: the set of practices (astrological calculation, prophetic manuscript reading, ceremonial preparation) through which millenarians prepared for and participated in the expected universal transformation.",
        "philosophical_meaning": "The conviction that history is structured by divinely ordained epochs with determinate endings; that present suffering and disorder are birth-pangs of a new age; that human intellectual and spiritual effort can align with the coming transformation.",
        "spiritual_meaning": "The coming age is not merely political or intellectual but spiritual: a genuinely new relationship between humanity and divinity, expressed as universal illumination, the perfection of knowledge, and the healing of all disease.",
        "transmission_genealogy": "Joachim of Fiore → Protestant apocalypticism → Paracelsus (Elias Artista) → Studion/Roeslin → Rosicrucian manifestoes → Bureus (Nordic) / Sperber (Gnostic) / Eglinus (Paracelsian)",
        "emblem_count": 0,
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 8,
        "related_concepts": [7, 29, 37],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Introduction and Chapters 1–4. Barnes, Robin. *Prophecy and Gnosis* (Stanford, 1988). Lehmann, Hartmut. *Das Zeitalter des Absolutismus* (Stuttgart, 1980).",
        "image_url": "",
        "emblem_links": []
    },
    {
        "id": 77,
        "name": "Leo Septentrionalis (Lion of the North)",
        "slug": "leo-septentrionalis",
        "category": "Prophetic Symbol / Political Eschatology",
        "summary": "The *Leo Septentrionalis* or 'Lion of the North' was a prophetic symbol predicting the advent of a great northern king who would cross the Baltic, drive south into Germany, defeat the Catholic powers, reform the church, and usher in a new age. Circulating through manuscript and print from the late sixteenth century onwards, the symbol drew on Paul Grebner's prophetic visions, Paracelsian millenarian prophecy, and Rosicrucian eschatology. Åkerman traces its genealogy and application, showing how it was deployed to frame Gustavus Adolphus of Sweden's entry into the Thirty Years' War in 1630.",
        "essay": "The *Leo Septentrionalis*—the Lion of the North—is one of the most politically consequential prophetic symbols of the seventeenth century, bridging esoteric millenarianism and dynastic politics. Its genealogy, carefully reconstructed by Åkerman, reveals the complex way in which esoteric traditions were mobilised in the service of political action during the Thirty Years' War.\n\nThe symbol's core elements are: a great lion (*Leo*) arising from a forest in the North (*ex Silva*), crossing the Baltic and advancing southward, defeating the 'eagle' (the Habsburgs) and the 'bear' (other powers), reforming the church, and dying in the act of triumph. This narrative template appears in Paul Grebner's prophetic manuscripts (c. 1570s–1604), in Helisaeus Roeslin's astrological calculations, in Paracelsian prophetic pamphlets, and in Rosicrucian millenarian texts from the 1614–1625 period.\n\nThe symbol's application to specific rulers was contested and shifting. Åkerman demonstrates that it was first applied in Denmark to the Danish king Christian IV (who briefly entered the war in 1625–29) before being transferred to Gustavus Adolphus of Sweden when he entered in 1630. This transferability is itself significant: the symbol was powerful enough to attract multiple claimants, suggesting that it expressed genuine widespread expectations rather than mere dynastic propaganda.\n\nThe historiographical debate about the symbol's political efficacy—the Nordström/Ahnlund controversy—is central to Åkerman's methodology. Johan Nordström (1934) argued that Paracelsian-Hermetic prophecy was a genuine political force, preparing the Swedish public for war. Nils Ahnlund (1939) countered that it had negligible influence on actual decisions. Åkerman's nuanced position distinguishes between direct causation (which cannot be demonstrated) and cultural atmosphere: the *Leo Septentrionalis* tradition created a symbolic-emotional context within which military action could be understood as divinely sanctioned, and this cultural preparation—even if it didn't determine decisions—shaped how those decisions were received and interpreted.\n\nThe symbol's Rosicrucian connection comes through the 'Gemstones of Ariel' tradition, in which angelic voices (the angel *ARIEL*) announce the coming of the reforming lion. This angelic endorsement locates the Leo prophecy within the specifically Rosicrucian vocabulary of celestial confirmation and divine agency—connecting political millenarianism to theosophical pneumatology.",
        "operational_meaning": "Politically: the symbol functioned as a template for interpreting military and political events, giving them eschatological significance and potential popular-mobilisation power.",
        "philosophical_meaning": "Philosophically: the Leo symbol embodies the Rosicrucian conviction that political transformation and spiritual transformation were aspects of a single divine process—that the right king, at the right moment, could inaugurate genuine universal reform.",
        "spiritual_meaning": "The Lion represents divine wrath and mercy combined: a purifying force that destroys corruption and clears the way for renewal, analogous to the nigredo phase in alchemical transformation.",
        "transmission_genealogy": "Paracelsian prophecy (Elias Artista) → Paul Grebner → Roesicrucian millenarian networks → Baltic pamphlet culture → 'Leo ex Silva' print tradition → Application to Gustavus Adolphus (1630)",
        "emblem_count": 0,
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 7,
        "related_concepts": [76, 29, 7],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 3, pp. 125–172. Nordström, Johan. 'Lejonet från Norden,' *De Yverbornes Ö* (Uppsala, 1934).",
        "image_url": "",
        "emblem_links": []
    },
    {
        "id": 78,
        "name": "Baltic Transmission Networks",
        "slug": "baltic-transmission-networks",
        "category": "Knowledge Transmission / Historical Geography",
        "summary": "The Baltic transmission networks were the specific channels—Hanseatic trade routes, court patronage systems, diplomatic missions, manuscript circulation systems, and itinerant scholars—through which Rosicrucian and Hermetic ideas spread across Northern Europe between approximately 1580 and 1650. Åkerman's archival reconstruction of these networks challenges vague claims of 'influence' by identifying precisely which texts travelled through which channels to reach which recipients. The networks connected Württemberg and Hesse-Kassel to Hamburg, Lübeck, Danzig, Riga, Copenhagen, Stockholm, and Amsterdam.",
        "essay": "The Baltic transmission networks are Åkerman's primary analytical tool for understanding how Rosicrucian ideas spread—and why they spread differently in the North than in the South. Rather than treating influence as a vague cultural diffusion, she reconstructs specific networks of personal connection, institutional patronage, and material text circulation.\n\nThe Hanseatic trade system provided the infrastructure. The cities of the Hansa—Hamburg, Lübeck, Wismar, Stralsund, Danzig, Riga, Reval (Tallinn)—were connected by regular shipping and merchant networks that carried not only goods but books, manuscripts, and letters. Learned merchants and itinerant scholars used the same routes. The printing centres of Hamburg and Danzig were closely connected to both the Hesse-Kassel Rosicrucian printing network and the Swedish and Danish courts.\n\nCourt patronage systems provided a second channel. The Reformed Protestant courts of the Baltic region—the Landgrave of Hesse-Kassel, the Elector Palatine, the Danish king, the Swedish king, the dukes of Holstein—were connected by diplomatic relationships, dynastic marriages, and shared Protestant political concerns. Many of the figures in Åkerman's study moved between these courts as physicians, tutors, chaplains, or officials, carrying intellectual networks with them.\n\nThe Danish-Dutch network documented by Åkerman for the years 1622–1625 is the most precisely reconstructed. It passed Rosicrucian materials—including works by Roeslin, Grebner prophecies, and Leo pamphlets—through a chain that included figures in Hesse-Kassel, Hamburg, Amsterdam, Copenhagen, and eventually Stockholm. Each node in the chain annotated, translated, or amplified the materials before passing them on.\n\nThe Livonian connection—the Baltic provinces (modern Latvia and Estonia) under Swedish and Polish rule—provided a third dimension. The Religious Orders in Livonia, discussed in Chapter 4 of *Rose Cross over the Baltic*, served as transmission nodes between Polish-Lithuanian cultural centres (Cracow, Wilno) and the Baltic coast, ensuring that Central European esoteric currents reached the furthest north-eastern extension of the network.\n\nThe significance of the network concept for historiography is substantial: it allows Åkerman to make precise causal claims about transmission that the vague language of 'influence' or 'diffusion' does not. It also reveals the importance of geographically peripheral figures—the Danzig astronomers, the Livonian playwrights—who appear at crucial nodes but have been largely ignored in scholarship focused on the great centres.",
        "operational_meaning": "Historically: the specific routes and institutions through which texts, ideas, and people moved—Hanseatic shipping, court patronage, diplomatic missions, printer-publisher networks.",
        "philosophical_meaning": "The network concept implies that ideas are not free-floating but materially embedded in specific social and economic structures; the same ideas travel differently through different networks and arrive transformed.",
        "spiritual_meaning": "For participants: the networks were channels of providential communication—the fact that Rosicrucian ideas spread so rapidly and so far confirmed for believers that a divine hand guided the dissemination of the fraternity's message.",
        "transmission_genealogy": "Hesse-Kassel printing → Hamburg/Lübeck trade → Danzig → Riga/Livonia → Stockholm / Copenhagen → Court networks",
        "emblem_count": 0,
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 9,
        "related_concepts": [7, 29, 37],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapters 3–4, pp. 125–195. Lindberg, Bo. *Europa och latinet* (Stockholm, 1993).",
        "image_url": "",
        "emblem_links": []
    },
    {
        "id": 79,
        "name": "Runic Theosophy",
        "slug": "runic-theosophy",
        "category": "Nordic Esotericism / Linguistic Mysticism",
        "summary": "Runic theosophy is the intellectual tradition, centred on Johannes Bureus but extending through Georg Stiernhielm and later Nordic Hermetism, in which the Norse runic alphabets are interpreted as sacred scripts encoding divine knowledge—specifically as Nordic equivalents of the Hebrew Kabbalistic alphabet. The tradition held that the runes preserved primordial wisdom in the monuments and manuscripts of Scandinavia, and that their proper interpretation would yield access to angelic realms, universal reform, and the hidden structure of creation. It represents the most sustained indigenous European esoteric tradition developed in conscious dialogue with Kabbalistic Hermetism.",
        "essay": "Runic theosophy emerges from the confluence of two streams: the sixteenth-century revival of interest in Norse antiquities (particularly runic inscriptions) that accompanied Swedish national consciousness, and the Kabbalistic Hermetism transmitted through Agrippa, Reuchlin, and the broader European learned tradition.\n\nThe runes—the writing systems of the ancient Germanic peoples, preserved in thousands of Scandinavian inscriptions on stone and metal—had been objects of antiquarian interest since the fifteenth century. Renaissance humanists treated them as evidence of Northern antiquity comparable to Greek and Latin monuments. Bureus transformed this antiquarian interest into an esoteric project: he argued that the runes were not merely an indigenous alphabet but a divinely transmitted script in which universal knowledge was encoded, analogous to but not derivative of the Hebrew alphabet of Kabbalistic tradition.\n\nThe key move in runic theosophy is the *comparison without subordination*: Bureus did not argue that the runes derived from Hebrew but that they were parallel and equally primordial expressions of the same divine knowledge. This gave Swedish esotericism a basis for claiming authentic indigenous participation in the universal Hermetic project without requiring derivative status.\n\nThe intellectual machinery was elaborate. Each rune was decomposed into component strokes (*stavar*), each stroke was assigned a Hebrew letter equivalent, and these assignments generated a system of correspondences connecting runic shapes, Hebrew letters, numbers, angelic names, and divine attributes. The resulting system—the *Adulruna*—was Bureus's life work.\n\nStiernhielm's contribution was to integrate runic theosophy with comparative philology: his argument that Gothic was the mother of languages placed Swedish cultural identity at the origin of human speech, reinforcing the theosophical claim that Nordic culture preserved primordial wisdom. This fusion of linguistic nationalism and Hermetic esotericism became characteristic of northern intellectual culture in the seventeenth and eighteenth centuries.\n\nThe tradition's lasting significance is its demonstration that indigenous symbolic traditions could be integrated into the mainstream of European Hermetism without simply being assimilated to it—a model that would influence later European esoteric revivals from Romanticism to the twentieth century.",
        "operational_meaning": "In practice: the study and interpretation of runic inscriptions through Kabbalistic letter-number correspondences; the generation of angelic names through runic combination; the reading of Norse monuments as theosophical texts.",
        "philosophical_meaning": "The claim that universal divine knowledge was preserved in indigenous Nordic symbolic traditions, parallel to and not derivative of the Hebrew Kabbalistic tradition.",
        "spiritual_meaning": "Access to the divine through the native symbolic heritage; the runes as a path to angelic communication and cosmic knowledge available to northerners without requiring Oriental (Hebrew, Arabic, Greek) transmission.",
        "transmission_genealogy": "Norse antiquarianism (15th–16th c.) + Kabbalistic Hermetism (Agrippa, Reuchlin) → Bureus (Adulruna synthesis) → Stiernhielm → Swedish Baroque Hermetism → Post-Swedenborgian tradition",
        "emblem_count": 0,
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 5,
        "related_concepts": [75, 36, 29],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 1. Also Lindqvist, Ivar. *Galdrar* (Göteborg, 1923).",
        "image_url": "",
        "emblem_links": []
    },
    {
        "id": 80,
        "name": "Elias Artista (Paracelsian Prophecy)",
        "slug": "elias-artista",
        "category": "Prophetic Figure / Paracelsian Eschatology",
        "summary": "The *Elias Artista* ('Elias the Artist/Craftsman') was a Paracelsian prophetic figure—a coming philosopher-physician who would reveal the hidden secrets of nature, reform medicine, and inaugurate a new era of human knowledge and healing. Derived from the biblical expectation of Elijah's return before the Last Day, Paracelsus and his followers elaborated the figure into a prophet of natural philosophy whose revelations would transform the world. The Elias Artista tradition was a crucial component of the millenarian framework in which the Rosicrucian manifestoes were received and interpreted.",
        "essay": "The *Elias Artista* tradition originates in Paracelsus's prophetic writings, particularly his *Astronomia Magna* (c. 1537), where he speaks of an imminent reformer of natural philosophy who will reveal what has been hidden in nature. The name 'Elias' combines the biblical Elijah—expected to return as a precursor to the messianic age—with *artista*, meaning a craftsman or practitioner of an art, specifically here natural philosophy and medicine.\n\nParacelsus was deliberately ambiguous about whether this figure was himself, a future disciple, or a coming third age of the Holy Spirit (in the tradition of Joachim of Fiore). His followers inherited this ambiguity and developed it in different directions. Some (the 'medical Paracelsians') interpreted the Artista primarily as a reformer of medicine who would reveal the true therapeutic use of chemical preparations. Others (the 'philosophical Paracelsians') interpreted him as a revealer of the true structure of nature—a philosopher who would complete the work of natural philosophy that Aristotle and Galen had left incomplete.\n\nRaphael Eglinus's *Disquisitio de Helia Artista* (1606) represents the most sophisticated pre-Rosicrucian treatment of the tradition. Eglinus carefully distinguished the biblical Elijah from the prophesied Artista, argued that the latter was a natural figure operating through divinely granted knowledge rather than supernatural miraculous power, and connected the tradition to the Paracelsian reform of medicine. His argument was available for the authors of the *Fama Fraternitatis* when they framed Christian Rosencreutz's journey as precisely this kind of universal natural-philosophical revelation.\n\nIn the *Confessio Fraternitatis* (1615), the Elias Artista is explicitly mentioned: the fraternity announces that while they do not claim to *be* the Elias, the reformation they offer anticipates and prepares for his coming. This careful hedging maintained the eschatological framing while avoiding the specific messianic claim.\n\nThe Elias Artista tradition also shaped the Baltic reception of Rosicrucianism. Bureus's Adulrunic project can be read as his own version of the Artista's revelation: the runic secrets he was uncovering were precisely the kind of universal natural-philosophical knowledge that the Paracelsian prophecy had promised. The tradition thus served as a template into which very different esoteric projects could be inserted.",
        "operational_meaning": "Prophetically: a specific figure expected to arrive and transform natural philosophy and medicine through revelation of hidden knowledge; functioned as an eschatological expectation shaping how new knowledge was received.",
        "philosophical_meaning": "The conviction that natural knowledge was not merely accumulated by human effort but periodically revealed by divinely appointed figures; that the coming revelation would be qualitatively different from and superior to all previous natural philosophy.",
        "spiritual_meaning": "The Artista represents the integration of prophetic grace with practical knowledge—the healer-prophet who demonstrates that divine revelation and empirical investigation are not opposites but aspects of a single divine gift.",
        "transmission_genealogy": "Joachim of Fiore (three ages) → Paracelsus (Elias Artista prophecy) → Paracelsian followers → Eglinus (*Disquisitio*, 1606) → *Confessio Fraternitatis* (1615) → Rosicrucian millenarianism broadly",
        "emblem_count": 0,
        "markdown_sources_found": ["Åkerman 1998"],
        "source_citations_count": 6,
        "related_concepts": [76, 4, 29],
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 4, pp. 173–178. Pagel, Walter. *Paracelsus* (Basel, 1958).",
        "image_url": "",
        "emblem_links": []
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# NEW TEXTS (IDs 93–99)
# ─────────────────────────────────────────────────────────────────────────────
NEW_TEXTS = [
    {
        "id": 93,
        "title": "Adulruna Rediviva",
        "slug": "adulruna-rediviva",
        "year": 1647,
        "language": "Swedish / Latin",
        "location": "Stockholm",
        "lat": 59.3293,
        "lng": 18.0686,
        "summary": "Johannes Bureus's *Adulruna Rediviva* (composed over several decades, final version c. 1647) is the central text of Adulrunic theosophy—a comprehensive system combining Norse runic lore with Kabbalistic Hermetism, Christian mysticism, and Rosicrucian millenarianism. Never printed in Bureus's lifetime, it circulated in manuscript at the Swedish court and provided the intellectual framework through which Northern European Rosicrucianism developed its most distinctive local character.",
        "essay": "*Adulruna Rediviva* ('The Noble Rune Revived') is Johannes Bureus's magnum opus, the product of a lifetime's research into Swedish runic monuments and their Kabbalistic-Hermetic significance. The work exists in multiple manuscript versions in the Uppsala University Library and the Swedish Royal Library, reflecting decades of revision and elaboration between approximately 1611 and 1647.\n\nThe text opens with an account of Bureus's discovery of the Adulrunic system—his realisation that the sixteen Younger Futhark runes could be decomposed into component shapes (*stavar*) that carried Hebrew letter equivalences. This discovery is presented as a revelation rather than a scholarly finding: Bureus experienced it as a gift of divine insight, confirming the special status of the Norse tradition as a repository of primordial knowledge.\n\nThe bulk of the work develops the combinatorial system: detailed tables of runic decomposition, Hebrew equivalences, numerical values, angelic names generated by combining Adulrunic components, and the cosmological principles each combination encodes. The architecture is recognisably Kabbalistic—the structure of the *Sefirot*, the practice of *Temurah* (letter permutation), the generation of divine names—but all rendered in Norse runic terms.\n\nThe work's Rosicrucian dimension is explicit. Bureus interprets the *Fama Fraternitatis*'s promise of universal reform as confirmation of what the Adulruna had revealed: a new age was approaching in which hidden knowledge would be made manifest. His analysis of the runic inscription at his proposed 'Temple at Damar' connects the physical landscape of Sweden to the Rosicrucian project of universal illumination.\n\nThe text's manuscript character is significant: it was not written for publication but for circulation within an initiated court circle, reflecting the Rosicrucian conviction that genuine wisdom must be transmitted personally rather than broadcast publicly. This esotericism was both a rhetorical stance and a practical necessity in a court where religious and political sensitivities made public millenarianism dangerous.",
        "concepts": [75, 79, 76, 7],
        "historical_context": "Composed during the reign of Gustavus Adolphus and Queen Christina, the period of Swedish imperial expansion and intense cultural production. The court context shaped both the work's patronage and its millenarian-political framing.",
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 1. Eriksson, Gunnar. *The Atlantic Vision: Olaus Rudbeck and Baroque Science* (Canton MA, 1994).",
        "transmission_history": "Manuscript at Uppsala University Library and Swedish Royal Library. Influenced Georg Stiernhielm directly. Long-term influence traceable through Swedish Hermetic culture to Swedenborg.",
        "image_url": ""
    },
    {
        "id": 94,
        "title": "Naometria",
        "slug": "naometria",
        "year": 1604,
        "language": "Latin",
        "location": "Marbach am Neckar",
        "lat": 48.9369,
        "lng": 9.2581,
        "summary": "Simon Studion's *Naometria* (1604) is an enormous unpublished Latin manuscript combining numerological analysis of the Temple of Solomon with astrological prediction, Paracelsian prophecy, and Protestant eschatology. One of the most important pre-Rosicrucian documents in European esoteric history, it elaborates the millenarian framework—including the figure of 'Elias Artista' and the expectation of universal reform—that would be deployed in the Rosicrucian manifestoes of 1614–15. It circulated in manuscript among the Württemberg-Kassel esoteric circle that included figures close to Johann Valentin Andreae.",
        "essay": "*Naometria* ('temple-measurement') takes its title from the practice of sacred geometry applied to the biblical Temple of Solomon—the conviction that the temple's dimensions, proportions, and symbolic arrangements encoded universal knowledge about creation, history, and eschatology. Studion spent decades composing this encyclopedic work, which runs to thousands of pages in the surviving manuscript at the Württemberg State Library in Stuttgart.\n\nThe text's central calculation concerns the timing of the universal reform: by combining numerological analysis of the temple's dimensions with astrological calculations based on Helisaeus Roeslin's 'celestial wheel' and the conjunction of Saturn and Jupiter in 1604, Studion argued that the present moment was the appointed time for the beginning of the final age.\n\nThe prophetic tradition that Studion drew on was Paracelsian: the figure of *Elias Artista* appears as the coming reformer who will reveal the hidden secrets of nature encoded in the temple's measurements. This figure is not yet identified with the Rosicrucian Christian Rosencreutz, but the structural parallels are close enough to confirm that the *Naometria* belongs to the same prophetic-intellectual environment that produced the manifestoes.\n\nCarlos Gilly's archival research has confirmed that the *Naometria* circulated in the same Württemberg-Kassel network that includes Tobias Hess and Johann Valentin Andreae. The specific numerological and prophetic vocabulary of the *Confessio Fraternitatis* (1615) shows clear echoes of Studion's framework, though the precise mechanism of influence—whether Andreae read *Naometria* directly or absorbed its ideas through the shared network—remains debated.\n\nThe *Naometria*'s significance lies in demonstrating that Rosicrucianism did not appear ex nihilo in 1614 but emerged from a rich substrate of millenarian expectation that had been building in the German Protestant intelligentsia for decades. Studion's death in 1605, before the manifestoes appeared, means that he belongs to the generative prehistory of the movement.",
        "concepts": [76, 80, 7, 29],
        "historical_context": "Württemberg, 1604: year of Saturn-Jupiter conjunction, interpreted as eschatological sign. The same region and decade that would produce the Rosicrucian manifestoes a decade later.",
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 2, pp. 97–104. Gilly, Carlos. 'Iter Rosicrucianum,' in *Das Erbe des Christian Rosenkreuz* (Amsterdam, 1988).",
        "transmission_history": "Manuscript, Württemberg State Library Stuttgart. Never printed. Circulated in the Württemberg-Kassel esoteric circle. Documented influence on *Confessio Fraternitatis* vocabulary.",
        "image_url": ""
    },
    {
        "id": 95,
        "title": "Echo der von Gott hocherleuchteten Fraternität",
        "slug": "echo-der-fraternitaet",
        "year": 1615,
        "language": "German",
        "location": "Danzig / Anhalt",
        "lat": 54.3520,
        "lng": 18.6466,
        "summary": "Julius Sperber's *Echo der von Gott hocherleuchteten Fraternität des löblichen Ordens R.C.* (1615) was one of the earliest and most theosophically sophisticated responses to the Rosicrucian *Confessio Fraternitatis*. Structured as an 'echo' that amplifies the manifesto's call, it develops the movement's Gnostic-theosophical dimension: the emphasis on interior illumination, cosmological speculation about the true structure of the heavens, and the role of luminescent phenomena as material signs of the divine influx. Åkerman identifies Sperber as the representative of a 'Gnostic wing' of Rosicrucianism distinct from the more reformist Hesse-Kassel tradition.",
        "essay": "The *Echo* ('Echo of the God-Illuminated Fraternity of the Praiseworthy Order R.C.') by Julius Sperber represents the reception of the *Confessio Fraternitatis* through a distinctly theosophical-Gnostic lens. Where other early respondents to the manifestoes focused on practical reform (of medicine, natural philosophy, church organisation), Sperber's *Echo* foregrounds the *interior transformation* of the individual as the proper response to the fraternity's call.\n\nSperber structures his text as a genuine echo: each major theme of the *Confessio* is amplified and developed in a theosophical direction. The manifesto's references to 'divine illumination' become, in Sperber's hands, a fully elaborated account of interior transformation through the reception of divine light—a process he describes in terms that blend Kabbalistic emanation theory, Paracelsian theories of the *Licht der Natur*, and the pneumatological vocabulary of German mysticism.\n\nThe astronomical dimension of the *Echo* is particularly significant for Åkerman's analysis. Sperber engages directly with the post-Tychonic debate about the structure of the cosmos, arguing that the Tychonic model—heliocentric planets around a geocentric earth—was spiritually superior to both pure Ptolemaic geocentrism and Copernican heliocentrism because it preserved the spiritual significance of the earth as the centre of human redemptive history while acknowledging the mathematical reality of planetary motion. This 'theosophical astronomy' connects Sperber to the *Oculus Sidereus* group at Danzig.\n\nSperber's discussion of 'Phosphoric Lights'—luminescent phenomena in nature including glow-worms, foxfire (bioluminescent fungi), will-o'-the-wisps, and phosphorescent minerals—as signs of the spirit's presence in matter represents one of the most distinctive contributions of his *Echo*. These phenomena, which sit at the intersection of natural philosophy and spiritual symbolism, become for Sperber evidence that matter itself is not spiritually inert but participates in the divine light that the fraternity promises to reveal fully in the coming age.",
        "concepts": [106, 76, 30, 7],
        "historical_context": "Published 1615, the year of the *Confessio Fraternitatis*. Part of the first wave of Rosicrucian responses that defined the movement's intellectual agenda before its fragmentation after 1620.",
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 5, pp. 208–215.",
        "transmission_history": "Published Danzig/Frankfurt 1615. Influenced Baltic theosophical culture. Connected to Sperber's Anhalt court context and the Danzig astronomical-theosophical circle.",
        "image_url": ""
    },
    {
        "id": 96,
        "title": "Stella Hieroglyphica",
        "slug": "stella-hieroglyphica",
        "year": 1618,
        "language": "Latin",
        "location": "Unknown (Southern Germany)",
        "lat": 48.5000,
        "lng": 9.5000,
        "summary": "Philippo à Gabella's *Stella Hieroglyphica* (1618) is an enigmatic Rosicrucian text—sometimes published as an appendix to the *Confessio Fraternitatis*—whose author remains obscure. The work develops the star symbolism of the Rosicrucian tradition (the 'hieroglyphic star' as a symbol of divine knowledge encoded in natural forms) and belongs to the visual-symbolic tradition that connects Rosicrucian emblems to late Renaissance hieroglyphics. Åkerman discusses it as part of the divergent paths of Rosicrucianism in the period 1614–1620.",
        "essay": "The *Stella Hieroglyphica* (Hieroglyphic Star) attributed to 'Philippo à Gabella' is one of the more obscure texts of the early Rosicrucian canon, yet its engagement with the hieroglyphic tradition makes it significant for understanding the visual-philosophical dimension of the movement.\n\nThe pseudonymous author 'Philippo à Gabella' has not been definitively identified, though Carlos Gilly and others have suggested connections to the broader Württemberg-Alsace esoteric circle. The choice of a Latinised Italian-sounding name was not uncommon in early Rosicrucian publication, where pseudonymity served both protective and rhetorical functions.\n\nThe text works with the concept of the 'hieroglyphic star': the star as a natural sign that encodes divine knowledge in visible form. This connects to two Renaissance traditions: the Egyptian hieroglyphic tradition as interpreted through Ficino and later emblem theory (where natural forms were treated as divine writing), and the specifically Rosicrucian 'Monas Hieroglyphica' tradition of John Dee, where a synthetic symbol encoded universal philosophical principles.\n\nThe work's position in the Rosicrucian canon is ambiguous: sometimes published as an appendix to the *Confessio* (as in some 1615–16 editions), it occupies a threshold position between the core manifestoes and the responses they generated. This ambiguity reflects the early movement's loose organisation: there was no central authority to certify or exclude texts, and the boundaries of the canon were determined by readers and publishers rather than by any fraternal authority.\n\nÅkerman's discussion places the *Stella Hieroglyphica* in the context of the 'divergent paths' of Rosicrucianism between 1614 and 1620—the period in which different readers and writers elaborated the manifestoes' themes in different directions, producing a varied family of texts rather than a unified doctrine.",
        "concepts": [7, 76, 36],
        "historical_context": "Published 1618, year the Bohemian War began—a political crisis that interrupted the Rosicrucian movement's public phase and drove it underground or into new forms.",
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 2, pp. 84–88. Gilly, Carlos. *Cimelia Rhodostaurotica* (Amsterdam, 1995).",
        "transmission_history": "Sometimes appended to *Confessio Fraternitatis* editions. Limited manuscript and print distribution.",
        "image_url": ""
    },
    {
        "id": 97,
        "title": "Candelabri Typici in Mosaicorum Tabernaculo",
        "slug": "candelabri-typici",
        "year": 1548,
        "language": "Latin",
        "location": "Paris",
        "lat": 48.8566,
        "lng": 2.3522,
        "summary": "Guillaume Postel's *Candelabri Typici in Mosaicorum Tabernaculo* (c. 1548) is a Kabbalistic meditation on the seven-branched candelabrum (*menorah*) of the biblical Tabernacle, arguing that its structure encodes universal divine knowledge. Åkerman's analysis demonstrates that the candelabrum symbolism and the concept of the *Cain Renatus* ('renewed Cain') in this work fed directly into the Rosicrucian manifestoes' imagery of the fraternity as custodians of revealed divine light—making Postel a crucial genealogical precursor of the Rosicrucian tradition.",
        "essay": "The *Candelabri Typici* ('Types of the Candelabrum in the Mosaic Tabernacle') is Postel's extended meditation on the *menorah* as a symbol of universal knowledge. The seven branches of the biblical lampstand represent for Postel the seven liberal arts transformed and perfected by divine illumination, the seven planets as spheres of divine intelligence, and the seven days of creation as stages of cosmic manifestation. Each lamp burns with the specific light of its corresponding divine attribute.\n\nPostel's treatment of the candelabrum was deeply Kabbalistic: he read the lampstand through the lens of the *Sefirot*, the ten divine attributes of Kabbalistic theology, seeing in its seven branches an accessible image of the divine structure that the more complex Kabbalistic tree of life elaborated in full. His project was ecumenical: the candelabrum belonged to the Hebrew tradition, but its universal significance—the seven as the number of cosmic completion—made it available for Christian theological elaboration without betraying its Jewish origins.\n\nThe *Cain Renatus* argument is the text's most distinctive contribution to the tradition that would flow into Rosicrucianism. Postel argued that Cain—the first murderer, cursed by God, exiled from Eden—was in the process of being 'renewed' (*renatus*) through spiritual transformation. This renewal was not a mere metaphor but a literal eschatological claim: in the coming age, even the most condemned lineage would be redeemed and transformed. The Rosicrucian figure of Christian Rosencreutz, who undergoes a death-and-rebirth narrative in the *Chymical Wedding*, can be read as precisely this kind of *Cain Renatus* figure.\n\nÅkerman's Chapter 4 analysis of 'Postel and the Rosicrucians' traces the specific path by which candelabrum symbolism and *Cain Renatus* theology reached the Rosicrucian writers through the manuscript network of the late sixteenth century. The *Confessio Fraternitatis*'s description of the fraternity as bearers of a divine 'light' that would illuminate all the world draws directly on the candelabrum imagery that Postel had elaborated seven decades earlier.",
        "concepts": [107, 76, 29],
        "historical_context": "Paris 1548: Postel was at the height of his scholarly career, a professor at the Collège Royal, before his later troubles with the Inquisition. The text belongs to his ecumenical-universalist phase.",
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 4, pp. 179–185. Kuntz, Marion Leathers. *Guillaume Postel* (The Hague, 1981).",
        "transmission_history": "Print, Paris 1548. Manuscript elaborations circulated through learned networks. Influence on *Confessio Fraternitatis* traced by Åkerman through shared imagery and vocabulary.",
        "image_url": ""
    },
    {
        "id": 98,
        "title": "Rose Cross over the Baltic",
        "slug": "rose-cross-over-the-baltic",
        "year": 1998,
        "language": "English",
        "location": "Leiden",
        "lat": 52.1601,
        "lng": 4.4970,
        "summary": "Susanna Åkerman's *Rose Cross over the Baltic: The Spread of Rosicrucianism in Northern Europe* (Brill, 1998) is the definitive study of the Rosicrucian movement in Scandinavia and the Baltic world. Displacing the southern-German and English focus of Frances Yates's foundational work, Åkerman draws on Swedish, Danish, German, and Dutch archives to reconstruct the millenarian, political, and theosophical dimensions of Nordic Rosicrucianism. The book studies Johannes Bureus's Adulrunic theosophy, the origins of the manifestoes in Württemberg, the 'Lion of the North' prophecy tradition, Guillaume Postel's influence, and the Gnostic Rosicrucian astronomy of Julius Sperber.",
        "essay": "*Rose Cross over the Baltic* is a work of sustained archival scholarship that transforms the historiography of the Rosicrucian movement by demonstrating that its reception and development in Northern Europe were not peripheral but constitutive of the movement as a whole.\n\nThe book's five chapters move geographically and thematically: Chapter 1 studies Johannes Bureus and the Swedish Adulrunic tradition; Chapter 2 investigates the origins of the manifestoes in the Württemberg esoteric circle (Studion, Roeslin, Andreae, Eglinus); Chapter 3 traces the 'Lion of the North' tradition through the Baltic networks of the 1620s; Chapter 4 examines Guillaume Postel's influence and the Livonian connections; Chapter 5 analyses the Gnostic Rosicrucian astronomy of Sperber and the *Oculus Sidereus* group at Danzig.\n\nÅkerman's methodological innovations are threefold. First, she treats *millenarianism*—the expectation of imminent world transformation—as the organizing category for understanding the movement, replacing the occult-revival thesis (Yates) and the proto-science thesis (McGuire) with a framework that better integrates the religious, political, and natural-philosophical dimensions.\n\nSecond, she insists on *network analysis*: rather than tracing vague 'influences,' she reconstructs specific channels of manuscript and print circulation, personal connection, and institutional patronage through which Rosicrucian ideas moved. Her reconstruction of the Danish-Dutch network of 1622–25 is a model of this approach.\n\nThird, she articulates a *northern perspective*: the Baltic reception of Rosicrucianism was not merely derivative but generative, producing the Adulrunic theosophy (Bureus), the Gnostic astronomical theosophy (Sperber), and the politicised Lion symbolism that fed back into the broader movement and eventually into Swedenborgianism.\n\nThe book builds on Yates while correcting her: Åkerman accepts the importance of Hermetism for early modern intellectual history but rejects the vagueness that Vickers criticised, replacing it with documented archival reconstruction. The result is one of the most important works in the historiography of Western esotericism published in the 1990s.",
        "concepts": [7, 76, 78, 75, 77],
        "historical_context": "Published 1998, during the flourishing of the academic study of Western esotericism following the founding of ESSWE and the establishment of university chairs in the field. The book exemplifies the archival-historical methodology that distinguishes post-Yates scholarship.",
        "scholarship": "The book itself is primary scholarship. It builds on: Yates, Frances. *The Rosicrucian Enlightenment* (London, 1972). Gilly, Carlos. *Cimelia Rhodostaurotica* (Amsterdam, 1995). Montgomery, John W. *Cross and Crucible* (The Hague, 1973).",
        "transmission_history": "Published by Brill (Leiden), a leading academic publisher in the history of religion and esotericism. Received and integrated into the scholarly literature; cited in subsequent work by Hanegraaff, Gilly, Faivre.",
        "image_url": ""
    },
    {
        "id": 99,
        "title": "Disquisitio de Helia Artista",
        "slug": "disquisitio-de-helia-artista",
        "year": 1606,
        "language": "Latin",
        "location": "Marburg",
        "lat": 50.8021,
        "lng": 8.7711,
        "summary": "Raphael Eglinus's *Disquisitio de Helia Artista* (1606) is the most important pre-Rosicrucian treatment of the 'Elias Artista' prophecy tradition—the Paracelsian expectation of a coming philosopher-physician who would reveal hidden natural knowledge and reform medicine. Published eight years before the *Fama Fraternitatis*, it demonstrates that the millenarian framework the manifestoes deployed had substantial intellectual preparation in Paracelsian-Hermetic circles before 1614. Eglinus carefully distinguishes the coming Artista from a miraculous prophet, grounding the figure in the tradition of divinely gifted natural philosophy.",
        "essay": "Raphael Eglinus's *Disquisitio* ('Investigation concerning Elias the Artisan') is one of the more remarkable pre-Rosicrucian documents in the history of esotericism, remarkable precisely because it predates the manifestoes by eight years while deploying much of the vocabulary that the *Fama Fraternitatis* would make famous.\n\nThe text addresses a specific question: what is the nature of the prophesied 'Elias Artista'? Is this figure a supernatural prophet like the biblical Elijah, or a natural philosopher operating through divinely granted insight? Eglinus's answer is systematic and careful: the Artista is a natural philosopher—specifically a Paracelsian physician-philosopher—who operates through a special gift of divine illumination that enables him to perceive what is hidden in nature. This illumination is neither miraculous (in the sense of suspending natural laws) nor merely the product of human effort, but something between: a *gratia gratum faciens*, a grace that makes the recipient pleasing to God by perfecting his natural faculties.\n\nThe practical content of the Artista's expected revelation is specifically Paracelsian: the hidden virtues of metals, plants, and minerals; the true structure of the human body in relation to the macrocosm; the preparation of the *arcana* that can heal all diseases. This medical-alchemical content distinguishes Eglinus's vision from purely spiritual or political millenarianism: the expected transformation is empirical as well as spiritual.\n\nThe *Disquisitio* was published at Marburg, in the intellectual environment of the Hessian court that would become one of the principal centres of Rosicrucian patronage after 1614. Its publication there is not coincidental: the Landgrave of Hesse-Kassel maintained a Paracelsian laboratory and patronised alchemical-medical research, creating exactly the intellectual climate in which Eglinus's treatment of the Artista prophecy would find its most receptive audience.\n\nFor the history of Rosicrucianism, the *Disquisitio* serves as documentary proof that the millenarian-Paracelsian framework was in place before the manifestoes, available as an interpretive grid for readers who encountered the *Fama* and *Confessio* after 1614.",
        "concepts": [80, 76, 32, 33],
        "historical_context": "Marburg 1606: the Hessian court of Landgrave Moritz, one of the most important centres of Paracelsian-Hermetic patronage in the German lands. Published before the Rosicrucian manifestoes but in the same intellectual milieu.",
        "scholarship": "Åkerman, Susanna. *Rose Cross over the Baltic* (Brill, 1998), Chapter 2, pp. 116–119. Moran, Bruce. *The Alchemical World of the German Court* (Stuttgart, 1991).",
        "transmission_history": "Print, Marburg 1606. Limited circulation but known to figures in the Hessian and Württemberg networks. Represents the Paracelsian wing of pre-Rosicrucian millenarianism.",
        "image_url": ""
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# TIMELINE EVENTS (Baltic / Nordic Rosicrucianism, 1575–1652)
# ─────────────────────────────────────────────────────────────────────────────
TIMELINE_EVENTS = [
    {
        "id": "t_bureus_born",
        "year": 1568,
        "title": "Johannes Bureus Born",
        "description": "Johannes Bureus born in Åkerby, Uppsala province, Sweden. He will become Sweden's royal antiquary and the architect of Adulrunic theosophy—the most distinctive Nordic contribution to European Hermetism.",
        "category": "Birth",
        "location": "Uppsala, Sweden",
        "lat": 59.8586, "lng": 17.6389,
        "figures": [101], "concepts": [], "texts": []
    },
    {
        "id": "t_postel_death",
        "year": 1581,
        "title": "Guillaume Postel Dies in Paris",
        "description": "Guillaume Postel dies in Saint-Martin-des-Champs, Paris, leaving behind a body of Kabbalistic-universalist writings—including the *Candelabri Typici*—that will quietly feed into the Rosicrucian movement three decades later.",
        "category": "Death",
        "location": "Paris, France",
        "lat": 48.8566, "lng": 2.3522,
        "figures": [107], "concepts": [76], "texts": [97]
    },
    {
        "id": "t_roeslin_manuscripts",
        "year": 1588,
        "title": "Roeslin Begins Circulating Apocalyptic Manuscripts",
        "description": "Helisaeus Roeslin begins circulating manuscripts under the pseudonym 'Lampertus Floridus' containing apocalyptic-millenarian cosmology. These manuscripts, noted later by Karl Wideman (1638), represent a crucial node in the pre-Rosicrucian prophetic network.",
        "category": "Publication",
        "location": "Ensisheim, Alsace",
        "lat": 47.8660, "lng": 7.3570,
        "figures": [102], "concepts": [76], "texts": []
    },
    {
        "id": "t_naometria",
        "year": 1604,
        "title": "Studion Completes Naometria",
        "description": "Simon Studion completes his *Naometria* in Marbach, Württemberg—an enormous manuscript combining temple numerology, astrological eschatology, and Paracelsian prophecy. The Saturn-Jupiter conjunction of 1604 confirms his millenarian calculations. The text circulates in manuscript to the Württemberg-Kassel esoteric circle that will produce the Rosicrucian manifestoes.",
        "category": "Text Composition",
        "location": "Marbach am Neckar, Württemberg",
        "lat": 48.9369, "lng": 9.2581,
        "figures": [103], "concepts": [76, 80], "texts": [94]
    },
    {
        "id": "t_disquisitio",
        "year": 1606,
        "title": "Eglinus Publishes Disquisitio de Helia Artista",
        "description": "Raphael Eglinus publishes *Disquisitio de Helia Artista* at Marburg—eight years before the *Fama Fraternitatis*. The work provides the most systematic pre-Rosicrucian treatment of the Paracelsian Elias Artista prophecy, demonstrating that the millenarian framework was in place before 1614.",
        "category": "Publication",
        "location": "Marburg, Hesse",
        "lat": 50.8021, "lng": 8.7711,
        "figures": [105], "concepts": [80, 76], "texts": [99]
    },
    {
        "id": "t_bureus_adulruna_begins",
        "year": 1611,
        "title": "Bureus Begins Composing Adulruna Rediviva",
        "description": "Johannes Bureus begins the sustained composition of *Adulruna Rediviva* under royal patronage at the Swedish court. His fusion of Norse runic analysis with Kabbalistic Hermetism creates a uniquely Nordic theosophical system that will shape the Swedish reception of Rosicrucianism.",
        "category": "Text Composition",
        "location": "Stockholm, Sweden",
        "lat": 59.3293, "lng": 18.0686,
        "figures": [101], "concepts": [75, 79], "texts": [93]
    },
    {
        "id": "t_fama_published",
        "year": 1614,
        "title": "Fama Fraternitatis Published at Kassel",
        "description": "The *Fama Fraternitatis* is published at Kassel, Hesse—the centre of Landgrave Moritz's court and the Rosicrucian printing network. The manifesto launches the public phase of the Rosicrucian movement. Within months it is circulating across the Baltic trade networks to Hamburg, Danzig, and Stockholm.",
        "category": "Publication",
        "location": "Kassel, Hesse",
        "lat": 51.3127, "lng": 9.4797,
        "figures": [1], "concepts": [7, 76, 29], "texts": [1]
    },
    {
        "id": "t_echo_sperber",
        "year": 1615,
        "title": "Sperber Publishes Echo der Fraternität",
        "description": "Julius Sperber publishes *Echo der von Gott hocherleuchteten Fraternität* at Danzig—one of the earliest Rosicrucian responses, representing the movement's Gnostic-astronomical wing. His emphasis on interior illumination and phosphoric lights distinguishes his reading from the reformist mainstream.",
        "category": "Publication",
        "location": "Danzig (Gdańsk), Poland",
        "lat": 54.3520, "lng": 18.6466,
        "figures": [106], "concepts": [76, 30], "texts": [95]
    },
    {
        "id": "t_roeslin_dies",
        "year": 1616,
        "title": "Helisaeus Roeslin Dies",
        "description": "Helisaeus Roeslin dies at Frankfurt. His apocalyptic cosmology and 'celestial wheel' calculations had provided the eschatological framework that Studion, Andreae, and others deployed in the Rosicrucian project. His death marks the passing of the generation that incubated Rosicrucianism.",
        "category": "Death",
        "location": "Frankfurt, Germany",
        "lat": 50.1109, "lng": 8.6821,
        "figures": [102], "concepts": [76], "texts": []
    },
    {
        "id": "t_stella_hieroglyphica",
        "year": 1618,
        "title": "Stella Hieroglyphica Published",
        "description": "Philippo à Gabella's *Stella Hieroglyphica* published, sometimes as an appendix to the *Confessio*. The Bohemian War begins the same year, interrupting the Rosicrucian movement's public phase and driving it underground or into Baltic exile.",
        "category": "Publication",
        "location": "Southern Germany",
        "lat": 48.5000, "lng": 9.5000,
        "figures": [], "concepts": [7, 76], "texts": [96]
    },
    {
        "id": "t_danish_dutch_network",
        "year": 1622,
        "title": "Danish-Dutch Rosicrucian Network Active",
        "description": "The 'Trumpet Blow of 1622'—the death of Carl Philip—marks the intensification of Rosicrucian millenarian activity in Northern Europe. A Danish-Dutch network for Rosicrucian materials, active 1622–1625, passes prophetic texts including Grebner's visions through Hamburg, Amsterdam, Copenhagen, and Stockholm.",
        "category": "Network Activity",
        "location": "Copenhagen, Denmark",
        "lat": 55.6761, "lng": 12.5683,
        "figures": [101, 104], "concepts": [77, 78, 76], "texts": []
    },
    {
        "id": "t_leo_denmark",
        "year": 1625,
        "title": "Lion of the North Symbol First Applied in Denmark",
        "description": "Nils Ahnlund documents that the *Leo Septentrionalis* (Lion of the North) prophecy symbol was first applied to a potential Nordic Protestant king in Denmark in 1625—initially to Christian IV before later transfer to Gustavus Adolphus. The symbol circulates through Rosicrucian-millenarian networks.",
        "category": "Symbol Circulation",
        "location": "Copenhagen, Denmark",
        "lat": 55.6761, "lng": 12.5683,
        "figures": [104], "concepts": [77, 76], "texts": []
    },
    {
        "id": "t_gustaf_sweden_enters_war",
        "year": 1630,
        "title": "Gustavus Adolphus Enters Thirty Years War",
        "description": "Gustavus Adolphus of Sweden lands in Germany (July 1630), beginning Sweden's active participation in the Thirty Years' War. The *Leo Septentrionalis* prophecy is rapidly applied to him by Rosicrucian-millenarian writers, especially in pamphlets published at Erfurt. The Baltic networks Åkerman documents supplied the prophetic vocabulary for this application.",
        "category": "Political Event",
        "location": "Stralsund / Pomerania",
        "lat": 54.3090, "lng": 13.0820,
        "figures": [101, 104], "concepts": [77, 76, 78], "texts": []
    },
    {
        "id": "t_stiernhielm_career",
        "year": 1640,
        "title": "Stiernhielm Active at Swedish Court",
        "description": "Georg Stiernhielm, now a senior court official and the leading intellectual figure of Swedish Baroque culture, is transmitting Bureus's Adulrunic-Hermetic tradition to a new generation. His work integrates runic theosophy, comparative philology (Gothic as mother language), and Hermetic natural philosophy.",
        "category": "Intellectual Transmission",
        "location": "Stockholm, Sweden",
        "lat": 59.3293, "lng": 18.0686,
        "figures": [108, 101], "concepts": [79, 75], "texts": []
    },
    {
        "id": "t_adulruna_rediviva_final",
        "year": 1647,
        "title": "Adulruna Rediviva Reaches Final Form",
        "description": "Johannes Bureus completes the final form of *Adulruna Rediviva* after decades of composition. The manuscript, preserved in Uppsala University Library, represents the most sustained synthesis of Norse runic tradition and Kabbalistic Hermetism in the European tradition.",
        "category": "Text Composition",
        "location": "Stockholm, Sweden",
        "lat": 59.3293, "lng": 18.0686,
        "figures": [101], "concepts": [75, 79], "texts": [93]
    },
    {
        "id": "t_bureus_death",
        "year": 1652,
        "title": "Johannes Bureus Dies",
        "description": "Johannes Bureus dies in Stockholm at age 84, having served three Swedish monarchs and composed the entirety of the Adulrunic theosophical system. His intellectual legacy passes to Georg Stiernhielm and through him to Swedish Hermetic culture of the late seventeenth century.",
        "category": "Death",
        "location": "Stockholm, Sweden",
        "lat": 59.3293, "lng": 18.0686,
        "figures": [101, 108], "concepts": [75, 79], "texts": [93]
    },
    {
        "id": "t_stiernhielm_hercules",
        "year": 1658,
        "title": "Stiernhielm Publishes Hercules",
        "description": "Georg Stiernhielm publishes *Hercules*, his major baroque poem encoding Hermetic principles within classical allegory. The work transmits Burean theosophy into mid-seventeenth century Swedish literary culture, and through Stiernhielm's wider intellectual production to the generation that precedes Swedenborg.",
        "category": "Publication",
        "location": "Stockholm, Sweden",
        "lat": 59.3293, "lng": 18.0686,
        "figures": [108], "concepts": [79, 75], "texts": []
    },
    {
        "id": "t_akerman_book",
        "year": 1998,
        "title": "Åkerman Publishes Rose Cross over the Baltic",
        "description": "Susanna Åkerman publishes *Rose Cross over the Baltic: The Spread of Rosicrucianism in Northern Europe* (Brill), the definitive study of Baltic Rosicrucianism. Drawing on Swedish, Danish, and German archives, it corrects the southern-German bias of Yates's scholarship and establishes millenarianism as the organizing category for understanding the movement.",
        "category": "Modern Scholarship",
        "location": "Stockholm / Leiden",
        "lat": 52.1601, "lng": 4.4970,
        "figures": [109], "concepts": [76, 78, 75], "texts": [98]
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# UPDATES TO EXISTING ENTRIES
# ─────────────────────────────────────────────────────────────────────────────

def update_andreae(fig):
    """Enrich Andreae entry with Akerman's scholarship on the Württemberg context."""
    if "Andreae" not in fig["name"]:
        return fig
    extra = (
        "\n\nSusanna Åkerman's *Rose Cross over the Baltic* (1998) substantially enriches the "
        "Andreae picture by situating him within the dense Württemberg esoteric network. Her "
        "Chapter 2 analysis shows that the millenarian framework of the manifestoes—the "
        "expectation of imminent universal reform—was not invented by Andreae but inherited from "
        "the pre-existing Württemberg-Kassel circle: Simon Studion's *Naometria* (1604) had "
        "already synthesised the Paracelsian Elias Artista prophecy, Helisaeus Roeslin's "
        "celestial wheel cosmology, and Kabbalistic temple numerology into a timetable for "
        "universal transformation. Andreae's contribution was literary and strategic: he gave "
        "the pre-existing millenarian expectation its most compelling narrative form. "
        "Åkerman also traces the 'doubted role' of Andreae in the manifestoes' authorship, "
        "noting that his later disavowal of the *Fama* and *Confessio* may reflect both genuine "
        "embarrassment at the movement's fragmentation and prudent distancing from politically "
        "dangerous millenarianism after the failure of the Palatinate cause."
    )
    if extra.strip() not in fig.get("essay", ""):
        fig["essay"] = fig.get("essay", "") + extra
    if "Åkerman" not in fig.get("scholars", []):
        fig.setdefault("scholars", []).append("Åkerman")
    return fig


def update_tycho(fig):
    """Add Akerman's discussion of the Tychonic debate context."""
    if "Tycho" not in fig["name"] and "Brahe" not in fig["name"]:
        return fig
    extra = (
        "\n\nÅkerman's *Rose Cross over the Baltic* (1998, Chapter 5) places Tycho's "
        "geo-heliocentric model at the centre of the Rosicrucian natural-philosophical "
        "debate. The 'Tychonic debate' at Danzig—involving Julius Sperber and the *Oculus "
        "Sidereus* group—turned on whether the Tychonic compromise between Ptolemy and "
        "Copernicus was theosophically superior to pure heliocentrism. Sperber argued that "
        "the Tychonic model preserved the spiritual significance of the earth as the centre "
        "of redemptive history while acknowledging mathematical reality—a position that made "
        "Tycho's system uniquely suited to Rosicrucian natural philosophy. Tycho's "
        "connection to Rosicrucian culture also runs through his observation of the nova of "
        "1572, which Roeslin and others interpreted as an eschatological sign of the coming "
        "universal reform. Pliny's rose symbolism in the context of Tycho's phosphoric "
        "lights—discussed by Åkerman in Chapter 5—connects his astronomical work to the "
        "emblematic tradition."
    )
    if extra.strip() not in fig.get("essay", ""):
        fig["essay"] = fig.get("essay", "") + extra
    if "Åkerman" not in fig.get("scholars", []):
        fig.setdefault("scholars", []).append("Åkerman")
    return fig


def update_bohme(fig):
    """Add Akerman's genealogical point about Böhme and Baltic reception."""
    if "Böhme" not in fig["name"] and "Bohme" not in fig["name"]:
        return fig
    extra = (
        "\n\nÅkerman's *Rose Cross over the Baltic* (1998) traces a genealogical arc from "
        "Rosicrucian millenarianism through Böhme's theosophy to Swedenborgianism. In her "
        "reading, the vocabulary of 'divine influx' and interior regeneration that Böhme "
        "developed—drawing on the same Paracelsian and Hermetic sources as the Rosicrucian "
        "writers—was absorbed into the Baltic theosophical tradition through Johannes Bureus "
        "and Georg Stiernhielm. Bureus's Adulrunic theosophy and Böhme's Aurora represent "
        "parallel responses to the same millenarian-Hermetic moment, both rooted in the "
        "conviction that divine knowledge was accessible through careful attention to the "
        "structure of nature and language. The connection between Böhme's influence and "
        "Swedenborg's mature theosophy runs partly through the Baltic Rosicrucian network "
        "that Åkerman documents, making the Nordic transmission chain an important but "
        "underexplored dimension of Böhme's historical legacy."
    )
    if extra.strip() not in fig.get("essay", ""):
        fig["essay"] = fig.get("essay", "") + extra
    if "Åkerman" not in fig.get("scholars", []):
        fig.setdefault("scholars", []).append("Åkerman")
    return fig


def update_fludd(fig):
    """Add Akerman's point about the Rose Cross in Denmark and England."""
    if "Fludd" not in fig["name"]:
        return fig
    extra = (
        "\n\nÅkerman's *Rose Cross over the Baltic* (1998, Chapter 3) documents 'the Rose "
        "Cross in Denmark and England'—a network connecting Fludd's English Rosicrucian "
        "sympathies to the Baltic reception through the Danish-English diplomatic and "
        "intellectual connections of the 1620s. The Danish-Dutch network for Rosicrucian "
        "material active in 1622–1625 passed through channels that connected Hamburg and "
        "Amsterdam to London, situating Fludd's publications within a broader Northern "
        "European information system rather than a purely English-German exchange."
    )
    if extra.strip() not in fig.get("essay", ""):
        fig["essay"] = fig.get("essay", "") + extra
    if "Åkerman" not in fig.get("scholars", []):
        fig.setdefault("scholars", []).append("Åkerman")
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# APPLY ALL CHANGES
# ─────────────────────────────────────────────────────────────────────────────

# Add new figures
existing_fig_ids = {safe_int(f["id"]) for f in data["figures"]}
for fig in NEW_FIGURES:
    if safe_int(fig["id"]) not in existing_fig_ids:
        data["figures"].append(fig)
        print(f"Added figure: {fig['name']}")

# Add new concepts
existing_con_ids = {safe_int(c["id"]) for c in data["concepts"]}
for con in NEW_CONCEPTS:
    if safe_int(con["id"]) not in existing_con_ids:
        data["concepts"].append(con)
        print(f"Added concept: {con['name']}")

# Add new texts
existing_txt_ids = {str(t.get("id", "")) for t in data["texts"]}
for txt in NEW_TEXTS:
    if str(txt["id"]) not in existing_txt_ids:
        data["texts"].append(txt)
        print(f"Added text: {txt['title']}")

# Add timeline if key doesn't exist
if "timeline" not in data:
    data["timeline"] = []
existing_tl_ids = {str(e.get("id", "")) for e in data["timeline"]}
added_tl = 0
for evt in TIMELINE_EVENTS:
    if str(evt["id"]) not in existing_tl_ids:
        data["timeline"].append(evt)
        added_tl += 1
print(f"Added {added_tl} timeline events")

# Update existing figures
for i, fig in enumerate(data["figures"]):
    data["figures"][i] = update_andreae(fig)
    data["figures"][i] = update_tycho(fig)
    data["figures"][i] = update_bohme(fig)
    data["figures"][i] = update_fludd(fig)

# ─────────────────────────────────────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────────────────────────────────────
with open(DATA_FILE, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n✓ Data saved to", DATA_FILE)
print("Summary:")
print(f"  Figures: {len(data['figures'])}")
print(f"  Concepts: {len(data['concepts'])}")
print(f"  Texts: {len(data['texts'])}")
print(f"  Timeline: {len(data['timeline'])}")
