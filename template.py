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

from website import Website
from podcast import Podcast
from article import Article
from book import Book

def read_from_file(input_file):
    sources = []
    read_source = [] 
    all_sources = []
    file = open(input_file, "r")
    line = file.readline()
    while True:
        while line != "\n":
            read_source.append(line.strip())  
            line = file.readline()
        if line == "\n":
            all_sources.append(read_source)
        if not line:
            break   
    for i in range(0, len(all_sources)):
        line = all_sources[i][0]
        line = line.split(":")
        if line[0] != "source":
            raise ValueError("Error! First line needs to specify source type!")
        elif line[0] == "source":
            source = line[1].strip()
            if source not in ["article", "book", "podcast", "website"]:
                raise ValueError("Error! Source not supported!")
        if source == "article":
            read_source.pop(0)
            article_template(read_source, sources)
        elif source == "book":
            book_template(read_source, sources)
        elif source == "podcast":
            podcast_template(read_source, sources)
        elif source == "website":
            website_template(read_source, sources)

def article_template(source, sources):
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


def website_template(source, sources):
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

def podcast_template(source, sources):
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
        

def book_template(source, sources):
    title = ""
    authors = ""
    date_published = ""
    digital = ""
    publication_place = ""
    url = ""
    accessed = ""
    publisher = ""
    for i in range(0, len(source)):
        info = source[i]
        info = info.split(":")
        for x in range(0, len(info)):
            info[x] = info[x].strip()
        if info[0] == "authors":
            author = info[1]
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
        elif info[0] == "accessed":
            accessed = info[1]
        elif info[0] == "publisher":
            publisher = info[1]
    sources.append(Book(title, authors, date_published, publisher, digital, publication_place, url, accessed))
    