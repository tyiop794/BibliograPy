from other_funcs import author_split, date_fix, citation_format
class Website:
    def __init__(self, title, authors, container, date_published, url, accessed, publisher):
        self.title = title
        self.authors = author_split(authors)
        self.container = container
        self.url = url
        self.accessed = date_fix(accessed)
        if len(accessed) == 3:
            self.ac_month = accessed[0]
            self.ac_day = accessed[1]
            self.ac_year = accessed[2]
        elif len(accessed) == 2:
            self.ac_month = accessed[0]
            self.ac_year = accessed[1]
        else:
            self.ac_year = accessed[0]
        self.date_published = date_fix(date_published)
        self.publisher = publisher
        if len(date_published) == 3:
            self.month = date_published[0]
            self.day = date_published[1]
            self.year = date_published[2]
        elif len(date_published) == 2:
            self.month = date_published[0]
            self.year = date_published[1]
        else:
            self.year = date_published[0]
    
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
        if self.url != "":
            citation += f"{self.url}. "
        if self.ac_year != "":
            try:
                citation += f"Accessed {self.ac_day} {self.ac_month}. {self.ac_year}. "
            except NameError:
                try:
                    citation += f"Accessed {self.ac_month}. {self.ac_year}. "
                except NameError:
                    citation += f"Accessed {self.ac_year}. "
        citation.strip()
        citation = citation_format(citation)
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
        citation = citation_format(citation)

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
        citation = citation_format(citation)

def web_ask(sources):
    title = input("Website article title?: ")
    authors = input("Authors? (First and last name; separate each full name by comma): ")
    container = input("Website name?: ")
    publisher = input("Publisher?: ")
    url = input("Website URL?: ")
    accessed = input("Date accessed? (MM, DD, YYYY; MM, YYYY;, or YYYY): ")
    date_published = input("Date published? (MM, DD, YYYY; MM, YYYY;, or YYYY): ")
    sources.append(Website(title, authors, container, date_published, url, accessed, publisher))