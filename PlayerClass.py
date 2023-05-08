import random 
import seaborn as sns
import argparse 
import sys
import re 
#crack open sequence unpacking 
# docstrings
#start with pdf
#read a file, magic method 


class Player:
    """Creates an instance of a player
    Attributes:
        Name (str) - player name
        Account (float) - amount of money in player's account"""
    
    def __init__(self, name, account= 1000, position=0): #Sanjana - regex
        """ initialize a player object with a name, account balance, and position on the board
        Args: self = self, name = player name, account = account balance of 
        player, position = position on board"""
        r = re.search(r"[A-Za-z]{2,25}( [A-Za-z]{2,25})?", name)
        self.name = r
        
        self.position = position 
        self.account = account 
        
    def __add__(self, other): #Lauren - magic methods
        """ add the specified amount to the player's account balance and prints the new balance
        Args: self = self, amount = current amount balance of player
        Returns: statement of player name and account balance
        Raises: TypeError: if other 
        """ 
        self.account = self.account + other.account
        return self.account
       
    def __sub__(self, other): #Lauren - magic methods
        """ subtract the specified amount to the player's account balance and prints the new balance
        Args: Args: self = self, amount = current amount balance of player
        Returns: statement of player name and account balance
        """
        self.account = self.account - other.account
        return self.account  
    
    def move(self): #Lauren
        """ moves the player by the number space specified by the dice roll  and prints the new position
        Args: self = self, dice_role = roll of a six sided die
        Returns: statement of the dice roll and the new position of the player on the board
        """
        dice_roll = random.randint(1,6)
        self.position += dice_roll if self.position+dice_roll <= 20 else "End Game"
        return self.position
    
    def __repr__(self):
        return f"{self.name} has {self.account} left and is at position {self.position}"
        
    def __str__(self):
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
        
    
        
class Car: #sanjana 
    def __init__(self, player_name, num_people=1):
        self.player_name = player_name 
        
    def add_person(self, player_name):
        self.num_people += 1



def main(self, filepath): #Sanjana 
    
    players = []
    cars = []

    green_spaces = [100, 200, 300, 400]
    blue_spaces = [500, 400, 200, 300]
    orange_spaces = [1,2,3,4]
    purple_spaces = [23, 45, 65, 89]

    num_players = int(input("How many players for this game?: "))
    if num_players == 2:
        p1 = input("Add a name for p1: ")
        players.append(Player(p1))
        cars.append(Car(p1))

        p2 = input("Add a name for p2: ")
        players.append(Player(p2))
        cars.append(Car(p2))

    elif num_players == 3:
        p1 = input("Add a name for p1: ")
        players.append(Player(p1))
        cars.append(Car(p1))

        p2 = input("Add a name for p2: ")
        players.append(Player(p2))
        cars.append(Car(p2))

        p3 = input("Add a name for p3: ")
        players.append(Player(p3))
        cars.append(Car(p3))

    elif num_players == 4:
        p1 = input("Add a name for p1: ")
        players.append(Player(p1))
        cars.append(Car(p1))

        p2 = input("Add a name for p2: ")
        players.append(Player(p2))
        cars.append(Car(p2))

        p3 = input("Add a name for p3: ")
        players.append(Player(p3))
        cars.append(Car(p3))

        p4 = input("Add a name for p4: ")
        players.append(Player(p4))
        cars.append(Car(p4))

    else: 
        print("Enter a 2, 3, or 4.")

    while True: 
        count = 0
        for x in players:
            print("\nPlayer" + ":",players[count].name)
            print("Balance: $",players[count].account)
            print("Position",players[count].position)
            print("Car: ", cars[count].num_people)
            print("----------------------------------")
            count += 1

            game = Boardgame(num_players, players)

            instruction = ""
            with open("board_game_spaces.txt", "r", encoding="utf-8") as f:
                for space in f:
                    number, color = space.strip().split()
                    for x in players:
                        players[count].move() #Where do we move this to make this work 
                        curr_player = x.position 
                        if curr_player == number:
                            player_space = color


                            if player_space =="Green":
                                #Add money if green 
                                add = green_spaces[random.randint(1,4)]
                                players[x] + add
                                print (f"You landed on green so {add} will be added to your account")

                            if player_space =="Blue":
                                #Subtract money if Blue 
                                sub = blue_spaces[random.randint(1,4)]
                                players[x] - sub
                                print (f"You landed on blue so {sub} will be subtracted from your account")

                            if player_space == "Orange":
                                #Add person if orange
                                additions = random.randint(1,4) 
                                players[x].add_person(additions)
                                print (f"You landed on orange so {additions} will be added to your car")

                            else:
                                if random.randint(1,2) == 1:
                                    #Add amount if randomly chooses 1
                                    tax_refund = purple_spaces[random.randint(1,4)]
                                    players[x] += tax
                                    print (f"You landed on purple so {tax_refund} will be added to your account as a tax refund")
                                else: 
                                    #subtract amount if randomly chooses 2
                                    tax = purple_spaces[random.randint(1,4)]
                                    players[x] -= tax
                                    print (f"You landed on purple so {tax} will be subtracted from your account as taxes")
def parse_args(args):
    parser = argparse.ArgumentParser("Run a simplified version of the Life board game.")
    parser.add_argument("filename", type=str,  help="board name")
    parsed = parser.parse_args(args)
    return parsed

    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)

                    
             
