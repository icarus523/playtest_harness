import unittest
import json
import os

from datetime import datetime

GAME_DENOM = [1, 2, 5, 10, 100]
GAME_MAXLINES = 30
GAME_BET_OPTION = [1, 2, 3, 5, 10] 
GAME_BET_OPTION_LINES = [1, 5, 10, 25, 30]

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

scatter_sym_index = {
    'DOLLAR': 0
}

scatter_valid_positions_base_game = [
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True 
]

scatter_valid_positions_free_game = [
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True 
]


# Paytables
# Base game for 1c, 2c, 5c and 10c denomination
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

# Free game paytable for 1c, 2c, 5c and 10c denomination
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
# Base game for 100c denomination
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
# Free game for 100c denomination
paytable_l_free_100c = [
            [0, 2, 5, 0, 300],  # sym_A
            [0, 2, 5, 0, 200],  # sym_B
            [0, 2, 5, 0, 200],  # sym_C
            [0, 2, 5, 0, 200],  # sym_D
            [0, 2, 5, 0, 150],  # sym_E
            [0, 0, 5, 40, 100],  # sym_ACE
            [0, 0, 5, 20, 100],  # sym_KING
            [0, 0, 5, 20, 100],  # sym_QUEEN
            [0, 0, 5, 20, 50],   # sym_JACK
            [0, 0, 5, 20, 50],   # sym_TEN
            [0, 0, 5, 20, 50]    # sym_NINE
            ]

# Scatter  paytable for 1c,2c and 5c,10c, 100c denom 
paytable_scat_basegame_1c_2c = [
                [ 0, 0, 5, 20, 100],  # DOLLAR
            ]

paytable_scat_basegame_5c_10c_100c = [
                [ 0, 2, 5, 20, 100],  # DOLLAR
              ]
# Scatter paytable for 1c,2c and 5c,10c, 100c denom 
paytable_scat_freegame_1c_2c_5c_10c = [
                [ 0, 0, 5, 20, 0],  # DOLLAR
              ]
# Scatter paytable for 100c denom 
paytable_scat_freegame_100c = [
                [ 0, 0, 5, 20, 0],  # DOLLAR
              ]

# Define Lines
# Positions [1]  [2]  [3]  [4]  [5]
#           [6]  [7]  [8]  [9]  [10]
#           [11] [12] [13] [14] [15]
paylines_30 = {
            1: [    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False,  
                    False,  False,  False,  False,  False], # Line 1
            2: [    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False],
            3: [    False,  False,  False,  False,  False,  
                    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True],
            4: [    True,   False,  False,  False,  True,  
                    False,  True,   False,  True,   True,   
                    False,  False,  True,   False,  False],
            5: [    False,  False,  True,   False,  False,  
                    False,  True,   False,  True,   False,   
                    True,   False,  False,  False,  True], 
            6: [    True,   True,   False,  True,   True,  
                    False,  False,  True,   False,  False,   
                    False,  False,  False,  False,  False], 
            7: [    False,  False,  False,  False,  False,  
                    False,  False,  True,   False,  False,  
                    True,   True,   False,  True,   True], 
            8: [    False,  False,  False,  False,  False,  
                    True,   False,  False,  False,  True,   
                    False,  True,   True,   True,   False], 
            9: [    False,  True,   True,   True,   False,  
                    True,   False,  False,  False,  True,   
                    False,  False,  False,  False,  False], 
            10:[    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False], 
            11:[    False,  False,  False,  False,  False,
                    False,   True,   True,   True,   False,   
                    True,   False,  False,  False,  True], 
            12: [   True,   False,  True,   False,  True,  
                    False,  True,   False,  True,   False,   
                    False,  False,  False,  False,  False], 
            13: [   False,  False,  False,  False,  False,  
                    False,  True,   False,  True,   False,   
                    True,   False,  True,   False,  True], 
            14: [   False,  True,   False,  True,   False, 
                    True,   False,  True,   False,  True,   
                    False,  False,  False,  False,  False], 
            15: [   False,  False,  False,  False,  False,  
                    True,   False,  True,   False,  True,  
                    False,  True,  False,   True,   False], 
            16: [   True,   True,   False,  True,   True,  # To Do from here
                    False,  False,  True,   False,  False,   
                    False,  False,  False,  False,  False], 
            17: [   False,  False,  False,  False,  False,  
                    False,  False,  True,   False,  False,  
                    True,   True,   False,  True,   True], 
            18: [   False,  False,  False,  False,  False,  
                    True,   False,  False,  False,  True,   
                    False,  True,   True,   True,   False], 
            19: [   False,  True,   True,   True,   False,  
                    True,   False,  False,  False,  True,   
                    False,  False,  False,  False,  False], 
            20:[    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False], 
            21:[    False,  False,  False,  False,  False,
                    False,   True,   True,   True,   False,   
                    True,   False,  False,  False,  True], 
            22: [   True,   False,  True,   False,  True,  
                    False,  True,   False,  True,   False,   
                    False,  False,  False,  False,  False], 
            23: [   False,  False,  False,  False,  False,  
                    False,  True,   False,  True,   False,   
                    True,   False,  True,   False,  True], 
            24: [   False,  True,   False,  True,   False, 
                    True,   False,  True,   False,  True,   
                    False,  False,  False,  False,  False], 
            25: [   False,  False,  False,  False,  False,  
                    True,   False,  True,   False,  True,  
                    False,  True,  False,   True,   False],
            26: [   True,   True,   False,  True,   True,  
                    False,  False,  True,   False,  False,   
                    False,  False,  False,  False,  False], 
            27: [   False,  False,  False,  False,  False,  
                    False,  False,  True,   False,  False,  
                    True,   True,   False,  True,   True], 
            28: [   False,  False,  False,  False,  False,  
                    True,   False,  False,  False,  True,   
                    False,  True,   True,   True,   False], 
            29: [   False,  True,   True,   True,   False,  
                    True,   False,  False,  False,  True,   
                    False,  False,  False,  False,  False], 
            30:[    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False],                                         
}

