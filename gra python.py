#gra :)

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

# player
class player:
    def __init__(self):
        self.name = []
        self.type = ''
        self.hp = 0
        self.mp = 0
        self.status_effect = []
        self.location = 'jail'
        self.game_over = False
myPlayer = player()

# title screen
def title_screen_selections():
    option = input(">")
    if option.lower() == ("play"):
        start_game() #placeholder
    elif option.lower() == ("help"):
        help_menu() #placeholder
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play' , 'help' , 'quit']:
        print("please give a vail imput uwu")
    option = input(">")
    if option.lower() == ("play"):
        start_game() #placeholder
    elif option.lower() == ("help"):
        help_menu() #placeholder
    elif option.lower() == ("quit"):
        sys.exit()
def title_screen():
    os.system('clear')
    print('#############################')
    print('##### welcome to the game####')
    print('         - Play -            ')
    print('         - help -            ')
    print('         - quit -            ')
    title_screen_selections()

def help_menu():
    print('#############################')
    print('##### welcome to the game####')
    print('   - use commands to play-'   )
    print('-use command map to show map-')
    print('         - GLHF -            ')
    title_screen_selections()



#map and movement :D
# ___________________________
# | a1| a2| a3| a4| a5| jail|
# _____________________
# | b1| b2| b3| b4| b5| 
# _____________________________
# | c1| c2| c3| c4| c5| boss 2|
# ____________________________
# | d1| d2| d3| d4| d5| exit|
#       | boss 1|


    room_data = {
    'DESCRIPTION': 'description',
    'RAIDED': False,
    'UP': 'up',
    'DOWN': 'down',
    'LEFT': 'left',
    'RIGHT': 'right'
}



RAIDED_rooms = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                    'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                    'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                    'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False,
                    'jail' : False, 'boss_1' : False, 'boss_2' :False, }
    
room_map = {
        'a1': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'DOWN': 'b1',
        'RIGHT': 'a2'
    },
        'a2': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'DOWN': 'b2',
        'LEFT': 'a1',
        'RIGHT': 'a3'
    },
        'a3': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'DOWN': 'b3',
        'LEFT': 'a2',
        'RIGHT': 'a4'
    },
        'a4': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'DOWN': 'b4',
        'LEFT': 'a3',
        'RIGHT': 'a5'
    },
        'a5': {
        'DESCRIPTION': 'where it all begins',
        'RAIDED': False,
        'DOWN': 'b5',
        'LEFT': 'a4',
        'RIGHT': 'jail'
    },
        'b1': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'a1',
        'DOWN': 'c1',
        'RIGHT': 'b2'
    },
        'b2': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'a2',
        'DOWN': 'c2',
        'LEFT': 'b1',
        'RIGHT': 'b3'
    },
        'b3': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'a3',
        'DOWN': 'c3',
        'LEFT': 'b2',
        'RIGHT': 'b4'
    },
        'b4': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'a4',
        'DOWN': 'c4',
        'LEFT': 'b3',
        'RIGHT': 'b5'
    },
        'b5': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'a5',
        'DOWN': 'c5',
        'LEFT': 'b4',
    },
        'c1': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'b1',
        'DOWN': 'd1',
        'RIGHT': 'c2'
    },
        'c2': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'b2',
        'DOWN': 'd2',
        'LEFT': 'c1',
        'RIGHT': 'c3'
    },
        'c3': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'b3',
        'DOWN': 'd3',
        'LEFT': 'c2',
        'RIGHT': 'c4'
    },
        'c4': {
        'DESCRIPTION': 'a room with a bomb',
        'RAIDED': False,
        'UP': 'b4',
        'DOWN': 'd4',
        'LEFT': 'c3',
        'RIGHT': 'c5'
    },
        'c5': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'b5',
        'DOWN': 'd5',
        'LEFT': 'c4',
        'RIGHT': 'boss_2'
    },
        'd1': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'c1',
        'RIGHT': 'd2'
    },
        'd2': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'c2',
        'LEFT': 'd1',
        'RIGHT': 'd3'
    },
        'd3': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'c3',
        'DOWN': 'boss_1',
        'LEFT': 'd2',
        'RIGHT': 'd4'
    },
        'd4': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'c4',
        'LEFT': 'c3',
        'RIGHT': 'c5'
    },
        'd5': {
        'DESCRIPTION': 'a room',
        'RAIDED': False,
        'UP': 'c5',
        'LEFT': 'd4',
        'RIGHT': 'exit'
    },
        'exit': {
        'DESCRIPTION': 'freedom',
        'RAIDED': False,
    },
        'jail': {
        'DESCRIPTION': 'stepbro help Im stuck',
        'RAIDED': False,
        'LEFT': 'a5',
    },
        'boss_1': {
        'DESCRIPTION': 'a old genral with a glowing hand',
        'RAIDED': False,
        'UP': 'd3',
    },
        'boss_2': {
        'DESCRIPTION': 'a big angry grey guy?',
        'RAIDED': False,
        'DOWN': 'exit',
    },
}
#game interactivety
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location + '#')
    print('#' + room_map[myPlayer.location]['DESCRIPTION'] + '#')
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    
def prompt():
    print("\n" + "======================")
    print("what will you do?")
    action = input("> ")
    acceptable_actions = ['go', 'quit']
    while action.lower() not in acceptable_actions:
        print('na uh try again')
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == 'go':
        player_move(action.lower)

def player_move(myAction):
    ask = "where do you wanna go?\n"
    dest = input(ask)
    if dest.lower() == 'up':
        movement_handler('UP')
    elif dest.lower() == 'down':
        movement_handler('DOWN')
    elif dest.lower() == 'left':
        movement_handler('LEFT')
    elif dest.lower() == 'right':
        movement_handler('RIGHT')
    else:
        print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")
def movement_handler(destination):
    # Handle the movement logic based on the specified destination
    print(f"Moving {destination}")
    myPlayer.location = destination
    print_location()

#game functionality
def start_game():
    return

def main_game_loop():
    while myPlayer.game_over == False:
        prompt()
#info gather
def setup_game():
    os.system('clear')
question1 = "Hello, what's your name?\n"
for character in question1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
player_name = input("> ")
myPlayer.name = player_name

question2 = "Good! Now, who do you want to be? Choose from warrior, ranged ir mage.\n"
for character in question2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)

player_type = input("> ")
valid_types = ['warrior', 'ranged', 'mage', 'god']

while player_type.lower() not in valid_types:
    print('That is not a valid type.')
    player_type = input("> ")

myPlayer.type = player_type
print("Good! You are now a " + player_type)

question3 = f"Welcome, {player_name}, the {player_type}!\n"
for character in question3:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
#player stasts
if myPlayer.type is 'warior':
    myPlayer.hp = 10
    myPlayer.mp = 5
if myPlayer.type is 'ranged':
    myPlayer.hp = 7
    myPlayer.mp = 7
if myPlayer.type is 'mage':
    myPlayer.hp = 5
    myPlayer.mp = 10
if myPlayer.type is 'god':
    myPlayer.hp = 999
    myPlayer.mp = 999

#inro





title_screen()
