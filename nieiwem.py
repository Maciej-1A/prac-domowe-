import time
import random

class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.gold = 0
        self.inventory = []
        self.level = 1
        self.status_effects = []

    def apply_status_effect(self, effect):
        for existing_effect in self.status_effects:
            if existing_effect.name == effect.name:
                existing_effect.duration = max(existing_effect.duration, effect.duration)
                return
        self.status_effects.append(effect)
        print_slow(f"You are now under the effect of {effect.name}!")

    def display_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Gold: {self.gold}")
        print("Inventory:", ', '.join(self.inventory) if self.inventory else "Empty")

class StatusEffect:
    def __init__(self, name, duration, effect):
        self.name = name
        self.duration = duration
        self.effect = effect

def update_status_effects(player):
    updated_effects = []
    for effect in player.status_effects:
        effect.duration -= 1
        if effect.duration > 0:
            updated_effects.append(effect)
        else:
            print_slow(f"The {effect.name} effect has worn off!")

    player.status_effects = updated_effects

class Dungeon:
    def __init__(self, name, description, enemies, boss):
        self.name = name
        self.description = description
        self.enemies = enemies
        self.boss = boss

def explore_dungeon(player, dungeon):
    print_slow(f"You enter the {dungeon.name}. {dungeon.description}")

    for enemy in dungeon.enemies:
        battle(player, enemy)

    print_slow(f"A fearsome boss, {dungeon.boss.name}, appears!")
    battle(player, dungeon.boss)

class Character:
    def __init__(self, name, health, attack, defense, gold_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.gold_reward = gold_reward

class Enemy:
    def __init__(self, name, health, attack, defense, gold_reward, experience_reward, status_effects=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.gold_reward = gold_reward
        self.experience_reward = experience_reward
        self.status_effects = status_effects or []

    def apply_status_effect(self, effect):
        for existing_effect in self.status_effects:
            if existing_effect.name == effect.name:
                existing_effect.duration = max(existing_effect.duration, effect.duration)
                return
        self.status_effects.append(effect)
        print_slow(f"The {self.name} is now under the effect of {effect.name}!")

    def update_status_effects(self):
        updated_effects = []
        for effect in self.status_effects:
            effect.duration -= 1
            if effect.duration > 0:
                updated_effects.append(effect)
            else:
                print_slow(f"The {effect.name} effect on the {self.name} has worn off!")

        self.status_effects = updated_effects

def apply_status_effect(target, effect):
    if isinstance(target, Player):
        target.apply_status_effect(effect)
    elif isinstance(target, Enemy):
        target.apply_status_effect(effect)

class Quest:
    def __init__(self, name, description, reward, experience_reward):
        self.name = name
        self.description = description
        self.reward = reward
        self.experience_reward = experience_reward
        self.completed = False

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def level_up(player):
    player.level += 1
    player.attack += 2
    player.defense += 1
    player.health += 5
    print_slow(f"Congratulations! You leveled up to level {player.level}. Your stats have increased.")

def battle(player, enemy):
    print_slow(f"A wild {enemy.name} appears!")

    while player.health > 0 and enemy.health > 0:
        print_slow("\nOptions:")
        print("1. Attack")
        print("2. Use item")
        print("3. Run")

        choice = input("Choose your action: ")

        if choice == "1":
            player_damage = max(0, player.attack - enemy.defense)
            enemy_damage = max(0, enemy.attack - player.defense)

            enemy.health -= player_damage
            player.health -= enemy_damage

            print_slow(f"You deal {player_damage} damage to {enemy.name}.")
            print_slow(f"{enemy.name} deals {enemy_damage} damage to you.")

        elif choice == "2":
            if player.inventory:
                print("Inventory:")
                for i, item in enumerate(player.inventory, start=1):
                    print(f"{i}. {item}")

                use_item = input("Choose an item to use (enter the number): ")
                try:
                    index = int(use_item) - 1
                    if 0 <= index < len(player.inventory):
                        used_item = player.inventory.pop(index)
                        print_slow(f"You used {used_item}.")
                    else:
                        print_slow("Invalid item selection.")
                except ValueError:
                    print_slow("Invalid input. Enter a number.")
            else:
                print_slow("Your inventory is empty.")

        elif choice == "3":
            print_slow("You run away!")
            return

        else:
            print_slow("Invalid choice. Try again.")

    if player.health <= 0:
        print_slow("You were defeated. Game over.")
    else:
        print_slow(f"You defeated the {enemy.name} and earned {enemy.gold_reward} gold!")
        player.gold += enemy.gold_reward
        player.display_stats()

        for quest in active_quests:
            if quest.name == "Defeat the Dragon" and enemy.name == "Dragon" and not quest.completed:
                quest.completed = True
                player.inventory.append(quest.reward)
                player.gold += quest.experience_reward
                print_slow(f"Quest completed: {quest.name}! You earned a {quest.reward} and {quest.experience_reward} experience points.")

                if player.gold >= 20:
                    level_up(player)

        enemy.update_status_effects()

def visit_shop(player):
    print_slow("Welcome to the Shop!")
    print_slow("1. Buy Health Potion (5 gold)")
    print_slow("2. Buy Sword Upgrade (10 gold)")
    print_slow("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if player.gold >= 5:
            player.gold -= 5
            player.inventory.append("Health Potion")
            print_slow("You bought a Health Potion.")
        else:
            print_slow("Not enough gold.")

    elif choice == "2":
        if player.gold >= 10:
            player.gold -= 10
            player.attack += 2
            print_slow("You upgraded your sword.")
        else:
            print_slow("Not enough gold.")

    elif choice == "3":
        print_slow("Thanks for visiting the Shop!")

    else:
        print_slow("Invalid choice. Try again.")

def main():
    player_name = input("Enter your name: ")
    player = Player(name=player_name, health=20, attack=5, defense=2)

    enemies = [
        Enemy(name="Goblin", health=8, attack=3, defense=1, gold_reward=5, experience_reward=2),
        Enemy(name="Orc", health=12, attack=4, defense=2, gold_reward=8, experience_reward=5),
        Enemy(name="Dragon", health=20, attack=8, defense=5, gold_reward=15, experience_reward=10),
        Enemy(name="Skeleton", health=6, attack=2, defense=1, gold_reward=3, experience_reward=1)
    ]

    dungeons = [
        Dungeon(name="Dark Forest", description="filled with mysterious creatures", enemies=enemies[:-1], boss=enemies[-1]),
        Dungeon(name="Cave of Wonders", description="rumored to hold great treasures", enemies=enemies[:2], boss=enemies[2])
    ]

    global active_quests
    active_quests = [
        Quest(name="Defeat the Dragon", description="Defeat the mighty Dragon.", reward="Sword Upgrade", experience_reward=8),
        Quest(name="Skeleton Hunt", description="Defeat 5 Skeletons.", reward="Golden Key", experience_reward=5)
    ]

    while True:
        player.display_stats()

        print_slow("\nOptions:")
        print("1. Explore a Dungeon")
        print("2. Visit the Shop")
        print("3. View Quests")
        print("4. Quit")

        choice = input("Choose your action: ")

        if choice == "1":
            dungeon = random.choice(dungeons)
            explore_dungeon(player, dungeon)

        elif choice == "2":
            visit_shop(player)

        elif choice == "3":
            print("\nQuests:")
            for quest in active_quests:
                status = "Completed" if quest.completed else "Incomplete"
                print(f"{quest.name}: {quest.description} - {status}")

        elif choice == "4":
            print_slow("Thanks for playing. Goodbye!")
            break

        else:
            print_slow("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
