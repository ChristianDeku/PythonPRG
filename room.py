import object as o
import inventory as i


class Room:
    def __init__(self, name, desc, inv, connections):
        self.name = name
        self.desc = desc
        self.inv = inv
        self.connections = connections

    def entry(self):
        print(f'\nyou have entered the {self.name} - {self.desc}, you see: \n')
        if self.inv is not None:
            self.inv.show_contents()
        #Event(f'y to enter the - {self.connections[0].name}, n to enter - {self.connections[1].name}', self.connections[0], self.connections[1])


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


def setup_rooms():
    all_rooms = []
    f = open('level.txt').readlines()
    for line in f:
        row = line.split(',')
        room_id, name, desc, connections, obj = [rm.strip() for rm in row]
        room_connections = connections.split('.')
        objects = []
        if int(obj[0]) == 1:
            items = obj.split('-')
            for item in range(1, len(items)):
                each_item = items[item].split('.')
                if each_item[0] == 'o':
                    objects.append(o.Object(each_item[1], each_item[2]))
                elif each_item[0] == 'p':
                    objects.append(o.Potion(each_item[1], each_item[2], each_item[3]))
                elif each_item[0] == 'w':
                    objects.append(o.Weapon(each_item[1], each_item[2], each_item[3]))
        if len(objects) > 0:
            room_inv = i.Inventory(objects)
            room = Room(name, desc, room_inv, room_connections)
        else:
            room = Room(name, desc, None, room_connections)
        all_rooms = all_rooms + [room]

    #room1 = r.Room("dungeon", 'a dark scary place', i.Inventory([o.Object('crystal', 'power up a sword')]))
    #room2 = r.Room("cave", 'a small scary place', i.Inventory([o.Object('rock', 'do nothing')]))
    #room3 = r.Room("woods", 'a gloomy forest', [])
    #room4 = r.Room("beach", 'a sunny place', [])

    #room1.connections = [room3, room4]
    #room2.connections = [room1, room3]
    #room3.connections = [room1, room4]
    #room4.connections = [room2, room3]

    # all_rooms = [room1, room2, room3, room4]
    for each_room in all_rooms:
        print(each_room.name)
    return all_rooms