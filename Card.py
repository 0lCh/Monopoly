import math
class Card:
    name ="FIELD"
    cost = math.inf
    owner = None

    def __init__(self, i):
        self.i = i

    def print(self):
        print("ПОЛЕ ", self.i)
