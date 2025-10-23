#random
import random

low = 1
high = 100
options = ["rock", "paper", "scissors"]
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#number = random.randint(low, high)
#number = random.random()
#options = random.choice(options)
random.shuffle(cards)
print(cards)


