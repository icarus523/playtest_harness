import random

from PlayTest_UnitTest import PlayTest_UnitTest
from playtest import LineWin, symbol_index, paytable_l_base_1c_2c_5c_10c, paytable_l_free_1c_2c_5c_10c, paytable_l_base_100c, paytable_l_free_100c, paylines_30

class test_LineWins(PlayTest_UnitTest):
   
    def test_Generate_5_of_a_kind_Line_Win_base_game_1c_2c_5c_10c(self):
        line_number = random.randint(1, self.lines_played)
        line_win = LineWin(300 * self.bet_multiplier, line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom)

        expected_prize = self.bet_multiplier * paytable_l_base_1c_2c_5c_10c[0][5-1]

        self.assertEqual(line_win.getLineWin(), expected_prize)

    def test_Generate_5_of_a_kind_Line_Win_free_game_1c_2c_5c_10c(self):
        line_number = random.randint(1, self.lines_played)
        line_win = LineWin(300 * self.bet_multiplier, line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'free_games', self.game_denom)

        expected_prize = self.bet_multiplier * paytable_l_free_1c_2c_5c_10c[0][5-1]

        self.assertEqual(line_win.getLineWin(), expected_prize)

    def test_Generate_5_of_a_kind_Line_Win_base_game_100c(self):
        line_number = random.randint(1, self.lines_played)
        line_win = LineWin(300 * self.bet_multiplier, line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom)

        expected_prize = self.bet_multiplier * paytable_l_base_100c[0][5-1]

        self.assertEqual(line_win.getLineWin(), expected_prize)

    def test_Generate_5_of_a_kind_Line_Win_free_game_100c(self):
        line_number = random.randint(1, self.lines_played)
        line_win = LineWin(300 * self.bet_multiplier, line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom)

        expected_prize = self.bet_multiplier * paytable_l_free_100c[0][5-1]

        self.assertEqual(line_win.getLineWin(), expected_prize)

    def test_displayPlayline_1(self): 
        line_number = 1
        displayed_playline = self.displayPlayline(line_number)

        self.assertEqual(displayed_playline, "[X]\t[X]\t[X]\t[X]\t[X]\t\nX\tX\tX\tX\tX\t\nX\tX\tX\tX\tX\t\n")

    def test_displayPlayline_2(self): 
        line_number = 2
        displayed_playline = self.displayPlayline(line_number)

        self.assertEqual(displayed_playline, "X\tX\tX\tX\tX\t\n[X]\t[X]\t[X]\t[X]\t[X]\t\nX\tX\tX\tX\tX\t\n")

    def test_displayPlayline_3(self): 
        line_number = 3
        displayed_playline = self.displayPlayline(line_number)

        self.assertEqual(displayed_playline, "X\tX\tX\tX\tX\t\nX\tX\tX\tX\tX\t\n[X]\t[X]\t[X]\t[X]\t[X]\t\n")

    def test_getPaytable_base_game_1c_2c_5c_10c(self): 
        line_number = random.randint(1, self.lines_played+1)
        line_win = LineWin(300 * self.bet_multiplier, line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom)

        self.assertEqual(line_win.getPayTable(), paytable_l_base_1c_2c_5c_10c)

    def test_getPaytable_free_game_1c_2c_5c_10c(self): 
        line_number = random.randint(1, self.lines_played)
        number_of_symbols = random.randint(1,6)
        line_win = LineWin(paytable_l_free_1c_2c_5c_10c[0][number_of_symbols - 1] * self.bet_multiplier, line_number, number_of_symbols, 'HOTEL', False, 1, self.bet_multiplier, 'free_games', self.game_denom)

        self.assertEqual(line_win.getPayTable(), paytable_l_free_1c_2c_5c_10c)

    def test_compareLinePatterns(self): 

        line_number = 1
        pattern =  [True,     True,   True,   True,   True,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False]
        line_win = LineWin(300 * self.bet_multiplier, line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom)

        self.assertTrue(line_win.compareLineWinPattern(pattern))        