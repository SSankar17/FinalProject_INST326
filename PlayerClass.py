import random 
import seaborn as sns
import argparse 
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
        self.position = position if position <= 20
        self.account = account 
        
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

    def generate_events(self):
        for i in range(0, self.size, 10):
            def get_pay_raise(player):
                if player.career:
                    player.money += player.career.salary
                    print(f"{player.name} received a pay raise of ${player.career.salary}!")
     #sequnce unpakcing 
     # a, b, c = name, age, account

        
    def dice_roll():
        """ the amount of time a player gets to roll the dice
        """
        return random.randint(1,6)
        
class Car:
    def __init__(self, player_name, num_people=1):
        self.player_name = player_name 
        
    def add_person(self, player_name):
        self.num_people += 1



def main(self, filepath):
    instruction = ""
    with open(filepath, "r", encoding="utf-8") as f:
        for space in f:
            number, color = space.strip().split()
            if self.position == number:
                instruction = space_dict[color]
            if instruction == "Add Person":
                add_person()
               
                
    print(instruction)
def parse_arguments():
    parser = argparse.ArgumentParser("Run a simplified version of the Life board game.")
    parser.add_argument("filename", type=str,  help="board name")
    return parser.parse_args()
        
if __name__ = "__main__":
    main()

                    
   
