#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board
# authors - vandanasubramanian, ruthvikreddy

# write your class below.

class Player:
    """a data type for the player of a board game connect 4"""
    
    def __init__(self,checker):
        
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """returns a string representing a Player object which indicates which checker the Player is using"""
        return 'Player' + ' ' + str(self.checker)
    
    def opponent_checker(self):
        """returns a one character string representing the checker
           of the Player object's opponent"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self,b):
        """returns the column in object Board where the player
           wants to make the next move"""
        
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if col >= b.width or col < 0:
                print('Try again!' + '\n')
            else:
                return col 
        
        
        
    