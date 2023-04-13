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
    
    def move(self, spaces):
        self.position += spaces
        print(f"{self.name}  has moved {spaces} spaces and it is now at a position {self.position}")
        

def dice_roll():
    """Rolls a die to determine how many spaces a player needs to move forward"""
    return random.randint(1,6)
    
    