import sys
import random
from mechanics.game import StartGame

def run():

    game = StartGame()
    position = game.position
    win = False
    while win is False:
        position = game.play()
        win = game.has_won(position)
        game.got_ladder(position)
        game.got_snake(position)

if __name__ == "__main__":
    run()