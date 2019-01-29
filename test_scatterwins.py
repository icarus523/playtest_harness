import random
import unittest

from PlayTest_UnitTest import PlayTest_UnitTest
from playtest_harness import ScatterWin, symbol_index, scatter_sym_index, paytable_scat_basegame_1c_2c, paytable_scat_basegame_5c_10c_100c, paytable_scat_freegame_1c_2c_5c_10c, paytable_scat_freegame_100c

class test_ScatterWins(PlayTest_UnitTest):


    def test_5_scatterwins_base(self): 

        # Set Bet Options
        self.bet_multiplier = 10 
        self.lines_played = 30 
        self.game_denom = 1

        scatterwin_pos = [True,     True,   True,   True,   True,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False]
        five_of_a_kind_scatter = 100 # 5 of a Kinda '$' for 1c denom
        expected_prize = self.bet_multiplier * self.lines_played * five_of_a_kind_scatter 

        five_scatter_win = ScatterWin(expected_prize, 5, 'DOLLAR', self.game_denom, self.bet_multiplier, \
            self.lines_played, 'base', scatterwin_pos)

        scat_idx = scatter_sym_index['DOLLAR']

        self.assertEqual(five_scatter_win.getScatterWin(), expected_prize)

    # note that this is an invalid test
    # there is no 5 scatter wins during free games. 
    # this should be asserted when checking of data i.e. creation of the scatter win object
    def test_5_scatterwins_freegames_1c(self):

        # Set Bet Options
        self.bet_multiplier = 5 
        self.lines_played = 30 
        self.game_denom = 1

        scatterwin_pos = [True,   True,   True,   True,   True,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False]
        # 5 of a Kinda '$' for 1c denom

        five_of_a_kind_scatter_free_game = 0 
        expected_prize = self.bet_multiplier * self.lines_played * five_of_a_kind_scatter_free_game 

        five_scatter_win_freegames = ScatterWin(expected_prize, 5, 'DOLLAR', self.game_denom, \
            self.bet_multiplier, self.lines_played, 'free_games', scatterwin_pos)
        
        self.assertEqual(five_scatter_win_freegames.getScatterWin(), five_of_a_kind_scatter_free_game)


    def test_4_scatterwins_base_100c(self): 

        # Set Bet Options
        self.bet_multiplier = 10 
        self.lines_played = 30 
        self.game_denom = 100
        scatterwin_pos = [True,     True,   True,   True,   False,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False]

        # 4 of a Kinda '$' for 100c denom
        scat_idx = scatter_sym_index['DOLLAR']
        four_of_a_kind_scatter = 20 
        total_credits_bet = self.bet_multiplier * self.lines_played
        expected_prize = total_credits_bet * four_of_a_kind_scatter 

        four_scatter_win = ScatterWin(expected_prize, 4, 'DOLLAR', self.game_denom, self.bet_multiplier, \
            self.lines_played, 'base', scatterwin_pos)

        self.assertEqual(four_scatter_win.getScatterWin(), expected_prize)


    def test_4_scatterwins_free_100c(self): 

        # Set Bet Options
        self.bet_multiplier = 10 
        self.lines_played = 30 
        self.game_denom = 100
        scatterwin_pos = [True,     True,   True,   True,   False,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False]
        
        # 4 of a Kinda '$' for 100c denom
        scat_idx = scatter_sym_index['DOLLAR']
        four_of_a_kind_scatter = 20 
        total_credits_bet = self.bet_multiplier * self.lines_played
        expected_prize = total_credits_bet * four_of_a_kind_scatter 
        
        four_scatter_win = ScatterWin(expected_prize, 4, 'DOLLAR', self.game_denom, self.bet_multiplier, \
            self.lines_played, 'free_games', scatterwin_pos)

        self.assertEqual(four_scatter_win.getScatterWin(), expected_prize)

    def test_3_scatterwins_free_2c(self): 

        # Set Bet Options
        self.bet_multiplier = 10 
        self.lines_played = 30 
        self.game_denom = 2
        scatterwin_pos = [True,     True,   True,   False,   False,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False]

        # 3 of a Kinda '$' for 100c denom
        scat_idx = scatter_sym_index['DOLLAR']
        five_of_a_kind_scatter = 5 
        total_credits_bet = self.bet_multiplier * self.lines_played
        expected_prize = total_credits_bet * five_of_a_kind_scatter 

        three_scatter_win = ScatterWin(expected_prize, 3, 'DOLLAR', self.game_denom, self.bet_multiplier, self.lines_played, 'free_games', scatterwin_pos)

        self.assertEqual(three_scatter_win.getScatterWin(), expected_prize)
