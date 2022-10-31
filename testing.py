"""
Use this to test each class element; make sure nothin's weird.
"""

from book import *
from main import *
from podcast import *
from other_funcs import *
from website import *
from article import *

sources = []
book = Book(
    "1984", "", "b", "George Orwell", "", "", "Secker & Warburg", "p", "London", "", "4, 8, 2018"
)
book.output()
sources.append(book)

journal = Article(
    "Use of library space and the library as place",
    "Svanhild Aabo, Ragnar Audunson",
    "p",
    "Library & information science research",
    "34",
    "2",
    "138-149",
    "2012",
    "",
    "",
)

website = Website(
    "Book bans and 'gag orders': the US schools crackdown no one asked for",
    "Adam Gabbatt",
    "The Guardian",
    "2, 21, 2022",
    "https://www.theguardian.com/world/2022/feb/21/books-bans-gag-orders-suppress-discussion-racism-lgbtq-us-schools?CMP=Share_AndroidApp_Other",
    "4, 20, 2022",
    ""
)
journal.output()
sources.append(journal)
website.output()
sources.append(website)
export_entries(sources, "m")