paylines_1 = {
    1 : paylines_30[1] ## [True,     True,   True,   True,   True,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False], # Line 1
}

paylines_5 = { 
    1 : paylines_30[1],
    2 : paylines_30[2],
    3 : paylines_30[3],
    4 : paylines_30[4],
    5 : paylines_30[5]
}
# GAME_BET_OPTION_LINES = [1, 5, 10, 25, 30]

paylines_10 = {
    1 : paylines_30[1],
    2 : paylines_30[2],
    3 : paylines_30[3],
    4 : paylines_30[4],
    5 : paylines_30[5],
    6 : paylines_30[6], 
    7 : paylines_30[7],
    8 : paylines_30[8], 
    9 : paylines_30[9],
    10: paylines_30[10]
}

paylines_25 = {
    1 : paylines_30[1],
    2 : paylines_30[2],
    3 : paylines_30[3],
    4 : paylines_30[4],
    5 : paylines_30[5],
    6 : paylines_30[6], 
    7 : paylines_30[7],
    8 : paylines_30[8], 
    9 : paylines_30[9],
    10: paylines_30[10],
    11 : paylines_30[11],
    12 : paylines_30[12],
    13 : paylines_30[13],
    14 : paylines_30[14],
    15 : paylines_30[15],  
    16 : paylines_30[16], 
    17 : paylines_30[17],
    18 : paylines_30[18], 
    19 : paylines_30[19],
    20 : paylines_30[20],
    21 : paylines_30[21],
    22 : paylines_30[22],
    23 : paylines_30[23],
    24 : paylines_30[24],
    25 : paylines_30[25]
}

