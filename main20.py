#NUMBER GUESSING GAME
import random

lowest_num = 1
highest_num = 100
number = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {lowest_num} and {highest_num}.")

while is_running:
    guess_input = input(f"Enter a number between {lowest_num} and {highest_num}: ")

    if guess_input.isdigit():
        guess = int(guess_input)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"Please enter a number between {lowest_num} and {highest_num}.")
        elif guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"You guessed it! The number was {number}.")
            print(f"You took {guesses} guesses.")
            is_running = False
    else:
        print("Please enter a valid number.")
        continue

print("Thanks for playing!")