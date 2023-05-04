import random 
import seaborn as sns
import argparse 
import sys
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
        """ initialize a player object with a name, account balance, and position on the board
        Args: self = self, name = player name, account = account balance of 
        player, position = position on board"""
        self.name = name
        self.position = position if 0<= position <= 20 else 0
        self.account = account 
        
    def add_amount(self, amount):
        """ add the specified amount to the player's account balance and prints the new balance
        Args: self = self, amount = current amount balance of player
        Returns: statement of player name and account balance
        """
        self.account += amount
        print(f"{amount} added to {self.name}'s account. The new balance is:{self.account}")
        
    def subtract_amount(self, amount):
        """ subtract the specified amount to the player's account balance and prints the new balance
        Args: Args: self = self, amount = current amount balance of player
        Returns: statement of player name and account balance
        """
        self.account -= amount
        print(f"{amount} subtracted from {self.name}'s account. The new balance is:{self.account}")
    
    def move(self, dice_roll):
        """ moves the player by the number space specified by ht e dice roll  and prints the new position
        Args: self = self, dice_role = roll of a six sided die
        Returns: statement of the dice roll and the new position of the player on the board
        """
        self.position += dice_roll
        print(f"{self.name}  has moved {dice_roll()} spaces and it is now at a position {self.position}")
        
class Boardgame:
    """create an instance for the boardgame
    Attributes: 
      num players(int)= number of players
    """
    def __init__(self, num_players):
        """ initiallizes the number of players
        Args: self=self, num_player = the number of players playing
        """
        self.num_players = num_players
        self.players = []

    def generate_events(self):
        """Generate pay raise events for players every 10 spaces on the game board.This function iterates over the range from 0 to self.size in the steps of 10 and calls get_pay_raise
            args: self
            returns: None
        """
        for i in range(0, self.size, 10):
            def get_pay_raise(player):
                if player.career:
                    player.money += player.career.salary
                    print(f"{player.name} received a pay raise of ${player.career.salary}!")
     
    def get_winner(self, player_name):
       scores = {}
       for money in self.players:
           scores = self.players.player_name, self.players.account
        
        scores.sort(key=lambda score: score[1], reverse=True)

        
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
                add_person(player_name)
               
                
    print(instruction)
    
def parse_args(args):
    parser = argparse.ArgumentParser("Run a simplified version of the Life board game.")
    parser.add_argument("filename", type=str,  help="board name")
    parsed = parser.parse_args(args)
    return parsed

    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)

                    
   
