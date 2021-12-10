def go(command):
    return 'go'


def use(player, command):
    if len(command) > 1:
        count = len(player.inv.objects)
        for item in player.inv.objects:
            count -= 1
            if command[1] == item.name:
                item.use()
                return
                # return f'used {item.name}' - handled by object at the moment
            if count == 0:
                return f'you do not have a {command[1]} to use'
    else:
        return 'please specify an item to use \n'
