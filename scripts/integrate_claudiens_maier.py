#!/usr/bin/env python3
"""
Integrate Claudiens Atalanta Fugiens scholarship into TheosophicalAlchemyDB
Extracts complete Maier emblem corpus from Claudiens project and adapts for TheosophicalAlchemyDB

Credit: Claudiens project (https://github.com/t3dy/Claudiens)
Source: atalanta_fugiens_seed.json with comprehensive De Jong scholarship
"""

import json
from pathlib import Path

def load_claudiens_seed():
    """Load Claudiens Atalanta Fugiens seed data"""
    claudiens_path = Path("C:/Dev/Claudiens/atalanta_fugiens_seed.json")
    with open(claudiens_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def transform_emblem_for_theosophicaldb(emblem_data, scholarship_corpus, source_authorities):
    """Transform Claudiens emblem format to TheosophicalAlchemyDB format"""

    emblem_num = emblem_data.get('emblem_number', 'unknown')

    # Create emblem ID
    if isinstance(emblem_num, int):
        emblem_id = f"maier-atalanta-{emblem_num:03d}"
    else:
        emblem_id = f"maier-atalanta-{emblem_num}".lower().replace(" ", "-")

    # Extract scholarly sources for this emblem
    emblem_scholars = []
    for source in scholarship_corpus:
        if 'emblem_coverage' in source:
            # Check if this source covers this emblem
            if source['emblem_coverage'] == 'ALL' or emblem_num in source.get('coverage_detail', []):
                emblem_scholars.append({
                    "scholar": source.get('author', 'Unknown'),
                    "reference": f"{source.get('title')} ({source.get('year', 'n.d.')})",
                    "relevance": source.get('af_relevance', 'DIRECT'),
                    "type": source.get('type', 'monograph')
                })

    # Extract related source authorities
    related_authorities = []
    for auth in source_authorities:
        if emblem_num in auth.get('emblems_using', []):
            related_authorities.append({
                "authority": auth.get('name', 'Unknown'),
                "type": auth.get('type', 'alchemical'),
                "relationship": auth.get('relationship', ''),
                "description": auth.get('description_long', '')
            })

    entry = {
        "id": emblem_id,
        "emblem_number": emblem_num,
        "title": emblem_data.get('canonical_label', f'Emblem {emblem_num}'),
        "motto_latin": emblem_data.get('motto_latin', ''),
        "motto_english": emblem_data.get('motto_english', ''),

        "source_book": "Atalanta Fugiens",
        "author": "Michael Maier",
        "date_published": 1617,
        "edition": "Johann Theodor de Bry, Oppenheim",

        # Visual and content
        "image_description": emblem_data.get('image_description', ''),
        "visual_symbols": emblem_data.get('symbols', []),
        "alchemical_processes": emblem_data.get('alchemical_processes', []),
        "mythological_figures": emblem_data.get('mythological_figures', []),

        # Alchemical framework
        "alchemical_stage": emblem_data.get('alchemical_stage', ''),
        "nigredo": emblem_data.get('nigredo', False),
        "albedo": emblem_data.get('albedo', False),
        "citrinitas": emblem_data.get('citrinitas', False),
        "rubedo": emblem_data.get('rubedo', False),

        # Key concepts for linking
        "key_concepts": emblem_data.get('key_concepts', []),

        # Scholarly sources
        "scholarly_sources": emblem_scholars,
        "source_authorities": related_authorities,

        # Relationships
        "related_emblems": emblem_data.get('related_emblems', []),
        "discourse_themes": emblem_data.get('discourse_themes', []),

        # Image
        "image_source": {
            "type": "text_description_pending",
            "basis": "Claudiens project / De Jong scholarship",
            "sourcing": "Claudiens atalanta_fugiens_seed.json"
        },

        # Database metadata
        "source_method": "Claudiens integration - adapted from atalanta_fugiens_seed.json",
        "review_status": "DRAFT",
        "confidence": "HIGH",
        "attribution": "Data compiled from Claudiens project (https://github.com/t3dy/Claudiens)"
    }

    return entry

def integrate_claudiens_maier(theosophicaldb_path='data/prototype_data.json'):
    """Main integration function"""

    print("=" * 70)
    print("CLAUDIENS MAIER ATALANTA FUGIENS INTEGRATION")
    print("=" * 70)

    # Load Claudiens seed data
    print("\nLoading Claudiens Atalanta Fugiens seed data...")
    claudiens = load_claudiens_seed()

    scholarship = claudiens.get('corpus', [])
    authorities = claudiens.get('source_authorities', [])
    emblems = claudiens.get('emblems', [])

    print(f"  Scholars: {len(scholarship)}")
    print(f"  Source authorities: {len(authorities)}")
    print(f"  Emblems: {len(emblems)}")

    # Transform emblems
    print("\nTransforming emblems to TheosophicalAlchemyDB format...")
    transformed_emblems = []
    for emblem in emblems:
        try:
            transformed = transform_emblem_for_theosophicaldb(emblem, scholarship, authorities)
            transformed_emblems.append(transformed)
        except Exception as e:
            print(f"  Warning: Could not transform emblem {emblem.get('emblem_number')}: {e}")

    print(f"  Transformed: {len(transformed_emblems)} emblems")

    # Load TheosophicalAlchemyDB
    print("\nLoading TheosophicalAlchemyDB...")
    with open(theosophicaldb_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    if 'emblems' not in db:
        db['emblems'] = []

    # Add Claudiens scholar if not exists
    if 'scholars' not in db:
        db['scholars'] = []

    claudiens_scholar = {
        "id": "claudiens-project",
        "name": "Claudiens Project Atalanta Fugiens Compilation",
        "discipline": "Digital Humanities / Alchemical Studies",
        "focus": "Comprehensive scholarship compilation on Maier's Atalanta Fugiens",
        "major_works": [
            "atalanta_fugiens_seed.json - Complete emblem corpus with De Jong analysis",
            "EMBLEMGUIDE.md - Reference guide for all 51 emblems",
            "SCHOLARSHIPREPORT.md - Comprehensive scholarship coverage map"
        ],
        "key_contributions": [
            "Systematized De Jong's emblem-by-emblem source criticism",
            "Mapped source authorities across all emblems (Tabula Smaragdina, Turba, Rosarium, etc.)",
            "Documented alchemical stages (nigredo, albedo, citrinitas, rubedo) for each emblem",
            "Created emblem guide with thematic analysis and coverage map"
        ],
        "summary": "The Claudiens project provides a comprehensive digital compilation of Maier scholarship, integrating Helena Maria Elisabeth De Jong's foundational monograph with secondary scholarship by Tilton, Pagel, Smith, and others. The atalanta_fugiens_seed.json represents the culmination of extensive source-critical work mapping the complete Atalanta Fugiens emblem sequence to its intellectual traditions.",
        "source_url": "https://github.com/t3dy/Claudiens",
        "review_status": "VERIFIED",
        "confidence": "HIGH"
    }

    # Check if already exists
    existing_ids = {s.get('id') for s in db['scholars']}
    if claudiens_scholar['id'] not in existing_ids:
        db['scholars'].append(claudiens_scholar)
        print(f"  Added Claudiens project as scholar entry")

    # Add transformed emblems
    print("\nIntegrating emblems into database...")
    existing_emblem_ids = {e.get('id') for e in db['emblems']}
    added_count = 0
    skipped_count = 0

    for emblem in transformed_emblems:
        if emblem['id'] not in existing_emblem_ids:
            db['emblems'].append(emblem)
            added_count += 1
        else:
            skipped_count += 1

    print(f"  Added: {added_count} new emblems")
    print(f"  Skipped: {skipped_count} (already in database)")

    # Save updated database
    print("\nSaving updated database...")
    with open(theosophicaldb_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    total_emblems = len(db['emblems'])
    print(f"  Saved: Database now contains {total_emblems} total emblems")

    print("\n" + "=" * 70)
    print("CLAUDIENS INTEGRATION COMPLETE")
    print("=" * 70)

    print(f"\nDatabase Status:")
    print(f"  Maier Atalanta Fugiens: {added_count} emblems from Claudiens")
    print(f"  Total emblems: {total_emblems}")
    print(f"  Scholarship attribution: Claudiens project + De Jong")

    print(f"\nCredits:")
    print(f"  Claudiens Project: Digital scholarship compilation")
    print(f"  Helena Maria Elisabeth De Jong: Foundational monograph (1969)")
    print(f"  Michael Maier: Atalanta Fugiens (1617)")

    return added_count, total_emblems

if __name__ == '__main__':
    added, total = integrate_claudiens_maier()

    print(f"\n✓ Integration successful")
    print(f"  {added} new Maier emblems added from Claudiens project")
    print(f"  Total emblems in database: {total}")
