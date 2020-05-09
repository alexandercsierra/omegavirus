class Player:
    def __init__(self, color, code):
        self.color = color
        self.inventory = []
        self.droid = False
        self.code = code

    def __str__(self):
        return f"{self.color}, has {self.inventory}. Droid? {self.droid} Secret code: {self.code}"


#player
    #color
    #inventory (possibly containing 4 weapons and 4 keys)
    #droid/no droid
    #code