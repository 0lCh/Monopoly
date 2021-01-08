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

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print(self):
        print("Игрок попадает на поле №", self.id, self.name)
