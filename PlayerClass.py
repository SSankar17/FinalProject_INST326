import random 
import seaborn as sns
#crack open sequence unpacking 
# docstrings
#start with pdf
#read a file, magic method 
class Player():
    """Creates an instance of a player
    Attributes:
        Name (str) - player name
        Account (float) - amount of money in player's account"""
    
    def __init__(self, name, account= 100000, position=0):
        """ initialize a player object with a name, account balance, and position on the board"""
        self.name = name
        position = []
        
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
        print(f"{self.name}  has moved {dice_roll} spaces and it is now at a position {self.position}")
        
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
    

        
    def dice_roll():
        """ the amount of time a player gets to roll the dice
        """
        return random.randint(1,6)
        

    
def main(self):
   temp = ""
   with open("board_game_spaces.txt", "r", encoding="utf-8") as f:
       for space in f:
           if self.position == space[0]:
               for space in space_dict.keys():
                   temp += space_dict[space]