class LineWin():

    def __init__(self, prize, line_number, n_of_sym, sym, sub=False, mul=1, bet=1, wintype="base", den=1, lines_played=1):
        self.prize = prize

        self.linenumber = line_number
        assert(self.linenumber in list(range(1,GAME_MAXLINES))) # 1-GAME_MAXLINES 
        
        self.number_of_symbols = n_of_sym
        assert(self.number_of_symbols in list(range(1,6))) # 1-5 symbols
        
        self.symbol = symbol_index[sym] # integer index based on symbol_index table
        self.substitute_win = sub
        assert(self.substitute_win in [True, False])
        self.multiplier = mul
        
        self.bet = bet
        assert(self.bet in GAME_BET_OPTION) 

        self.win_type = wintype
        assert(self.win_type in ["base", "free_games"])

        self.denom = den
        assert(self.denom in GAME_DENOM)

        self.lines_played = lines_played
        assert(self.lines_played in GAME_BET_OPTION_LINES)

    def getLineWin(self):
        linewin_ptable = self.getPayTable()

        return (self.bet * linewin_ptable[self.symbol][self.number_of_symbols - 1] * self.multiplier)

    def getPayTable(self): 
        if (self.denom == 1 or self.denom == 2 or self.denom == 5 or self.denom == 10) and self.win_type == 'base': 
            return paytable_l_base_1c_2c_5c_10c
        elif (self.denom == 1 or self.denom == 2 or self.denom == 5 or self.denom == 10) and self.win_type == 'free_games':  
            return paytable_l_free_1c_2c_5c_10c
        elif self.denom == 100 and self.win_type == 'base': 
            return paytable_l_base_100c
        elif self.denom == 100 and self.win_type == 'free_games':
            return paytable_l_free_100c
        else: 
            print("No valid paytable identified")
            return None

    def getPayLines(self): 
        paylines = list()

        if self.lines_played == 30:
            paylines = paylines_30
        elif self.lines_played == 25: 
            paylines = paylines_25
        elif self.lines_played == 10: 
            paylines = paylines_10
        elif self.lines_played == 5: 
            paylines = paylines_5
        elif self.lines_played == 1: 
            paylines = paylines_1

        return paylines

    def displayPlayline(self): 
        k = 1
        outputstr = ''
        print("\n")
        paylines = None
        paylines = self.getPayLines()

        for pay in paylines[self.linenumber ]: 
            if k % 5 == 0: 
                if pay == True: 
                    print("[X]\t" , end='\n')
                    outputstr = outputstr + "[X]\t" + '\n'
                else:   
                    print("X\t" , end='\n')
                    outputstr = outputstr + "X\t"  + '\n'
            else: 
                if pay == True: 
                    print("[X]\t", end = '')
                    outputstr = outputstr + "[X]\t"
                else:
                    print("X\t" , end='')
                    outputstr = outputstr + "X\t"

            k = k + 1

        return outputstr


    def compareLineWinPattern(self, pattern_l): 
        paylines = self.getPayLine()

        return pattern_l == paylines[self.linenumber]

    def getPayLine(self): 
        if self.lines_played == 30: 
            return paylines_30
        elif self.lines_played == 1: 
            return paylines_1
        else: 
            print("Could not determine the paylines to use!")
            return None

class FreeGamesFeature(): 

    def __init__(self): 
        self.games_list = list() 
        self.free_games_total_prize = 0 

# helper class for ScatterWin prizes.    
class ScatterWin():

    # validate data input
    def __init__(self, prize, n_of_sym, sym, denom, bet, lines, win_type, positions_list):
        self.prize = prize

        self.denom = denom
        assert(self.denom in GAME_DENOM)
        
        self.symbol = sym
        idx = scatter_sym_index[self.symbol]

        self.win_type = win_type
        assert(win_type in ["base", "free_games"])

        self.total_bet = bet * lines

        if (self.denom in [1, 2] and self.win_type == "base"): 
            assert(self.prize/self.total_bet in paytable_scat_basegame_1c_2c[idx])
        elif self.denom in [5, 10, 100] and self.win_type == "base":
             assert(self.prize/self.total_bet in paytable_scat_basegame_5c_10c_100c[idx] )
        elif self.denom in [1, 2, 5, 10] and self.win_type == "free_games":
            assert(self.prize/self.total_bet in paytable_scat_freegame_1c_2c_5c_10c[idx] )
        elif self.denom == 100 and self.win_type == "free_games":
            assert(self.prize/self.total_bet in paytable_scat_freegame_100c[idx] )

        self.number_of_symbols = n_of_sym
        assert(self.number_of_symbols in list(range(1,6))) # 1-5 symbols

        self.positions_list = positions_list
        assert(len(self.positions_list) == 15)
        assert(self.positions_list.count(True) == self.number_of_symbols)

        # Apply Game Rules
        assert(self.checkScatterRules_Scatter_Positions() == True)
        assert(self.checkScatterRules_Number_of_Scatters() == True)

    # this needs to be modified per game. 
    def checkScatterRules_Scatter_Positions(self): 
        # check positions of Scatter
        print(self.positions_list, self.win_type)
        print(scatter_valid_positions_base_game)

        for pos in self.positions_list:
            if pos == True and scatter_valid_positions_base_game.index(pos):
                print(pos)


        if self.positions_list in scatter_valid_positions_base_game and self.win_type == 'base': 
            return True
        elif self.positions_list in scatter_valid_positions_free_game and self.win_type == 'free_games': 
            return True
        else: 
            return False

    def checkScatterRules_Number_of_Scatters(self): 
        # check number of scatters 
        paytable = self.getPayTable() 

        if not paytable[self.number_of_symbols - 1] == 0: 
            return True
        else: 
            return False

    def getScatterWin(self):
        scatter_paytable = self.getPayTable()

        return self.total_bet * scatter_paytable[self.number_of_symbols - 1]
    
    def getPayTable(self): 
        scat_idx = scatter_sym_index[self.symbol]

        if (self.denom == 1 or self.denom == 2) and self.win_type == 'base': 
            return paytable_scat_basegame_1c_2c[scat_idx]

        if (self.denom == 5 or self.denom == 10 or self.denom == 100) and self.win_type == 'base': 
            return paytable_scat_basegame_5c_10c_100c[scat_idx]

        elif (self.denom == 1 or self.denom == 2 or self.denom == 5 or self.denom == 10) and self.win_type == 'free_games':  
            return paytable_scat_freegame_1c_2c_5c_10c[scat_idx]

        elif self.denom == 100 and self.win_type == 'free_games':  
            return paytable_scat_freegame_100c[scat_idx]
        else: 
            print("No valid paytable identified")
            return None

    def printPaytable(self): 
        print(self.getPayTable())

