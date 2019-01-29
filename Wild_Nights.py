import unittest
import os

GAME_DENOM = [1, 2, 5, 10, 100]
GAME_MAXLINES = 30
GAME_BET_OPTION = [1, 2, 3, 5, 10] 
GAME_BET_OPTION_LINES = [1, 5, 10, 25, 30]

scatter_sym_index = {
    'DOLLAR': 0
}

scatter_valid_positions_base_game = [
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True 
]

scatter_valid_positions_free_game = [
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True 
]

# Define Lines
# Positions [1]  [2]  [3]  [4]  [5]
#           [6]  [7]  [8]  [9]  [10]
#           [11] [12] [13] [14] [15]
paylines_30 = {
            1: [    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False,  
                    False,  False,  False,  False,  False], # Line 1
            2: [    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False],
            3: [    False,  False,  False,  False,  False,  
                    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True],
            4: [    True,   False,  False,  False,  True,  
                    False,  True,   False,  True,   True,   
                    False,  False,  True,   False,  False],
            5: [    False,  False,  True,   False,  False,  
                    False,  True,   False,  True,   False,   
                    True,   False,  False,  False,  True], 
            6: [    True,   True,   False,  True,   True,  
                    False,  False,  True,   False,  False,   
                    False,  False,  False,  False,  False], 
            7: [    False,  False,  False,  False,  False,  
                    False,  False,  True,   False,  False,  
                    True,   True,   False,  True,   True], 
            8: [    False,  False,  False,  False,  False,  
                    True,   False,  False,  False,  True,   
                    False,  True,   True,   True,   False], 
            9: [    False,  True,   True,   True,   False,  
                    True,   False,  False,  False,  True,   
                    False,  False,  False,  False,  False], 
            10:[    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False], 
            11:[    False,  False,  False,  False,  False,
                    False,   True,   True,   True,   False,   
                    True,   False,  False,  False,  True], 
            12: [   True,   False,  True,   False,  True,  
                    False,  True,   False,  True,   False,   
                    False,  False,  False,  False,  False], 
            13: [   False,  False,  False,  False,  False,  
                    False,  True,   False,  True,   False,   
                    True,   False,  True,   False,  True], 
            14: [   False,  True,   False,  True,   False, 
                    True,   False,  True,   False,  True,   
                    False,  False,  False,  False,  False], 
            15: [   False,  False,  False,  False,  False,  
                    True,   False,  True,   False,  True,  
                    False,  True,  False,   True,   False], 
            16: [   True,   True,   False,  True,   True,  # To Do from here
                    False,  False,  True,   False,  False,   
                    False,  False,  False,  False,  False], 
            17: [   False,  False,  False,  False,  False,  
                    False,  False,  True,   False,  False,  
                    True,   True,   False,  True,   True], 
            18: [   False,  False,  False,  False,  False,  
                    True,   False,  False,  False,  True,   
                    False,  True,   True,   True,   False], 
            19: [   False,  True,   True,   True,   False,  
                    True,   False,  False,  False,  True,   
                    False,  False,  False,  False,  False], 
            20:[    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False], 
            21:[    False,  False,  False,  False,  False,
                    False,   True,   True,   True,   False,   
                    True,   False,  False,  False,  True], 
            22: [   True,   False,  True,   False,  True,  
                    False,  True,   False,  True,   False,   
                    False,  False,  False,  False,  False], 
            23: [   False,  False,  False,  False,  False,  
                    False,  True,   False,  True,   False,   
                    True,   False,  True,   False,  True], 
            24: [   False,  True,   False,  True,   False, 
                    True,   False,  True,   False,  True,   
                    False,  False,  False,  False,  False], 
            25: [   False,  False,  False,  False,  False,  
                    True,   False,  True,   False,  True,  
                    False,  True,  False,   True,   False],
            26: [   True,   True,   False,  True,   True,  
                    False,  False,  True,   False,  False,   
                    False,  False,  False,  False,  False], 
            27: [   False,  False,  False,  False,  False,  
                    False,  False,  True,   False,  False,  
                    True,   True,   False,  True,   True], 
            28: [   False,  False,  False,  False,  False,  
                    True,   False,  False,  False,  True,   
                    False,  True,   True,   True,   False], 
            29: [   False,  True,   True,   True,   False,  
                    True,   False,  False,  False,  True,   
                    False,  False,  False,  False,  False], 
            30:[    False,  False,  False,  False,  False,  
                    True,   True,   True,   True,   True,   
                    False,  False,  False,  False,  False],                                         
}

paylines_1 = {
    1 : paylines_30[1] ## [True,     True,   True,   True,   True,   False,  False,  False,  False,  False,  False,  False,  False,  False,  False], # Line 1
}

paylines_5 = { 
    1 : paylines_30[1],
    2 : paylines_30[2],
    3 : paylines_30[3],
    4 : paylines_30[4],
    5 : paylines_30[5]
}
# GAME_BET_OPTION_LINES = [1, 5, 10, 25, 30]

paylines_10 = {
    1 : paylines_30[1],
    2 : paylines_30[2],
    3 : paylines_30[3],
    4 : paylines_30[4],
    5 : paylines_30[5],
    6 : paylines_30[6], 
    7 : paylines_30[7],
    8 : paylines_30[8], 
    9 : paylines_30[9],
    10: paylines_30[10]
}

