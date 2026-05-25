#!/usr/bin/env python3
"""
Extract text from Vickers' "Frances Yates and the Writing of History" PDF
"""

import sys
try:
    import pdfplumber
except ImportError:
    print("Installing pdfplumber...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pdfplumber", "-q"])
    import pdfplumber

pdf_path = r"C:\Users\PC\Downloads\[The Journal of Modern History 1979-jun vol. 51 iss. 2] Frances Yates and the Writing of History{Vickers, Brian}(1979 June)[10.1086_241901]{79480974} libgen.li.pdf"

try:
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Total pages: {len(pdf.pages)}\n")

        # Extract first 15 pages for the main content
        full_text = ""
        for i, page in enumerate(pdf.pages[:15]):
            text = page.extract_text()
            if text:
                full_text += text + "\n"

        # Save to file
        with open(r"C:\Dev\TheosophicalAlchemyDB\data\vickers_yates_extract.txt", 'w', encoding='utf-8') as f:
            f.write(full_text)

        print(f"Extracted {len(full_text.split())} words from first 15 pages")
        print("\n=== FIRST 1000 CHARACTERS ===\n")
        print(full_text[:1000])

except Exception as e:
    print(f"Error: {e}")
