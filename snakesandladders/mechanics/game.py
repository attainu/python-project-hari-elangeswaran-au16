import sys
import random
from entities.players import Players
from entities.ladders import Ladders
from entities.snakes import Snakes
from entities.constants import Constants

class StartGame:

    def __init__(self):
        
        player = Players()
        players = player.player_names()
        self.players = players

        ladder = Ladders()
        ladders = ladder.ladder_location()
        self.ladders = ladders

        snake = Snakes()
        snakes = snake.snake_location()
        self.snakes = snakes

        for snake_position in self.snakes: 
            if snake_position in self.ladders:
                print("You have entered Snakes in same position as Ladders \n Please Re-Enter Non-coinciding Snake positions")
                snake = Snakes()
                snakes = snake.snake_location()
                self.snakes = snakes

        print("Start Game \n")

        self.position = {}
        for player in self.players:
            self.position[player] = 0

        self.dice = {}
        

    def has_won(self, position):
        for player in self.position:
            if self.position[player] == Constants.BOARD:
                print(f"{player} rolled {self.dice[player]} and WINS THE GAME !! \n")
                return True
            elif self.position[player] > Constants.BOARD:
                self.position[player] -= self.dice[player]
                print(f"{player} rolled {self.dice[player]} but needs {Constants.BOARD - self.position[player]} to win")
            elif self.position[player] < Constants.BOARD:
                print(f"{player} rolled {self.dice[player]} and moved from {self.position[player]-self.dice[player]} to {self.position[player]}")
        print()
        return False

    def play(self):
        for player in self.players:
            self.dice[player] = random.randint(1, Constants.DICE)
            self.position[player] += self.dice[player]
        return self.position

    def got_ladder(self, position):
        for player in self.position:
            if self.position[player] in self.ladders:
                self.position[player] = self.ladders[self.position[player]]
                print(f"{player} found a LADDER and climbed to {self.position[player]} \n")

    def got_snake(self, position):
        for player in self.position:
            if self.position[player] in self.snakes:
                self.position[player] = self.snakes[self.position[player]]
                print(f"{player} got bitten by a SNAKE and was sent back to {self.position[player]} \n")

            
