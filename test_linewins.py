import random

from PlayTest_UnitTest import PlayTest_UnitTest
from playtest import LineWin, symbol_index, paytable_l_base_1c_2c_5c_10c, paytable_l_free_1c_2c_5c_10c, paytable_l_base_100c, paytable_l_free_100c, paylines

class test_LineWins(PlayTest_UnitTest):
   
    def test_Generate_5_of_a_kind_Line_Win(self):
    # def __init__(self, line_number, n_of_sym, sym, sub, mul, bet, wintype):
        line_number = random.randint(1, self.lines_played)
        line_win = LineWin(line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom)

        self.assertEqual(line_win.getLineWin() == 30000)