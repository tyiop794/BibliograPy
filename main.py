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

"""
import sys
import os
import datetime
import curses
import pdfkit
import tkinter as tk
import time
from tkinter import filedialog
import info
from website import Website, web_ask
from podcast import Podcast, podcast_ask 
from article import Article, article_ask 
from book import Book, book_ask 

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
         
def export_entries(sources, type):
    # Will export entries using html + css
    root = tk.Tk()
    root.withdraw()
    html = '''
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
    '''
    if type == "m":
        for i in range(0, len(sources)): 
            html += f'<p class="p1">{sources[i].mla()}</p>\n'
        html += "</body>\n</html>"
    elif type == "a":
        for i in range(0, len(sources)):
            html += f'<p class="p1">{sources[i].apa()}</p>\n'
        html += "</body>\n</html>"
    elif type == "c":
        for i in range(0, len(sources)):
            html += f'<p class="p1">{sources[i].chicago()}</p>\n'
        html += "</body>\n</html>"
    #file = open("biblio.html", "w") 
    #file.write(html)
    #file.close()
    print("Exporting as PDF:")
    pdf_name = filedialog.asksaveasfilename()
    pdfkit.from_string(html, pdf_name) 
    return pdf_name
    

def usage():
    print(info.usage_def)

def main():
    s=" "
    while True:
        # Book: def __init__(self, title, authors, date_published, publisher, digital, publication_place, url, accessed): 
        # Podcast: 
        sources = []
        print("Welcome to BibliograPy!")
        print(s) 
        biblio = ""
        while biblio not in ["m", "a", "c", "i"]:
            biblio = input("Will bibliography be in MLA (9th edition) (m), APA (a), Chicago (c), or IEEE (i)?: ")
            if biblio not in ["m", "a", "c", "i"]:
                print("Not possible! Asking again!")
        print("For each entry type in information from the source you are trying to cite")
        print(s) 
        time.sleep(1)
        print("(or leave blank if information is unknown)")
        print()
        while True:
            authors = []
            source = input("Type of source (j for scholarly article, b for book, a for audio/podcast): ")
            print(s) 
            time.sleep(1)
            if source == "j":
            # def __init__(self, title, authors, digital, journal, volume, issue, pages, date_published, url, accessed):
                digital = input("Physical or digital (p for physical, d for digital): ")
                print(s) 
                time.sleep(1)
            title = input("Title of work?: ")
            print(s) 
            time.sleep(1)
            try:
                author_no = int(input("Number of authors (default is 1): "))
            except ValueError:
                author_no = 1
            print("Authors' names should be listed in order they appear on source!: ")
            print(s) 
            time.sleep(1)
            if author_no > 1:
                for i in range(0, author_no):
                    lastname = input(f"Last name of author {i + 1}: ")
                    print(s) 
                    time.sleep(1)
                    firstname = input(f"First name of author {i + 1}: ")
                    print(s) 
                    time.sleep(1)
                    authors.append((lastname, firstname))
            else:
                lastname = input("Last name of author?: ")
                print(s) 
                time.sleep(1)
                firstname = input("First name of author?: ")
                print(s) 
                time.sleep(1)
                authors.append((lastname, firstname))
            date_published = input("Date of publication? ((YYYY), (MM, YYYY) or (MM, DD, YYYY)): ")
            print(s) 
            time.sleep(1)
            if source == "b":
                publisher = input("Publisher?: ")
                print(s) 
                time.sleep(1)
                location = input("Publication location?: ")
                print(s) 
                time.sleep(1)
            if digital == "d":
                url = input("URL/DOI? (address of website typed into webbrowser): ")
                print(s) 
                time.sleep(1)
            else:
                url = ""
            if source == "j":
                journal = input("Journal of publication?: ")
                print(s) 
                time.sleep(1)
                pages = input("Article pages? (page-page): ")
                print(s) 
                time.sleep(1)
                issue = input("Article issue? (no. only): ")
                print(s) 
                time.sleep(1)
                volume = input("Journal volume?: ")
                print(s) 
                time.sleep(1)
            accessed = input("Date accessed (MM, DD, YYYY): ")
            print(s) 
            time.sleep(1)
            if source == "b":
                sources.append(Book(title, authors, digital, date_published, publisher, location, url, accessed))
            elif source == "j":
                sources.append(Article(title, authors, digital, journal, volume, issue, pages, date_published, url, accessed))
            print("Current sources added: ")
            print(s) 
            time.sleep(1)
            for i in range(0, len(sources)):
                sources[i].output()
            source_add = input("Add another source? (Y/n): ")
            print(s) 
            time.sleep(1)
            if source_add == "n":
                break
        pdf_name = export_entries(sources, biblio) 
        print(f"Entries successfully exported as {pdf_name}!")
        print(s) 
        time.sleep(1)

# Test entry for journal article
if len(sys.argv) == 1:
    main()
if len(sys.argv) == 2 and (sys.argv[1] == "--usage" or sys.argv[1] == "--help"):
    usage()
elif len(sys.argv) == 2 and (sys.argv[1] == "-s" or sys.argv[1] == "--source"):
    print("Error: no source specified!")
    print(s) 
    time.sleep(1)
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
                print(s) 
                time.sleep(1)
                exit(1)
            elif sys.argv[i + 1][0] == "\"" and sys.argv[i + 1][len(sys.argv[i + 1]) - 1] == "\"":
                title = sys.argv[i + 1]
            else:
                print("Invalid title! Did you surround title with quotes?")
                print(s) 
                time.sleep(1)
        elif sys.argv[i] == "-a":
            if i == len(sys.argv) - 1:
                print("Error! No authors specified!")
                print(s) 
                time.sleep(1)
                exit(1)






