from omega_virus import Omega_virus
from droid import Droid
from item import Item
from player import Player
from room import Room




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
    player = Player(player_color, player_code)
    print(player)
    while quit != True:
        action = input('What do you want to do?')
        if action == 'q':
            quit = True
    print('Thanks for playing')

game()









