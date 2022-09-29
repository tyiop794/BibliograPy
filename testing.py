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
book = Book("1984", "George Orwell", "", "Secker & Warburg", "p", "London", "", "4, 8, 2018")
book.output()
sources.append(book)

journal = Article("Use of library space and the library as place", "Svanhild Aabo, Ragnar Audunson", "p", "Library & information science research", "34", "2", "138-149", "2012", "", "")
journal.output()
sources.append(journal)
export_entries(sources, "a")



