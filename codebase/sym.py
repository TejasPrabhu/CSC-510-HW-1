import math
from collections import defaultdict


class Sym:

    def __init__(self, c=0, s=''):
        self.n = 0
        self.at = c
        self.name = s
        self._has = defaultdict(lambda: 0)

    def __repr__(self):
        return f'at: {self.at}, n: {self.n}, name: {self.name}'

    def add(self, v):
        if v != '?':
            self.n = self.n + 1
            self._has[v] = 1 + self._has[v]

    def div(self):
        e = 0
        for item in self._has.values():
            if item > 0:
                e = e - (item/self.n)*math.log((item/self.n), 2)
        return e

    def mid(self):
        most = -1
        mode = 0
        for k, v in self._has.items():
            if v > most:
                mode, most = k, v
        return mode
