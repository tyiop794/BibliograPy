"""
Video citation support
"""
from other_funcs import author_split


class Movie:
    def __init__(self, title, directors, performers, distributor, year):
        self.title = title
        self.directors = author_split(directors)
        self.performers = author_split(performers)
        self.distributor = distributor
        self.year = year

