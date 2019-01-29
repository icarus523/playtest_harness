import unittest

from playtest_harness import ScatterWin, LineWin, GameWin, symbol_index, scatter_sym_index, paytable_scat_basegame_1c_2c, paytable_scat_basegame_5c_10c_100c, paytable_scat_freegame_1c_2c_5c_10c, paytable_scat_freegame_100c
from PlayTest_UnitTest import PlayTest_UnitTest
from PlayTest import PlayTest

class test_PlayTestHarness(PlayTest_UnitTest):

    def test_read_game_history(self):
        fname = "test_egm_playdata.json"
        myplaytest = PlayTest(fname, self.bet_multiplier, self.lines_played, self.game_denom ) # bet, lines, denom


        # First Game is: 
        #   5 of a Kind (sym_TEN) = 50 * 10 credits = 500 credits
        #   3 of a Kinda (HOTEL) = 5 * 10 credits = 50 credits 
        #   Total Credits = 550 credits


        # Second Game is: 
        #   5 of a Kinda (Hotel) = 300 * 10 = 3000 credits

        # Third Game is: 
        #   3 x Scatters = 5 * 300 = 1500 credits

        index = 0
        expected_line_prizes = [550, 3000, 0]
        expected_scatter_prizes = [0, 0, 1500]

        for game in myplaytest.games_l: 

            symbol = ''
            linewin_total = 0 
            scatterwin_total = 0

            # calculate line win total
            for linewin in game.linewin_list: 
                for k,v in symbol_index.items(): 
                    if v == linewin.symbol:
                        symbol = k

                print("Line Win:", linewin.number_of_symbols, "x", symbol, '=', linewin.getLineWin())
                linewin_total = linewin_total + linewin.getLineWin()
            
            self.assertEqual(linewin_total, expected_line_prizes[index])

            # calculate scatter win total 
            for scatterwin in game.scatterwin_list: 
                for k,v in scatter_sym_index.items(): 
                    if v == scatterwin.symbol:
                        symbol = k

                print("Scatter Win: ", scatterwin.number_of_symbols, "x", symbol, '=', scatterwin.getScatterWin())
                scatterwin_total = scatterwin_total + scatterwin.getScatterWin()
            
            self.assertEqual(scatterwin_total, expected_scatter_prizes[index])

            print("GameID: " + str(game.gameID) + ', Game Prize: ' + str(linewin_total) + " + " +  str(scatterwin_total) + " = " + str(game.calculateWin()))

            self.assertEqual(game.calculateWin(), expected_line_prizes[index] + expected_scatter_prizes[index])

            index = index + 1
