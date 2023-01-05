"""
BibliograPy by Kamil Yousuf (@tyiop794)

Features:
 - generate citations in MLA, APA, and Chicago
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
    if type == "m" or type == "mla" or type == "MLA":
        print("m")
        for i in range(0, len(sources)):
            alpha_sources.append(sources[i].mla())
        alpha_sources.sort()
        for i in range(0, len(sources)):
            html += f'<p class="p1">{alpha_sources[i]}</p>\n'
        html += "</body>\n</html>"
    elif type == "a" or type == "apa" or type == "APA":
        print("a")
        for i in range(0, len(sources)):
            alpha_sources.append(sources[i].apa())
        alpha_sources.sort()
        for i in range(0, len(sources)):
            html += f'<p class="p1">{alpha_sources[i]}</p>\n'
        html += "</body>\n</html>"
    elif type == "c" or type == "chicago" or type == "Chicago":
        print("c")
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
            "Will bibliography be in MLA (9th edition) (m), APA (a), or Chicago?: "
        )
        if biblio not in ["m", "mla", "MLA", "a", "APA", "c", "Chicago" "i"]:
            print("Not possible! Asking again!")
    print("For each entry type in information from the source you are trying to cite")
    print("(or leave blank if information is unknown)")
    print()
    while True:
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
elif len(sys.argv) == 3 and sys.argv[1] == "-f":
    if os.path.exists(sys.argv[2]):
        sources = read_from_file(sys.argv[2])
        cite_type = input("Citation type? (m for mla, c for chicago, or a for apa): ")
        export_entries(sources, cite_type)
    else:
        raise ValueError("Error! File does not exist!")

