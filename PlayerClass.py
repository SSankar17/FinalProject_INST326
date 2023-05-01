import random 
import seaborn as sns
#crack open sequence unpacking 
# docstrings
#start with pdf
#read a file, magic method 
space_dict = {"Green": "+300",
              "Blue": "-200",
              "Purple": "Add Person",
              "Orange": "+45"}

class Player():
    """Creates an instance of a player
    Attributes:
        Name (str) - player name
        Account (float) - amount of money in player's account"""
    
    def __init__(self, name, account= 100000, position=0):
        """ initialize a player object with a name, account balance, and position on the board"""
        self.name = name
        position = position
        
    def add_amount(self, account, amount):
        """ add the specified amount to the player's account balance and prints the new balance
        """
        self.account += amount
        print(f"{amount} added to {self.name}'s account. The new balance is:{self.account}")
        
    def subtract_amount(self, account, amount):
        """ subtract the specified amount to the player's account balance and prints the new balance
        """
        self.account -= amount
        print(f"{amount} subtracted from {self.name}'s account. The new balance is:{self.account}")
    
    def move(self, dice_roll):
        """ moves the player by the number space specified by ht e dice roll  and prints the new position
        """
        self.position += dice_roll
        print(f"{self.name}  has moved {dice_roll()} spaces and it is now at a position {self.position}")
        
class Boardgame:
    """create an instance for the boardgame
    attributes: 
      num players(int)= number of players
    """
    def __init__(self, num_players):
        """
        """
        self.num_players = num_players
        self.players = []
     #sequnce unpakcing 
     # a, b, c = name, age, account

        
    def dice_roll():
        """ the amount of time a player gets to roll the dice
        """
        return random.randint(1,6)
        
class Car:
    def __init__(self, player_name, num_people=1):
        self.player_name = player_name 
        
        
    def add_person(player_name):
        pass



def main(self, filepath):
    instruction = ""
    with open(filepath, "r", encoding="utf-8") as f:
        for space in f:
            number, color = space.strip().split()
            if self.position == number:
                instruction = space_dict[color]
                       
    print(instruction)
                       
