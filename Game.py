from Player import Player
from CityCard import CityCard
from Card import Card
import time


class Game:
    active = True
    actplayer = 0
    cards = [Card(0), CityCard(1, "Гдыня", 600, 20, 100, 300, 900, 1600, 2500, 300, 500, 500), Card(2),
             CityCard(1, "Тайбэй", 600, 40, 200, 600, 1800, 3200, 4500, 300, 500, 500), Card(4), Card(5),
             CityCard(2, "Токио", 1000, 60, 300, 900, 2700, 4000, 5500, 500, 500, 500), Card(7),
             CityCard(2, "Барселона", 1000, 60, 300, 900, 2700, 4000, 5500, 500, 500, 500),
             CityCard(2, "Афины", 1200, 80, 400, 1000, 3000, 4500, 6000, 600, 500, 500), Card(10),
             CityCard(3, "Стамбул", 1400, 100, 500, 1500, 4500, 6250, 7500, 700, 1000, 1000), Card(12),
             CityCard(3, "Киев", 1400, 100, 500, 1500, 4500, 6250, 7500, 700, 1000, 1000),
             CityCard(3, "Торонто", 1600, 120, 600, 1800, 5000, 7000, 9000, 800, 1000, 1000), Card(15),
             CityCard(4, "Рим", 1800, 140, 700, 2000, 5500, 7500, 9500, 900, 1000, 1000), Card(17),
             CityCard(4, "Шанхай", 1800, 140, 700, 2000, 5500, 7500, 9500, 900, 1000, 1000),
             CityCard(4, "Ванкувер", 2000, 160, 800, 2200, 6000, 8000, 10000, 1000, 1000, 1000), Card(20),
             CityCard(5, "Сидней", 2200, 180, 900, 2500, 7000, 8750, 10500, 1100, 1500, 1500), Card(22),
             CityCard(5, "Нью Йорк", 2200, 180, 900, 2500, 7000, 8750, 10500, 1100, 1500, 1500),
             CityCard(5, "Лондон", 2400, 200, 1000, 3000, 7500, 9250, 11000, 1200, 1500, 1500), Card(25),
             CityCard(6, "Пекин", 2600, 220, 1100, 3300, 8000, 9750, 11500, 1300, 1500, 1500),
             CityCard(6, "Гонконг", 2600, 220, 1100, 3300, 8000, 9750, 11500, 1300, 1500, 1500), Card(28),
             CityCard(6, "Иерусалим", 2800, 240, 1200, 3600, 8500, 10250, 12000, 1400, 1500, 1500), Card(30),
             CityCard(7, "Париж", 3000, 260, 1300, 3900, 9000, 11000, 12750, 1500, 2000, 2000),
             CityCard(7, "Белград", 3000, 260, 1300, 3900, 9000, 11000, 12750, 1500, 2000, 2000), Card(33),
             CityCard(7, "Кейптаун", 3200, 280, 1500, 4500, 10000, 12000, 14000, 1600, 2000, 2000), Card(35),
             Card(36),
             CityCard(8, "Рига", 3500, 350, 1750, 5000, 11000, 13000, 15000, 1750, 2000, 2000), Card(38),
             CityCard(8, "Монреаль", 4000, 500, 2000, 6000, 14000, 17000, 20000, 2000, 2000, 2000)]

    def __init__(self):
        # cplayers = int(input("Введите количество игроков "))
        self.cplayers = 2
        self.players = []
        for i in range(self.cplayers):
            self.players.append(Player("Player " + str(i + 1), i))

    def gameprogress(self):
        print("--------------------------")
        print("Ход игрока ", end="")
        apl = self.actplayer
        self.players[apl].print()
        # Выбрасывание кубиков и переход на новое поле
        flag = self.players[apl].move()
        loc = self.players[apl].location
        # !!! Будет проверка на тип карточки
        print("игрок попал на поле №", loc + 1, self.cards[loc].name, "цена", self.cards[loc].cost)
        # Проверка на возможность покупки и присвоение
        if self.cards[loc].owner == None:
            self.cards[loc].owner = self.players[apl].buycity(self.cards[loc].cost, self.cards[loc].group, loc)
        elif self.cards[loc].owner != apl:
            # Плата аренды
            rent = self.cards[loc].checkrent()
            print(self.players[apl].name, "платит игроку", self.players[self.cards[loc].owner].name, "аренду в размере",
                  rent)
            self.players[apl].payrent(rent)
            self.players[self.cards[loc].owner].getrent(rent)
        print("Остаток на счету игрока", self.players[apl].wallet)
        # Проверка на возможеость построить дом
        spot = self.players[apl].checkbuilt()
        if spot != None:
            if self.cards[spot].d < 4:
                if self.players[apl].wallet > self.cards[spot].dc:
                    self.players[apl].wallet -= self.cards[spot].dc
                    self.cards[spot].plusd()
            else:
                if self.players[apl].wallet > self.cards[spot].hc:
                    self.cards[spot].d = 0
                    print("Игрок строит отель на поле", self.cards[spot].name)
                    self.cards[spot].h = 1

        # Задержка времени
        time.sleep(0.5)
        # Проверка на повторный ход игрока
        if flag != True:
            self.actplayer = (self.actplayer + 1) % self.cplayers
        # Проверка на банкрота
        self.players[apl].checkbankrupt()
        if self.players[apl].active == False:
            self.players.pop(apl)
        # Проверка на конец игры
        if len(self.players) == 1:
            self.active = False
            print("КОНЕЦ ИГРЫ")
            print("ПОБЕДИЛ ИГРОК", self.players[0].name)
        # for i in self.cards:
        #   print(i.name, i.owner,end="")

        # self.field.cards[self.players[self.actplayer].location].print()
    # self.field.cards[0].print()
