#!/usr/bin/env python3
"""
PDF Ingestion Pipeline for TheosophicalAlchemyDB
Extracts text from PDFs and EPUBs, converts to markdown, populates database
"""

import os
import json
import sqlite3
from pathlib import Path
from datetime import datetime
import re

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

try:
    import ebooklib
    from ebooklib import epub
except ImportError:
    ebooklib = None

# Paths
PDF_DIRS = [
    r"E:\pdf\alchemy\spiritual alchemy",
    r"E:\pdf\Rosicrucian"
]
OUTPUT_DIR = Path(__file__).parent.parent / "corpus"
DB_PATH = Path(__file__).parent.parent / "data" / "theosophical_alchemy.db"

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def init_database():
    """Create database schema"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS sources (
        id INTEGER PRIMARY KEY,
        filename TEXT UNIQUE,
        title TEXT,
        authors TEXT,
        year INTEGER,
        source_type TEXT,
        file_path TEXT,
        processed_date TEXT,
        word_count INTEGER,
        excerpt_md TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS concepts (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        definition TEXT,
        source_ids TEXT,
        frequency INTEGER
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS source_concepts (
        source_id INTEGER,
        concept_id INTEGER,
        FOREIGN KEY(source_id) REFERENCES sources(id),
        FOREIGN KEY(concept_id) REFERENCES concepts(id)
    )
    ''')

    conn.commit()
    return conn

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdfplumber"""
    if not pdfplumber:
        return None

    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages[:50]:  # First 50 pages
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting PDF {pdf_path}: {e}")
        return None

def extract_text_from_epub(epub_path):
    """Extract text from EPUB"""
    if not ebooklib:
        return None

    try:
        book = epub.read_epub(epub_path)
        text = ""
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                text += item.get_content().decode('utf-8', errors='ignore')
        return text
    except Exception as e:
        print(f"Error extracting EPUB {epub_path}: {e}")
        return None

def extract_metadata_from_filename(filename):
    """Parse metadata from filename"""
    # Format: "Author - Title (Year).pdf"
    parts = filename.rsplit('.', 1)[0]  # Remove extension

    if ' - ' in parts:
        author, rest = parts.split(' - ', 1)
        # Extract year in parentheses
        year_match = re.search(r'\((\d{4})\)', rest)
        year = int(year_match.group(1)) if year_match else None
        title = rest.replace(f'({year})', '').strip() if year else rest.strip()
        return {
            'author': author.strip(),
            'title': title,
            'year': year
        }
    return {'author': 'Unknown', 'title': parts, 'year': None}

def create_markdown_summary(text, title, authors, year):
    """Create markdown summary from extracted text"""
    # Extract first meaningful paragraphs
    lines = [line.strip() for line in text.split('\n') if line.strip()]

    # Get first 500 words as preview
    words = []
    for line in lines:
        words.extend(line.split())
        if len(words) >= 500:
            break

    preview = ' '.join(words[:500])

    # Create markdown
    md = f"""# {title}

**Author(s):** {authors}
**Year:** {year or 'Unknown'}

## Summary

{preview}...

## Source

This is an excerpt from the original scholarly work.
"""
    return md

def process_pdfs():
    """Main ingestion pipeline"""
    conn = init_database()
    c = conn.cursor()

    processed_count = 0

    for pdf_dir in PDF_DIRS:
        if not os.path.exists(pdf_dir):
            print(f"Directory not found: {pdf_dir}")
            continue

        for filename in os.listdir(pdf_dir):
            filepath = os.path.join(pdf_dir, filename)

            if not os.path.isfile(filepath):
                continue

            # Check if already processed
            try:
                c.execute("SELECT id FROM sources WHERE filename = ?", (filename,))
                if c.fetchone():
                    print(f"Already processed: {filename}")
                    continue
            except:
                pass

            print(f"Processing: {filename}")

            # Extract text
            text = None
            source_type = None

            if filename.endswith('.pdf'):
                text = extract_text_from_pdf(filepath)
                source_type = 'PDF'
            elif filename.endswith('.epub'):
                text = extract_text_from_epub(filepath)
                source_type = 'EPUB'
            elif filename.endswith('.txt'):
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    text = f.read()
                source_type = 'TXT'

            if not text:
                print(f"  -> Could not extract text")
                continue

            # Parse metadata
            metadata = extract_metadata_from_filename(filename)

            # Create markdown
            md_content = create_markdown_summary(
                text,
                metadata['title'],
                metadata['author'],
                metadata['year']
            )

            # Save markdown
            md_filename = f"{metadata['author'].replace(' ', '_')}_{metadata['title'].replace(' ', '_')[:30]}.md"
            md_path = OUTPUT_DIR / md_filename
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)

            # Store in database
            try:
                c.execute('''
                    INSERT INTO sources
                    (filename, title, authors, year, source_type, file_path, processed_date, word_count, excerpt_md)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    filename,
                    metadata['title'],
                    metadata['author'],
                    metadata['year'],
                    source_type,
                    str(filepath),
                    datetime.now().isoformat(),
                    len(text.split()),
                    str(md_path)
                ))
                conn.commit()
                processed_count += 1
                print(f"  -> Ingested: {metadata['title']}")
            except sqlite3.IntegrityError:
                print(f"  -> Already in database")
            except Exception as e:
                print(f"  -> Error: {e}")

    conn.close()
    print(f"\nProcessed {processed_count} sources")

if __name__ == '__main__':
    process_pdfs()