class GameWin():

    def __init__(self, gameID, linewin_list={}, scatterwin_list={}, bonus_prizes_list={}, progressive_prizes_list={}, free_games_feature_list={}):
        self.gameID = gameID
        self.linewin_list = linewin_list
        self.bonus_prizes_list = bonus_prizes_list
        self.progressive_prizes_list = progressive_prizes_list
        self.scatterwin_list = scatterwin_list
        
        self.prize = self.calculateWin()
        # self.DisplayExpectedGameWin() 
        
    def calculateWin(self):
        prize = 0        
        # calculate linewin prizes
        for linewin in self.linewin_list: 
            prize = prize + linewin.getLineWin() 

        for scatterwin in self.scatterwin_list: 
            prize = prize + scatterwin.getScatterWin()

        # calculate bonus prizes 
        for bonusprize in self.bonus_prizes_list: 
            prize = prize + bonusprize.getBonusPrizeWin() 

        # calculate progressize_prizes 
        for progressive_prize in self.progressive_prizes_list: 
            prize = prize + progressive_prize.GetProgressiveWin()

        # calculate free_games_feature
        return prize
        
    def DisplayExpectedGameWin(self):
        # show expected line win
        print("to do")

class ProgressiveWin(): 

    def __init__(self, name, amt, level=0, multiplier = 1):
        self.name = name
        self.amt = amt
        self.level = level
        self.multiplier = multiplier

    def GetProgressiveWin(self): 
        return self.amt * self.multiplier

class BonusPrize(): 

    def __init__(self, name, prize, multiplier=1): 
        self.name = name
        self.prize = prize
        self.multiplier = multiplier

    def getBonusPrizeWin():
        return self.prize * self.multiplier

