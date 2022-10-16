"""
BibliograPy by Kamil Yousuf (@tyiop794)

Features:
 - generate citations in MLA, APA, Chicago, and IEEE
 - citations are properly formatted and can be exported to a file for a bibliography
 - can add to an existing bibliography
 - can find link from the internet if link is unknown (attempt to fill in blanks if blank exists)
 - choose from different source types (internet article, book, journal article, video)
 - specify parts directly to the command line w/o needing to enter the program interactively
 - switch between different editions of the formats (more commonly used
   such as MLA 8th edition) (might be a bit tricky)
 - create a GUI or interactive / easy-to-use TUI using tkinter or curses (that's a maybe?)
 - try looking up unknown information about source and filling in missing bits in citation
 - provide a reference for in-text citations of specific source (provide option for reference; can be 
 easily disabled)

 To-do list:
 - Export citations in *alphabetical* order

"""
import sys
import os
import datetime
import curses
import pdfkit
import tkinter as tk
from tkinter import filedialog
import info
from website import Website, web_ask
from podcast import Podcast, podcast_ask
from article import Article, article_ask
from book import Book, book_ask
from template import read_from_file
from typing import List, Union

# Date formatting needs to be fixed across the board! (Super inconsistent, man!)
"""
Fixing date stuffs:
Things to ask for:
- year 
- month
- day

Things to figure out:
- formatting across different bibliographic styles
"""

# Ask for month, day, and year


def export_entries(sources, type) -> str:
    # Will export entries using html + css
    root = tk.Tk()
    root.withdraw()
    html = """
    <html>
    <head>
    <head>
    <style>
    .p1 {
    font-family: "Times New Roman", Times, serif;
    font-size: 20px;
    padding-left: 50px;
    text-indent: -50px;
    }
    </style>
    <body>
    """
    # Sources in alphabetical order
    alpha_sources = []
    if type == "m" or "mla" or "MLA":
        for i in range(0, len(sources)):
            alpha_sources.append(sources[i].mla())
        alpha_sources.sort()
        for i in range(0, len(sources)):
            html += f'<p class="p1">{alpha_sources[i]}</p>\n'
        html += "</body>\n</html>"
    elif type == "a" or "apa" or "APA":
        for i in range(0, len(sources)):
            alpha_sources.append(sources[i].apa())
        alpha_sources.sort()
        for i in range(0, len(sources)):
            html += f'<p class="p1">{alpha_sources[i]}</p>\n'
        html += "</body>\n</html>"
    elif type == "c" or "chicago" or "Chicago":
        for i in range(0, len(sources)):
            alpha_sources.append(sources[i].chicago())
        alpha_sources.sort()
        for i in range(0, len(sources)):
            html += f'<p class="p1">{alpha_sources[i]}</p>\n'
        html += "</body>\n</html>"
    # file = open("biblio.html", "w")
    # file.write(html)
    # file.close()
    print("Exporting as PDF:")
    pdf_name = filedialog.asksaveasfilename()
    pdfkit.from_string(html, pdf_name)
    return pdf_name


def usage() -> None:
    """Print program usage help."""
    print(info.usage_def)


def main() -> None:
    # Make sure to test this!!!
    # Book: def __init__(self, title, authors, date_published, publisher, digital, publication_place, url, accessed):
    # Podcast:
    sources = []
    print("Welcome to BibliograPy!")
    biblio = ""
    while biblio not in ["m", "mla", "MLA", "a", "APA", "c", "Chicago" "i"]:
        biblio = input(
            "Will bibliography be in MLA (9th edition) (m), APA (a), Chicago (c), or IEEE (i)?: "
        )
        if biblio not in ["m", "mla", "MLA", "a", "APA", "c", "Chicago" "i"]:
            print("Not possible! Asking again!")
    print("For each entry type in information from the source you are trying to cite")
    print("(or leave blank if information is unknown)")
    print()
    while True:
        authors = []
        source = input(
            "Type of source (j for scholarly article, b for book, a for audio/podcast, w for website): "
        )
        if source not in ["j", "scholarly article", "article", "b", "book", "a", "audio/podcast", "w", "website"]:
            print("Not possible! Asking again!")
        if source == "j" or "scholarly article" or "article":
            article_ask(sources)
        elif source == "b" or "book":
            book_ask(sources)
        elif source == "a" or "audio/podcast":
            podcast_ask(sources)
        elif source == "w" or "website":
            web_ask(sources)
        print("Current sources added: ")
        for i in range(0, len(sources)):
            sources[i].output()
        source_add = input("Add another source? (Y/n): ")
        if source_add == "n":
            break
    pdf_name = export_entries(sources, biblio)
    print(f"Entries successfully exported as {pdf_name}!")


# Test entry for journal article
if len(sys.argv) == 1:
    main()
"""
if len(sys.argv) == 2 and (sys.argv[1] == "--usage" or sys.argv[1] == "--help"):
    usage()
elif len(sys.argv) == 2 and (sys.argv[1] == "-s" or sys.argv[1] == "--source"):
    print("Error: no source specified!")
    usage()
elif len(sys.argv) > 2 and (sys.argv[1] == "-s" or sys.argv[1] == "--source"):
    if sys.argv[2] == "a":
        source = 0
    elif sys.argv[2] == "w":
        source = 1 
    elif sys.argv[2] == "p":
        source = 2 
    elif sys.argv[2] == "b":
        source = 3 
if source == 3 and (sys.argv[(len(sys.argv) - 1)]) == "--usage":
    print(info.usage_book)
    exit(0)
elif source == 0 and (sys.argv[(len(sys.argv) - 1)]) == "--usage":
    print(info.usage_article)
    exit(0)
elif source == 1 and (sys.argv[(len(sys.argv) - 1)]) == "--usage":
    print(info.usage_website)
    exit(0)
elif source == 2 and (sys.argv[(len(sys.argv) - 1)]) == "--usage":
    print(info.usage_podcast)
    exit(0)

if source == 3:
    for i in range(0, len(sys.argv)):
        if sys.argv[i] == "-t":
            if i == len(sys.argv) - 1 or sys.argv[i + 1][0] == "-":
                print("Error: No title specified!")
                exit(1)
            elif sys.argv[i + 1][0] == "\"" and sys.argv[i + 1][len(sys.argv[i + 1]) - 1] == "\"":
                title = sys.argv[i + 1]
            else:
                print("Invalid title! Did you surround title with quotes?")
        elif sys.argv[i] == "-a":
            if i == len(sys.argv) - 1:
                print("Error! No authors specified!")
                exit(1)
"""
