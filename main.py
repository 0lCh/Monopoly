from Player import Player
from CityCard import CityCard
from Card import Card
from TaxCard import TaxCard
from TransportCard import TransportCard
from EnergyCard import EnergyCard
import random
import time


def chance(apl):
    a = random.randint(0, 2)
    b = [250, 150, 100, 1000, 1500]
    m = b[random.randint(0, len(b) - 1)]
    if a == 0:
        print("Заплатите банку", m)
        players[apl].payrent(m)
    elif a == 1:
        print("Заплатите соперникам", m)
        players[apl].payrent(m)
        players[(apl + 1) % 2].getrent(m)
    elif a == 2:
        print("Вы получаете от банка", m)
        players[apl].getrent(m)


active = True
apl = 0
stop = 0
cards = [Card(0, "Поле вперед"),
         CityCard(1, 1, "Гдыня", 600, 20, 100, 300, 900, 1600, 2500, 300, 500, 500),
         Card(2, "Шанс"),
         CityCard(3, 1, "Тайбэй", 600, 40, 200, 600, 1800, 3200, 4500, 300, 500, 500),
         TaxCard("Подоходный налог", 4, 2000),
         TransportCard(5, "Железная дорога монополиии"),
         CityCard(6, 2, "Токио", 1000, 60, 300, 900, 2700, 4000, 5500, 500, 500, 500),
         Card(7, "Шанс"),
         CityCard(8, 2, "Барселона", 1000, 60, 300, 900, 2700, 4000, 5500, 500, 500, 500),
         CityCard(9, 2, "Афины", 1200, 80, 400, 1000, 3000, 4500, 6000, 600, 500, 500),
         Card(10, "Тюрьма"),
         CityCard(11, 3, "Стамбул", 1400, 100, 500, 1500, 4500, 6250, 7500, 700, 1000, 1000),
         EnergyCard(12, "Солнечная энергия"),
         CityCard(13, 3, "Киев", 1400, 100, 500, 1500, 4500, 6250, 7500, 700, 1000, 1000),
         CityCard(14, 3, "Торонто", 1600, 120, 600, 1800, 5000, 7000, 9000, 800, 1000, 1000),
         TransportCard(15, "Авиакомапния монополии"),
         CityCard(16, 4, "Рим", 1800, 140, 700, 2000, 5500, 7500, 9500, 900, 1000, 1000),
         Card(17, "Шанс"),
         CityCard(18, 4, "Шанхай", 1800, 140, 700, 2000, 5500, 7500, 9500, 900, 1000, 1000),
         CityCard(19, 4, "Ванкувер", 2000, 160, 800, 2200, 6000, 8000, 10000, 1000, 1000, 1000),
         Card(20, "Парковка"),
         CityCard(21, 5, "Сидней", 2200, 180, 900, 2500, 7000, 8750, 10500, 1100, 1500, 1500),
         Card(22, "Шанс"),
         CityCard(23, 5, "Нью Йорк", 2200, 180, 900, 2500, 7000, 8750, 10500, 1100, 1500, 1500),
         CityCard(24, 5, "Лондон", 2400, 200, 1000, 3000, 7500, 9250, 11000, 1200, 1500, 1500),
         TransportCard(25, "Круиз монополии"),
         CityCard(26, 6, "Пекин", 2600, 220, 1100, 3300, 8000, 9750, 11500, 1300, 1500, 1500),
         CityCard(27, 6, "Гонконг", 2600, 220, 1100, 3300, 8000, 9750, 11500, 1300, 1500, 1500),
         EnergyCard(28, "Энергия ветра"),
         CityCard(29, 6, "Иерусалим", 2800, 240, 1200, 3600, 8500, 10250, 12000, 1400, 1500, 1500),
         Card(30, "Тюрьма"),
         CityCard(31, 7, "Париж", 3000, 260, 1300, 3900, 9000, 11000, 12750, 1500, 2000, 2000),
         CityCard(32, 7, "Белград", 3000, 260, 1300, 3900, 9000, 11000, 12750, 1500, 2000, 2000),
         Card(33, "Шанс"),
         CityCard(34, 7, "Кейптаун", 3200, 280, 1500, 4500, 10000, 12000, 14000, 1600, 2000, 2000),
         TransportCard(35, "Космическое путешествие монополии"),
         Card(36, "Шанс"),
         CityCard(37, 8, "Рига", 3500, 350, 1750, 5000, 11000, 13000, 15000, 1750, 2000, 2000),
         TaxCard("Налог на добавочную стоимость", 38, 1000),
         CityCard(39, 8, "Монреаль", 4000, 500, 2000, 6000, 14000, 17000, 20000, 2000, 2000, 2000)]

allrealty = {1: [1, 3],
             2: [6, 8, 9],
             3: [11, 13, 14],
             4: [16, 18, 19],
             5: [21, 23, 24],
             6: [26, 27, 29],
             7: [31, 32, 34],
             8: [37, 39]}

