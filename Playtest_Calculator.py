import sys
import unittest

from playtest_harness import LineWin, ScatterWin, GameWin

# game specific
from Wild_Nights import Wild_Nights, GAME_MAXLINES, GAME_DENOM, GAME_BET_OPTION, GAME_BET_OPTION_LINES, \
    scatter_valid_positions_base_game, scatter_valid_positions_free_game, scatter_sym_index, symbol_index, \
    paytable_l_base_1c_2c_5c_10c, paytable_l_free_1c_2c_5c_10c, paytable_l_base_100c, paytable_l_free_100c, \
    paytable_scat_basegame_1c_2c, paytable_scat_basegame_5c_10c_100c, paytable_scat_freegame_1c_2c_5c_10c, \
    paytable_scat_freegame_100c, paylines_1, paylines_5, paylines_10, paylines_30

from tkinter import *
from tkinter import ttk

VERSION = "1.0"


class Playtest_Cacluclator_Unittest(unittest.TestCase):

    def setUp(self):
        # Set Bet Options
        self.bet_multiplier = 10 
        self.lines_played = 30 
        self.game_denom = 1


class Playtest_Calculator(): 

    def __init__(self, bet, lines, denom): 
        complete = False 
        self.root = Tk() 

        self.denom = denom
        self.lines_played = lines
        self.bet_multiplier = bet
        self.line_win_game = None
        self.number_of_symbols = 0
        self.button_pressed_list = list() 

        self.my_game = Wild_Nights() # instantiate the game
        self.win_type = ""
        self.game_pattern = list()

        # Prompt for User Input in Menu
        #while not complete:
        # complete = self.ProcessOption(self.menu())
        self.gui() 

    def gui(self): 
        self.root.wm_title("Playtest Calculator v"+VERSION)
        self.root.resizable(0,0)        

        frame_Header = ttk.Labelframe(self.root, text ='Select Symbol, then Bet Options')

        # Win Type: 
        win_type = [
            ("Base Game", "1"),
            ("Free Games", "2"),
        ]

        self.vars_win_type = IntVar() 
        self.vars_win_type.set(1)
        for text, mode in win_type: 
            b = ttk.Radiobutton(frame_Header, text=text, variable=self.vars_win_type, value=mode, command=self.HandleRadioButton)
            b.pack(side = RIGHT, anchor="e", padx = 5, pady=5, fill=X, expand = True)

        # Symbol:         
        frame_Header.pack(side = TOP, padx = 5, pady=5, fill=X, expand =True)
        self.cbSymbol = StringVar() 
        self.combobox_Symbol = ttk.Combobox(frame_Header, justify=LEFT, textvariable=self.cbSymbol, width = 50, state='normal')
        self.combobox_Symbol.pack(side = LEFT, padx=5, pady=5)
        self.combobox_Symbol.set('1. Select a Symbol...')
        self.combobox_Symbol['values'] =  self.generateSymbolList() # generate values based on Template List        
        self.combobox_Symbol.bind('<<ComboboxSelected>>', self.handleComboBoxChanges)        

        # Button
        frame_ReelPositions = ttk.Labelframe(self.root, text ='Select Symbol, then Bet Options')
        frame_ReelPositions.pack(side = BOTTOM, padx = 5, pady=5, fill=X, expand =True)


        symbol_l = ['X','X','X','X','X']
        self.button_l = list() 

        col = 1
        for row in list(range(1,4)): 
            for symbol in symbol_l: 
                button = ttk.Button(frame_ReelPositions,
                    text = symbol,
                    width = 10)
                button.bind('<Button-1>', self.handleButtonPress)
                button.grid(row=row, column=col, padx=3, pady=3, sticky='e')

                self.button_l.append(button)
                
                    # command = lambda: self.handleButtonPress('__tab_delimited_file__'))
                if col % 5 == 0: 
                    col = 1
                else: 
                    col = col + 1

            row = row + 1

        self.root.mainloop()

    def generateSymbolList(self): 
        symbol_list = list() 

        for symbol,_ in symbol_index.items(): 
            symbol_list.append(symbol)

        for symbol,_ in scatter_sym_index.items(): 
            symbol_list.append(symbol)


        return sorted(symbol_list)

    def getWinTypeLine_Scatter(self):
        linewin_symbol_list = list()
        line_win_game = False

        for symbol,_ in symbol_index.items(): 
            linewin_symbol_list.append(symbol)

        print(linewin_symbol_list, self.cbSymbol.get())

        if str(self.cbSymbol.get()) in linewin_symbol_list:
            line_win_game = True 
        else: 
            line_win_game = False         

        return line_win_game

    def getWin(self): 
        win = "" 
        line_win = None

        # get win type: lines/scatter
        symbol_chosen = str(self.cbSymbol.get())

        # Line Win or Scatter Win? 
        if self.line_win_game == None: 
            self.line_win_game = self.getWinTypeLine_Scatter()   

        if self.line_win_game: 
            # self.displayPossibleLineWins()
            self.HandleRadioButton() # get win_type

            paytable = self.my_game.getPayTable(int(self.denom), self.win_type)
            
            prize = paytable[symbol_index[symbol_chosen]][int(self.number_of_symbols)-1]
            line_number = self.getLine(self.game_pattern)

            # line_win = LineWin(300 * self.bet_multiplier, line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom)
            
            line_win = LineWin(prize * self.bet_multiplier, line_number, self.number_of_symbols, symbol_chosen, False, 1, self.bet_multiplier,  self.win_type, self.denom)
 
            return line_win.getLineWin()
        
        else: #scatter win
            self.HandleRadioButton() # get win_type
            paytable = self.my_game.getPayTable(int(self.denom), self.win_type)


            return 

    def getLine(self, pattern): 
        paylines = {} 

        if self.lines_played == 1: 
            paylines = paylines_1
        elif self.lines_played == 5:
            paylines = paylines_5
        elif self.lines_played == 10: 
            paylines = paylines_10
        elif self.lines_played == 25: 
            paylines = paylines_25
        elif self.lines_played == 30: 
            paylines = paylines_30
        else: 
            print("Error could not determine paylines, check self.lines_played")

        for k,v in paylines.items(): 
            if paylines == v: 
                return k

    def displayPossibleLineWins(self):
        print("todo: displayPossibleLineWins")

    def HandleRadioButton(self): 
        if self.vars_win_type.get() == 1: # base game
            self.win_type = 'base'
        elif self.vars_win_type.get() == 2: # free game
            self.win_type = 'free_games'

    def handleComboBoxChanges(self, cmd): 
        self.init() 

    def init(self):
        self.number_of_symbols = 0
        self.line_win_game = None
        self.game_pattern = list() 
        self.button_pressed_list = list() 

        self.HandleRadioButton() # update self.win_type

        # set all buttons to init
        for button in self.button_l:
            button['text'] = "X"

        # reset all values to False. 
        for pos in self.game_pattern: 
            pos = False


    def handleButtonPress(self, event): 
        pressed_button = event.widget
        
        index = self.button_l.index(pressed_button)
        pattern_l = list()

        self.line_win_game = self.getWinTypeLine_Scatter()   

        # Toggle Symbol locations
        if pressed_button["text"] == "[X]":
            pressed_button.config(text=("X"))
            self.button_pressed_list.remove(index) 
        else: 
            pressed_button.config(text=("[X]"))
            self.button_pressed_list.append(index)

        # determine number of "pressed buttons"
        self.number_of_symbols = len(self.button_pressed_list)
        self.game_pattern = self.translatePressedNumbers(self.button_pressed_list)

        valid_win_l = self.isValidLineWin(self.game_pattern)

        if not valid_win_l == None: 
            for win in valid_win_l: 
                if self.number_of_symbols > 0 and win['valid_win'] == True : 
                    # determine possible line wins that match the pattern. 
                    
                    # print("button number: " + str(index) + " was pressed")
                    print(str(self.number_of_symbols) + " x " + \
                        str(self.cbSymbol.get()) + " symbols, Line Win: " + str(self.getWin()))

                elif self.number_of_symbols > 0 and self.line_win_game == False: # scatter
                    print(str(self.number_of_symbols) + " x " + \
                        str(self.cbSymbol.get()) + " symbols, Scatter Win: " + str(self.getWin()))
                else: 
                    print("no win")


    def getPayLine(self): 
        paylines = dict() 

        if self.lines_played == 1: 
            paylines = paylines_1
        elif self.lines_played == 5:
            paylines = paylines_5
        elif self.lines_played == 10: 
            paylines = paylines_10
        elif self.lines_played == 25: 
            paylines = paylines_25
        elif self.lines_played == 30: 
            paylines = paylines_30
        else: 
            print("Could not determine the paylines to use!")
            return None
        return paylines

    def isValidLineWin(self, pattern):

        paylines_l = self.getPayLine()
        winning_lines_l = list() 

        for line_number, pos in paylines_l.items(): 
            print(line_number, pos)
            if set(pattern).issubset(set(pos)):
                winning_lines_l.append({ 'valid_win': True, 'line_number': line_number})

        return winning_lines_l 

    def translatePressedNumbers(self, button_l): 
        pattern_l = list(range(0, 15))
        positions = list(range(0, 15))

        # Sets True elements
        for button in button_l:
            idx = positions.index(button) 
            # print("idx: ", idx)
            if not idx == None:
                pattern_l[idx] = True

        # Set all non True Elements to False                
        for pos in pattern_l:
            if not pos == True:
                idx = pattern_l.index(pos) 
                pattern_l[idx] = False

        return pattern_l

    def displayLineSymbols(self):
        print("Reel Symbols: ")
        for k,v in sorted(symbol_index.items()):
            print("\t"+ k) 
    
    def displayScatterSymbols(self):
        print("\nScatter Symbols: ")
        for k,v in sorted(scatter_sym_index.items()):
            print("\t"+k) 

    def ProcessOption(self, opt):
        complete = False

        if opt == "1": 
            # prompt for line win

            line_number = int(input('Line Number: '))
            number_of_symbols = int(input('Number of Symbols: '))
            print(self.displayLineSymbols())
            symbol = input('Which Line Symbol: ') # can't convert to uppercase

            sub_s = input("Substitute Win? (True/False): ")
            if sub_s.upper() == "TRUE":
                sub = True
            else: 
                sub = False

            mul = int(input("Multiplier: "))

            win_type = input("base or free_games?: ")
            if win_type == 'base':
                win_type = 'base'
            else: 
                win_type = 'free_games'

            paytable = self.my_game.getPayTable(int(self.denom), win_type)
            prize = paytable[symbol_index[symbol]][int(number_of_symbols)-1]
            
            # line_win = LineWin(300 * self.bet_multiplier, line_number, 5, 'HOTEL', False, 1, self.bet_multiplier, 'base', self.game_denom)
            
            line_win = LineWin(prize * self.bet_multiplier, line_number, number_of_symbols, symbol, sub, mul, self.bet_multiplier,  win_type, self.denom)
            
            # print(line_win.displayPlayline())
            print("Line Win:", line_win.number_of_symbols, "x", symbol, '=', line_win.getLineWin())

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