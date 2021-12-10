class Inventory:
    def __init__(self, objects):
        self.can_hold = 3
        self.objects = objects

    def show_contents(self):
        for item in self.objects:
            item.describe()
        print() # make new line
# inv.objects.append() - adds item to inventory
