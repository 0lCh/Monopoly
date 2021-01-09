import math
import pygame


class Card:
    name = "FIELD"
    cost = math.inf
    owner = None
    group = None
    h = 0
    d = 0
    dc = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def print(self, screen):
        font = pygame.font.SysFont("intro", 30)
        string1 = font.render("Игрок попадает на поле N " + str(self.id) + " " + str(self.name), True, [0, 0, 0],
                              [150, 150, 150])
        screen.blit(string1, [450, 300])
