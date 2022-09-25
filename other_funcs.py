from datetime import datetime
def author_split(string):
    array = []
    authors = string.split(",")
    for i in range(0, len(authors)):
        author_split = authors[i].split()
        array.append((author_split[1].strip(), author_split[0].strip()))
    return array

def date_fix(date):
    date = date.split(",")
    if len(date) == 1:
        year = date[0]
        return (year)
    elif len(date) == 2:
        month = date[0]
        month = datetime.datetime.strptime(month, "%m").strftime("%b")
        year = date[1]
        return (month, year)
    elif len(date) == 3:
        month = date[0]
        month = datetime.datetime.strptime(month, "%m").strftime("%b")
        day = date[1]
        year = date[2]
        return (month, day, year)
    else:
        year = ""
        return (year)
