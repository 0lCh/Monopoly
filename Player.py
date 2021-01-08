import collections
import random


class Player:
    wallet = 15000
    property = []
    additional = []
    active = True
    location = 0

    allrealty = {1: [1, 3],
                 2: [6, 8, 9],
                 3: [11, 13, 14],
                 4: [16, 18, 19],
                 5: [21, 23, 24],
                 6: [26, 27, 29],
                 7: [31, 32, 34],
                 8: [37, 39],
                 9: [5, 15, 25, 35],
                 10: [12, 28]}

    def __init__(self, name, id):
        self.realty = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
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
        print("\033[32mНа кубиках выпало", n1, n2)
        # Если d=1 следует игрок прошел поле вперед и ему начисляется 2 млн
        d = (self.location + n1 + n2) // 40
        if d == 1:
            print(self.name, "пересекает поле вперед и получает 2 млн")
            self.wallet += 2000
        self.location = (self.location + n1 + n2) % 40
        flag = False
        if n1 == n2:
            flag = True
        return flag

    def getamount(self, group):
        return len(self.realty[group])

    def buycard(self, cost, group, loc):
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
        print(self.name, "\nНа счету ", self.wallet)

    """
    def getrandomr(self):
        k = list(self.realty.keys())
        k1 = []
        for i in k:
            if self.realty[i] != []:
                k1.append(k1)
        j = random.randint(0, len(k1) - 1)
        z = list(set(self.allrealty[j]) - set(self.realty[j]))
        while len(z) == 0:
            j = random.randint(0, len(k) - 1)
            z = list(set(self.allrealty[j]) - set(self.realty[j]))
        return z[0]

    def findcard(self, nogroup):
        k = list(self.realty)
        for i in k:
            a = list(set(self.allrealty[i]) - set(self.realty[i]))
            if len(a) == 1 and i != nogroup:
                return a[0]
        self.getrandomr()
"""

    def fndonecard(self, srealty, nogroup):
        k = list(self.realty)
        j = None
        for i in k:
            a = list(set(srealty[i]) - set(self.realty[i]))
            if len(a) == 1 and i != nogroup:
                j = a[0]
        if j != None:
            return j
        else:
            self.findfreecard(srealty, nogroup)

    def findfreecard(self, srealty, nogroup):
        k = list(self.realty)
        arr = []
        for i in k:
            if i != nogroup and collections.Counter(srealty[i]) != collections.Counter(self.allrealty[i]):
                if len(srealty[i]) != 0:
                    arr.append(srealty[i])
        j = random.randint(0, len(arr) - 1)
        b = arr[j][0]
        return b

    # self.getrandomr()

    def addr(self, key, value):
        self.realty[key].append(value)

    def remr(self, key, value):
        self.realty[key].remove(value)
