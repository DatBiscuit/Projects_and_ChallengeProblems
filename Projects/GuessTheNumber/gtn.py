import random

guesses = 3
randomNum = random.randint(1,10)

while guesses > 0:
    player_guess = int(input("Guess a number between 1-10 "))
    if player_guess == randomNum:
        print("You are correct!")
        break
    else:
        print("Sorry that is incorrect")
        guesses -= 1

if guesses == 0:
    print("Game over! the correct answer was:", randomNum)
