from omega_virus import Omega_virus
from droid import Droid
from item import Item
from player import Player
from room import Room



# Room(name, code, player_codes, is_trapped, items, color)

entry = Room('entry', 123, 321, False, [], 'green')
hall = Room('hall', 213, 321, False, [], 'green')
win_room = Room('win_room', 000, 321, False, [], 'green')
entry.n = hall
hall.s=entry
entry.e = win_room
win_room.w = entry




def game():
    quit = False
    player_color = None
    player_code = None

    #choose player color
    while player_color == None:
        player_color_choice = input('Pick your color: Blue, Green, Yellow, or Red?\n')
        if player_color_choice.lower() in ['blue', 'green', 'yellow', 'red']:
            player_color = player_color_choice
        elif player_color_choice.lower() in ['quit', 'q']:
            break
        else:
            print('please enter a valid color name')

    #choose player code
    while player_code == None:
        player_code_choice = input('Enter a 3 digit code\n')
        if player_code_choice.isdigit() == True:
            if len(player_code_choice) == 3:
                player_code = int(player_code_choice)
            else:
                print('please enter a 3-digit number')
        elif player_code_choice in ['quit', 'q']:
            break
        else: 
            print('please enter a number')
    player = Player(player_color, player_code, entry)
    print(player)



    while quit != True:
        if player.loc == win_room:
            win_room.code = player.code
        print(player.loc)
        action = input('What do you want to do?\n')
        split = action.split()
        if action == 'q':
            quit = True
        elif split[0] == 'go' or split[0] == 'move':
            if len(split) == 1: 
                print(f'Sorry, {split[0]} where?')
            elif split[1].lower() in ['n', 'north', 'w', 'west', 's', 'south', 'e', 'east']:
                player.move(split[1][0])
        elif action in ['i', 'inventory', 'check inventory', 'open inventory']:
            print(player.print_inv())
        else:
            print("sorry don't recognize that")
        
    print('Thanks for playing')

game()









