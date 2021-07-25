#Guess_Game

import random

x = random.randint(1, 50)
turns = 1
print("The computer just chose a random number from 1 to 50\nYou get 5 tries to guess the number!")
while turns < 6:
    y = int(input("Your guess: "))
    if y > x:
        print("Your guess is bigger than the number!\n")
    if y < x:
        print("Your guess is smaller than the number!\n")
    if y == x:
        print("You guessed right!")
        break
    if y != x and turns == 5:
        print("No more tries, game over!")
    turns += 1