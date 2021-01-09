from Card import Card

""" Карточка города
Поля    
    d - количество домов
    h - количество отелей
    owner - хозяин карточки
    name - название города
    cost - цена покупки карточки
    d0 - аренда
    d1 - аренда с 1 домом
    d2 - аренда с 2 домами
    d3 - аренда с 3 домами
    d4 - аренда с 4 домами
    h1 - аренда с 1 отелем
    dc - стоимость дома
    hc - стоимость отел
Методы
    
"""


class CityCard(Card):
    d = 0
    h = 0
    owner = None

    def __init__(self, id, group, name, cost, d0, d1, d2, d3, d4, h1, dc, hc):
        self.id = id
        self.group = group
        self.name = name
        self.cost = cost
        self.d0 = d0
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.h1 = h1
        self.dc = dc
        self.hc = hc


    def checkrent(self):
        cost = 0
        if self.d == 0:
            cost = self.d0
            if self.h == 1:
                cost = self.h1
        elif self.d == 1:
            cost = self.d1
        elif self.d == 2:
            cost = self.d2
        elif self.d == 3:
            cost = self.d4
        elif self.d == 4:
            cost = self.d4
        return cost

    def plusd(self):
        self.d += 1
