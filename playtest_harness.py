import unittest
import json
import os

from datetime import datetime

# game specific
from Wild_Nights import GAME_MAXLINES, GAME_DENOM, GAME_BET_OPTION, GAME_BET_OPTION_LINES, \
    scatter_valid_positions_base_game, scatter_valid_positions_free_game, scatter_sym_index, symbol_index, \
    paytable_l_base_1c_2c_5c_10c, paytable_l_free_1c_2c_5c_10c, paytable_l_base_100c, paytable_l_free_100c, \
    paytable_scat_basegame_1c_2c, paytable_scat_basegame_5c_10c_100c, paytable_scat_freegame_1c_2c_5c_10c, \
    paytable_scat_freegame_100c, paylines_1, paylines_5, paylines_10, paylines_25


class LineWin():

    def __init__(self, prize, line_number, n_of_sym, sym, sub=False, mul=1, bet=1, wintype="base", den=1, lines_played=1):
        self.prize = prize

        self.linenumber = line_number
        line_list = list(range(1,GAME_MAXLINES+1))
        #if (self.linenumber in line_list) == False:
        #    print("line number: ", self.linenumber, "line_list", line_list)

        # assert(self.linenumber in line_list) # 1-GAME_MAXLINES 
        
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

    # game specific
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
        #print("\n")
        paylines = None
        paylines = self.getPayLines()

        for pay in paylines[self.linenumber]: 
            if k % 5 == 0: 
                if pay == True: 
                    #print("[X]\t" , end='\n')
                    outputstr = outputstr + "[X]\t" + '\n'
                else:   
                    #print("X\t" , end='\n')
                    outputstr = outputstr + "X\t"  + '\n'
            else: 
                if pay == True: 
                    #print("[X]\t", end = '')
                    outputstr = outputstr + "[X]\t"
                else:
                    #print("X\t" , end='')
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
    def __init__(self, prize, n_of_sym, sym, denom, bet, lines, win_type, positions_list=scatter_valid_positions_base_game):
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
        #assert(self.checkScatterRules_Scatter_Positions() == True)
        #assert(self.checkScatterRules_Number_of_Scatters() == True)

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
        line_wins = self.calculateLineWin()
        scatter_wins = self.calculateScatterWin()
        bonus_prizes = self.calculateBonusWins() 
        progressive_prizes = self.calculateProgressiveWins() 
        feature_wins = self.calculateFeaturePrizes()

        return line_wins + scatter_wins + bonus_prizes + progressive_prizes + feature_wins

    def calculateBonusWins(self):
        prize = 0        
        for bonusprize in self.bonus_prizes_list: 
            prize = prize + bonusprize.getBonusPrizeWin() 
        return prize 

    def calculateProgressiveWins(self): 
        prize = 0
        for progressive_prize in self.progressive_prizes_list: 
            prize = prize + progressive_prize.GetProgressiveWin()

        return prize

    def calculateFeaturePrizes(self): 
        prize = 0
        return prize

    def calculateLineWin(self): 
        prize = 0
        for linewin in self.linewin_list: 
            prize = prize + linewin.getLineWin() 
        
        return prize

    def calculateScatterWin(self): 
        prize = 0        
        for scatterwin in self.scatterwin_list: 
            prize = prize + scatterwin.getScatterWin()

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