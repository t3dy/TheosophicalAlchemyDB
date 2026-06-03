#!/usr/bin/env python3
"""Restore concept coordinates. Idempotent."""
import json

with open('/home/user/TheosophicalAlchemyDB/data/prototype_data.json') as f:
    data = json.load(f)

concept_coords = {
    4: {'lat': 31.1991, 'lng': 29.9173, 'location': 'Alexandria, Egypt'},
    5: {'lat': 31.1991, 'lng': 29.9173, 'location': 'Alexandria, Egypt'},
    6: {'lat': 50.0755, 'lng': 14.4378, 'location': 'Prague, Bohemia (Czech Republic)'},
    7: {'lat': 51.3127, 'lng': 9.4797, 'location': 'Kassel, Hessen, Germany'},
    8: {'lat': 43.7696, 'lng': 11.2558, 'location': 'Florence, Italy'},
    15: {'lat': 43.6108, 'lng': 3.8767, 'location': 'Montpellier, France'},
    16: {'lat': 43.7696, 'lng': 11.2558, 'location': 'Florence, Italy'},
    18: {'lat': 43.6108, 'lng': 3.8767, 'location': 'Montpellier, France'},
    19: {'lat': 50.0755, 'lng': 14.4378, 'location': 'Prague, Bohemia (Czech Republic)'},
    20: {'lat': 43.6108, 'lng': 3.8767, 'location': 'Montpellier, France'},
    22: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    23: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    24: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    25: {'lat': 37.9838, 'lng': 23.7275, 'location': 'Athens, Greece'},
    26: {'lat': 43.7696, 'lng': 11.2558, 'location': 'Florence, Italy'},
    27: {'lat': 51.1541, 'lng': 14.9875, 'location': 'Görlitz, Germany'},
    28: {'lat': 51.3127, 'lng': 9.4797, 'location': 'Kassel, Hessen, Germany'},
    29: {'lat': 51.3127, 'lng': 9.4797, 'location': 'Kassel, Hessen, Germany'},
    30: {'lat': 51.5074, 'lng': -0.1278, 'location': 'London, England'},
    31: {'lat': 50.0755, 'lng': 14.4378, 'location': 'Prague, Bohemia (Czech Republic)'},
    32: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    33: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    34: {'lat': 38.0432, 'lng': 23.5409, 'location': 'Eleusis, Greece'},
    35: {'lat': 38.0432, 'lng': 23.5409, 'location': 'Eleusis, Greece'},
    36: {'lat': 51.5074, 'lng': -0.1278, 'location': 'London, England'},
    37: {'lat': 48.8566, 'lng': 2.3522, 'location': 'Paris, France'},
    38: {'lat': 37.9838, 'lng': 23.7275, 'location': 'Athens, Greece'},
    39: {'lat': 37.9838, 'lng': 23.7275, 'location': 'Athens, Greece'},
    40: {'lat': 50.0755, 'lng': 14.4378, 'location': 'Prague, Bohemia (Czech Republic)'},
    41: {'lat': 51.1541, 'lng': 14.9875, 'location': 'Görlitz, Germany'},
    42: {'lat': 31.1991, 'lng': 29.9173, 'location': 'Alexandria, Egypt'},
    43: {'lat': 50.1109, 'lng': 8.6821, 'location': 'Frankfurt am Main, Germany'},
    44: {'lat': 35.4247, 'lng': 36.4058, 'location': 'Apamea, Syria'},
    45: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    46: {'lat': 32.9647, 'lng': 35.4966, 'location': 'Safed, Israel'},
    47: {'lat': 50.9333, 'lng': 6.95, 'location': 'Cologne, Germany'},
    48: {'lat': 51.1541, 'lng': 14.9875, 'location': 'Görlitz, Germany'},
    49: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    50: {'lat': 43.7696, 'lng': 11.2558, 'location': 'Florence, Italy'},
    61: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    62: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    63: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    66: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
    67: {'lat': 43.6108, 'lng': 3.8767, 'location': 'Montpellier, France'},
    68: {'lat': 47.5596, 'lng': 7.5886, 'location': 'Basel, Switzerland'},
}

updated = 0
for concept in data['concepts']:
    cid = concept.get('id')
    if cid in concept_coords:
        coords = concept_coords[cid]
        concept['lat'] = coords['lat']
        concept['lng'] = coords['lng']
        concept['location'] = coords['location']
        updated += 1
print(f'Restored coordinates for {updated} concepts')

with open('/home/user/TheosophicalAlchemyDB/data/prototype_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print('Saved.')