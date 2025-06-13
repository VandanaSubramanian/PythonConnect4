#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__(self,checker,tiebreak,lookahead):
        """a data type for object AIPlayer"""
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak 
        self.lookahead = lookahead
    
    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        return 'Player' + ' ' + str(self.checker) + ' ' + '(' + str(self.tiebreak.upper()) + ', ' + str(self.lookahead)+')'
    
    def max_score_column(self,scores):
        """takes a list scores containing a score for each column and that 
           returns the index of the column of the maximum score"""
        
        lc = [i for i in range(len(scores)) if scores[i] == max(scores)]
        if self.tiebreak == 'LEFT':
            return lc[0]
        elif self.tiebreak == 'RIGHT':
            return lc[-1]
        else:
            return random.choice(lc)
    
    def scores_for(self,b):
        """returns a list containing one score for each column based on the AIPlayer's lookahead value"""
        
        scores = [0] * b.width 
        for c in range(b.width):
            if not b.can_add_to(c) == False:
                scores[c] = -1
            elif b.is_win_for(self.checker) == True:
                scores[c] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[c] = 0
            elif self.lookahead == 0:
                scores[c] = 50
            else:
                    b.add_checker(self.checker,c)
                    opponent = AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead - 1)
                    opponent_score = max(opponent.scores_for(b))
                    if opponent_score == 100:
                        scores[c] = 0
                    elif opponent_score == 0:
                        scores[c] = 100
                    else:
                        scores[c] = 50
                    b.remove_checker(c)
        return scores
    
    def next_move(self,b):
        """return the called AIPlayer's judgement of its best possible move"""
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))

                
        
        
