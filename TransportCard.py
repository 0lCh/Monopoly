from Card import Card
from Player import Player


class TransportCard(Card):
    cost = 2000
    a1 = 250
    a2 = 500
    a3 = 1000
    a4 = 2000
    group = 9
    owner = None

    def checkrent(self, player):
        count = player.getamount(9)
        if count == 1:
            cost = self.a1
        if count == 2:
            cost = self.a2
        if count == 3:
            cost = self.a3
        if count == 4:
            cost = self.a4
        return cost


