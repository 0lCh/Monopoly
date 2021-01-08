import math


class Card:
    name = "FIELD"
    cost = math.inf
    owner = None
    group = None
    h = 0
    d = 0
    dc = 0

    def plusd(self):
        return

    def __init__(self, id):
        self.id = id

    def print(self):
        print("ПОЛЕ №", self.id, self.name)
