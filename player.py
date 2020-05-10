class Player:
    def __init__(self, color, code, start):
        self.color = color
        self.inventory = ['green keycard']
        self.droid = False
        self.code = code
        self.loc = start

    def __str__(self):
        return f'{self.color}, has {self.inventory}. Droid? {self.droid} Secret code: {self.code}'

    def move(self, new_room):
        if hasattr(self.loc, new_room) and getattr(self.loc, new_room) != None:
            self.loc = getattr(self.loc, new_room)

    def print_loc(self):
        return f'You are standing in {self.loc.name}'

    def print_inv(self):
        return f'You currently have: {self.inventory}'


#player
    #color
    #inventory (possibly containing 4 weapons and 4 keys)
    #droid/no droid
    #code