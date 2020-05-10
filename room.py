class Room:
    def __init__(self, name, code, player_code, is_trapped, items, color):
        self.name=name
        self.code=code
        self.player_codes = {
            'blue': player_code,
            'green': player_code,
            'yellow': player_code,
            'red': player_code
        }
        self.is_trapped = is_trapped
        self.items = items
        self.color = color 
        self.n = None
        self.e = None
        self.w = None
        self.s = None

    def __str__(self):
        return f'\n You are in the {self.name}. The code is: {self.code}\n'


#room
    #code
    #code of each player
    #location on board?
    #is booby trapped?
        #correct code
    #inventory
    #color (key it needs for entrance)