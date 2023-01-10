# Add option to create structured bibliography from file created by BibliograPy
# or using other files from other bibliography utilities
# Easily create file in format compatible with BibliograPy! (wanted feature)
import sys

usage_def = """BibliograPy version 1.0:

with no options: run in interactive mode
with options: provide source info in CLI

Options:
with no options: run in interactive mode (bibpy)
- input source info in CLI

with options : (eg. bibpy -s [source] -c [citation type] <file name> scans a file and converts source info to citations)
-f : template file 
-t <source> : template documentation for <source> (b [book], a [article], w [website], p [podcast])

For more specific info, provide the source type and citation format before
adding --usage flag.

--tui: work in progress
"""

usage_book = f"""
{sys.argv[0]} -s b --usage: template style

Template options:
Not all need to be specified
Can be written in file in any order

title : title of book
authors : authors of book (separated by commas)
date_published : date published (MM, DD, YYYY; MM, YYYY; or YYYY)
digital : d (digital) or p (physical)
publication_place : location of publisher
url : only specify if book is digital
publisher : latest publisher of book
by_chapter : c (chapter) or b (book)
editors : only specify if citing specific chapter in book
pages : by_chapter citation only
chapter_title : by_chapter citation only


"""
