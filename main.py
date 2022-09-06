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
   such as MLA 8th edition)
 - create a GUI using tkinter or curses (that's a maybe?)
 - try looking up unknown information about source and filling in missing bits in citation

"""
import sys
import os
import datetime
import curses
import pdfkit
import tkinter as tk
from tkinter import filedialog

class Podcast:
    def __init__(self, title, authors):
        pass

# Refers to scholarly article
class Article:
    def __init__(self, title, authors, digital, journal, volume, issue, pages, date_published, url=None):
        self.title = title
        self.authors = authors
        self.digital = digital
        self.journal = journal
        self.volume = volume
        self.issue = issue
        self.pages = pages
        self.date_published = date_published
        self.url = url
    
    def mla(self):
        citation = ""
        if self.authors != []:
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1]}. "
            elif len(self.authors) == 2:
                print(self.authors[0][0] < self.authors[1][0])
                if self.authors[0][0] < self.authors[1][0]:
                    citation += f"{self.authors[0][0]}, {self.authors[0][1]} and {self.authors[1][1]} {self.authors[1][0]}. "
                else:
                    citation += f"{self.authors[1][0]}, {self.authors[1][1]} and {self.authors[0][1]} {self.authors[0][0]}. "
        if self.title != "": 
            citation += f"{self.title}. "
        if self.journal != "":
            citation += f"<em>{self.journal}</em>, "
        if self.volume != "":
            citation += f"vol. {self.volume}, "
        if self.issue != "":
            citation += f"no. {self.issue}, "
        if self.date_published != "":
            citation += f"{self.date_published}, "
        if self.pages != "":
            citation += f"pp. {self.pages}. "
        citation.strip()
        new_citation = ""
        cnt = 0
        for i in range(0, len(citation)):
            new_citation += citation[i]
            """
            if i == 90:
               new_citation += "\n     " 
               cnt += 1
            elif i == (90 + (75 * cnt)):
                new_citation += "     "
                cnt += 1
            """
        if new_citation[len(new_citation) - 1] == ",":
            new_citation = new_citation[0:len(new_citation) - 1] + "."
        return new_citation
            
    def apa(self):
        citation = ""
        if self.authors != []:
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1][0]}. "
            elif len(self.authors) == 2:
                citation += f"{self.authors[0][0]}, {self.authors[0][1][0]}., & {self.authors[1][0]}, {self.authors[1][1][0]}. "
            else:
                print("Placeholder boi")
        if self.date_published != "":
            citation += f"({self.date_published}). "
        if self.title != "":
            citation += f"{self.title}. "
        if self.journal != "":
            citation += f"<em>{self.journal}</em>, "
        if self.volume != "":
            citation += f"<em>{self.volume}</em>"
        if self.issue != "":
            citation += f"({self.issue}), "
        if self.pages != "":
            citation += f"{self.pages}. "
        if self.digital == "d":
            citation += f"{self.url}"
        citation.strip()
        new_citation = ""
        cnt = 0
        for i in range(0, len(citation)):
            new_citation += citation[i]
            """
            if i == 90:
                new_citation += "\n     " 
                cnt += 1
            elif i == (90 + (75 * cnt)):
                new_citation += "     "
                cnt += 1
            """
        if new_citation[len(new_citation) - 1] == ",":
            new_citation = new_citation[0:len(new_citation) - 1] + "."
        return new_citation 

    def chicago(self):
        print()

    def output(self):
        print("Title: " + self.title)
        if len(self.authors) == 1:
            print("Author(s): " + self.authors[0][1] + " " + self.authors[0][0])
        elif len(self.authors) == 2:
            print("Author(s): " + self.authors[0][1] + " " + self.authors[0][0] + " and "
            + self.authors[1][1] + self.authors[1][0])
        else:
            print("Authors: ", end='')
            for i in range(0, len(self.authors)):
                if i == (len(self.authors) - 1):
                    print("and " + self.authors[i][1] + self.authors[i][0])
                else:
                    print(self.authors[i][1] + self.authors[i][0] + ", ", end='')
        if self.digital == "p":
            digital = "No"
        elif self.digital == "d":
            digital = "Yes"
        print("Digital: " + digital)
        print("Journal: " + self.journal)
        print("Volume: " + self.volume)
        print("Issue: " + self.issue)
        print("Pages: " + self.pages)
        print("Year published: " + self.date_published)
        if self.digital == "d":
            print("URL/DOI: " + self.url)


class Book:
    def __init__(self, title, authors, date_published, publisher, digital,  url=None): 
        self.title = title
        self.authors = authors
        self.date_published = date_published
        self.publisher = publisher
        self.digital = digital
        self.url = url

    def mla(self):
        citation = ""
        if self.authors != []:
            authors = self.authors
            for i in range(0, len(authors)):
                if len(authors) == 1:
                    citation += f"{authors[0][0]}, {authors[0][1]}. "
                elif len(authors) == 2:
                    if i == 0:
                        citation += f"{authors[0][0]}, {authors[0][1]}. "
                    elif i == 1:
                        citation += f"{authors[1][1]} {authors[1][0]}. "
        if self.title != "":
            citation += f"<em>{self.title}</em>. "
        if self.publisher != "":
            citation += f"{self.publisher}, "
        if self.date_published != "":
            citation += f"{self.date_published}, "
        citation.strip()
        new_citation = ""
        cnt = 0
        for i in range(0, len(citation)):
            new_citation += citation[i]
            """
            if i == 90:
                new_citation += "\n     " 
                cnt += 1
            elif i == (90 + (75 * cnt)):
                new_citation += "     "
                cnt += 1
            """
        if new_citation[len(new_citation) - 1] == ",":
            new_citation = new_citation[0:len(new_citation) - 1] + "."
        return new_citation
    
    def apa(self):
        citation = ""
        if self.authors != []:
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1][0]}. "
            elif len(self.authors) == 2:
                citation += f"{self.authors[0][0]}, {self.authors[0][1][0]}., & {self.authors[1][0]}, {self.authors[1][1][0]}. "
            elif len(self.authors) > 2 and len(self.authors) <= 20:
                print("Placeholder boi")
                print("More than two authors oh dear")
                for i in range(0, len(self.authors)):
                    citation += f"{self.authors[i][0]}, {self.authors[0][1][0]},"
        if self.date_published != "":
            citation += f"({self.date_published}). "
        if self.title != "":
            citation += f"<em>{self.title}</em>. " 
        if self.publisher != "":
            citation += f"{self.publisher}. "
        if self.digital == "d":
            citation += f"{self.url}"
        citation.strip()
        new_citation = ""
        cnt = 0
        for i in range(0, len(citation)):
            new_citation += citation[i]
            if i == 90:
                new_citation += "\n     " 
                cnt += 1
            elif i == (90 + (75 * cnt)):
                new_citation += "     "
                cnt += 1
        if new_citation[len(new_citation) - 1] == ",":
            new_citation = new_citation[0:len(new_citation) - 1] + "."
        return new_citation 

    def output(self):
        """
        self.title = title
        self.authors = authors
        self.date_published = date_published
        self.publisher = publisher
        self.digital = digital
        self.url = url
        """
        print("Title: " + self.title)
        if len(self.authors) == 1:
            print("Author(s): " + self.authors[0][1] + " " + self.authors[0][0])
        elif len(self.authors) == 2:
            print("Author(s): " + self.authors[0][1] + " " + self.authors[0][0] + " and "
            + self.authors[1][1] + self.authors[1][0])
        else:
            print("Authors: ", end='')
            for i in range(0, len(self.authors)):
                if i == (len(self.authors) - 1):
                    print()
                    print("and " + self.authors[i][1] + self.authors[i][0])
                else:
                    print(self.authors[i][1] + self.authors[i][0] + ", ", end='')
        print("Publisher: " + self.publisher)
        if self.digital == "d":
            digital = "Yes"
        elif self.digital == "p":
            digital = "No"
        print("Digital: " + digital)
        if self.digital == "d":
            print("URL/DOI: " + self.url)

    def chicago(sources):
        print()


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
    #file = open("biblio.html", "w") 
    #file.write(html)
    #file.close()
    print("Exporting as PDF:")
    pdf_name = filedialog.asksaveasfilename()
    pdfkit.from_string(html, pdf_name) 
    


def main():
    while True:
        sources = []
        print("Welcome to BibliograPy!")
        biblio = ""
        while biblio not in ["m", "a", "c", "i"]:
            biblio = input("Will bibliography be in MLA (9th edition) (m), APA (a), Chicago (c), or IEEE (i)?: ")
            if biblio not in ["m", "a", "c", "i"]:
                print("Not possible! Asking again!")
        print("For each entry type in information from the source you are trying to cite")
        print("(or leave blank if information is unknown)")
        print()
        while True:
            authors = []
            source = input("Type of source (j for scholarly article, b for book, a for audio/podcast): ")
            if source == "j":
                digital = input("Physical or digital (p for physical, d for digital): ")
            title = input("Title of work?: ")
            try:
                author_no = int(input("Number of authors (default is 1): "))
            except ValueError:
                author_no = 1
            if author_no > 1:
                for i in range(0, author_no):
                    lastname = input(f"Last name of author {i + 1}: ")
                    firstname = input(f"First name of author {i + 1}: ")
                    authors.append((lastname, firstname))
            else:
                lastname = input("Last name of author?: ")
                firstname = input("First name of author?: ")
                authors.append((lastname, firstname))
            date_published = input("Year of publication? (YYYY): ")
            if source == "b":
                publisher = input("Publisher?: ")
            if digital == "d":
                url = input("URL/DOI? (address of website typed into webbrowser): ")
            if source == "j":
                journal = input("Journal of publication?: ")
                pages = input("Article pages? (page-page): ")
                issue = input("Article issue? (no. only): ")
                volume = input("Journal volume?: ")
            if source == "b":
                sources.append(Book(title, authors, digital, date_published, publisher, url))
            elif source == "j":
                sources.append(Article(title, authors, digital, journal, volume, issue, pages, date_published))
            print("Current sources added: ")
            for i in range(0, len(sources)):
                sources[i].output()
            source_add = input("Add another source? (Y/n): ")
            if source_add == "n":
                break
        export_entries(sources, biblio) 
        print("Entries successfully exported as biblio.pdf!")

# Test entry for journal article
source = Article("Use of library space and the library as place", [("Aabo", "Svanhild"), ("Audunson", "Ragnar")], "p", "Library & information science research", "34", "2", "138-149", "2012")
sources = []
sources.append(source)
source = Article("The role and value of public libraries in the age of digital technologies", [("Aabo", "Svanhild")], "p", "Journal of librarianship and information science", "37", "2", "205-211", "2005")
sources.append(source)
export_entries(sources, "a") 

    

