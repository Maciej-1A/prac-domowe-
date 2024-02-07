import cmd
import textwrap
import sys
import os
import time
import random

# Player class
class Player:
    def __init__(self):
        self.name = ''
        self.type = ''
        self.hp = 0
        self.mp = 0
        self.status_effect = []
        self.location = 'jail'
        self.game_over = False

myPlayer = Player()

# Title screen and menu functions
def title_screen_selections():
    option = input(">")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    else:
        print("Please give a valid input uwu")
        title_screen_selections()

def title_screen():
    os.system('clear')
    print('#############################')
    print('##### Welcome to the game ####')
    print('         - Play -            ')
    print('         - Help -            ')
    print('         - Quit -            ')
    title_screen_selections()

def help_menu():
    print('#############################')
    print('##### Welcome to the game ####')
    print('   - Use commands to play -')
    print('- Use command "map" to show map -')
    print('         - GLHF -            ')
    title_screen_selections()

# Game functionality
def start_game():
    setup_game()
    main_game_loop()

def main_game_loop():
    while not myPlayer.game_over:
        prompt()

# Info gathering
def setup_game():
    os.system('clear')
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    myPlayer.name = input("> ")

    question2 = "Good! Now, who do you want to be? Choose from warrior, ranged, or mage.\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_type = input("> ")
    valid_types = ['warrior', 'ranged', 'mage', 'god']
    while player_type.lower() not in valid_types:
        print('That is not a valid type. Please choose from warrior, ranged, or mage.')
        player_type = input("> ")
    myPlayer.type = player_type

    # Player stats based on type
    if myPlayer.type == 'warrior':
        myPlayer.hp = 10
        myPlayer.mp = 5
    elif myPlayer.type == 'ranged':
        myPlayer.hp = 7
        myPlayer.mp = 7
    elif myPlayer.type == 'mage':
        myPlayer.hp = 5
        myPlayer.mp = 10
    elif myPlayer.type == 'god':
        myPlayer.hp = 999
        myPlayer.mp = 999

    # Introduction
    speech1 = "You are located in a Noxian military jail. Your only mission: escape!"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
speech2 = "you notcied a guard walking by so you knock him out taking his map and weapon"
for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
def print_map():
    print(print_map)



# Map and movement

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
                'jail': False, 'boss_1': False, 'boss_2': False}

room_map = {
    'a1': {'DESCRIPTION': 'a room', 'RAIDED': False, 'DOWN': 'b1', 'RIGHT': 'a2'},
    'a2': {'DESCRIPTION': 'a room', 'RAIDED': False, 'DOWN': 'b2', 'LEFT': 'a1', 'RIGHT': 'a3'},
    'a3': {'DESCRIPTION': 'a room', 'RAIDED': False, 'DOWN': 'b3', 'LEFT': 'a2', 'RIGHT': 'a4'},
    'a4': {'DESCRIPTION': 'a room', 'RAIDED': False, 'DOWN': 'b4', 'LEFT': 'a3', 'RIGHT': 'a5'},
    'a5': {'DESCRIPTION': 'where it all begins', 'RAIDED': False, 'DOWN': 'b5', 'LEFT': 'a4', 'RIGHT': 'jail'},
    'b1': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'a1', 'DOWN': 'c1', 'RIGHT': 'b2'},
    'b2': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'a2', 'DOWN': 'c2', 'LEFT': 'b1', 'RIGHT': 'b3'},
    'b3': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'a3', 'DOWN': 'c3', 'LEFT': 'b2', 'RIGHT': 'b4'},
    'b4': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'a4', 'DOWN': 'c4', 'LEFT': 'b3', 'RIGHT': 'b5'},
    'b5': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'a5', 'DOWN': 'c5', 'LEFT': 'b4'},
    'c1': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'b1', 'DOWN': 'd1', 'RIGHT': 'c2'},
    'c2': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'b2', 'DOWN': 'd2', 'LEFT': 'c1', 'RIGHT': 'c3'},
    'c3': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'b3', 'DOWN': 'd3', 'LEFT': 'c2', 'RIGHT': 'c4'},
    'c4': {'DESCRIPTION': 'a room with a bomb', 'RAIDED': False, 'UP': 'b4', 'DOWN': 'd4', 'LEFT': 'c3', 'RIGHT': 'c5'},
    'c5': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'b5', 'DOWN': 'd5', 'LEFT': 'c4', 'RIGHT': 'boss_2'},
    'd1': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'c1', 'RIGHT': 'd2'},
    'd2': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'c2', 'LEFT': 'd1', 'RIGHT': 'd3'},
    'd3': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'c3', 'DOWN': 'boss_1', 'LEFT': 'd2', 'RIGHT': 'd4'},
    'd4': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'c4', 'LEFT': 'c3', 'RIGHT': 'c5'},
    'd5': {'DESCRIPTION': 'a room', 'RAIDED': False, 'UP': 'c5', 'LEFT': 'd4', 'RIGHT': 'exit'},
    'exit': {'DESCRIPTION': 'freedom', 'RAIDED': False},
    'jail': {'DESCRIPTION': 'stepbro help Im stuck', 'RAIDED': False, 'LEFT': 'a5'},
    'boss_1': {'DESCRIPTION': 'an old general with a glowing hand', 'RAIDED': False, 'UP': 'd3'},
    'boss_2': {'DESCRIPTION': 'a big angry grey guy?', 'RAIDED': False, 'DOWN': 'exit'},
}

