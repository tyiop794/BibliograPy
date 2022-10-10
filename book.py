from typing import List

from other_funcs import author_split, citation_format, date_fix


class Book:
    """
    To-do list:
    Ask for page numbers.
    Only ask for year of publication (full date not needed).
    Cite specific essay in a collection book (essay by one author)
    Cite a specific chapter
    """
    def __init__(
        self,
        title,
        chapter_title,
        by_chapter,
        authors,
        editors,
        date_published,
        publisher,
        digital,
        publication_place,
        url,
        pages
    ):
        self.title = title
        self.authors = author_split(authors)
        self.editors = author_split(editors)
        self.publisher = publisher
        self.digital = digital
        self.url = url
        self.publication_place = publication_place
        self.date_published = date_published
        self.pages = pages
        self.chapter_title = chapter_title
        self.by_chapter = by_chapter
        newdate = date_fix(date_published)
        if len(newdate) == 3:
            self.month = newdate[0]
            self.day = newdate[1]
            self.year = newdate[2]
        elif len(newdate) == 2:
            self.month = newdate[0]
            self.year = newdate[1]
        else:
            self.year = newdate[0]
        """
        self.accessed = accessed
        new_accessed = date_fix(accessed)
        try:
            if len(new_accessed) == 3:
                self.ac_month = new_accessed[0]
                self.ac_day = new_accessed[1]
                self.ac_year = new_accessed[2]
            elif len(new_accessed) == 2:
                self.ac_month = new_accessed[0]
                self.ac_year = new_accessed[1]
            else:
                self.ac_year = new_accessed[0]
        except IndexError:
            self.ac_year = ""
        """

    def mla(self) -> str:
        """Builds citation string for MLA Style Citation."""
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

    def apa(self) -> str:
        """Builds citation string for APA Style Citation."""
        citation = ""
        if self.authors != []:
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1][0]}. "
            elif len(self.authors) == 2:
                citation += f"{self.authors[0][0]}, {self.authors[0][1][0]}., & {self.authors[1][0]}, {self.authors[1][1][0]}. "
            else:
                for i in range(0, len(self.authors)):
                    if i != (len(self.authors) - 1):
                        citation += f"{self.authors[i][0]}, {self.authors[i][1][0]}., "
                    else:
                        citation += f"& {self.authors[i][0]}, {self.authors[i][1][0]}. "
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

    def chicago(self) -> str:
        """Builds citation string for Chicago Style Citation."""
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
        """Outputs user entered information."""
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
        else:
            digital = "No"
        print("Digital: " + digital)
        if self.digital == "d":
            print("URL/DOI: " + self.url)


def book_ask(sources: List) -> None:
    """Prompts for inputting information about a Book source."""
    title = input("Title?: ")
    by_chapter = ""
    while by_chapter not in ["b", "c"]:
        by_chapter = input("Whole book by one author (b) or by chapter (multiple authors) (c)?: ")
        if by_chapter not in ["b", "c"]:
            print("Invalid response! Asking again.")
    if by_chapter == "b":
        authors = input("Author(s)? (first and last name; each full name split by comma): ")
        editors = ""
        chapter_title = ""
        pages = ""
    else:
        editors = input("Editor(s) of full book? (first and last name; each full name split by comma): ")
        chapter_title = input("Chapter title?: ")
        pages = input("Page numbers of chapter? (First-Last): ")
        authors = input("Author(s) of chapter? (first and last name; each full name split by comma): ")
    date_published = input("Year published?: ")
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
    # accessed = input("Date accessed (MM, DD, YYYY; MM, YYYY; or YYYY): ")
    sources.append(
        Book(
            title,
            chapter_title,
            by_chapter,
            authors,
            editors,
            date_published,
            publisher,
            digital,
            publication_place,
            url,
            pages
            # accessed,
        )
    )
