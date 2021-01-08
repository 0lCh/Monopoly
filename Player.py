import random


class Player:
    wallet = 15000
    property = []
    additional = []
    active = True
    location = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def move(self):
        n1 = random.randint(1, 6)
        n2 = random.randint(1, 6)
        print("ВЫПАЛО", n1, n2)
        # Если d=1 следует игрок прошел поле вперед и ему начисляется 2 млн
        d = (self.location + n1 + n2) // 39
        if d == 1:
            print(self.name, "пересекает поле вперед и получает 2 млн")
            self.wallet += 2000
        self.location = (self.location + n1 + n2) % 39
        flag = False
        if n1 == n2:
            flag = True
        return flag

    def buycity(self, cost):
        if cost <= self.wallet:
            print(self.name, " покупает это поле")
            self.wallet -= cost
            return self.id
        else:
            return None

    def payrent(self, cost):
        self.wallet -= cost

    def getrent(self, cost):
        self.wallet += cost

    def checkbankrupt(self):
        if self.wallet < 0:
            self.active = False

    def print(self):
        print(self.name, "\nОстаток на счету игрока= ", self.wallet)
