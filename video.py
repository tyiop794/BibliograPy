"""
Video citation support
"""
from other_funcs import author_split
from other_funcs import citation_format

class Movie:
    def __init__(self, title, directors, performers, distributor, year):
        self.title = title
        self.directors = author_split(directors)
        self.performers = author_split(performers)
        self.distributor = distributor
        self.year = year

    def mla(self):
        citation = ""
        if self.title != "":
            citation += f"<em>{self.title}</em>. "
        if self.directors != []:
            for i in range(0, len(self.directors)):
                if i == 0:
                    citation += f"Directed by {self.directors[i][1]} {self.directors[i][0]}"
                elif i > 0 and i != len(self.directors) - 1:
                    citation += f", {self.directors[i][1]} {self.directors[i][0]}"
                else:
                    citation += f", and {self.directors[i][1]} {self.directors[i][0]}, "
        if self.performers != []:
            for i in range(0, len(self.performers)):
                if i == 0:
                    citation += f"performances by {self.performers[i][1]} {self.performers[i][0]}"
                elif i > 0 and i != len(self.performers) - 1:
                    citation += f", {self.performers[i][1]} {self.performers[i][0]}"
                else:
                    citation += f", and {self.performers[i][1]} {self.performers[i][0]}, "
        if self.distributor != "":
            citation += f"{self.distributor}, "
        if self.year != "":
            citation += f"{self.year}"
        citation = citation.strip()
        citation = citation_format(citation)
        return citation
