#!/usr/bin/env python3
"""
Add Brian Vickers critique to database and update Frances Yates entry
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "prototype_data.json"

# Load current data
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Read Vickers extract for context
with open(Path(__file__).parent.parent / "data" / "vickers_yates_extract.txt", 'r', encoding='utf-8') as f:
    vickers_text = f.read()

# Get word count and create summary
vickers_words = len(vickers_text.split())
first_1000_chars = vickers_text[:1000]

# Update Frances Yates entry (id 11) with critique info
yates_idx = None
for i, fig in enumerate(data['figures']):
    if fig['id'] == 11:  # Frances Yates
        yates_idx = i
        break

if yates_idx is not None:
    fig = data['figures'][yates_idx]
    # Add reference to Vickers critique in essay
    original_essay = fig.get('essay', '')
    critique_addition = """

## Critical Reception and Historiographical Debate

Yates's *The Rosicrucian Enlightenment* prompted significant scholarly debate. Harvard historian Brian Vickers published an influential critique ("Frances Yates and the Writing of History," *Journal of Modern History*, 1979) that challenged the evidentiary basis of Yates's claims. Vickers argued that Yates's work, while rhetorically brilliant and intellectually exciting, construed limited and speculative evidence as definitive historical fact. He particularly criticized her treatment of Johann Valentin Andreae, arguing that Yates understated Andreae's explicit opposition to Rosicrucian claims and overstated connections between figures like Andreae, Dee, and Fludd. Vickers's critique illustrated the historiographical tensions between imaginative intellectual reconstruction and strict documentary evidence—a debate that continues to inform scholarship on Renaissance esotericism."""

    fig['essay'] = original_essay + critique_addition
    if 'scholars' not in fig:
        fig['scholars'] = []
    if "Vickers" not in fig['scholars']:
        fig['scholars'].append("Vickers")
    print(f"Updated Frances Yates entry with Vickers critique reference")

# Add Brian Vickers as a scholar figure
vickers_figure = {
    "id": 51,
    "name": "Brian Vickers",
    "slug": "brian-vickers",
    "birth_year": 1937,
    "death_year": None,
    "nationality": "English",
    "location": "Cambridge, England",
    "lat": 52.2044,
    "lng": 0.1183,
    "primary_discipline": "Literary Scholar, Historian of Ideas",
    "summary": "Cambridge and Harvard-based literary scholar and intellectual historian whose critique of Frances Yates established methodological rigor in Renaissance intellectual history. Major contributions to historiography of science and esotericism.",
    "essay": "Brian Vickers (born 1937) is a distinguished British literary scholar and historian of ideas whose meticulous scholarship has set standards for intellectual rigor in Renaissance studies. Based at Cambridge and Harvard, Vickers combined close textual analysis with archival research to challenge romantic reconstructions of Renaissance intellectual history. His most influential contribution to esoteric studies is 'Frances Yates and the Writing of History' (Journal of Modern History, 1979), a comprehensive critique of Yates's *The Rosicrucian Enlightenment*. In this review article, Vickers demonstrated that while Yates possessed exceptional imaginative and rhetorical gifts, her work frequently constructed elaborate historical narratives from fragmentary or speculative evidence. Vickers's critique was not dismissive but methodologically constructive, arguing that serious historical scholarship requires faithful reconstruction of documentary evidence and careful attention to semantic and contextual meaning. His work on Andreae, Dee, and the Rosicrucian manifestos exemplified how meticulous scholarship can revise popular interpretations. Vickers's broader scholarly interests encompassed Renaissance rhetoric, the history of the Royal Society, and the epistemological foundations of early modern science. His insistence on documentary evidence and critical skepticism toward grand narratives influenced subsequent scholarship on Renaissance magic and esotericism, establishing important correctives to more speculative approaches.",
    "scholars": ["Vickers", "Contemporary scholars"],
    "key_works": ["Frances Yates and the Writing of History", "Occult and Scientific Mentalities in the Renaissance", "The Royal Society and Its Historians"]
}

data['figures'].append(vickers_figure)
print(f"Added Brian Vickers as new figure (id 51)")

