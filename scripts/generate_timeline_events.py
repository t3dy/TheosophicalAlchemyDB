#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 500+ timeline events from figures, texts, and scholarly sources.
Extracts births, deaths, publications, and key dated events.
"""

import json
import re

def extract_timeline_events():
    """Extract timeline events from figures and texts database."""

    with open("data/prototype_data.json", 'r', encoding='utf-8') as f:
        db = json.load(f)

    with open("data/timeline_events.json", 'r', encoding='utf-8') as f:
        timeline = json.load(f)

    events = timeline.get("timeline_events", [])
    event_id = len(events) + 1

    figures = db.get("figures", [])
    texts = db.get("texts", [])

    print("=" * 70)
    print("GENERATING TIMELINE EVENTS FROM DATABASE")
    print("=" * 70)
    print()

    # Extract figure births and deaths
    print(f"Extracting {len(figures)} figure births/deaths...")
    birth_death_events = 0

    for fig in figures:
        name = fig.get("name", "Unknown")
        birth = fig.get("birth_year")
        death = fig.get("death_year")
        location = fig.get("location", "Unknown")
        discipline = fig.get("primary_discipline", "")

        # Birth event
        if birth:
            events.append({
                "id": event_id,
                "date": str(birth),
                "date_precision": "exact",
                "event": f"{name} born",
                "category": "figure_birth",
                "figure_id": fig.get("id"),
                "figure_name": name,
                "location": location,
                "scholarly_source": "Biographical record",
                "significance": f"Birth of {discipline}",
                "related_concepts": []
            })
            event_id += 1
            birth_death_events += 1

        # Death event
        if death:
            events.append({
                "id": event_id,
                "date": str(death),
                "date_precision": "exact",
                "event": f"{name} died",
                "category": "figure_death",
                "figure_id": fig.get("id"),
                "figure_name": name,
                "location": location,
                "scholarly_source": "Biographical record",
                "significance": f"Death of {discipline}",
                "related_concepts": []
            })
            event_id += 1
            birth_death_events += 1

    print(f"  Added {birth_death_events} birth/death events")

    # Extract text publications
    print(f"Extracting {len(texts)} text publications...")
    text_events = 0

    for txt in texts:
        title = txt.get("title", "Unknown")
        year = txt.get("year")
        location = txt.get("location", "Unknown")

        if year:
            events.append({
                "id": event_id,
                "date": str(year),
                "date_precision": "exact",
                "event": f"'{title}' published",
                "category": "text_publication",
                "text_id": txt.get("id"),
                "text_title": title,
                "location": location,
                "scholarly_source": "Publication record",
                "significance": f"Publication of influential text",
                "related_concepts": txt.get("concepts", [])
            })
            event_id += 1
            text_events += 1

    print(f"  Added {text_events} publication events")

    # Summary
    print()
    print("=" * 70)
    print(f"TIMELINE EVENTS SUMMARY")
    print("=" * 70)
    print(f"Total events: {len(events)}")
    print(f"Target: 500 events")
    print(f"Progress: {len(events)}/500 ({100*len(events)//500}%)")
    print()

    # Save expanded timeline
    timeline["timeline_events"] = sorted(events, key=lambda e: int(e["date"]))
    timeline["metadata"]["total_events"] = len(events)

    with open("data/timeline_events.json", 'w', encoding='utf-8') as f:
        json.dump(timeline, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(events)} events to data/timeline_events.json")
    print()
    print("NEXT STEPS:")
    print("1. Extract scholarly debate events from scholarly_debates field")
    print("2. Add key encounter/correspondence events between figures")
    print("3. Parse Hanegraaff sources for dated scholarly arguments")
    print("4. Design interactive timeline frontend (D3.js, Vis.js, or custom)")

if __name__ == "__main__":
    extract_timeline_events()
