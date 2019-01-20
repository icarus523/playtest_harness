import unittest

from playtest import paylines_30

class PlayTest_UnitTest(unittest.TestCase):

    def setUp(self):
        # Set Bet Options
        self.bet_multiplier = 10 
        self.lines_played = 30 
        self.game_denom = 1

    def displayPlayline(self, line_number): 
        k = 1
        outputstr = ''
        print("\n")
        paylines = None

        if self.lines_played == 30:
            paylines = paylines_30
        # todo add paylines_25, paylines_10, etc...

        for pay in paylines[line_number]: 
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