# Combat system
def start_combat(enemy_type):
    enemy_hp = 10  # Adjust this based on the enemy type or make it random
    print(f"A wild {enemy_type} appears!")

    # Player's special moves
    special_moves = {
        '1': {'name': 'Attack', 'damage': (1, 5)},
        '2': {'name': 'Fireball', 'damage': (3, 8), 'mp_cost': 3},
        '3': {'name': 'Heal', 'healing': 5, 'mp_cost': 2}
    }

    while myPlayer.hp > 0 and enemy_hp > 0:
        print("\n" + "=" * 20)
        print(f"{myPlayer.name}'s HP: {myPlayer.hp}")
        print(f"{enemy_type}'s HP: {enemy_hp}")
        print("Actions:")
        for move_key, move_data in special_moves.items():
            print(f"{move_key}. {move_data['name']}")

        choice = input("Choose your action: ")

        if choice in special_moves:
            move = special_moves[choice]

            # Check if the player has enough MP for special moves
            if 'mp_cost' in move and myPlayer.mp < move['mp_cost']:
                print("Not enough MP to use this special move!")
                continue

            # Execute special move
            if 'damage' in move:
                # Player deals damage
                damage_range = move['damage']
                player_damage = random.randint(damage_range[0], damage_range[1])
                enemy_hp -= player_damage
                print(f"You use {move['name']} and deal {player_damage} damage to the {enemy_type}!")
            elif 'healing' in move:
                # Player heals
                myPlayer.hp += move['healing']
                print(f"You use {move['name']} and heal for {move['healing']} HP.")

            # Consume MP if applicable
            if 'mp_cost' in move:
                myPlayer.mp -= move['mp_cost']

            # Enemy attacks
            enemy_damage = random.randint(1, 3)  # Adjust damage based on enemy type
            myPlayer.hp -= enemy_damage
            print(f"The {enemy_type} hits you for {enemy_damage} damage!")

        elif choice.lower() == 'run':
            # Player attempts to run
            if random.random() < 0.5:  # 50% chance to successfully run
                print("You successfully run away!")
                return
            else:
                print("You failed to run away!")
                # Enemy attacks since the player couldn't run
                enemy_damage = random.randint(1, 3)
                myPlayer.hp -= enemy_damage
                print(f"The {enemy_type} hits you for {enemy_damage} damage!")

        else:
            print("Invalid choice. Try again.")

    if myPlayer.hp <= 0:
        print("You were defeated. Game over.")
        myPlayer.game_over = True
    else:
        print(f"You defeated the {enemy_type}!")

# Prompt for player action
def prompt():
    print("\n" + "=" * 20)
    print("What will you do?")
    action = input("> ")
    acceptable_actions = ['go', 'quit', 'map']

    if myPlayer.location in ['boss_1', 'boss_2']:
        acceptable_actions.append('attack')  # Allow attack option when encountering a boss

    while action.lower() not in acceptable_actions:
        print('Invalid action. Try again.')
        action = input("> ")

    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == 'go':
        player_move(action.lower())
    elif action.lower() == 'map':
        print_map()
    elif action.lower() == 'attack':
        start_combat('boss' if myPlayer.location == 'boss_1' else 'boss_2')
    else:
        player_special_move(action)
# Player movement
def player_move(my_action):
    ask = "Where do you want to go?\n"
    dest = input(ask)
    if dest.lower() in ['up', 'down', 'left', 'right']:
        movement_handler(dest.lower())
    else:
        print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")

# Movement handler
def movement_handler(destination):
    print(f"Moving {destination}...")
    myPlayer.location = room_map[myPlayer.location][destination]
    print_location()

# Print current location information
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location + '#')
    print('#' + room_map[myPlayer.location]['DESCRIPTION'] + '#')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

# Function to handle player special moves
def player_special_move(choice):
    # Handle special moves logic here
    # You can customize this based on your game's special moves
    pass

# Call title_screen at the end to start the game
title_screen()


