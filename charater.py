class Player:
    def __init__(self, name, inv):
        self.name = name
        self.health = 100
        self.inv = inv

    def attack(self):
        print('attacked ' + str(self.health))