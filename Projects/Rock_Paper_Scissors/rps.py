import random

# 0 is rock
# 1 is paper 
# 2 is scissors
computers_choice = random.randint(0,2)
players_choice = int(input("Type 0 for rock, 1 for paper, or 2 for scissors "))
print("Computer played:", computers_choice)

if players_choice == computers_choice:
    print("Draw!")

elif players_choice == 0:
    if computers_choice == 1:
        print("Computer won!")
    else:
        print("You win!")

elif players_choice == 1:
    if computers_choice == 0:
        print("You win!")
    else:
        print("Computer won!")

elif players_choice == 2:
    if computers_choice == 0:
        print("Computer won!")
    else:
        print("You win!")
