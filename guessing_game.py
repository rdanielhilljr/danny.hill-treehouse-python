"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    print("\nWelcome to the number guessing game!!")
    n = random.randint(1, 10)
    guess = int(input("Enter an integer from 1 to 10: "))
    count = 1
    while n != "guess":
        if guess < n:
            print("Guess is low")
            guess = int(input("Enter an integer from 1 to 10: "))
            count = count + 1
        elif guess > n:
            print("Guess is high")
            guess = int(input("Enter an integer from 1 to 10: "))
            count = count + 1
        else:
            print("You guessed it. It took you {} tries.".format(count))

            play_again = input("Do you want to play again? (Y/N) ")
            play_again = play_again.upper()
            if play_again == 'Y':
                start_game()
            else:
                print("\nThanks for playing!!")
                break




    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


# Kick off the program by calling the start_game function.
start_game()