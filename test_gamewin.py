import random

from PlayTest_UnitTest import PlayTest_UnitTest
from playtest import LineWin, symbol_index, ScatterWin, GameWin

class test_GameWin(PlayTest_UnitTest):

    def test_GameWin_3_Linewins(self):

        linewin_l = list() 
        line_1 = LineWin(1, 3, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_1)
        line_2 = LineWin(2, 4, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_2)
        line_3 = LineWin(3, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_3)

        expected_prize = (300 * self.bet_multiplier) + (100 * self.bet_multiplier) + (5 * self.bet_multiplier)

        gamewin_3_line = GameWin("3_line_Win_test", linewin_l) 
        self.assertTrue(gamewin_3_line.calculateWin() == expected_prize) 


    def test_GameWin_Linewins_and_Scatter(self):

        linewin_l = list() 
        line_1 = LineWin(1, 3, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_1)
        line_2 = LineWin(2, 4, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_2)
        line_3 = LineWin(3, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_3)

        scatterwin_l = list() 
        scatterwin_pos = [True,     True,   True,   True,   True,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False]
        five_scatter_win = ScatterWin(5, 'DOLLAR', self.game_denom, self.bet_multiplier, self.lines_played, 'base', scatterwin_pos)
        scatterwin_l.append(five_scatter_win)
        self.displayScatterPosition(scatterwin_pos)
        
        gamewin_3_line_and_scatter = GameWin("3_line_Win_test", linewin_l, scatterwin_l) 

        # line wins
        expected_prize = (300 * self.bet_multiplier) + (100 * self.bet_multiplier) + (5 * self.bet_multiplier) + \
            100 * self.bet_multiplier * self.lines_played

        self.assertTrue(gamewin_3_line_and_scatter.calculateWin() == expected_prize) 
