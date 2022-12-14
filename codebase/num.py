import re
import sys
import random
import math
from .cli import the


class LibraryFunctions:

    @staticmethod
    def per(t, p):
        p = math.floor(((p or 0.5) * len(t)) + 0.5)

        return t[max(1, min(len(t), p)) - 1]


class Num:
    """
    This is num class to summarize the numbers.
    """

    def __init__(self, c=0, s="") -> None:

        self.n = 0
        self.at = c or 0
        self.name = s or ""
        self.has = []
        self.lo = sys.maxsize * 2 + 1
        self.hi = - sys.maxsize * 2 + 1
        self.is_sorted = True
        self.w = -1 if re.search("-$", self.name) else 1

    def nums(self):

        if not self.is_sorted:
            self.has = sorted(self.has)
            self.is_sorted = True

        return self.has

    def __str__(self):
        return f'at: {self.at}, hi: {self.hi}, isSorted: {self.is_sorted}, ' \
               f'lo: {self.lo}, n: {self.n}, name: ''{self.name}, w: {self.w}'

    def add(self, v):
        """
        Add a new number to the numbers.
        """
        if v != "?":
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)

            if len(self.has) < the["nums"]:
                self.has.append(v)
                self.is_sorted = False

            elif random.random() < the["nums"] / self.n:
                pos = random.randint(0, len(self.has) - 1)
                self.has[pos] = v
                self.is_sorted = False

    def div(self):
        """
        Returns diversity of the numbers.
        """
        a = self.nums()
        x = LibraryFunctions.per(a, 0.9) - LibraryFunctions.per(a, 0.1)
        return x / 2.58

    def mid(self):
        """
        Returns middle of the number.
        """
        return LibraryFunctions.per(self.nums(), 0.5)
