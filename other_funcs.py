from datetime import datetime
from typing import List, Tuple


def author_split(string: str) -> List[Tuple[str, str]]:
    array = []
    authors = string.split(",")
    for i in range(0, len(authors)):
        author_split = authors[i].split()
        array.append((author_split[1].strip(), author_split[0].strip()))
    return array


def date_fix(date: str) -> List[str]:
    date = date.split(",")
    print(date)
    if len(date) == 1:
        year = date[0].strip()
        newdate = [f"{year}"]
        return newdate
    elif len(date) == 2:
        month = date[0].strip()
        month = datetime.strptime(month, "%m").strftime("%b")
        year = date[1].strip()
        newdate = [f"{month}", f"{year}"]
        return newdate
    elif len(date) == 3:
        month = date[0].strip()
        month = datetime.strptime(month, "%m").strftime("%b")
        day = date[1].strip()
        year = date[2].strip()
        newdate = [month, day, year]
        return newdate
    else:
        year = ""
        newdate = [year]
        return newdate


def citation_format(citation: str) -> str:
    print(citation[len(citation) - 1])
    if citation[len(citation) - 1].isalpha():
        citation += "."
    elif citation[len(citation) - 1] != ".":
        citation = citation[0 : len(citation) - 1] + "."
    return citation
