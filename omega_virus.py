class Omega_virus:
    def __init__(self, code, counter, phrases):
        self.code = code
        self.counter = counter
        self.phrases = phrases
        self.player_codes = {
            'blue':000,
            'green':000,
            'yellow':000,
            'red':000
        }
    
    def set_player_code(self, player, code):
        self.player_codes[player] = code

#omega_virus
    #correct code to win
    #counter for number of turns
    #list of phrases