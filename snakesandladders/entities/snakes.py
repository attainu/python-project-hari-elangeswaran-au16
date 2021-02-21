from entities.constants import Constants

class Snakes:

    def __init__(self):
        self.number_of_snakes = int(input("Enter the number of Snakes you wish to have : "))
        self.snake = 1
        self.snake_dict = {}

    def snake_location(self):
        while self.snake <= self.number_of_snakes:
            self.snake_list = list(map(int, input(f"Enter Beginning Tile and Ending Tile of Snake {self.snake}: ").split()))
            
            if self.snake_list[0] < self.snake_list[1]:
                print("Snake Beginning Tile should be greater than Snake Ending Tile")
                continue
            
            if self.snake_list[0] > Constants.BOARD or self.snake_list[1] < 0:
                print(f"Snake cannot be below 0 Position or beyond board size of {Constants.BOARD}")
                continue

            if self.snake_list[0] == 100:
                print(f"You cannot have a snake at Finish point {Constants.BOARD}")

            self.snake_dict[self.snake_list[0]]=self.snake_list[1]
            self.snake += 1

        return(self.snake_dict)