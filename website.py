from datetime import datetime
class Website:
    def __init__(self, title, authors, container, date_published, url, accessed):
        self.title = title
        self.authors = authors
        self.authors = self.authors.split(",")
        array = []
        for i in range(0, len(self.authors)):
            author_split = self.authors[i].split()
            array.append((author_split[1], author_split[0]))
        self.authors = array
        self.container = container
        self.url = url
        self.accessed = accessed
        self.date_published = date_published
        self.date_published = self.date_published.split(",")
        if len(self.date_published) == 1:
            self.year = self.date_published[0]
        elif len(self.date_published) == 2:
            self.month = self.date_published[0]
            self.month = datetime.datetime.strptime(self.month, "%m").strftime("%b")
            self.year = self.date_published[1]
        elif len(self.date_published) == 3:
            self.month = self.date_published[0]
            self.month = datetime.datetime.strptime(self.month, "%m").strftime("%b")
            self.day = self.date_published[1]
            self.year = self.date_published[2]
        else:
            self.year = ""

    
    def mla(self):
        citation = ""
        # Add multiple authors
        if self.authors != []:
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1]}. "
        if self.title != "":
            citation += f"\"{self.title}\""
        if self.container != "":
            citation += f"<em>{self.container}</em>, "
        if self.publisher != "":
            citation += f"{self.publisher}, "
        if self.year != "":
            citation += f"{self.year}, "
        if self.url != "":
            citation += f"{self.url}. "
        if self.accessed != "":
            accessed = self.accessed.split(",")
            if len(accessed) == 1:
                year = accessed[0]
                citation += f"Accessed {year}. "
            elif len(accessed) >= 2:
                if len(accessed) == 3:
                    month = accessed[0]
                    day = accessed[1]
                    year = accessed[2]
                    month_obj = datetime.datetime.strptime(month, "%m")
                    month_name = month_obj.strftime("%b")
                    citation += f"Accessed {day} {month_name}. {year}. " 
                else:
                    month = accessed[0]
                    year = accessed[1]
                    month_obj = datetime.datetime.strptime(month, "%m")
                    month_name = month_obj.strftime("%b")
                    citation += f"Accessed {month_name}. {year}. " 
        citation.strip()
        if citation[len(citation) - 1].isalpha():
            citation += "."
        elif citation[len(citation) - 1] != ".":
            citation = citation[0:len(citation)] + "."
        return citation

    def apa(self):
        citation = ""
        # Add multiple authors
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
        elif self.publisher != "":
            citation += f"{self.publisher}. "
        if self.year != "":
            try:
                citation += f"({self.year}, {self.month} {self.day}). " 
            except NameError:
                try:
                    citation += f"({self.year}, {self.month}). "
                except NameError:
                    citation += f"({self.year}). "
        else:
            citation += "(n.d.). "
        if self.title != "":
            citation += f"<em>{self.title}</em>. "
        if self.container != "":
            citation += f"{self.container}. "
        if self.accessed != "":
            citation += f"Retrieved {self.accessed}, "
        if self.url != "":
            citation += f"from {self.url} "
        citation.strip()
        if citation[len(citation) - 1] == ",":
            citation = citation[0:len(citation) - 1] + "."
        return citation

    def chicago(self):
        citation = ""
        if self.authors == []:
            # Add multiple authors
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1]}. "
        if self.title != "":
            citation += f"\"{self.title}.\" "
        if self.container != "":
            citation += f"{self.container}. "
        if self.publisher != "":
            citation += f"{self.publisher}. "
        # Fix the date, yeesh! (Good here [i think])
        if self.year != "":
            try:
                citation += f"{self.month} {self.day}, {self.year}. " 
            except NameError:
                try:
                    citation += f"{self.month} {self.year}. "
                except NameError:
                    citation += f"{self.year}. "
        if self.url != "":
            citation += f"{self.url}. "
        citation.strip()
        if citation[len(citation) - 1].isalpha():
            citation += "."
        elif citation[len(citation) - 1] != ".":
            citation = citation[0:len(citation) - 1] + "."
        return citation

def web_ask(sources):
    title = input("Website article title?: ")
    authors = input("Authors? (First and last name; separate each full name by comma): ")
    container = input("Website name?: ")
    url = input("Website URL?: ")
    accessed = input("Date accessed? (MM, DD, YYYY; MM, YYYY;, or YYYY): ")
    date_published = input("Date published? (MM, DD, YYYY; MM, YYYY;, or YYYY): ")
    sources.append(Website(title, authors, container, date_published, url, accessed))