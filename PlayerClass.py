import random 
import seaborn as sns
import argparse 
import sys
import re 
#crack open sequence unpacking 
# docstrings
#start with pdf
#read a file, magic method 


class Player():
    """Creates an instance of a player
    Attributes:
        Name (str) - player name
        Account (float) - amount of money in player's account"""
    
    def __init__(self, name, account= 100000, position=0): #Sanjana - regex
        """ initialize a player object with a name, account balance, and position on the board
        Args: self = self, name = player name, account = account balance of 
        player, position = position on board"""
        r = re.search("[A-Za-z]{2,25}( [A-Za-z]{2,25})?", name)
        self.name = r.group(0)
        
        self.position = position 
        self.account = account 
        
    def __add__(self, other): #Lauren - magic methods
        """ add the specified amount to the player's account balance and prints the new balance
        Args: self = self, amount = current amount balance of player
        Returns: statement of player name and account balance
        Raises: TypeError: if other 
        """  
        if not isinstance(other, Player):
            raise TypeError(f"unsupported operand type for other")
        self.account + other.account
       
    def __sub__(self, other): #Lauren - magic methods
        """ subtract the specified amount to the player's account balance and prints the new balance
        Args: Args: self = self, amount = current amount balance of player
        Returns: statement of player name and account balance
        """
        if not isinstance(other, Player):
            raise TypeError(f"unsupported operand type for other")
        self.account - other.account   
    
    def move(self): #Lauren
        """ moves the player by the number space specified by ht e dice roll  and prints the new position
        Args: self = self, dice_role = roll of a six sided die
        Returns: statement of the dice roll and the new position of the player on the board
        """
        dice_roll = random.randint(1,6)
        self.position += dice_roll if self.position+dice_roll <= 20 else "End Game"
        return self.position
    
    def __repr__(self): #Sanjana - magic method
        return f"{self.name} has {self.account} left and is at position {self.position}"
        
    def __str__(self): #Sanjana - magic method
        return f"Player({self.name}, {str(self.account)}, {str(self.position)})"

class Boardgame:
    """create an instance for the boardgame
    Attributes: 
      num players(int)= number of players
    """
    def __init__(self, num_players): #sanjana
        """ initiallizes the number of players
        Args: self=self, num_player = the number of players playing
        """
        self.num_players = num_players
        self.players = []

    def generate_events(self): #Glory
        """
        """
        for i in range(0, self.size, 10):
            def get_pay_raise(player):
                if player.career:
                    player.money += player.career.salary
                    print(f"{player.name} received a pay raise of ${player.career.salary}!")
     
    def get_winner(self, ): #Sanjana
       scores = []
       name_score = [[i for i, j in self.players], [j for i, j in self.players]]
       name_score.sort(reverse=True)

        
    def dice_roll(): #Sanjana
        """ the amount of time a player gets to roll the dice
        """
        return random.randint(1,6)
        
class Car: #sanjana 
    def __init__(self, player_name, num_people=1):
        self.player_name = player_name 
        
    def add_person(self, player_name):
        self.num_people += 1



def main(self, filepath): #Sanjana 
    
    space_dict = {"Green": "+300",
              "Blue": "-200",
              "Purple": "Add Person",
              "Orange": "+45"}
    
    players = []
    
    while True:
        try:
            num_players = int(input("How many players for this game?: "))
            if num_players == 2:
                p1 = input("Add a name: ")
                players.append(Player(p1))
                p2 = input("Add a name: ")
                players.append(Player(p2))
            if num_players == 3:
                p1 = input("Add a name: ")
                players.append(Player(p1))
                p2 = input("Add a name: ")
                players.append(Player(p2))
                p3 = input("Add a name: ")
                players.append(Player(p3))
            if num_players == 4:
                p1 = input("Add a name: ")
                players.append(Player(p1))
                p2 = input("Add a name: ")
                players.append(Player(p2))
                p3 = input("Add a name: ")
                players.append(Player(p3))
                p4 = input("Add a name: ")
                players.append(Player(p4))
            
        except:
            print("Input a number between 2 and 4.")
        
        while True: 
            for x in range(players):
                players[x].move()
                print("\nPlayer" + ":",players[x].name)
                print("Balance: $",players[x].account)
                print("Position",players[x].position)
        
            instruction = ""
            with open(filepath, "r", encoding="utf-8") as f:
                for space in f:
                    number, color = space.strip().split()
                    for x in players:
                        if players[x].position == number:
                            player_space = color
                        
    print(instruction)
    



def parse_args(args):
    parser = argparse.ArgumentParser("Run a simplified version of the Life board game.")
    parser.add_argument("filename", type=str,  help="board name")
    parsed = parser.parse_args(args)
    return parsed

    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)

                    
                  
   
