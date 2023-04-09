import random 

class Player():
    """Creates an instance of a player
    Attributes:
        Name (str) - player name
        Account (float) - amount of money in player's account"""
    
    def __init__(self, name, account= 100000, position=0):
        self.name = name
        position = []
        

def dice_roll():
    """Rolls a die to determine how many spaces a player needs to move forward"""
    return random.randint(1,6)
    
    