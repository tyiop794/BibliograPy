from other_funcs import author_split, citation_format, date_fix


class Website:
    def __init__(
        self, title, authors, container, date_published, url, accessed, publisher
    ):
        self.title = title
        if authors != "":
            self.authors = author_split(authors)
        else:
            self.authors = ""
        self.container = container
        self.url = url
        if accessed != "":
            accessed = date_fix(accessed)
            if len(accessed) == 3:
                self.ac_month = accessed[0]
                self.ac_day = accessed[1]
                self.ac_year = accessed[2]
            elif len(accessed) == 2:
                self.ac_month = accessed[0]
                self.ac_year = accessed[1]
            else:
                self.ac_year = accessed[0]
        else:
            self.accessed = ""
        self.publisher = publisher
        if date_published != "":
            date_published = date_fix(date_published)
            if len(date_published) == 3:
                self.month = date_published[0]
                self.day = date_published[1]
                self.year = date_published[2]
            elif len(date_published) == 2:
                self.month = date_published[0]
                self.year = date_published[1]
            else:
                self.year = date_published[0]
        else:
            self.year = ""

    def mla(self) -> str:
        """Builds citation string for MLA Style Citation."""
        citation = ""
        # Add multiple authors
        if self.authors != []:
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1]}. "
        if self.title != "":
            citation += f'"{self.title}"'
        if self.container != "":
            citation += f"<em>{self.container}</em>, "
        if self.publisher != "":
            citation += f"{self.publisher}, "
        if self.year != "":
            citation += f"{self.year}, "
        if self.year != "":
            try:
                citation += f"({self.year}, {self.month} {self.day}). "
            except AttributeError:
                try:
                    citation += f"({self.year}, {self.month}). "
                except AttributeError:
                    citation += f"({self.year}). "
        else:
            citation += "(n.d.). "
        if self.url != "":
            citation += f"{self.url}. "
        if self.ac_year != "":
            try:
                citation += f"Accessed {self.ac_day} {self.ac_month}. {self.ac_year}. "
            except AttributeError:
                try:
                    citation += f"Accessed {self.ac_month}. {self.ac_year}. "
                except AttributeError:
                    citation += f"Accessed {self.ac_year}. "
        citation.strip()
        citation = citation_format(citation)
        return citation

    def apa(self) -> str:
        """Builds citation string for APA Style Citation."""
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
            except AttributeError:
                try:
                    citation += f"({self.year}, {self.month}). "
                except AttributeError:
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
        return citation

    def chicago(self) -> str:
        """Builds citation string for Chicago Style Citation."""
        citation = ""
        if self.authors == []:
            # Add multiple authors
            if len(self.authors) == 1:
                citation += f"{self.authors[0][0]}, {self.authors[0][1]}. "
        if self.title != "":
            citation += f'"{self.title}." '
        if self.container != "":
            citation += f"{self.container}. "
        if self.publisher != "":
            citation += f"{self.publisher}. "
        # Fix the date, yeesh! (Good here [i think])
        if self.year != "":
            try:
                citation += f"{self.month} {self.day}, {self.year}. "
            except AttributeError:
                try:
                    citation += f"{self.month} {self.year}. "
                except AttributeError:
                    citation += f"{self.year}. "
        if self.url != "":
            citation += f"{self.url}. "
        citation = citation.strip()
        citation = citation_format(citation)
        return citation

    def output(self):
        """Outputs user entered information."""
        """
        self.title = title
        if authors != "":
            self.authors = author_split(authors)
        self.container = container
        self.url = url
        if accessed != "":
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
        """
        print(f"Title: {self.title}")
        print("Author(s): ", end="")
        if len(self.authors) == 0:
            print("N/A")
        elif len(self.authors) == 1:
            print(f"{self.authors[0][1]} {self.authors[0][0]}")
        else:
            author_string = ""
            for i in range(0, len(self.authors) - 1):
                author_string += f"{self.authors[i][1]} {self.authors[i][0]}, "
            author_string += f"{self.authors[len(self.authors) - 1][1]} {self.authors[len(self.authors) - 1][0]}"
            print(author_string)
        if self.accessed != "":
            try:
                print(f"Access date: {self.ac_month} {self.ac_day}, {self.ac_year}")
            except AttributeError:
                try:
                    print(f"Access date: {self.ac_month} {self.ac_year}")
                except AttributeError:
                    print(f"Access date: {self.ac_year}")
        else:
            print("Accessed: N/A")
        if self.container != "":
            print(f"Website: {self.container}")
        else:
            print("Website: N/A")
        print("Publisher: ", end="")
        if self.publisher != "":
            print(f"{self.publisher}")
        else:
            print("N/A")
        print("URL/DOI: ", end="")
        if self.url != "":
            print(f"{self.url}")
        else:
            print("N/A")
        print("Publication date: ", end="")
        if self.year != "":
            try:
                print(f"{self.month} {self.day}, {self.year}")
            except AttributeError:
                try:
                    print(f"{self.month} {self.year}")
                except AttributeError:
                    print(f"{self.year}")


def web_ask(sources) -> None:
    """Prompts for inputting information about a Web Article source."""
    title = input("Website article title?: ")
    authors = input(
        "Authors? (First and last name; separate each full name by comma): "
    )
    container = input("Website name?: ")
    publisher = input("Publisher?: ")
    url = input("Website URL?: ")
    accessed = input("Date accessed? (MM, DD, YYYY; MM, YYYY;, or YYYY): ")
    date_published = input("Date published? (MM, DD, YYYY; MM, YYYY;, or YYYY): ")
    sources.append(
        Website(title, authors, container, date_published, url, accessed, publisher)
    )
