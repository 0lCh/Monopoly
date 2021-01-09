import pygame

from Player import Player
from CityCard import CityCard
from Card import Card
from TaxCard import TaxCard
from TransportCard import TransportCard
from EnergyCard import EnergyCard
import random
import time


# Генерация шанса
def chance(apl):
    a = random.randint(0, 2)
    b = [250, 150, 100, 1000, 1500]
    m = b[random.randint(0, len(b) - 1)]
    txt = ""
    if a == 0:
        txt = "Заплатите банку " + str(m)
        players[apl].payrent(m)
    elif a == 1:
        txt = "Заплатите соперникам " + str(m)
        players[apl].payrent(m)
        players[(apl + 1) % 2].getrent(m)
    elif a == 2:
        txt = "Вы получаете от банка " + str(m)
        players[apl].getrent(m)
    return txt


running = True
apl = 0
stop = 0
cards = [Card(0, "Поле вперед"),
         CityCard(1, 1, "Гдыня", 600, 20, 100, 300, 900, 1600, 2500, 300, 500, 500),
         Card(2, "Шанс"),
         CityCard(3, 1, "Тайбэй", 600, 40, 200, 600, 1800, 3200, 4500, 300, 500, 500),
         TaxCard("Подоходный налог", 4, 2000),
         TransportCard(5, "Железная дорога"),
         CityCard(6, 2, "Токио", 1000, 60, 300, 900, 2700, 4000, 5500, 500, 500, 500),
         Card(7, "Шанс"),
         CityCard(8, 2, "Барселона", 1000, 60, 300, 900, 2700, 4000, 5500, 500, 500, 500),
         CityCard(9, 2, "Афины", 1200, 80, 400, 1000, 3000, 4500, 6000, 600, 500, 500),
         Card(10, "Тюрьма"),
         CityCard(11, 3, "Стамбул", 1400, 100, 500, 1500, 4500, 6250, 7500, 700, 1000, 1000),
         EnergyCard(12, "Солнечная энергия"),
         CityCard(13, 3, "Киев", 1400, 100, 500, 1500, 4500, 6250, 7500, 700, 1000, 1000),
         CityCard(14, 3, "Торонто", 1600, 120, 600, 1800, 5000, 7000, 9000, 800, 1000, 1000),
         TransportCard(15, "Авиакомапния"),
         CityCard(16, 4, "Рим", 1800, 140, 700, 2000, 5500, 7500, 9500, 900, 1000, 1000),
         Card(17, "Шанс"),
         CityCard(18, 4, "Шанхай", 1800, 140, 700, 2000, 5500, 7500, 9500, 900, 1000, 1000),
         CityCard(19, 4, "Ванкувер", 2000, 160, 800, 2200, 6000, 8000, 10000, 1000, 1000, 1000),
         Card(20, "Парковка"),
         CityCard(21, 5, "Сидней", 2200, 180, 900, 2500, 7000, 8750, 10500, 1100, 1500, 1500),
         Card(22, "Шанс"),
         CityCard(23, 5, "Нью Йорк", 2200, 180, 900, 2500, 7000, 8750, 10500, 1100, 1500, 1500),
         CityCard(24, 5, "Лондон", 2400, 200, 1000, 3000, 7500, 9250, 11000, 1200, 1500, 1500),
         TransportCard(25, "Круиз"),
         CityCard(26, 6, "Пекин", 2600, 220, 1100, 3300, 8000, 9750, 11500, 1300, 1500, 1500),
         CityCard(27, 6, "Гонконг", 2600, 220, 1100, 3300, 8000, 9750, 11500, 1300, 1500, 1500),
         EnergyCard(28, "Энергия ветра"),
         CityCard(29, 6, "Иерусалим", 2800, 240, 1200, 3600, 8500, 10250, 12000, 1400, 1500, 1500),
         Card(30, "Тюрьма"),
         CityCard(31, 7, "Париж", 3000, 260, 1300, 3900, 9000, 11000, 12750, 1500, 2000, 2000),
         CityCard(32, 7, "Белград", 3000, 260, 1300, 3900, 9000, 11000, 12750, 1500, 2000, 2000),
         Card(33, "Шанс"),
         CityCard(34, 7, "Кейптаун", 3200, 280, 1500, 4500, 10000, 12000, 14000, 1600, 2000, 2000),
         TransportCard(35, "Космическое путешествие"),
         Card(36, "Шанс"),
         CityCard(37, 8, "Рига", 3500, 350, 1750, 5000, 11000, 13000, 15000, 1750, 2000, 2000),
         TaxCard("Налог на добавочную стоимость", 38, 1000),
         CityCard(39, 8, "Монреаль", 4000, 500, 2000, 6000, 14000, 17000, 20000, 2000, 2000, 2000)]

