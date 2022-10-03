# Add option to create structured bibliography from file created by BibliograPy
# or using other files from other bibliography utilities
# Easily create file in format compatible with BibliograPy! (wanted feature)
usage_def = """BibliograPy version 1.0:

with no options: run in interactive mode
with options: provide source info in CLI

Options:
with no options: run in interactive mode

-s, --source: source type (article (a), website (w), podcast (p), book (b))
-c, --citation: citation format (MLA (m), APA (a), Chicago/Turabian (c))

For more specific info, provide the source type and citation format before
adding --usage flag.

--tui: work in progress
"""

"""
def __init__(self, title, authors, date_published, publisher, digital, publication_place, url, accessed): 
    self.title = title
    self.authors = authors
    self.date_published = date_published
    self.publisher = publisher
    self.digital = digital
    self.url = url
    self.publication_place = publication_place
    self.accessed = accessed
"""
usage_book = """Book source options:
(using all options not necessary)
(surround info specified with quotes)
-t, --title: title of book in quotes (i.e. "Nineteen Eighty-Four")
-a, --authors: list of author or authors (First name and last name; full names split by commas)
(ex. "John Doe, Johnny Appleseed")
-d, --date: Date published (MM, DD, YYYY; MM, YYYY; or YYYY)
-u, --url: URL 
   -a, --accessed: date accessed (MM, DD, YYYY; MM, YYYY; or YYYY)
-l, --publisher-location: location of publisher
"""

usage_article = ""
usage_podcast = ""
usage_website = ""
