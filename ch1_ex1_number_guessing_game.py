# For this exercise

# Write a function (guessing_game) that takes no arguments.
# When run, the function chooses a random integer between 0 and 100 (inclusive).
# Then ask the user to guess what number has been chosen.
# Each time the user enters a guess, the program indicates one of the following:
# Too high
# Too low
# Just right
# If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
# The program only exits after the user guesses correctly.
# We’ll use the randint (http://mng.bz/mBEn) function in the random module to generate a random number.

import random


def guessing_game():
    number = random.randint(0, 100)
    remaining_guesses = 2

    while True:
        guess = int(input('Guess a number between 0 and 100: '))

        if remaining_guesses == 0:
            print('Sorry- you are out of guesses!')
            break

        if guess == number:
            print(f'{guess} is exactly right!')
            break

        if guess > number:
            remaining_guesses -= 1
            print(f'{guess} is too high')
        else:
            remaining_guesses -= 1
            print(f'{guess} is too low')


guessing_game()
