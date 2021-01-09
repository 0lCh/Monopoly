import collections
import random
import pygame
import time


class Player:
    wallet = 15000
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

    def __init__(self, name, id, x1, color):
        self.realty = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
        self.name = name
        self.id = id
        self.x1 = x1
        self.color = color

    def checkbuilt(self):
        keys = self.realty.keys()
        fl = None
        a = []
        for i in keys:
            if collections.Counter(self.realty[i]) == collections.Counter(self.allrealty[i]):
                a.append(self.realty[i][random.randint(0, len(self.realty[i]) - 1)])
        if len(a) != 0:
            fl = a[random.randint(0, len(a) - 1)]
        return fl

    def move(self, screen, coords):
        n1 = random.randint(1, 6)
        n2 = random.randint(1, 6)
        # Вывод кубиков на экран
        cub1 = pygame.image.load('images/random/' + str(n1) + "dice.png").convert_alpha()
        screen.blit(cub1, [450, 150])
        cub1 = pygame.image.load('images/random/' + str(n2) + "dice.png").convert_alpha()
        screen.blit(cub1, [750, 150])

        # Если d=1 следует игрок прошел поле вперед и ему начисляется 2 млн
        d = (self.location + n1 + n2) // 40
        if d == 1:
            font = pygame.font.SysFont("intro", 30)
            string1 = font.render(str(self.name) + " пересекает поле вперед и получает 2 млн", True, [0, 0, 0],
                                  [150, 150, 150])
            screen.blit(string1, [460, 500])
            self.wallet += 2000
        # Прорисовка траекторий
        for i in range(self.location, self.location + n1 + n2 + 1):
            pygame.draw.circle(screen, self.color, coords[i % 40], 20)
            pygame.display.flip()
            time.sleep(0.1)
        self.location = (self.location + n1 + n2) % 40

        # Проверка на повторный ход
        flag = False
        if n1 == n2:
            flag = True
        return flag

    # Отрисовка недвижомости
    def drawrealty(self, screen, cards):
        k = list(self.realty.keys())
        y = 200
        x = self.x1
        color = {1: [139, 69, 19], 2: [135, 206, 235], 3: [255, 0, 255], 4: [255, 165, 0], 5: [255, 0, 0],
                 6: [255, 255, 0], 7: [0, 100, 0], 8: [0, 0, 139], 9: [50, 50, 50], 10: [0, 0, 0]}
        for i in k:
            if len(self.realty[i]) != 0:
                for j in self.realty[i]:
                    font = pygame.font.SysFont("intro", 30)
                    d = cards[j].d
                    h = cards[j].h
                    ds = '*' * d + "$" * h
                    string1 = font.render(cards[j].name + " " + ds, True, [255, 255, 255], color[i])
                    screen.blit(string1, [x, y])
                    y += 30

    # возвращает количество карточек определенной категории
    def getamount(self, group):
        return len(self.realty[group])

    # Покупка карты
    def buycard(self, cost, group, loc, screen):
        if cost <= self.wallet:
            font1 = pygame.font.SysFont("intro", 30)
            string1 = font1.render(str(self.name) + " покупает это поле", True, [0, 0, 0],
                                   [150, 150, 150])
            screen.blit(string1, [450, 340])
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

    # Находит наиболее благоприятную карту для обмена у соперника
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

    # Находит карту для обмена у соперника
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


    def addr(self, key, value):
        self.realty[key].append(value)

    def remr(self, key, value):
        self.realty[key].remove(value)
