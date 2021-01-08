import collections
import random


class Player:
    wallet = 15000
    property = []
    additional = []
    active = True
    location = 0

    allrealty = {1: [1, 3], 2: [6, 8, 9],
                 3: [11, 13, 14],
                 4: [16, 18, 19],
                 5: [21, 23, 24],
                 6: [26, 27, 29],
                 7: [31, 32, 34],
                 8: [37, 39]}

    def __init__(self, name, id):
        self.realty = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        self.name = name
        self.id = id

    def checkbuilt(self):
        keys = self.realty.keys()
        fl = None
        a = []
        for i in keys:
            if collections.Counter(self.realty[i]) == collections.Counter(self.allrealty[i]):
                # !!!Достать стоимость дома
                print(self.name, "собрал все карточки группы №", i, "и может строить дом")
                a.append(self.realty[i][random.randint(0, len(self.realty[i]) - 1)])

        if len(a) != 0:
            fl = a[random.randint(0, len(a) - 1)]
        return fl
        # print(self.realty)

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

    def buycity(self, cost, group, loc):
        if cost <= self.wallet:
            print(self.name, " покупает это поле")
            self.wallet -= cost
            if loc not in self.realty[group]:
                self.realty[group].append(loc)
                # print(self.realty)
            return self.id
        else:
            return None

    def payrent(self, cost):
        self.wallet -= cost

    def getrent(self, cost):
        self.wallet += cost

    def checkbankrupt(self):
        if self.wallet <= 0:
            self.active = False

    def print(self):
        print(self.name, "\nОстаток на счету игрока= ", self.wallet)
