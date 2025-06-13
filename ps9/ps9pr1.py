#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self,height,width):
        
        self.height = height
        self.width = width
        self.slots = [[' ']*self.width for row in range(self.height)] 


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s += '-'*(self.width+(self.width+1))
        s += '\n'
        for col in range(self.width):
            s += ' ' + str(col % 10) 
        s += '\n'
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = 0
        for i in range(self.height-1):
            if self.slots[i+1][col] == ' ':
                row += 1
            else:
                break 
        self.slots[row][col] = checker 
            
            
    ### add your reset method here ###
    def reset(self):
        """resets the board so that every slot contains a space character"""
        for r in range(self.height):
            for c in range(self.width):
                if self.slots[r][c] == 'X' or self.slots[r][c] == 'O':
                    self.slots[r][c] = ' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self,col):
        """returns True if a checker can be added to the column and False if it cannot"""
        if col < 0 or col > self.width - 1:
            return False
        for r in range(self.height):
            if self.slots[r][col] == ' ':
                return True 
        return False
    
    def is_full(self):
        """returns True if the called object Board is completely full of checkers"""
        for i in range(self.width):
            if self.can_add_to(i) == True:
                return False 
        return True
    
    def remove_checker(self,col):
        """removes the top checker from coulmn col of the called Board object. If the column
           is empty the method should do nothing"""
        for r in range(self.height):
            if self.slots[r][col] != ' ':
                break
        self.slots[r][col] = ' '
    
    def is_win_for(self,checker):
        """returns True if there are four consecutive slots containing checker on the board
           and False otherwise"""
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or self.is_vertical_win(checker) == True or self.is_up_diagonal_win(checker) == True or self.is_down_diagonal_win(checker) == True:
            return True 
        return False 
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
           for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
            if self.slots[row][col] == checker and \
               self.slots[row][col + 1] == checker and \
               self.slots[row][col + 2] == checker and \
               self.slots[row][col + 3] == checker:
                return True

   
        return False
    
    def is_vertical_win(self,checker):
        """checks for a vertical win for the specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and self.slots[row+1][col] == checker and self.slots[row+2][col] == checker and self.slots[row+3][col] == checker:
                    return True
        return False 
    
    def is_up_diagonal_win(self,checker):
        """checks for a diagonal win in the upward direction for a specified checker"""
        for r in range(3,self.height):
            for c in range(self.width -3):
                if self.slots[r][c] == checker and self.slots[r-1][c+1] == checker and self.slots[r-2][c+2] == checker and self.slots[r-3][c+3] == checker:
                    return True 
        return False
    
    def is_down_diagonal_win(self,checker):
        """checks for a diagonal win in the downward direction for a specified checker"""
        for r in range(self.height -3):
            for c in range(self.width - 3):
                if self.slots[r][c] == checker and self.slots[r+1][c+1] == checker and self.slots[r+2][c+2] == checker and self.slots[r+3][c+3] == checker:
                    return True 
        return False 
        
        
            
