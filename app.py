import random

# Character creation
char_name = input("What is your character's name? ")
char_class = input("\nClass: Warrior (W), Mage (M), Thief (T) ").title()

# (Class, Weapon, Damage)
char_class = [
    ["Warrior", "Sword", 20],
    ["Mage", "Staff", 5],
    ["Thief", "Dagger", 10]
]

player_xp = 0
player_health = 100
player_level = 1

base_attack = 10
char_atk_bonus = 5
crit_chance = 20

# Enemies
# (Name, Health, Attack)
enemies = [
    ["Slime", 30, 2],
    ["Goblin", 50, 5],
    ["Orc", 80, 10],
    ["Dragon Spawn", 120, 15]
]

# Action Menu 
def Action_Menu(player_health, player_xp):
    global base_attack, player_level
    while player_health > 0:
        choice = input(f"\n{char_name} is resting. HP: {player_health} \nSelect an option: \nExplore (E) \nRest (R) \nQuit (Q) ").upper()
        if choice == "E":
            random_enemy = random.choice(enemies)
            player_health, player_xp = Combat(player_health, player_xp, random_enemy)

            # Level up check after combat
            if player_xp >= (player_level * 50):
                player_level += 1
                base_attack += 5
                print(f"\nLEVEL UP! You are now level {player_level}!")
                print(f"\nBase attack increased to {base_attack}")

        elif choice == "R":
            print(f"{char_name} rests for the night and restores all his HP.")
            player_health = 100
        else:
            print("Thanks for playing!")
            exit()

# Combat system
def Combat(player_health, player_xp, enemy_data):
    # Unpack enemy data
    e_name, e_h, e_atk = enemy_data[0], enemy_data[1], enemy_data[2]

    print(f"\nA wild {e_name} appears! (HP: {e_h}, ATK: {e_atk})")

    while e_h > 0 and player_health > 0:
        choice = input("\nAttack? Y or N ").upper()

        if choice == "Y":
            # -- Player's turn --
            roll = random.randint(1, 100) # Picks a number between 1 and 100
            damage = base_attack + char_atk_bonus

            if roll <= crit_chance:
                damage = damage * 2
                print("CRITICAL HIT!! Double damage!!")

            e_h -= damage
            print(f"You hit {e_name} for {damage} damage! Enemy HP: {max(0, e_h)}")

            # Check if enemy died
            if e_h <= 0: break

            # -- Enemy's turn --
            player_health -= e_atk
            print(f"\nThe {e_name} attacks! {char_name}'s health decreases by {e_atk}; {char_name}'s health is now {player_health}")

            if player_health <= 0:
                print("You have been defeated.")
                exit()

        elif choice == "N":
            print(f"\nYou try to dodge but are blocked! The {e_name} attacks! Your health decreases by 2")
            player_health -= 2
            print(f"{char_name}'s HP: {player_health}")
        else: 
            print(f"\nInvalid input! The {e_name} attacks and you take {e_atk}HP damage")
            player_health -= 5
    print(f"{e_name} has been defeated! ")
    player_xp += 20
    return player_health, player_xp

# Start the game
Action_Menu(player_health, player_xp)