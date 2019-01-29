import os
import json

from playtest_harness import GameWin, LineWin, ScatterWin, symbol_index, scatter_sym_index, GAME_MAXLINES

class PlayTest(): 

    def __init__(self, fname, bet=1, lines=1, denom=1 ): 
        self.input_fname = fname
        
        # Generate a GameWin
        self.games_l = list() 

        # Set Bet Options
        self.bet_multiplier = bet 
        self.lines_played = lines 
        self.game_denom = denom

        self.playResult(True) 
        self.games_l = self.processGames()

        for game in self.games_l: 
            print("GameID: " + str(game.gameID) + " Prize: " + str(game.prize))

        self.doChecklist()

    def doChecklist(self): 
        # Verify that the game has paid out on all expected lines
        lines_won = list() 
        for game in self.games_l: 
            for linewin in game.linewin_list: 
                lines_won.append(linewin.linenumber)

        play_test_lines_won = list(set(lines_won))
        expected_game_lines_to_win = list(range(1, GAME_MAXLINES))
        if play_test_lines_won == expected_game_lines_to_win:
            print("All pay lines have been awarded a prize")
        else: 
            print("Paylines that have not been awarded a prize: ")
            print(list(set(expected_game_lines_to_win) - set(play_test_lines_won)))

        # Verify that the substitute symbols have paid out for all expected symbols
        substitute_win = list() 
        subwin_symbols_l = list() 

        for game in self.games_l: 
            for linewin in game.linewin_list: 
                if linewin.substitute_win == True: 
                    substitute_win.append(linewin)

            for win in substitute_win:
                subwin_symbols_l.append(win.symbol)

    def processGames(self): 
        games_list = list()

        for game_outcome in self.games['game_data']: 
            linewin_l = list() 
            scatterwin_l = list() 

            for win in game_outcome['game_details']: 

                symbol = ""
                if win['win_type'] == "linewin": 
                    for k,v in symbol_index.items(): 
                        if v == win['symbol']: 
                            symbol = k
                    
                    line_win = LineWin(win['prize'], win['line_number'], win['number_of_symbols'], symbol, \
                        win['substitute_win'],win['multiplier'], win['bet'], win['game_type'], win['den'], \
                        win['lines_played']) 
                    linewin_l.append(line_win)

                elif win['win_type'] == "scatterwin": 
                    for k,v in scatter_sym_index.items(): 
                        if v == win['symbol']: 
                            symbol = k

                    if win['pattern']:
                        scatterwin = ScatterWin(win['prize'], win['number_of_symbols'], symbol, win['den'], \
                            win['bet'], win['lines_played'], win['game_type'], win['pattern'])
                    else: 
                        scatterwin = ScatterWin(win['prize'], win['number_of_symbols'], symbol, win['den'], \
                        win['bet'], win['lines_played'], win['game_type'])

                    scatterwin_l.append(scatterwin)
                # todo: bonus prizes / progressives / features / free games

                else: 
                    print("Unknown win data")
                    print(json.dumps(win, indent=4, sort_keys=True, separators=(',',':')))


            game_win = GameWin(game_outcome['id'], linewin_l, scatterwin_l) 
            games_list.append(game_win)

        return games_list

    def playResult(self, readfile = False): 
        gameresult = None

        if not readfile: 
            #  def __init__(self, gameID, linewin_list={}, scatterwin_list={}, bonus_prizes_list={}, progressive_prizes_list={}, free_games_feature_list={}):
            linewin_list = self.prompt_for_line_win() 
            # gameresult = GameWin("test", ) 
        else: 
            self.games = self.readGameHistoryfromFile(self.input_fname)


    def readGameHistoryfromFile(self, json_filename): 
        data = dict() 

        if (os.path.isfile(json_filename)):       
            with open(json_filename, 'r') as json_file:
                data = json.load(json_file)
        else: 
            # build JSON data as a dict
            data = dict() 
            data['game_data'] = list()
            game_info_1 =         {
                'id' : 1,
                'game_details' : [
                    {
                        'win_type' : "linewin",
                        'line_number' : 1,
                        'number_of_symbols' : 5,
                        'symbol' : 9, 
                        'substitute_win' : False, 
                        'multiplier' : 1,
                        'bet' : 10, 
                        'lines_played' : 30, 
                        'game_type' : "base",
                        'den' : 1,
                        'pattern' : [ True,    True,  True,  True,  True,  False,  False,  False,  False,  False,  False,   False,   False,   False,   False],
                        'prize': 500,                       
                    }, 
                    {
                        'win_type' : "linewin",
                        'line_number' : 2,
                        'number_of_symbols' : 3,
                        'symbol' : 0, 
                        'substitute_win' : False, 
                        'multiplier' : 1,
                        'bet' : 10, 
                        'lines_played' : 30, 
                        'game_type' : "base",
                        'den' : 1,
                        'pattern' : [ False,    False,  False,  False,  False,  True,  True,  True,  True,  True,  False,   False,   False,   False,   False],
                        'prize': 50,                         
                    },                     
                ]
            }
            data['game_data'].append(game_info_1)

            game_info_2 =         {
                'id' : 2,
                'game_details' : [
                    {
                        'win_type' : "linewin",
                        'line_number' : 3,
                        'number_of_symbols' : 5,
                        'symbol' : 9, 
                        'substitute_win' : False, 
                        'multiplier' : 1,
                        'bet' : 10, 
                        'lines_played' : 30, 
                        'game_type' : "base",
                        'den' : 1,
                        'pattern' : [ False,    False,  False,  False,  False,  False,  False,  False,  False,  False,  True,   True,   True,   True,   True],
                        'prize': 500,                         
                    }                    
                ]
            }
            data['game_data'].append(game_info_2)

            game_info_3 =         {
                'id' : 3,
                'game_details' : [
                    {
                        'win_type' : "scatterwin",
                        'line_number' : 0,
                        'number_of_symbols' : 3,
                        'symbol' : 0, # scatter symbol 
                        'substitute_win' : False, 
                        'multiplier' : 1,
                        'bet' : 10, 
                        'lines_played' : 30, 
                        'game_type' : "base",
                        'den' : 1,
                        'pattern' : [ False,    False,  False,  False,  False,  False,  False,  False,  False,  False,  False,   False,   True,   True,   True],
                        'prize': 1500
                    }                    
                ]
            }
            data['game_data'].append(game_info_3)

            with open(json_filename, 'w+') as json_file:
                # write test json data to disk
                json.dump(data, json_file, sort_keys=True, indent=4, separators=(',',':')) # write to disk

        return data

    def prompt_for_line_win(self): 
        linewin_l = list() 

        # def __init__(self, line_number, n_of_sym, sym, sub, mul, bet, wintype, den, lines_played=30):
        line_number = input('Line Number: ')
        number_of_symbols = input('Number of Symbols: ')
        print(self.displaySymbols())
        line_number = input('Symbol: ')

    def displaySymbols(self):
        print("Reel Symbols: ")
        for k,v in sorted(symbol_index.items()):
            print("\t"+ k) 

        print("\nScatter Symbols: ")
        for k,v in sorted(scatter_sym_index.items()):
            print("\t"+k) 

    def generateWin(self): 
        ts = datetime.now().timestamp()

        lw = LineWin(18, 3, 'HOTEL', False, 1, self.bet_multiplier,'base')

        linewin_list = list() 
        linewin_list.append(lw)

        win = GameWin(ts, linewin, 0, 0)
        self.games_played.append(win)


def main(): 
    app = PlayTest("egm_play_data.json", 10,30, 1) # bet, lines, denom

if __name__ == "__main__": main()