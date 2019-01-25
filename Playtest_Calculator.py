import sys

from playtest_harness import LineWin, ScatterWin, GameWin, symbol_index, GAME_BET_OPTION, GAME_DENOM, \
    paytable_l_base_1c_2c_5c_10c, paytable_l_free_1c_2c_5c_10c, paytable_l_base_100c, paytable_l_free_100c

from Wild_Nights import GetPayTable

class Playtest_Calculator(): 

    def __init__(self, bet, lines, denom): 
        complete = False 

        self.denom = denom
        self.lines_played = lines
        self.bet = bet

        # Prompt for User Input in Menu
        while not complete:
            complete = self.ProcessOption(self.menu())

        sys.exit(0)

    def displayLineSymbols(self):
        print("Reel Symbols: ")
        for k,v in sorted(symbol_index.items()):
            print("\t"+ k) 
    
    def displayScatterSymbols(self):
        print("\nScatter Symbols: ")
        for k,v in sorted(scatter_sym_index.items()):
            print("\t"+k) 


            return None

    def ProcessOption(self, opt):
        complete = False

        if opt == "1": 
            # prompt for line win

            line_number = input('Line Number: ')
            number_of_symbols = input('Number of Symbols: ')
            print(self.displayLineSymbols())
            line_number = input('Which Line Symbol: ')

            sub_s = input("Substitute Win? (True/False): ")
            if sub_s.upper() == "TRUE":
                sub = True
            else: 
                sub = False

            mul = input("Multiplier: ")

            #bet = input("Bet Multiplier: " + str(GAME_BET_OPTION) + ": ")
            #den = input("Denomination: : " + str(GAME_DENOM) + ": ")

            win_type = input("base or free_games?: ")


            paytable = self.getPayTable(int(den), win_type)

            prize = paytable[symbol_index[sub]][number_of_symbols-1]

            line_win = LineWin(300 * self.bet_multiplier, line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom)

        elif opt == "2": 
            # prompt for scatter win
            number_of_symbols = input('Number of Symbols: ')
            print(self.displayScatterSymbols())
            scatter_sym = input('Which Scatter Symbol: ')


        elif opt == "0": 
            # quit 
            complete = True
        else: 
            print("invalid option")

        return complete

    def menu(self): 
        print("1: Line Win") 
        print("2: Scatter Win")
        print("0: Quit")
        option = input("Enter Choice: ")

        return option

    def prompt_for_line_win(self): 
        linewin_l = list() 

        # def __init__(self, line_number, n_of_sym, sym, sub, mul, bet, wintype, den, lines_played=30):
        line_number = input('Line Number: ')
        number_of_symbols = input('Number of Symbols: ')
        print(self.displaySymbols())
        line_number = input('Symbol: ')

def main(): 
    app = Playtest_Calculator(10,30, 1) # bet, lines, denom

if __name__ == "__main__": main()