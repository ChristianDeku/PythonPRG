import room as r
import object as o
import inventory as i
import charater as c
import commands

current_room = None
inv = i.Inventory([o.Object('wool', 'start a fire'), o.Weapon('sword', 'slay a dragon', 20),
                   o.Potion('healing_potion', 'heal you', 10)])
player = c.Player('', inv)

def intro():
    name = input("what is your name? \n")
    player.name = name
    print(f"Hey {player.name} here are the contents of your backpack: \n")
    player.inv.show_contents()
    return r.Event('you have fallen into a dark hole, do you follow the light? (y/n) \n', rooms[0], rooms[1])


def process_input():
    command = input('what would you like to do? \n')
    return command.split(' ')


def update(command):
    if command[0] == 'go':
        return commands.go(command)
    elif command[0] == 'use':
        return commands.use(player, command)
    else:
        return 'please enter a valid command \n'


def render(processed_command):
    if processed_command is not None:
        print(f'\n{processed_command}\n')


def game_loop():
    while True:
        command = process_input()
        processed_command = update(command)
        render(processed_command)


if __name__ == '__main__':
    rooms = r.setup_rooms()
    current_room = intro()
    game_loop()
