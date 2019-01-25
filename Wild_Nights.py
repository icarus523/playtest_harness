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
    	self.denom = denom
    	self.win_type = win_type


	def getPayTable(self): 
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
