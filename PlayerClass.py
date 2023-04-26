import random 

class Player():
    """Creates an instance of a player
    Attributes:
        Name (str) - player name
        Account (float) - amount of money in player's account"""
    
    def __init__(self, name, account= 100000, position=0):
        self.name = name
        position = []
        
    def add_amount(self, account, amount):
        self.account += amount
        print(f"{amount} added to {self.name}'s account. The new balance is:{self.account}")
        
    def subtract_amount(self, account, amount):
        self.account -= amount
        print(f"{amount} subtracted from {self.name}'s account. The new balance is:{self.account}")
    
    def move(self, dice_roll):
        self.position += dice_roll
        print(f"{self.name}  has moved {dice_roll} spaces and it is now at a position {self.position}")
        
class Boardgame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []

    def dice_roll():
        return random.randint(1,6)
        self
def dice_roll():
    """Rolls a die to determine how many spaces a player needs to move forward"""
    return random.randint(1,6)
    
def main(self):
   temp = ""
   with open("board_game_spaces.txt", "r", encoding="utf-8") as f:
       for space in f:
           if self.position == space[0]:
               for space in space_dict.keys():
                   temp += space_dict[space]
