from other_funcs import author_split, date_fix, citation_format
class Article:
    def __init__(self, title, authors, digital, journal, volume, issue, pages, date_published, url, accessed):
        self.title = title
        self.authors = author_split(authors)
        print()
        self.digital = digital
        self.journal = journal
        self.volume = volume
        self.issue = issue
        self.pages = pages
        self.date_published = date_published;
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
        self.url = url
        new_accessed = date_fix(accessed)
        try:
            if len(new_accessed) == 3:
                self.ac_month = accessed[0]
                self.ac_day = accessed[1]
                self.ac_year = accessed[2]
            elif len(accessed) == 2:
                self.ac_month = accessed[0]
                self.ac_year = accessed[1]
            else:
                self.ac_year = accessed[0]
        except IndexError:
            self.ac_year = ""

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
        if self.year != "":
            citation += f"{self.year}, "
        if self.pages != "":
            citation += f"pp. {self.pages}. "
        citation = citation.strip()
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
                for i in range(0, len(self.authors)):
                    if i != (len(self.authors) - 1):
                        citation += f"{self.authors[i][0]}, {self.authors[i][1][0]}., "
                    else:
                        citation += f"& {self.authors[i][0]}, {self.authors[i][1][0]}. "
        if self.year != "": # Make sure formatting is right here!
            citation += f"({self.year}). "
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
        citation = citation.strip()
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
        citation = ""
        if self.authors != []:
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1]}. "
            elif len(self.authors) == 2:
                citation += f"{self.authors[0][0]}, {self.authors[0][1]} and {self.authors[1][1]} {self.authors[1][0]}. "
        if self.title != "":
            citation += f"\"{self.title}.\" "
        if self.journal != "":
            citation += f"<em>{self.journal}</em> "
        if self.volume != "":
            citation += f"{self.volume}, "
        if self.issue != "":
            citation += f"no. {self.issue} "
        if self.year != "":
            citation += f"({self.year}): "
        if self.pages != "":
            citation += f"{self.pages}."
        citation = citation.strip()
        if citation[len(citation) - 1] != ".":
            citation = citation[0:len(citation) - 1] + "."
        return citation
        


    def output(self):
        print("Title: " + self.title)
        if len(self.authors) == 1:
            print("Author(s): " + self.authors[0][1] + " " + self.authors[0][0])
        elif len(self.authors) == 2:
            print("Author(s): " + self.authors[0][1] + " " + self.authors[0][0] + " and "
            + self.authors[1][1] + self.authors[1][0])
        else:
            print("Author(s): ", end='')
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

def article_ask(sources):
        title = input("Article title?: ")
        authors = input("Authors (Full names split by comma; if known, order by importance): ")
        journal = input("Journal title?: ")
        volume = input("Volume?: ")
        issue = input("Issue?: ")
        pages = input("Page numbers? (first-last): ")
        date_published = input("Date published (MM, DD, YYYY; MM, YYYY; or YYYY): ")
        date_accessed = input("Date accessed? (MM, DD, YYYY; MM, YYYY; or YYYY): ")
        while True:
            digital = input("Physical (p) or digital (d)?: ")
            if digital != "p" and digital != "d":
                print("Invalid input! Asking again!")
            else:
                break
        if digital == "d":
            url = input("URL/DOI?: ")
        else:
            url = "" 
        sources.append(Article(title, authors, digital, journal, volume, issue, pages, date_published, url, date_accessed))