paylines_25 = {
    1 : paylines_30[1],
    2 : paylines_30[2],
    3 : paylines_30[3],
    4 : paylines_30[4],
    5 : paylines_30[5],
    6 : paylines_30[6], 
    7 : paylines_30[7],
    8 : paylines_30[8], 
    9 : paylines_30[9],
    10: paylines_30[10],
    11 : paylines_30[11],
    12 : paylines_30[12],
    13 : paylines_30[13],
    14 : paylines_30[14],
    15 : paylines_30[15],  
    16 : paylines_30[16], 
    17 : paylines_30[17],
    18 : paylines_30[18], 
    19 : paylines_30[19],
    20 : paylines_30[20],
    21 : paylines_30[21],
    22 : paylines_30[22],
    23 : paylines_30[23],
    24 : paylines_30[24],
    25 : paylines_30[25]
}

symbol_index = { 
        'HOTEL' : 0, 
        '777': 1, 
        'VEGAS': 2, 
        'FLARE': 3, 
        'ELECTRIC_GIRL': 4, 
        'sym_ACE': 5, 
        'sym_KING': 6, 
        'sym_QUEEN': 7, 
        'sym_JACK': 8, 
        'sym_TEN': 9, 
        'sym_NINE' : 10
    }

# Paytables
# Base game for 1c, 2c, 5c and 10c denomination
paytable_l_base_1c_2c_5c_10c = [
            [0, 0, 5, 100, 300],  # sym_A
            [0, 0, 5, 100, 200], # sym_B
            [0, 0, 5, 75, 200], # sym_C
            [0, 0, 5, 75, 200], # sym_D
            [0, 0, 5, 50, 150], # sym_E
            [0, 0, 5, 40, 100], # sym_ACE
            [0, 0, 5, 20, 100], # sym_KING
            [0, 0, 5, 20, 100], # sym_QUEEN
            [0, 0, 5, 20, 50], # sym_JACK
            [0, 0, 5, 20, 50], # sym_TEN
            [0, 0, 5, 20, 50], # sym_NINE
            ]

# Free game paytable for 1c, 2c, 5c and 10c denomination
paytable_l_free_1c_2c_5c_10c = [
            [0, 0, 5, 0, 300],    # sym_A
            [0, 0, 5, 0, 200],    # sym_B
            [0, 0, 5, 0, 200],    # sym_C
            [0, 0, 5, 0, 200],    # sym_D
            [0, 0, 5, 0, 150],    # sym_E
            [0, 0, 5, 0, 100],    # sym_ACE
            [0, 0, 5, 0, 100],    # sym_KING
            [0, 0, 5, 0, 100],    # sym_QUEEN
            [0, 0, 5, 0, 50],    # sym_JACK
            [0, 0, 5, 0, 50],    # sym_TEN
            [0, 0, 5, 0, 50]    # sym_NINE
            ]
# Base game for 100c denomination
paytable_l_base_100c = [
            [0, 2, 5, 100, 300],   # sym_A
            [0, 2, 5, 100, 200],   # sym_B
            [0, 2, 5, 75, 200],   # sym_C
            [0, 2, 5, 75, 200],   # sym_D
            [0, 2, 5, 50, 150],   # sym_E
            [0, 0, 5, 40, 100],   # sym_ACE
            [0, 0, 5, 20, 100],   # sym_KING
            [0, 0, 5, 20, 100],   # sym_QUEEN
            [0, 0, 5, 20, 50],   # sym_JACK
            [0, 0, 5, 20, 50],   # sym_TEN
            [0, 0, 5, 20, 50]    # sym_NINE
            ]
# Free game for 100c denomination
paytable_l_free_100c = [
            [0, 2, 5, 0, 300],  # sym_A
            [0, 2, 5, 0, 200],  # sym_B
            [0, 2, 5, 0, 200],  # sym_C
            [0, 2, 5, 0, 200],  # sym_D
            [0, 2, 5, 0, 150],  # sym_E
            [0, 0, 5, 40, 100],  # sym_ACE
            [0, 0, 5, 20, 100],  # sym_KING
            [0, 0, 5, 20, 100],  # sym_QUEEN
            [0, 0, 5, 20, 50],   # sym_JACK
            [0, 0, 5, 20, 50],   # sym_TEN
            [0, 0, 5, 20, 50]    # sym_NINE
            ]

# Scatter  paytable for 1c,2c and 5c,10c, 100c denom 
paytable_scat_basegame_1c_2c = [
                [ 0, 0, 5, 20, 100],  # DOLLAR
            ]

paytable_scat_basegame_5c_10c_100c = [
                [ 0, 2, 5, 20, 100],  # DOLLAR
              ]
# Scatter paytable for 1c,2c and 5c,10c, 100c denom 
paytable_scat_freegame_1c_2c_5c_10c = [
                [ 0, 0, 5, 20, 0],  # DOLLAR
              ]
# Scatter paytable for 100c denom 
paytable_scat_freegame_100c = [
                [ 0, 0, 5, 20, 0],  # DOLLAR
              ]

class Wild_Nights(): 

    def __init__(self): 
        self.denom = 1
        self.win_type = 'base'


    def getPayTable(self, den, win_type): 

        self.denom = den
        self.win_type = win_type

        if (self.denom == 1 or self.denom == 2 or self.denom == 5 or self.denom == 10) and self.win_type == 'base': 
            return paytable_l_base_1c_2c_5c_10c
        elif (self.denom == 1 or self.denom == 2 or self.denom == 5 or self.denom == 10) and self.win_type == 'free_games':  
            return paytable_l_free_1c_2c_5c_10c
        elif self.denom == 100 and self.win_type == 'base': 
            return paytable_l_base_100c
        elif self.denom == 100 and self.win_type == 'free_games':
            return paytable_l_free_100c
        else: 
            print("No valid paytable identified")
