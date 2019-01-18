import unittest

from datetime import datetime

symbol_index = { 
        'HOTEL' : 0, 
        '777': 1, 
        'VEGAS': 2, 
        'FLARE': 3, 
        'ELECTRIC_GIRL': 4, 
        'sym_ACE': 5, 
        'sym_KING': 6, 
        'sym_QUEEN': 7, 
        'sym_JACK': 8, 
        'sym_TEN': 9, 
        'sym_NINE' : 10
    }

# Paytable
paytable_l_base_1c_2c_5c_10c = [
            [0, 0, 5, 100, 300],  # sym_A
            [0, 0, 5, 100, 200], # sym_B
            [0, 0, 5, 75, 200], # sym_C
            [0, 0, 5, 75, 200], # sym_D
            [0, 0, 5, 50, 150], # sym_E
            [0, 0, 5, 40, 100], # sym_ACE
            [0, 0, 5, 20, 100], # sym_KING
            [0, 0, 5, 20, 100], # sym_QUEEN
            [0, 0, 5, 20, 50], # sym_JACK
            [0, 0, 5, 20, 50], # sym_TEN
            [0, 0, 5, 20, 50], # sym_NINE
            ]

paytable_l_free_1c_2c_5c_10c = [
            [0, 0, 5, 0, 300],    # sym_A
            [0, 0, 5, 0, 200],    # sym_B
            [0, 0, 5, 0, 200],    # sym_C
            [0, 0, 5, 0, 200],    # sym_D
            [0, 0, 5, 0, 150],    # sym_E
            [0, 0, 5, 0, 100],    # sym_ACE
            [0, 0, 5, 0, 100],    # sym_KING
            [0, 0, 5, 0, 100],    # sym_QUEEN
            [0, 0, 5, 0, 50],    # sym_JACK
            [0, 0, 5, 0, 50],    # sym_TEN
            [0, 0, 5, 0, 50]    # sym_NINE
            ]

paytable_l_base_100c = [
            [0, 2, 5, 100, 300],   # sym_A
            [0, 2, 5, 100, 200],   # sym_B
            [0, 2, 5, 75, 200],   # sym_C
            [0, 2, 5, 75, 200],   # sym_D
            [0, 2, 5, 50, 150],   # sym_E
            [0, 0, 5, 40, 100],   # sym_ACE
            [0, 0, 5, 20, 100],   # sym_KING
            [0, 0, 5, 20, 100],   # sym_QUEEN
            [0, 0, 5, 20, 50],   # sym_JACK
            [0, 0, 5, 20, 50],   # sym_TEN
            [0, 0, 5, 20, 50]    # sym_NINE
            ]

paytable_l_free_100c = [
            [ 300, 0, 5, 2, 0], # sym_A
            [ 200, 0, 5, 2, 0],   # sym_B
            [ 200, 0,  5, 2, 0],   # sym_C
            [ 200, 0,  5, 2, 0],   # sym_D
            [ 150, 0,  5, 2, 0],   # sym_E
            [0, 2, 5, 0, 300],  
            [0, 2, 5, 0, 200],  
            [0, 2, 5, 0, 200],  
            [0, 2, 5, 0, 200],  
            [0, 2, 5, 0, 150]
            ]

paytable_scat_base = [
                [ 0, 0, 5, 20, 100], # sym_scat_1c_2c
                [ 0, 2, 5, 20, 100],  # sym_scat_5c_10c_100c
              ]

# Define Lines
# Positions [1]  [2]  [3]  [4]  [5]
#           [6]  [7]  [8]  [9]  [10]
#           [11] [12] [13] [14] [15]
paylines = {
            1 : [True,     True,   True,   True,   True,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False], # Line 1
            2: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False],
            3: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False],
            4: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            5: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            6: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            7: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            8: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            9: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            10: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            11: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            12: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            13: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            14: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False], 
            15: [ False,    False,  False,  False,  False,  True,   True,   True,   True,   True,   False,  False,  False,  False,  False]
}

class LineWin():

    def __init__(self, line_number, n_of_sym, sym, sub, mul, bet, wintype, den):
        self.linenumber = line_number
        self.number_of_symbols = n_of_sym
        self.symbol = symbol_index[sym] # integer index based on symbol_index table
        self.substitute_win = sub
        self.multiplier = mul
        self.bet = bet
        self.win_type = wintype
        self.denom = den

    def getLineWin(self):
        linewin_ptable = self.getPayTable()

        return (self.bet * linewin_ptable[self.symbol][self.number_of_symbols])

    def getPayTable(self): 
        if (self.denom == 1 or self.denom == 2 or self.denom == 5 or self.denom == 10) and self.win_type == 'base': 
            return paytable_l_base_1c_2c_5c_10c
        elif (self.denom == 1 or self.denom == 2 or self.denom == 5 or self.denom == 10) and self.win_type == 'free_games':  
            return paytable_l_free_1c_2c_5c_10c
        elif self.denom == 100 and self.win_type == 'base': 
            return paytable_l_base_100c
        elif self.denom == 100 and self.win_type == 'free_games':
            return paytable_l_free_100c

    def getPayTableIndex(self): 
        index = 0

        return index


class ScatterWin():

    def __init__(self, n_of_sym, sym, total_bet, paytable):
        self.number_of_symbols = n_of_sym
        self.symbol = sym
        self.total_bet = total_bet
        self.paytable_l = paytable

    def calculateWin(self):
        prize = 0
        
        return prize

class GameWin():

    def __init__(self, gameID, linewin_list, bonus_prizes, progressive_prizes):
        self.gameID = gameID
        self.linewin_list = linewin_list
        self.bonus_prizes = bonus_prizes
        self.progressive_prizes = progressive_prizes
        
        self.prize = self.calculateWin()
        self.DisplayExpectedGameWin() 
        
    def calculateWin(self):
        prize = 0        
        
        return prize
        
    def DisplayExpectedGameWin(self):
        # show expected line win
        print("to do")
    
class PlayTest(): 

    def __init__(self): 
        # Generate a GameWin
        self.games_played = list() 

        # Set Bet Options
        self.bet_multiplier = 10 
        self.lines_played = 30 
        self.game_self.denomom = 1

        self.generateWin() 

    def generateWin(self): 
        ts = datetime.now().timestamp()
        #     def __init__(self, line_number, n_of_sym, sym, sub, mul, bet, wintype):

        lw = LineWin(18, 3, 'HOTEL', False, 1, self.bet_multiplier,'base')

        linewin_list = list() 
        linewin_list.append(lw)

        win = GameWin(ts, linewin, 0, 0)
        self.games_played.append(win)



def main(): 
    app = PlayTest() 

if __name__ == "__main__": main()