coords = {0: [1050, 740], 1: [960, 740], 2: [895, 740], 3: [830, 740], 4: [765, 740], 5: [700, 740], 6: [630, 740],
          7: [565, 740], 8: [505, 740], 9: [440, 740], 10: [350, 740], 11: [350, 660], 12: [350, 590],
          13: [350, 530], 14: [350, 470], 15: [350, 405], 16: [350, 340], 17: [350, 270], 18: [350, 200],
          19: [350, 140], 20: [350, 50], 21: [440, 50], 22: [505, 50], 23: [565, 50], 24: [630, 50], 25: [700, 50],
          26: [765, 50], 27: [830, 50], 28: [895, 50], 29: [960, 50], 30: [1050, 50], 31: [1050, 140], 32: [1050, 200],
          33: [1050, 270], 34: [1050, 340], 35: [1050, 405], 36: [1050, 470], 37: [1050, 530], 38: [1050, 590],
          39: [1050, 660]}

players = [Player("Player 1", 0, 20, [255, 0, 0]), Player("Player 2", 1, 1120, [0, 0, 255])]

pygame.init()
screen = pygame.display.set_mode((1400, 800))
clock = pygame.time.Clock()
pygame.display.set_caption('Monopoly')

font = pygame.font.SysFont("intro", 50)
font1 = pygame.font.SysFont("intro", 30)
DARKGREEN = [9, 85, 58]
DARKRED = [85, 9, 22]
DARKBLUE = [23, 59, 138]

