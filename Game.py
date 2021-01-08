from Player import Player
from CityCard import CityCard
from Card import Card
import time


class Game:
    active = True
    actplayer = 0
    cards = [Card(0), CityCard("Гдыня", 600, 20, 100, 300, 900, 1600, 2500, 300, 500, 500), Card(2),
             CityCard("Тайбэй", 600, 40, 200, 600, 1800, 3200, 4500, 300, 500, 500), Card(4), Card(5),
             CityCard("Токио", 1000, 60, 300, 900, 2700, 4000, 5500, 500, 500, 500), Card(7),
             CityCard("Барселона", 1000, 60, 300, 900, 2700, 4000, 5500, 500, 500, 500),
             CityCard("Афины", 1200, 80, 400, 1000, 3000, 4500, 6000, 600, 500, 500), Card(10),
             CityCard("Стамбул", 1400, 100, 500, 1500, 4500, 6250, 7500, 700, 1000, 1000), Card(12),
             CityCard("Киев", 1400, 100, 500, 1500, 4500, 6250, 7500, 700, 1000, 1000),
             CityCard("Торонто", 1600, 120, 600, 1800, 5000, 7000, 9000, 800, 1000, 1000), Card(15),
             CityCard("Рим", 1800, 140, 700, 2000, 5500, 7500, 9500, 900, 1000, 1000), Card(17),
             CityCard("Шанхай", 1800, 140, 700, 2000, 5500, 7500, 9500, 900, 1000, 1000),
             CityCard("Ванкувер", 2000, 160, 800, 2200, 6000, 8000, 10000, 1000, 1000, 1000), Card(20),
             CityCard("Сидней", 2200, 180, 900, 2500, 7000, 8750, 10500, 1100, 1500, 1500), Card(22),
             CityCard("Нью Йорк", 2200, 180, 900, 2500, 7000, 8750, 10500, 1100, 1500, 1500),
             CityCard("Лондон", 2400, 200, 1000, 3000, 7500, 9250, 11000, 1200, 1500, 1500), Card(25),
             CityCard("Пекин", 2600, 220, 1100, 3300, 8000, 9750, 11500, 1300, 1500, 1500),
             CityCard("Гонконг", 2600, 220, 1100, 3300, 8000, 9750, 11500, 1300, 1500, 1500), Card(28),
             CityCard("Иерусалим", 2800, 240, 1200, 3600, 8500, 10250, 12000, 1400, 1500, 1500), Card(30),
             CityCard("Париж", 3000, 260, 1300, 3900, 9000, 11000, 12750, 1500, 2000, 2000),
             CityCard("Белград", 3000, 260, 1300, 3900, 9000, 11000, 12750, 1500, 2000, 2000), Card(33),
             CityCard("Кейптаун", 3200, 280, 1500, 4500, 10000, 12000, 14000, 1600, 2000, 2000), Card(35),
             Card(36),
             CityCard("Рига", 3500, 350, 1750, 5000, 11000, 13000, 15000, 1750, 2000, 2000), Card(38),
             CityCard("Монреаль", 4000, 500, 2000, 6000, 14000, 17000, 20000, 2000, 2000, 2000)]

    def __init__(self):
        # cplayers = int(input("Введите количество игроков "))
        self.cplayers = 2
        self.players = []
        for i in range(self.cplayers):
            self.players.append(Player("Player " + str(i + 1), i))

    def gameprogress(self):
        print("--------------------------")
        print("Ход игрока ", end="")
        self.players[self.actplayer].print()
        # Выбрасывание кубиков и переход на новое поле
        flag = self.players[self.actplayer].move()
        loc = self.players[self.actplayer].location
        # !!! Будет проверка на тип карточки
        print("игрок попал на поле №", loc + 1, self.cards[loc].name, "цена", self.cards[loc].cost)
        # Проверка на возможность покупки и присвоение
        self.cards[loc].owner = self.players[self.actplayer].buycity(self.cards[loc].cost)
        # Задержка времени
        time.sleep(1)
        # Проверка на повторный ход игрока
        if flag != True:
            self.actplayer = (self.actplayer + 1) % self.cplayers
        # Проверка на банкрота
        if self.players[self.actplayer].active == False:
            self.players.pop(self.actplayer)
        # Проверка на конец игры
        if len(self.players) == 1:
            self.active = False

            # self.field.cards[self.players[self.actplayer].location].print()
    # self.field.cards[0].print()
