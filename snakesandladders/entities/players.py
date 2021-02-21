class Players:

    def __init__(self):
        self.number_of_players = int(input("Enter Number of Players : "))
        self.player_list = []

    def player_names(self):
        for player in range(1, self.number_of_players + 1):
            player_name = input(f"Enter Name of Player {player} : ")
            self.player_list.append(player_name.upper())
        
        return(self.player_list)