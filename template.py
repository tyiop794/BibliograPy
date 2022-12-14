from website import Website
from podcast import Podcast
from article import Article
from book import Book
from typing import List
"""
Reads a file containing source info and exports as a bibliographic
format of the users' choice.

Other thoughts: have separation of dates by both commas and em-dashes (currently
only using commas)
- each source separated by newline (\n)
"""

"""
Website info:
    def __init__(
        self, 
        title, 
        authors, 
        container, 
        date_published, 
        url, 
        accessed, 
        publisher
    ):

    Template:
    source :
    title :
    authors :
    container :
    date_published :
    url :
    accessed :
    publisher :
    - can be in any order (ideally)


Book info:
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

    Template:
    source :
    title :
    authors :
    date_published :
    digital :
    publication_place : 
    url :
    accessed :
    publisher : 

Article info:
    def __init__(
        self,
        title,
        authors,
        digital,
        journal,
        volume,
        issue,
        pages,
        date_published,
        url,
        accessed,
    ):
    Template:
    source :
    title :
    authors :
    digital :
    journal :
    volume :
    issue :
    pages :
    date_published :
    url : 
    accessed :

Podcast info:
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
        
    Template:
    source :
    host :
    title :
    publisher :
    podcast :
    date :
    url :
    duration :
"""


def read_from_file(input_file) -> List:
    sources = []
    source = ""
    read_source = []
    all_sources = []
    file = open(input_file, "r")
    line = file.readline()
    while line:
        while line != "\n" and line != "":
            read_source.append(line.strip())
            line = file.readline()
        if line == "\n":
            all_sources.append(read_source)
            read_source = []
            line = file.readline()
        if not line:
            break
    print(all_sources)
    for i in range(0, len(all_sources)):
        line = all_sources[i][0]
        line = line.split(":")
        line[0] = line[0].strip()
        if line[0] != "source":
            raise ValueError("Error! First line needs to specify source type!")
        elif line[0] == "source":
            source = line[1].strip()
            if source not in ["article", "book", "podcast", "website"]:
                raise ValueError("Error! Source not supported!")
        source = source.lower()
        if source == "article":
            all_sources[i].pop(0)
            article_template(all_sources[i], sources)
        elif source == "book":
            all_sources[i].pop(0)
            book_template(read_source, sources)
        elif source == "podcast":
            all_sources[i].pop(0)
            podcast_template(read_source, sources)
        elif source == "website":
            all_sources[i].pop(0)
            website_template(read_source, sources)
    return sources


def article_template(source, sources) -> None:
    author = ""
    title = ""
    digital = ""
    journal = ""
    volume = ""
    issue = ""
    pages = ""
    date_published = ""
    url = ""
    accessed = ""
    for i in range(0, len(source)):
        info = source[i]
        info = info.split(":")
        for x in range(0, len(info)):
            info[x] = info[x].strip()
        if info[0] == "authors":
            author = info[1]
        elif info[0] == "title":
            title = info[1]
        elif info[0] == "digital":
            digital = info[1]
        elif info[0] == "journal":
            journal = info[1]
        elif info[0] == "volume":
            volume = info[1]
        elif info[0] == "issue":
            issue = info[1]
        elif info[0] == "pages":
            pages = info[1]
        elif info[0] == "date_published":
            date_published = info[1]
        elif info[0] == "accessed":
            accessed = info[1]
        elif info[0] == "url":
            url = info[1]
    sources.append(Article(title, author, digital, journal, volume, issue, pages, date_published, url, accessed))


def website_template(source, sources) -> None:
    title = ""
    authors = ""
    container = ""
    date_published = ""
    url = ""
    accessed = ""
    publisher = ""
    for i in range(0, len(source)):
        info = source[i]
        info = info.split(":")
        for x in range(0, len(info)):
            info[x] = info[x].strip()
        if info[0] == "title":
            title = info[1]
        elif info[0] == "authors":
            authors = info[1]
        elif info[0] == "container":
            container = info[1]
        elif info[0] == "date_published":
            date_published = info[1]
        elif info[0] == "url":
            url = info[1]
        elif info[0] == "accessed":
            accessed = info[1]
        elif info[0] == "publisher":
            publisher = info[1]
    sources.append(Website(title, authors, container, date_published, url, accessed, publisher))


def podcast_template(source, sources) -> None:
    host = ""
    title = ""
    publisher = ""
    podcast = ""
    date = ""
    url = ""
    duration = ""
    for i in range(0, len(source)):
        info = source[i]
        info = info.split(":")
        for x in range(0, len(info)):
            info[x] = info[x].strip()
        if info[0] == "host":
            host = info[1]
        elif info[0] == "title":
            title = info[1]
        elif info[0] == "publisher":
            publisher = info[1]
        elif info[0] == "podcast":
            podcast = info[1]
        elif info[0] == "date":
            date = info[1]
        elif info[0] == "url":
            url = info[1]
        elif info[0] == "duration":
            duration = info[1]
    sources.append(Podcast(title, host, publisher, podcast, date, url, duration))


def book_template(source, sources) -> None:
    title = ""
    authors = ""
    date_published = ""
    digital = ""
    publication_place = ""
    url = ""
    publisher = ""
    pages = ""
    by_chapter = ""
    editors = ""
    chapter_title = ""
    for i in range(0, len(source)):
        info = source[i]
        info = info.split(":")
        for x in range(0, len(info)):
            info[x] = info[x].strip()
        if info[0] == "authors":
            authors = info[1]
        elif info[0] == "title":
            title = info[1]
        elif info[0] == "date_published":
            date_published = info[1]
        elif info[0] == "digital":
            digital = info[1]
        elif info[0] == "publication_place":
            publication_place = info[1]
        elif info[0] == "url":
            url = info[1]
        elif info[0] == "publisher":
            publisher = info[1]
        elif info[0] == "pages":
            pages = info[1]
        elif info[0] == "by_chapter":
            by_chapter = info[1]
        elif info[0] == "editors":
            editors = info[1]
        elif info[0] == "chapter_title":
            chapter_title = info[1]
    sources.append(Book(title,
                        authors,
                        editors,
                        publisher,
                        digital,
                        url,
                        publication_place,
                        date_published,
                        pages,
                        chapter_title,
                        by_chapter))
