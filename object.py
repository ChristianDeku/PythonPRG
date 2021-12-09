class Object:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def describe(self):
        print(self.name + ' - can ' + self.desc)

    def use(self):
        print('this item cant be used')


class Weapon(Object):
    def __init__(self, name, desc, ap):
        super().__init__(name, desc)
        self.attack_points = ap

    def use(self):
        print('You attacked with your sword')


class Potion(Object):
    def __init__(self, name, desc, hp):
        super().__init__(name, desc)
        self.attack_points = hp

    def use(self):
        print('you drank a potion')