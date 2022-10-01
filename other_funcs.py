from datetime import datetime
s=" "
def author_split(string):
    array = []
    authors = string.split(",")
    for i in range(0, len(authors)):
        author_split = authors[i].split()
        array.append((author_split[1].strip(), author_split[0].strip()))
    return array

def date_fix(date):
    date = date.split(",")
    print(s) 
    time.sleep(1)
    print(date)
    if len(date) == 1:
        year = date[0]
        newdate = [f"{year}"]
        return newdate
    elif len(date) == 2:
        month = date[0]
        month = datetime.strptime(month, "%m").strftime("%b")
        year = date[1]
        newdate = [f"{month}", f"{year}"]
        return newdate
    elif len(date) == 3:
        month = date[0]
        month = datetime.strptime(month, "%m").strftime("%b")
        print(s) 
        time.sleep(1)
        print(month)
        day = date[1]
        year = date[2]
        print([month, day, year])
        newdate = [month, day, year]
        return newdate
    else:
        year = ""
        newdate = [year]
        return newdate

def citation_format(citation):
    print(s) 
    time.sleep(1)
    print(citation[len(citation) - 1])
    if citation[len(citation) - 1].isalpha():
        citation += "."
    elif citation[len(citation) - 1] != ".":
        citation = citation[0:len(citation) - 1] + "."
    return citation