class PlayTest(): 

    def __init__(self, fname, bet=1, lines=1, denom=1 ): 
        self.input_fname = fname
        
        # Generate a GameWin
        self.games_l = list() 

        # Set Bet Options
        self.bet_multiplier = bet 
        self.lines_played = lines 
        self.game_denom = denom

        self.playResult(True) 
        self.games_l = self.processGames()

        for game in self.games_l: 
            print("GameID: " + str(game.gameID) + " Prize: " + str(game.prize))

        self.doChecklist()

    def doChecklist(self): 


        lines_won = list() 
        for game in self.games_l: 
            for linewin in game.linewin_list: 
                lines_won.append(linewin.linenumber)

        play_test_lines_won = list(set(lines_won))
        expected_game_lines_to_win = list(range(1, GAME_MAXLINES))
        if play_test_lines_won == expected_game_lines_to_win:
            print("All pay lines have been awarded a prize")
        else: 
            print("Paylines that have not been awarded a prize: ")
            print(list(set(expected_game_lines_to_win) - set(play_test_lines_won)))



    def processGames(self): 
        games_list = list()

        for game_outcome in self.games['game_data']: 
            linewin_l = list() 
            scatterwin_l = list() 

            for win in game_outcome['game_details']: 

                symbol = ""
                if win['win_type'] == "linewin": 
                    for k,v in symbol_index.items(): 
                        if v == win['symbol']: 
                            symbol = k
                    
                    line_win = LineWin(win['prize'], win['line_number'], win['number_of_symbols'], symbol, \
                        win['substitute_win'],win['multiplier'], win['bet'], win['game_type'], win['den'], \
                        win['lines_played']) 
                    linewin_l.append(line_win)

                elif win['win_type'] == "scatterwin": 
                    for k,v in scatter_sym_index.items(): 
                        if v == win['symbol']: 
                            symbol = k

                    scatterwin = ScatterWin(win['prize'], win['number_of_symbols'], symbol, win['den'], \
                        win['bet'], win['lines_played'], win['game_type'], win['pattern'])
                    scatterwin_l.append(scatterwin)
                # todo: bonus prizes / progressives / features / free games

                else: 
                    print("Unknown win data")
                    print(json.dumps(win, indent=4, sort_keys=True, separators=(',',':')))


            game_win = GameWin(game_outcome['id'], linewin_l, scatterwin_l) 
            games_list.append(game_win)

        return games_list

    def playResult(self, readfile = False): 
        gameresult = None

        if not readfile: 
            #  def __init__(self, gameID, linewin_list={}, scatterwin_list={}, bonus_prizes_list={}, progressive_prizes_list={}, free_games_feature_list={}):
            linewin_list = self.prompt_for_line_win() 
            # gameresult = GameWin("test", ) 
        else: 
            self.games = self.readGameHistoryfromFile(self.input_fname)


    def readGameHistoryfromFile(self, json_filename): 
        data = dict() 

        if (os.path.isfile(json_filename)):       
            with open(json_filename, 'r') as json_file:
                data = json.load(json_file)
        else: 
            # build JSON data as a dict
            data = dict() 
            data['game_data'] = list()
            game_info_1 =         {
                'id' : 1,
                'game_details' : [
                    {
                        'win_type' : "linewin",
                        'line_number' : 1,
                        'number_of_symbols' : 5,
                        'symbol' : 9, 
                        'substitute_win' : False, 
                        'multiplier' : 1,
                        'bet' : 10, 
                        'lines_played' : 30, 
                        'game_type' : "base",
                        'den' : 1,
                        'pattern' : [ True,    True,  True,  True,  True,  False,  False,  False,  False,  False,  False,   False,   False,   False,   False],
                        'prize': 500,                       
                    }, 
                    {
                        'win_type' : "linewin",
                        'line_number' : 2,
                        'number_of_symbols' : 3,
                        'symbol' : 0, 
                        'substitute_win' : False, 
                        'multiplier' : 1,
                        'bet' : 10, 
                        'lines_played' : 30, 
                        'game_type' : "base",
                        'den' : 1,
                        'pattern' : [ False,    False,  False,  False,  False,  True,  True,  True,  True,  True,  False,   False,   False,   False,   False],
                        'prize': 50,                         
                    },                     
                ]
            }
            data['game_data'].append(game_info_1)

            game_info_2 =         {
                'id' : 2,
                'game_details' : [
                    {
                        'win_type' : "linewin",
                        'line_number' : 3,
                        'number_of_symbols' : 5,
                        'symbol' : 9, 
                        'substitute_win' : False, 
                        'multiplier' : 1,
                        'bet' : 10, 
                        'lines_played' : 30, 
                        'game_type' : "base",
                        'den' : 1,
                        'pattern' : [ False,    False,  False,  False,  False,  False,  False,  False,  False,  False,  True,   True,   True,   True,   True],
                        'prize': 500,                         
                    }                    
                ]
            }
            data['game_data'].append(game_info_2)

            game_info_3 =         {
                'id' : 3,
                'game_details' : [
                    {
                        'win_type' : "scatterwin",
                        'line_number' : 0,
                        'number_of_symbols' : 3,
                        'symbol' : 0, # scatter symbol 
                        'substitute_win' : False, 
                        'multiplier' : 1,
                        'bet' : 10, 
                        'lines_played' : 30, 
                        'game_type' : "base",
                        'den' : 1,
                        'pattern' : [ False,    False,  False,  False,  False,  False,  False,  False,  False,  False,  False,   False,   True,   True,   True],
                        'prize': 1500
                    }                    
                ]
            }
            data['game_data'].append(game_info_3)

            with open(json_filename, 'w+') as json_file:
                # write test json data to disk
                json.dump(data, json_file, sort_keys=True, indent=4, separators=(',',':')) # write to disk

        return data

    def prompt_for_line_win(self): 
        linewin_l = list() 

        # def __init__(self, line_number, n_of_sym, sym, sub, mul, bet, wintype, den, lines_played=30):
        line_number = input('Line Number: ')
        number_of_symbols = input('Number of Symbols: ')
        print(self.displaySymbols())
        line_number = input('Symbol: ')

    def displaySymbols(self):
        print("Reel Symbols: ")
        for k,v in sorted(symbol_index.items()):
            print("\t"+ k) 

        print("\nScatter Symbols: ")
        for k,v in sorted(scatter_sym_index.items()):
            print("\t"+k) 

    def generateWin(self): 
        ts = datetime.now().timestamp()

        lw = LineWin(18, 3, 'HOTEL', False, 1, self.bet_multiplier,'base')

        linewin_list = list() 
        linewin_list.append(lw)

        win = GameWin(ts, linewin, 0, 0)
        self.games_played.append(win)


def main(): 
    app = PlayTest("egm_play_data.json", 10,30, 1) # bet, lines, denom

if __name__ == "__main__": main()