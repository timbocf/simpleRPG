import random

# Character creation
char_name = input("What is your character's name? ")
player_xp = 0
player_health = 100
char_class = "Warrior"
weapon = "Sword"
weapon_dmg = 0
base_attack = 10
char_atk_bonus = 5
crit_chance = 20
if weapon == "Sword":
    weapon_dmg = 10

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
    while player_health > 0:
        choice = input(f"\n{char_name} is resting. Select an option: \nExplore (E) \nRest (Quit) (R) \n").upper()
        if choice == "E":
            random_enemy = random.choice(enemies)
            player_health, player_xp = Combat(player_health, player_xp, random_enemy)
            # Level up check after combat
            if player_xp >= 10:
                print(f"\nLEVEL UP! Your XP is {player_xp}. Base attack increased!")
        else:
            print("Thanks for playing!")
            break

# Combat system
def Combat(player_health, player_xp, enemy_data):
    # Unpack enemy data
    e_name = enemy_data[0]
    e_h = enemy_data[1]
    e_atk = enemy_data[2]

    print(f"\nA wild {e_name} appears! (HP: {e_h}, ATK: {e_atk})")

    while e_h > 0 and player_health > 0:
        choice = input("\nAttack? Y or N ").upper()

        if choice == "Y":
            # -- Player's turn --
            roll = random.randint(1, 100) # Picks a number between 1 and 100
            damage = base_attack + char_atk_bonus + weapon_dmg

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