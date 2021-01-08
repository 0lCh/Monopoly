from Game import Game

game = Game()
cpls = len(game.players)
while game.active == True:
    game.gameprogress()
