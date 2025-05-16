"""
These Number Guessing Game Contains an random module to select a random number between 1 and 100.
The player has to guess the number within a limited number of attempts.
The player can exit the game at any time by typing 'exit'.
The game provides feedback on whether the guess is too high or too low.
The game ends when the player guesses the number correctly or runs out of attempts.
The game is simple and easy to play, making it a fun way to practice Python programming.
The game is designed to be played in a console or terminal.
"""
import random
Target_Number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 100.")
print("Can you guess what it is?")
attempts = 5
while True:
    guess = input("Enter your guess (or 'exit' to quit): ")
    if guess.lower() == 'exit':
        print("Thanks for playing!")
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts -= 1
    if attempts == 0:
        print("Game over! You've used all your attempts.")
        print("Sorry, you've run out of attempts. The number was:")
        print( {Target_Number})
        break
    if guess < Target_Number:
        print("Too low! Try again.")
    elif guess > Target_Number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {Target_Number} in {attempts} attempts.")
        break
# This is a simple number guessing game where the player has to guess a randomly selected number.
# The player has a limited number of attempts to guess the number correctly.

