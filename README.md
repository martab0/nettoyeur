# Nettoyeur
 
Cleaning a CSV with unidirectional glossary - suitable for Google Translate Advanced and other MTs that can be customised with a glossary. 

* Specification: Marta Bartnicka
* Written by: Claude v3.5 Sonnet

## How to run
```
python nettoyeur.py
```

## How to use

1. Nettoyeur asks for a name of the CSV to clean, name for the cleaned CSV and name for the CSV with problematic rows.

2. Nettoyeur parses a CSV file, checks for rows not applicable in a glossary and saves:
- a cleaned CSV without problematic rows,
- a CSV with problematic rows only.

## What is cleaned

As a minimum, Nettoyeur removes the following rows from CSV (this should be good enough for Google Translate Advanced glossary):
- duplicates,
- rows with identical source (left side) and different targets (right side).

**Further cleaning can be customised if you comment/uncomment one or more lines 24-32.**

For a reasonable glossary functinality, Nettoyeur removes (but you can comment these options):
- rows with no comma,
- rows with more than one comma,
- rows with empty field before or after the comma.

Optionally, Nettoyeur can also remove the following rows (if you uncomment these options):
- rows with quotation marks,
- rows with HTML tags,
- rows that start or end with a space,
- rows that contain invisible Unicode characters.
