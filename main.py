import room as r
import object as o
import inventory as i
import charater as c

current_room = None


def intro():
    name = input("what is your name?")
    inv = i.Inventory()
    inv.objects.append(o.Object('wool', 'start a fire'))
    inv.objects.append(o.Weapon('sword', 'slay a dragon', 20))
    inv.objects.append(o.Potion('healing potion', 'heal you', 10))
    player = c.Player(name, inv)
    print(f"Hey {player.name} here are the contents of your backpack: ")
    for item in inv.objects:
        item.describe()

    room3_connections = []
    room3 = r.Room("woods", 'a gloomy forest', None, room3_connections)

    room4_connections = []
    room4 = r.Room("beach", 'a sunny place', None, room4_connections)

    room1_inv = i.Inventory()
    room1_inv.objects.append(o.Object('crystal', 'power up a sword'))
    room1_connections = [room3, room4]
    room1 = r.Room("dungeon", 'a dark scary place', room1_inv, room1_connections)

    room2_inv = i.Inventory()
    room2_inv.objects.append(o.Object('rock', 'do nothing'))
    room2_connections = [room1, room3]
    room2 = r.Room("cave", 'a small scary place', room2_inv, room2_connections)

    room3_connections.append(room1)
    room3_connections.append(room4)

    room4_connections.append(room2)
    room4_connections.append(room3)

    room = r.Event('you have fallen into a dark hole, do you follow the light?', room1, room2)


def game_loop():
    #while True:
        #input
        #update
        #render
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rooms = setuprooms() # reads a txt file and setup up values and stores in a room array
    intro()
    game_loop()
