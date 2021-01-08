from Card import Card
import random
from Player import Player


class EnergyCard(Card):
    cost = 1500
    group = 10
    owner = None

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def checkrent(self, player):
        count = player.getamount(10)
        n1 = random.randint(1, 6)
        n2 = random.randint(1, 6)
        print("на кубиках выпало", n1 + n2)
        if count == 1:
            print("соперник владеет 1 предприятием, заплатите сумму на кубиках, умноженную на 4")
            return (n1 + n2) * 40
        if count == 2:
            print("соперник владеет 2 предприятиятими, заплатите сумму на кубиках, умноженную на 10")
            return (n1 + n2) * 10

    def print(self):
        print("Игрок попал на поле №", self.id, self.name, "его стоимость", self.cost)
