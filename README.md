# Simple RPG

A terminal-based Python combat game built around exploring, fighting randomly selected enemies, resting and gaining experience.

## Run

Use Python 3 with f-string support and an interactive terminal. No third-party packages are required.

~~~bash
python3 app.py
~~~

On Windows, **py app.py** may be the appropriate command for your Python installation.

## Play

Enter a character name and respond to the class prompt. At the main menu:

| Input | Action |
| --- | --- |
| E | Explore and encounter a random enemy |
| R | Rest and restore health to 100 |
| Q | Quit |

The menu uppercases input, so lowercase letters work too. At present, any main-menu choice other than E or R exits.

In combat, enter **Y** to attack or **N** to attempt a dodge. The dodge currently inflicts two points of damage rather than offering a successful escape.

## Combat and progression

- Start with 100 health and level 1.
- Basic damage is base attack (10 initially) plus an attack bonus of 5.
- A 1–100 random roll gives a 20% critical-hit chance, doubling damage.
- Enemies include Slime, Goblin, Orc and Dragon Spawn, each with different health and attack values.
- A defeated enemy awards 20 XP.
- Reaching the current level × 50 XP threshold increases the level and base attack by five.

Resting fully restores health. There is no inventory, gold, equipment purchasing or save/load system.

## Source layout

All code is in [app.py](app.py):

- Top-level data defines the player defaults, class/weapon list and enemies.
- **Action_Menu()** runs the exploration/rest loop and level-up check.
- **Combat()** handles the encounter and returns updated health and experience.

## Current implementation notes

The class response is overwritten by a list of class definitions, so choosing Warrior, Mage or Thief does not yet change combat behavior.

Some invalid-input and defeat paths are incomplete: an invalid combat choice prints enemy-specific damage but deducts a fixed five health, and health reaching zero outside the normal attack branch is not handled consistently. This is a learning prototype with those behaviors visible in the source.

## Manual checks

Start a character, explore, complete an encounter, rest and quit. Check a critical hit and level-up through repeated play or temporary local adjustments to test values. There is no automated test suite in the repository.