while running == True:
    screen.fill([220, 220, 220])

    # Подсвечивание стороны экрана у активного игрока
    if apl == 0:
        pygame.draw.rect(screen, [173, 255, 47], [0, 0, 600, 800])
    if apl == 1:
        pygame.draw.rect(screen, [173, 255, 47], [600, 0, 1200, 800])

    # Игровое поле
    field = pygame.image.load('images/field.jpg').convert_alpha()
    screen.blit(field, [300, 0])

    # Заголовки
    string1 = font.render("Player 1", True, DARKGREEN)
    screen.blit(string1, [50, 20])
    string1 = font.render("На счету:", True, DARKRED)
    screen.blit(string1, [50, 60])

    string1 = font.render("Имущество:", True, DARKBLUE)
    screen.blit(string1, [50, 140])
    string2 = font.render("Player 2", True, DARKGREEN)
    screen.blit(string2, [1150, 20])
    string2 = font.render("На счету:", True, DARKRED)
    screen.blit(string2, [1150, 60])
    string2 = font.render("Имущество:", True, DARKBLUE)
    screen.blit(string2, [1150, 140])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    # Вывод текущего баланса
    string1 = font.render(str(players[0].wallet) + "к", True, DARKRED)
    screen.blit(string1, [50, 100])
    string2 = font.render(str(players[1].wallet) + "k", True, DARKRED)
    screen.blit(string2, [1150, 100])

    # Вывод имущества
    players[0].drawrealty(screen, cards)
    players[1].drawrealty(screen, cards)

    # Текущее местоположение
    pygame.draw.circle(screen, players[0].color, coords[players[0].location], 20)
    pygame.draw.circle(screen, players[1].color, coords[players[1].location], 20)

    # Выбрасывание кубиков и переход на новое поле
    flag = players[apl].move(screen, coords)

    if stop > 0:
        flag = True
        stop -= 1

    # Новоем местоположение текущего игрока
    loc = players[apl].location
    cards[loc].print(screen)

    # Тюрьма посещение, заключение и бесплатная парковка
    txt = ""
    if loc == 10:
        txt = "Вы попали на поле посещение тюрьмы"
    if loc == 20:
        txt = "Вы попали на поле бесплатная парковка теперь вы пропустите два хода"
        stop = 2
    if loc == 30:
        players[apl].location = 10
        txt = "Вы попали на поле заключение в  тюрьму теперь вы пропустите два хода"
        stop = 2
    if loc in [2, 7, 17, 22, 33, 36]:
        txt = chance(apl)

    # Оплпта налога
    if isinstance(cards[loc], TaxCard) == True:
        txt = "Игрок платит налог в размере " + str(cards[loc].tax)
        players[apl].wallet -= cards[loc].tax

    # Проверка на возможность покупки и присвоение
    if cards[loc].owner == None:
        cards[loc].owner = players[apl].buycard(cards[loc].cost, cards[loc].group, loc, screen)
    elif cards[loc].owner != apl:
        # Плата аренды
        if isinstance(cards[loc], TransportCard) == True or isinstance(cards[loc], EnergyCard) == True:
            rent = cards[loc].checkrent(players[cards[loc].owner])
        else:
            rent = cards[loc].checkrent()
        txt = str(players[apl].name) + " платит игроку " + str(
            players[cards[loc].owner].name) + " аренду в размере " + str(rent)
        players[apl].payrent(rent)
        players[cards[loc].owner].getrent(rent)

    if txt != "":
        string1 = font1.render(txt, True, [0, 0, 0],
                               [150, 150, 150])
        screen.blit(string1, [450, 340])

    # Проверка на возможность построить дом
    txt1 = ""
    spot = players[apl].checkbuilt()
    if spot != None and cards[spot].h != 1:
        if cards[spot].d < 4:
            if players[apl].wallet > cards[spot].dc:
                players[apl].wallet -= cards[spot].dc
                txt1 = "Игрок строит дом на поле " + str(cards[spot].name)
                cards[spot].plusd()
        else:
            if players[apl].wallet > cards[spot].hc:
                cards[spot].d = 0
                players[apl].wallet -= cards[spot].hc
                txt1 = "Игрок строит отель на поле " + str(cards[spot].name)
                cards[spot].h = 1

    if txt1 != "":
        string1 = font1.render(txt1, True, [0, 0, 0],
                               [150, 150, 150])
        screen.blit(string1, [450, 380])

    # Проверка на повторный ход игрока
    if flag == False:
        apl = (apl + 1) % 2

    # Обмен карточек между игроками
    g = 0
    txt2 = ""
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
            txt2 = str(players[0].name) + " обменивает у игрока " + str(players[1].name) + " карточку " + str(
                cards[r1].name) + " на карточку " + str(cards[r2].name)
    if txt2 != "":
        string1 = font1.render(txt2, True, [0, 0, 0],
                               [150, 150, 150])
        screen.blit(string1, [420, 380])
    # Проверка на банкрота
    players[apl].checkbankrupt()
    if players[apl].active == False:
        players.pop(apl)

        # Проверка на конец игры
    if len(players) == 1:
        screen.fill((255, 127, 80))
        string1 = font.render("КОНЕЦ ИГРЫ", True, [255, 255, 255])
        screen.blit(string1, [550, 300])
        string1 = font.render("ПОБЕДИТЕЛЬ " + str(players[0].name), True, [255, 255, 255])
        screen.blit(string1, [500, 400])
        pygame.display.flip()
        time.sleep(3)
        running = False
    pygame.display.update()
    time.sleep(0.8)

pygame.quit()
quit()
