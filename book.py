from other_funcs import date_fix, author_split, citation_format
from datetime import datetime


class Book:
    def __init__(
        self,
        title,
        authors,
        date_published,
        publisher,
        digital,
        publication_place,
        url,
        accessed,
    ):
        self.title = title
        self.authors = author_split(authors)
        self.publisher = publisher
        self.digital = digital
        self.url = url
        self.publication_place = publication_place
        self.date_published = date_published
        newdate = date_fix(date_published)
        print(newdate)
        if len(newdate) == 3:
            self.month = newdate[0]
            self.day = newdate[1]
            self.year = newdate[2]
        elif len(newdate) == 2:
            self.month = newdate[0]
            self.year = newdate[1]
        else:
            self.year = newdate[0]
        print(self.year)
        self.accessed = accessed
        new_accessed = date_fix(accessed)
        try:
            if len(new_accessed) == 3:
                self.ac_month = newdate[0]
                self.ac_day = newdate[1]
                self.ac_year = newdate[2]
            elif len(new_accessed) == 2:
                self.ac_month = newdate[0]
                self.ac_year = newdate[1]
            else:
                self.ac_year = newdate[0]
        except IndexError:
            self.ac_year = ""

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
        if self.year != "":
            citation += f"{self.year}. "
        citation = citation.strip()
        citation = citation_format(citation)
        return citation

    def apa(self):
        citation = ""
        if self.authors != []:
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1][0]}. "
            elif len(self.authors) == 2:
                citation += f"{self.authors[0][0]}, {self.authors[0][1][0]}., & {self.authors[1][0]}, {self.authors[1][1][0]}. "
            elif len(self.authors) > 2 and len(self.authors) <= 20:
                # Finish writing this!!!!
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
        citation = citation.strip()
        if citation[len(citation) - 1] != ".":
            citation = citation[0 : len(citation) - 1] + "."
        return citation

    def chicago(self):
        citation = ""
        if self.authors != []:
            # Is this the same for journal citation?
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1]}. "
            elif len(self.authors) == 2:
                citation += f"{self.authors[0][0]}, {self.authors[0][1]} and {self.authors[0][1]}{self.authors[0][0]}. "
        if self.title != "":
            citation += f"<em>{self.title}</em>. "
        if self.publication_place != "":
            citation += f"{self.publication_place}: "
        if self.publisher != "":
            citation += f"{self.publisher}, "
        if self.date_published != "":
            citation += f"{self.date_published}. "
        citation = citation.strip()
        if citation[len(citation) - 1] != ".":
            citation = citation[0 : len(citation) - 1] + "."
        return citation

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
            print(
                "Author(s): "
                + self.authors[0][1]
                + " "
                + self.authors[0][0]
                + " and "
                + self.authors[1][1]
                + self.authors[1][0]
            )
        else:
            print("Authors: ", end="")
            for i in range(0, len(self.authors)):
                if i == (len(self.authors) - 1):
                    print()
                    print("and " + self.authors[i][1] + self.authors[i][0])
                else:
                    print(self.authors[i][1] + self.authors[i][0] + ", ", end="")
        print("Publisher: " + self.publisher)
        if self.digital == "d":
            digital = "Yes"
        elif self.digital == "p":
            digital = "No"
        print("Digital: " + digital)
        if self.digital == "d":
            print("URL/DOI: " + self.url)


def book_ask(sources):
    title = input("Title?: ")
    authors = input("Author(s)? (first and last name; each full name split by comma): ")
    date_published = input("Date published? (MM, DD, YYYY; MM, YYYY; or YYYY): ")
    publisher = input("Publisher?: ")
    digital = input("Physical (p) or digital (d)?: ")
    while True:
        if digital != "d" and digital != "p":
            print("Invalid input! Asking again!")
        else:
            break
    if digital == "d":
        url = input("URL/DOI?: ")
    else:
        url = ""
    publication_place = input("Place of publication?: ")
    accessed = input("Date accessed (MM, DD, YYYY; MM, YYYY; or YYYY): ")
    sources.append(
        Book(
            title,
            authors,
            date_published,
            publisher,
            digital,
            publication_place,
            url,
            accessed,
        )
    )
