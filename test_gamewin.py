import random
import unittest

from PlayTest_UnitTest import PlayTest_UnitTest
from playtest_harness import LineWin, symbol_index, ScatterWin, GameWin

class test_GameWin(PlayTest_UnitTest):

    # Game Win - 3 Line Wins only. 
    # Line 1, 2, 3
    # Higest Paying Symbol in game, 5 of a kind, 4 of a kind, 3 of a kind
    def test_GameWin_3_Linewins(self):

        linewin_l = list() 
        line_1 = LineWin(300 * self.bet_multiplier, 1, 3, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_1)
        line_2 = LineWin(100 * self.bet_multiplier, 2, 4, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_2)
        line_3 = LineWin(5 * self.bet_multiplier, 3, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_3)

        expected_prize = (300 * self.bet_multiplier) + (100 * self.bet_multiplier) + (5 * self.bet_multiplier)

        gamewin_3_line = GameWin("3_line_Win_test", linewin_l) 
        self.assertTrue(gamewin_3_line.calculateWin() == expected_prize) 

    def test_GameWin_Linewins_and_Scatter(self):

        linewin_l = list() 
        line_1 = LineWin(300 * self.bet_multiplier, 1, 3, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_1)
        line_2 = LineWin(100 * self.bet_multiplier, 2, 4, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_2)
        line_3 = LineWin(5 * self.bet_multiplier, 3, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom, self.lines_played)
        linewin_l.append(line_3)

        scatterwin_l = list() 
        scatterwin_pos = [True, True, True, True, True, False, False,  False,  False,  False,  False,  False,  False,  False,  False]
        five_of_a_kind_scatter = 100 # 5 of a Kinda '$' for 1c denom
        expected_prize = self.bet_multiplier * self.lines_played * five_of_a_kind_scatter 
        
        five_scatter_win = ScatterWin(expected_prize, 5, 'DOLLAR', self.game_denom, self.bet_multiplier, self.lines_played, 'base', scatterwin_pos)
        scatterwin_l.append(five_scatter_win)
        

        gamewin_3_line_and_scatter = GameWin("3_line_Win_test", linewin_l, scatterwin_l) 

        # line wins
        expected_prize = (300 * self.bet_multiplier) + (100 * self.bet_multiplier) + (5 * self.bet_multiplier) + \
            100 * self.bet_multiplier * self.lines_played

        self.assertTrue(gamewin_3_line_and_scatter.calculateWin() == expected_prize) 

    @unittest.skip('to do')
    def test_caculate_15_free_games_feature(self): 
        print("skipping")

    @unittest.skip('to do')
    def test_game_Linked_Progressive_Win(self): 
        print("skipping")

    @unittest.skip('to do')
    def test_game_Standalone_Progressive_Win(self): 
        print("skipping")        

