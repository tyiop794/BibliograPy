from other_funcs import author_split, date_fix, citation_format
class Podcast:
    def __init__(self, title, host, publisher, podcast, date, url, duration):
        self.host = host
        self.title = title
        self.publisher = publisher
        self.podcast = podcast
        self.date = date_fix(date)
        self.url = url
        self.duration = duration
        if len(date) == 3:
            self.month = date[0]
            self.day = date[1]
            self.year = date[2]
        elif len(date) == 2:
            self.month = date[0]
            self.year = date[1]
        else:
            self.year = date[0]


    def mla(self):
        citation = ""
        if self.title != "":
            citation += f"\"{self.title}.\" "
        if self.podcast != "":
            citation += f"<em>{self.podcast}</em> "
        if self.publisher != "":
            citation += f"from {self.publisher}, "
        if self.year != "":
            try:
                citation += f"{self.day} {self.month} {self.year}, " 
            except NameError:
                try:
                    citation += f"{self.month} {self.year}, "
                except NameError:
                    citation += f"{self.year}, "
        if self.url != "":
            citation += f"{self.url}. "
        citation = citation.strip()
        if citation[len(citation) - 1] == ",":
            citation = citation[0:len(citation) - 1] + "."
        elif citation[len(citation) - 1].isalpha():
            citation = citation[0:len(citation)] + "."

    def apa(self):
        citation = ""
        if self.host != []:
            if len(self.host) == 1:
                citation += f"{self.host[0]}, {self.host[1][0]}. "
        if self.year != "":
            try:
                citation += f"({self.year}, {self.month} {self.day}). " 
            except NameError:
                try:
                    citation += f"({self.year}, {self.month}). "
                except NameError:
                    citation += f"({self.year}). "
        if self.title != "":
            citation += f"{self.title}. "
        if self.podcast != "":
            citation += f"In <em>{self.podcast}</em>. "
        if self.publisher != "":
            citation += f"{self.publisher}. "
        if self.url != "":
            citation += f"{self.url}"
        citation.strip()
        if citation[len(citation) - 1].isalpha():
            citation += "."
        elif citation[len(citation) - 1] == ",":
            citation = citation[0:len(citation) - 1] + "."
        return citation
    
    def chicago(self):
        citation = ""
        if self.host != []:
            if len(self.host) == 1:
                citation += f"{self.host[0][0]}, {self.host[0][1]}. "
            elif len(self.host) == 2:
                citation += f"{self.host[0][0]}, {self.host[0][1]} and {self.host[1][1]} {self.host[1][0]}. "
        if self.publisher != "":
            citation += f"Produced by {self.publisher}. "
        if self.podcast != "":
            citation += f"<em>{self.podcast}</em>. "
        if self.year != "":
            try:
                citation += f"{self.month} {self.day}, {self.year}. " 
            except NameError:
                try:
                    citation += f"{self.month} {self.year}. "
                except NameError:
                    citation += f"{self.year}. "
        if self.duration != "":
            citation += f"Podcast, MP3 audio, {self.duration}, "
        if self.url != "":
            citation += f"{self.url}. "
        citation.strip()
        if citation[len(citation) - 1].isalpha():
            citation += "."
        elif citation[len(citation) - 1] != ".":
            citation = citation[0:len(citation) - 1] + "."
        return citation

def podcast_ask(sources):
    title = input("Episode name?: ")
    host = input("Host?: ")
    publisher = input("Publisher?: ")
    podcast = input("Title of podcast?: ")
    date = input("Date of release (MM, DD, YYYY; MM, YYYY; or YYYY): ")
    url = input("URL?: ")
    duration = input("Duration? (H:M:S): ")
    sources.append(Podcast(title, host, publisher, podcast, date, url , duration))