import random

char_name = input("What is your character's name? ")
player_xp = 0
health = 100
char_class = "Warrior"
weapon = "Sword"
weapon_dmg = 0
enemy = "Slime"
enemy_health = 50
enemy_attack = 2
base_attack = 10
char_atk_bonus = 5
crit_chance = 20

if weapon == "Sword":
    weapon_dmg = 10

def Combat(health, enemy_health, player_xp):
    print(f"\nAn {enemy} attacks!")
    while enemy_health > 0:
        choice = input("\nAttack? Y or N ").upper()

        if choice == "Y":
            # -- Player's turn --
            roll = random.randint(1, 100) # Picks a number between 1 and 100
            damage = base_attack + char_atk_bonus + weapon_dmg

            if roll <= crit_chance:
                damage = damage * 2
                print("CRITICAL HIT!! Double damage!!")

            enemy_health -= damage
            print(f"You dealt {damage} damage! Enemy HP: {max(0, enemy_health)}")

            # Check if enemy died
            if enemy_health <= 0:
                break

            # -- Enemy's turn --
            health -= enemy_attack

            print(f"\nThe {enemy} attacks! {char_name}'s health decreases by {enemy_attack}; {char_name}'s health is now {health}")

        elif choice == "N":
            print(f"\nYou try to dodge but are blocked! The {enemy} attacks! Your health decreases by 2")
            health -= 2
            print(f"{char_name}'s HP: {health}")
        else: 
            print(f"\nInvalid input! The {enemy} attacks and you take {enemy_attack}HP damage")
            health -= 5
    print(f"The {enemy} has been defeated!")
    player_xp += 10
    return health, player_xp

health, player_xp = Combat(health, enemy_health, player_xp)
print(f"\nYour XP has increased by 10. Your XP is now {player_xp}")

if player_xp >= 10:
    print(f"\nLEVEL UP! Your base attack has increased by 2.")
    base_attack += 2