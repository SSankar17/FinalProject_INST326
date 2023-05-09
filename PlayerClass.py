import re
import random
class Player:
    """Creates an instance of a player
    Attributes:
        Name (str) - player name
        Account (float) - amount of money in player's account"""
    
    def __init__(self, name, account= 1000, position=0): #Sanjana - regex
        """ initialize a player object with a name, account balance, and position on the board
        Args: self = self, name = player name, account = account balance of 
        player, position = position on board"""
        r = re.search(r"(?P<name>[A-Za-z]{2,25}([A-Za-z]{2,25})?)", name)
        self.name = r.group(0)
        
        self.car = Car(self.name)
        self.position = int(position) 
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
    
    def move(self): #Sanjana 
        """ moves the player by the number space specified by the dice roll  and prints the new position
        Args: self = self, dice_role = roll of a six sided die
        Returns: statement of the dice roll and the new position of the player on the board
        """
        dice_roll = random.randint(1, 6)  # Roll a dice
        self.position = (self.position + dice_roll) if (self.position + dice_roll) <= 20 else 20
        #while self.position <= 20:
        #    return self.position
        #else:
        #    print("You cannot move, you are at the end of the game")
            
    
    def __repr__(self):
        return f"{self.name} has {self.account} left and is at position {self.position}"
        
    def __str__(self):
        return f"Player({self.name}, {str(self.account)}, {str(self.position)})"

class Boardgame:
    """create an instance for the boardgame
    Attributes: 
      num players(int)= number of players
    """
    def __init__(self, num_players, players): #sanjana
        """ initiallizes the number of players
        Args: self=self, num_player = the number of players playing
        """
        self.num_players = num_players
        self.players = []
        self.board_game = self.read_file()

    def generate_events(self): #Glory
        """
        """
        for i in range(0, self.size, 10):
            def get_pay_raise(player):
                if player.career:
                    player.money += player.career.salary
                    print(f"{player.name} received a pay raise of ${player.career.salary}!")
     
    def get_winner(self): #Sanjana
        score_dict = {}
        for player in self.players:
            score_dict[player.name] = player.account
        max_val = max(score_dict.values())
        return max_val
    
    def read_file(self):
        board_game = {}
        with open("board_game_spaces.txt", "r", encoding="utf-8") as f:
        #read this once and load it into dictionary and find the corresponding color
            for space in f:
                number, color = space.strip().split()
                board_game[int(number)] = color
            return board_game
    
    
    def check_space(self, player):
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

        # How do we add people into the car?
        if player_space == "Orange":
            #Add person if orange
            additions = random.randint(0,3) 
            player.car.add_person(additions)  
            print (f"You landed on orange so {additions} will be added to your car")

        else:
            if random.randint(1,2) == 1:
                #Add amount if randomly chooses 1
                tax_refund = purple_spaces[random.randint(0,3)]
                player.account += tax_refund
                print (f"You landed on purple so {tax_refund} will be added to your account as a tax refund")
            else: 
                #subtract amount if randomly chooses 2
                tax = purple_spaces[random.randint(0,3)]
                player.account -= tax
                print (f"You landed on purple so {tax} will be subtracted from your account as taxes")

class Car: #sanjana 
    def __init__(self, player_name, num_people=1):
        self.player_name = player_name 
        self.num_people = num_people
        
    def add_person(self, additions):
        return self.num_people + additions

def main():
    players = []
    #cars = []


    #clean up lines 11-48 to iterate efficiently - loop
    num_players = int(input("How many players for this game?: "))
    if num_players == 2:
        p1 = input("Add a name for p1: ")
        players.append(Player(p1))
        #cars.append(Car(p1)) #pass the name of the player to player then the car

        p2 = input("Add a name for p2: ")
        players.append(Player(p2))
        #cars.append(Car(p2))

    elif num_players == 3:
        p1 = input("Add a name for p1: ")
        players.append(Player(p1))
        #cars.append(Car(p1))

        p2 = input("Add a name for p2: ")
        players.append(Player(p2))
        #cars.append(Car(p2))

        p3 = input("Add a name for p3: ")
        players.append(Player(p3))
        #cars.append(Car(p3))

    elif num_players == 4:
        p1 = input("Add a name for p1: ")
        players.append(Player(p1))
        #cars.append(Car(p1))

        p2 = input("Add a name for p2: ")
        players.append(Player(p2))
        #cars.append(Car(p2))

        p3 = input("Add a name for p3: ")
        players.append(Player(p3))
        #cars.append(Car(p3))

        p4 = input("Add a name for p4: ")
        players.append(Player(p4))
        #cars.append(Car(p4))
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

            #if x.position <= 20: #only play game if position <= 20
            x.move()
            print(f"{x.name} is at position {x.position}")
            #player_space = board_game[x.position]
            boardGame1.check_space(x)

            if x.position == 20:
                print("You are at the end. The winner is " + boardGame1.get_winner())
                break
        if x.position == 20:
            break #return - this will be replaced
        
main()
