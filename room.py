class Room:
    def __init__(self, name, desc, inv, connections):
        self.name = name
        self.desc = desc
        self.inv = inv
        self.connections = connections

    def entry(self):
        print(f'you have entered the {self.name} - {self.desc}, you see')
        if self.inv is not None:
            for item in self.inv.objects:
                item.describe()
        Event(f'y to enter the - {self.connections[0].name}, n to enter - {self.connections[1].name}', self.connections[0], self.connections[1])

class Event:
    def __init__(self, prompt, room1, room2):
        self.room2 = room2
        self.room1 = room1
        self.prompt = prompt
        self.event()

    def event(self):
        inp = input(self.prompt)
        if inp == 'y':
            self.room1.entry()
            return self.room1
        elif inp == 'n':
            self.room2.entry()
            return self.room2
        else:
            print('invalid selection')
            return None