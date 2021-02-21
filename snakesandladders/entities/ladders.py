from entities.constants import Constants

class Ladders:

    def __init__(self):
        self.number_of_ladders = int(input("Enter the number of Ladders you wish to have : "))
        self.ladder = 1
        self.ladder_dict = {}

    def ladder_location(self):
        while self.ladder <= self.number_of_ladders:
            self.ladder_list = list(map(int, input(f"Enter Beginning Tile and Ending Tile of Ladder {self.ladder}: ").split()))
            
            if self.ladder_list[0] > self.ladder_list[1]:
                print("Ladder Beginning Tile should be less than Ladder Ending Tile")
                continue

            if self.ladder_list[0] < 1 or self.ladder_list[1] > Constants.BOARD:
                print(f"Ladder cannot be below First or beyond board size of {Constants.BOARD}")
                continue

            self.ladder_dict[self.ladder_list[0]]=self.ladder_list[1]
            self.ladder += 1

        return(self.ladder_dict)