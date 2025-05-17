"""This game is maded where user can play the rock,paper and scissor with computer where user will select one of it and will enter and computer will also select one of it
Where by conditional statement it will be checked three time that who will win it will be best of three 
Workflow of Project:
1. input from user(rock, paper, scissor):
2. computer choice will be randomly selection from any three 
3. print result

Cases: 
A- rock
rock - rock = tie
rock - paper = paper win's
rock - scissor = rock win's

B- paper
paper - rock = paper win's
paper - paper = tie
paper - scissor = scissor win's

C- scissor 
scissor - rock = rock win's
scissor - paper = scissor win's
scissor - scissor = tie

"""
import random

def Rock(a, b):
    if a == b:
        return "tie"
    elif b == "paper":
        return "computer"
    else:
        return "user"

def Paper(a, b):
    if a == b:
        return "tie"
    elif b == "rock":
        return "user"
    else:
        return "computer"

def Scissor(a, b):
    if a == b:
        return "tie"
    elif b == "rock":
        return "computer"
    else:
        return "user"

Item = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0
rounds = 0

# Simulated do-while loop
while True:
    User_choice = input("Enter Your move (rock, paper, scissor): ").lower()
    if User_choice not in Item:
        print("Invalid input. Please choose rock, paper, or scissor.\n")
        continue  # Invalid input — ask again without increasing rounds

    Computer_choice = random.choice(Item)
    A = User_choice
    B = Computer_choice

    print(f"User Choice = {User_choice}, Computer Choice = {Computer_choice}")

    if User_choice == "rock":
        result = Rock(A, B)
    elif User_choice == "paper":
        result = Paper(A, B)
    else:
        result = Scissor(A, B)

    if result == "user":
        print("You win this round!")
        user_score += 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("This round is a tie.")

    rounds += 1
    print(f"Score: You = {user_score}, Computer = {computer_score}\n")

    if rounds == 3:
        break  # End the loop after 3 valid rounds

# Final result after loop ends
print("Final Result:")
if user_score > computer_score:
    print("🎉 You win the match! 🎉")
elif computer_score > user_score:
    print("😔 Computer wins the match! 😔")
else:
    print("🤝 It's a tie match! 🤝")