cplayers = 2
players = []
for i in range(cplayers):
    players.append(Player("Player " + str(i + 1), i))
strtpl = []
strtpl = players.copy()

while active == True:
    print("--------------------------")
    print("Ход игрока ", end="")
    players[apl].print()

    # Выбрасывание кубиков и переход на новое поле

    flag = players[apl].move()
    if stop > 0:
        flag = True
        stop -= 1
    loc = players[apl].location

    # Тюрьма посещение, заключение и бесплатная парковка
    if loc == 10:
        print("Вы попали на поле посещение тюрьмы")
    if loc == 20:
        print("Вы попали на поле бесплатная парковка\nтеперь вы пропустите два хода")
        stop = 2
    if loc == 30:
        players[apl].location = 10
        print("Вы попали на поле заключение в  тюрьму\nтеперь вы пропустите два хода")
        stop = 2
    if loc in [2, 7, 17, 22, 33, 36]:
        chance(apl)

    # !!! Будет проверка на тип карточки
    cards[loc].print()
    if isinstance(cards[loc], TaxCard) == True:
        print("Игрок платит налог в размере", cards[loc].tax)
        players[apl].wallet -= cards[loc].tax

    # if isinstance(cards[loc], TransportCard) == True:

    # Проверка на возможность покупки и присвоение
    if cards[loc].owner == None:
        cards[loc].owner = players[apl].buycard(cards[loc].cost, cards[loc].group, loc)
    elif cards[loc].owner != apl:
        # Плата аренды
        if isinstance(cards[loc], TransportCard) == True or isinstance(cards[loc], EnergyCard) == True:
            rent = cards[loc].checkrent(players[cards[loc].owner])
        else:
            rent = cards[loc].checkrent()
        print(players[apl].name, "платит игроку", players[cards[loc].owner].name,
              "аренду в размере",
              rent)
        players[apl].payrent(rent)
        players[cards[loc].owner].getrent(rent)
    print("Остаток на счету игрока", players[apl].wallet)

    # Проверка на возможность построить дом
    spot = players[apl].checkbuilt()
    if spot != None and cards[spot].h != 1:
        if cards[spot].d < 4:
            if players[apl].wallet > cards[spot].dc:
                players[apl].wallet -= cards[spot].dc
                cards[spot].plusd()
        else:
            if players[apl].wallet > cards[spot].hc:
                cards[spot].d = 0
                players[apl].wallet -= cards[spot].hc
                print("Игрок строит отель на поле", cards[spot].name)
                cards[spot].h = 1

    # Задержка времени
    # time.sleep(0.01)

    # Проверка на повторный ход игрока

    if flag == False:
        apl = (apl + 1) % cplayers

    # Обмен
    g = 0
    if spot == None:
        for i in cards:
            if i.owner != None:
                g += 1
        if g >= 18:
            r1 = players[0].fndonecard(players[1].realty, 0)
            r2 = players[1].fndonecard(players[0].realty, cards[r1].group)
            cards[r1].owner = 0
            cards[r2].owner = 1

            players[0].addr(cards[r1].group, r1)
            players[1].remr(cards[r1].group, r1)
            players[1].addr(cards[r2].group, r2)
            players[0].remr(cards[r2].group, r2)
            print(players[0].name, "обменивает у игрока", players[1].name, "карточку", cards[r1].name, "на карточку",
                  cards[r2].name)

            """          
            r1 = players[0].findcard(0)
            r2 = players[1].findcard(cards[r1].group)
            cards[r1].owner = 0
            cards[r2].owner = 1

            players[0].addr(cards[r1].group, r1)
            players[1].remr(cards[r1].group, r1)
            players[1].addr(cards[r2].group, r2)
            players[0].remr(cards[r2].group, r2)
            print(players[0].name, "обменивает у игрока", players[1].name, "карточку", cards[r1].name, "на карточку",
                  cards[r2].name)

        
            r1 = players[0].getrandomr()
            r2 = players[1].getrandomr()
            cards[r1].owner = 0
            cards[r2].owner = 1
            players[0].addr(cards[r2].group, r2)
            players[1].addr(cards[r1].group, r1)
            print(players[0].name, "обменивает у игрока", players[1].name, "карточку", cards[r1].name, "на карточку",
                  cards[r2].name)"""
    # Проверка на банкрота
    players[apl].checkbankrupt()
    if players[apl].active == False:
        players.pop(apl)

    # Проверка на конец игры
    if len(players) == 1:
        active = False
        print("КОНЕЦ ИГРЫ")
        print("ПОБЕДИЛ ИГРОК", players[0].name)
        # for i in cards:
        #  if isinstance(i, CityCard) == True:
        # print(i.name, strtpl[i.owner].name, i.d, i.h)

    # input()
