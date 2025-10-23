# Dice Rolling Program
#Import random
import random

#Define the dice_art dictionary for dice faces 1-6
dice_art = {
    1: (
        "┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘",
    ),
    2: (
        "┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘",
    ),
    3: (
        "┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘",
    ),
    4: (
        "┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘",
    ),
    5: (
        "┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘",
    ),
    6: (
        "┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘",
    ),
}

#Create an empty dice list and total variable
dice = []
total = 0

#Ask the user for the number of dice
num_of_dice = int(input("How many dice?: "))

#Roll the dice and append to the list
for _ in range(num_of_dice):
    dice.append(random.randint(1, 6))

#Print the dice art side by side
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

#Sum up the dice and print the total
for die in dice:
    total += die
print(f"total: {total}")