import re
import argparse
import random
class Player: 
    """Creates an instance of a player
    
    Attributes:
        name (str) - player name
        account (int) - amount of money in player's account
        position (int) - the current position of the player which starts at 0
        car (Car object) - creates a car object for the player"""
    
    def __init__(self, name, account= 1000, position=0): #Sanjana - regex
        """ initialize a player object with a name, account balance, and 
        position on the board
        
        Args: self = self, name = player name, account = account balance of 
        player which is 1000 by default, position = position on board which starts at 0
        
        Side Effects: Name validation on the name to ensure that the name doesn't 
        contain anything other than letters
        
        """
        r = re.search(r"(?P<name>[A-Za-z]{2,25}([A-Za-z]{2,25})?)", name)
        self.name = r.group(0)
        
        self.car = Car(self.name)
        self.position = int(position) 
        self.account = account 
        
    def __add__(self, other): #Lauren - magic methods
        """ adds the specified amount to the player's account balance and returns 
        the new balance
        
        Args: self = self, other = anount to be added
        
        Returns: account balance
        """ 
        self.account = self.account + other.account
        return self.account
       
    def __sub__(self, other): #Lauren - magic methods
        """ subtracts the specified amount to the player's account balance and returns 
        the new balance
        
        Args: self = self, other = amount to be subtracted
        
        Returns: account balance
        """ 
        self.account = self.account - other.account
        return self.account  
    
    def move(self): #Sanjana: conditional expression
        """ moves the player by the number space specified by the dice roll
       
        Args: self = self
        
        Side Effects: updates the player's position to the inital postition plus
        whatever number they rolled on the dice 
        """
        dice_roll = random.randint(1, 6)  # Roll a dice
        self.position = (self.position + dice_roll) if (self.position + dice_roll) <= 20 else 20
    
    def __repr__(self): 
        """
        Args: self = self
        Returns: formal string representation of name account and position. """
        return f"{self.name} has {self.account} left and is at position {self.position}"
        
    def __str__(self):
        """
        Args: self = self
        Returns: informal string representation of name, account, and position.
        """
        return f"Player({self.name}, {str(self.account)}, {str(self.position)})"

class Boardgame: 
    """create an instance for the boardgame
    
    Attributes: 
      num_players(int)= number of players
      players (list of Player Objects) = list of players playing the game 
      board_game (dictionary) = a dictionary containing the spaces in the board game
    """
    
    def __init__(self, num_players, players): #sanjana
        """ initializes the number of players, player list, and the board game
        Args: 
            self=self
            num_players = the number of players playing
            players (list of Player objects) = the Players in the game
        Side Effects: updates the number of players and the list of players
        """
        self.num_players = num_players
        self.players = []
        self.board_game = self.read_file()
    
    def read_file(self): #Sanjana - with open
        """ reads in a file containing the board game spaces information and 
        stores the information into a dictionary
        
        Side Effects = parse through a file using a for loop in a with statement and populates
        a dictionary
        
        Returns: board_game (dictionary) = contains information about the board game spaces
        """
        board_game = {}
        with open("board_game_spaces.txt", "r", encoding="utf-8") as f:
        #read this once and load it into dictionary and find the corresponding color
            for space in f:
                number, color = space.strip().split()
                board_game[int(number)] = color
            return board_game
    
    
    def check_space(self, player): #Sanjana 
        """checks what space the player landed on and performs a function on that 
        depending on the color. If the player lands on gree, money is added to their
        account. If they land on blue, money is subtracted from their account. If they 
        land on orange, a person is added to their car. If they land on purple, depending
        on whether the random number generator returns a 1, they get a tax refund, otherwise 
        they have to pay taxes. 
        
        Args: player (Player object) = contains information about a players position &
        account balance
        
        Side Effects: updates to player account balance or number of people in car 
        """
        green_spaces = [100, 200, 300, 400]
        blue_spaces = [500, 400, 200, 300]
        orange_spaces = [1,2,3,4]
        purple_spaces = [23, 45, 65, 89]

        player_space = self.board_game[player.position]

        if player_space == "Green":
            #Add money if green 
            add = green_spaces[random.randint(0,3)]
            player.account += add
            print(f"You landed on green so {add} will be added to your account")

        if player_space == "Blue":
            #Subtract money if blue 
            sub = blue_spaces[random.randint(0,3)]
            player.account -= sub
            print (f"You landed on blue so {sub} will be subtracted from your account")

        if player_space == "Orange":
            #Add person if orange
            additions = orange_spaces[random.randint(0,3)]
            player.car.add_person(additions)  
            print (f"You landed on orange so {additions} will be added to your car")

        if player_space == "Purple":
            if random.randint(1,2) == 1:
                #Add amount if randomly chooses 1
                tax_refund = purple_spaces[random.randint(0,3)]
                player.account += tax_refund*player.car.num_people
                print (f"You landed on purple so {tax_refund*player.car.num_people} will be added to your account as a tax refund")
            else: 
                #subtract amount if randomly chooses 2
                tax = purple_spaces[random.randint(0,3)]
                player.account -= tax*player.car.num_people
                print (f"You landed on purple so {tax*player.car.num_people} will be subtracted from your account as taxes")

class Car: #sanjana 
    """
    Creates an instance for the car
    Attributes: 
        name (str) - player name
        num_players = the number of players playing
    """
   
    def __init__(self, player_name, num_people=1):
        """
        Args: self = self, player_name = name of player, num_people = num of
        people in the car
        
        Side Effects: updates the list of number of poeple according to the 
        car"""
        self.player_name = player_name 
        self.num_people = num_people
        
    def add_person(self, additions):
        """Args: self = self, additions = addition (math)
        Returns number of people and additions of car"""
        return self.num_people + additions
    
    
def parse_args(args): #Glory
    parser= argparse.ArgumentParser("runs a simplified version of the Life boardgame")
    parser.add_argument("filename", type=str, help="boardgame")
    parsed = parser.parse_args(args)
    return parsed
                             
def main(): #Sanjana - Lambda expression to use max
    """ This is where the program is run - the program asks the user
    for a number of players which has to be between 2 and 4. After that
    the user is asked to assign names to the players. Once that is done,
    the simulation runs and the players move with their bank accounts 
    implementing the changes according to the space they land on. The
    winner is listed at the end.
    
    Side Effect: Player objects creates, BoardGame object created - 
    Player Objects move forward until someone reaches 20 and the winner
    is declared."""
    players = []
    #cars = []

    num_players = int(input("How many players for this game?: "))
    if num_players == 2 or num_players == 3 or num_players ==4:
        for x in range(num_players):
            players.append(Player(input(f"Add a name for player{x+1}")))
    else: 
        print("Enter a 2, 3, or 4.")

    boardGame1 = Boardgame(len(players), players)

    count=0    
    while True: 
        for x in players:
            print("\nPlayer" + ":",x.name)
            print("Balance: $",x.account)
            print("Position",x.position)
            print("Car: ", x.car.num_people)
            print("----------------------------------")
            print("Now this player will move")
            print("----------------------------------")

            x.move()
            print(f"{x.name} is at position {x.position}")
            boardGame1.check_space(x)

            if x.position == 20:
                print("You are at the end.")
                max_score = max(players, key=lambda x: x.account)
                print("The winner is " +max_score.name +" with $" +str(max_score.account))
                    
                break
        if x.position == 20:
            break 
         
main()