# Add the Vickers article as a text entry
vickers_text_entry = {
    "id": 51,
    "title": "Frances Yates and the Writing of History",
    "slug": "vickers-frances-yates-writing",
    "year": 1979,
    "language": "English",
    "location": "Cambridge, England",
    "lat": 52.2044,
    "lng": 0.1183,
    "summary": "Brian Vickers's influential critique of Frances Yates's methodological approach to Renaissance intellectual history. Challenges the evidentiary basis of Yates's claims while preserving her contributions to imaginative reconstruction.",
    "essay": """Brian Vickers's 'Frances Yates and the Writing of History' (published in *Journal of Modern History* 51.2 [June 1979]: 287-316) stands as the most comprehensive scholarly critique of Frances Yates's historiographical methodology. Vickers's article addresses fundamental questions about the relationship between historical evidence and historical narrative, particularly in the study of Renaissance intellectual movements.

The essay begins by acknowledging Yates's considerable achievements: her erudition, her ability to synthesize disparate materials, and her capacity to inspire readers with a vision of Renaissance intellectual culture. However, Vickers argues that these rhetorical and imaginative strengths have led to serious distortions in historical interpretation. The Rosicrucian movement, as Yates presents it, becomes through her rhetoric a vast intellectual and political force shaping the development of science, politics, and philosophy. Yet the documentary evidence is thin: two anonymous pamphlets (Fama Fraternitatis and Confessio Fraternitatis) from 1614-1615, brief and in many respects obscure texts.

Vickers's central methodological critique concerns the treatment of evidence. He demonstrates repeatedly how Yates moves from speculation to assertion, from suggestive connections to causal relationships. The case of Johann Valentin Andreae exemplifies the problem. Yates, following Paul Arnold's earlier work, claims that Andreae was a central figure in Rosicrucian activity. However, J. W. Montgomery's authoritative two-volume study of Andreae (1973) reveals that Andreae was actually an orthodox Lutheran pastor and theologian who explicitly opposed Rosicrucian esotericism and the occult. Andreae's Chymische Hochzeit (1616), which Yates treats as a quasi-Rosicrucian manifesto, Montgomery and other Andreae scholars recognize as a Christian allegory deliberately opposing the Rosicrucian myth. Andreae later expressed disgust that his work had become confused with Rosicrucian materials, and he devoted multiple published works to attacking the Rosicrucians and other occultists.

Vickers argues that Yates glosses over these embarrassing facts and maintains a speculative narrative through what Montgomery called 'guilt by association'—because some of Andreae's friends had occult interests, Yates assumes Andreae shared them. This pattern repeats with Dee, Fludd, and others. The connections Yates draws between these figures are contested or nonexistent, yet she presents them as historical facts.

Furthermore, Vickers demonstrates that the Rosicrucian movement itself, as a historical phenomenon, was insignificant. The Fama and Confessio were brief literary productions, possibly exercises in mystical fiction. No one knows whether an actual 'Rosicrucian brotherhood' ever existed. The manifestos describe an idealistic society devoted to occult study and Christian reform, but the extent of actual organization remains mysterious. Yates transforms this obscure episode into a decisive intellectual movement.

Vickers also criticizes Yates's approach to the history of science. She claims that Rosicrucian ideas influenced the founders of the Royal Society and the development of experimental science. However, historians of science and scholars like A. J. Turner found this claim unconvincing. The rhetoric of Yates's presentation—with its excitement, mystery, and suggestion of hidden connections—creates an impression of significance that the evidence does not support.

The article concludes that while Yates is an imaginative and exciting historian, her work must be judged as history, not as inspired speculation. A historian has special obligations to the meaning of documents, to accurate context, and to the distinction between evidence and inference. Vickers does not dismiss Yates's contributions but insists on methodological rigor as the foundation of legitimate historical interpretation. The debate between Yates and her critics established important standards for scholarship on Renaissance esotericism and intellectual history, emphasizing the need to balance imaginative reconstruction with documentary evidence and critical skepticism toward grand narratives.""",
    "concepts": [1, 25, 27, 37, 40]
}

data['texts'].append(vickers_text_entry)
print(f"Added Vickers article as text entry (id 51)")

# Save updated data
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully updated prototype_data.json")
print(f"- Added Brian Vickers (figure id 51)")
print(f"- Added 'Frances Yates and the Writing of History' (text id 51)")
print(f"- Updated Frances Yates entry with critique context")
print(f"\nNew totals:")
print(f"  Figures: {len(data['figures'])}")
print(f"  Concepts: {len(data['concepts'])}")
print(f"  Texts: {len(data['texts'])}")
