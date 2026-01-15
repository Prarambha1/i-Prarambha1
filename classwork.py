"""
a program needs to calculate a user's final score in  a game and also keep track of the highest score achieved by any player. What two different kindas of information does it need to store?
"""

highest_score = 0
total_score = 0
is_running = True

while is_running == True:
    score = int(input("Enter your score: "))
    total_score += score
    if score > highest_score:
        highest_score = score

    run = input("enter do u wanna keep running this program? yes/no: ")
    if run == "yes":
        is_running = True
    elif run == "no":
        is_running = False
    else:
        print("Invalid! say 'yes' or 'no'..")

print(f"Your total score in this pragram is {total_score}")
print(f"your highest score in this program is {highest_score}")



