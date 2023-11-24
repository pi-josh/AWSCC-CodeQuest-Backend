# Simple rock-paper-scissor game

import random

# Starting the game
print("Welcome to the rock-paper-scissor game!")
print("Instruction: Choose one of the choices (Rock/Paper/Scissors) you feel would defeat your opponent. Good luck!")

# List of choices
choice = ["rock", "paper", "scissors"]

# Prompting the user for their choices
player1 = input("Player 1: ").lower()
player2 = random.choice(choice)
print(f"Player 2: {player2}")

# Evaluating who wins
if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
    print("Player 1 Wins!")
elif player2 == "rock" and player1 == "scissors" or (player2 == "scissors" and player1 == "paper") or (player2 == "paper" and player1 == "rock"):
    print("Player 2 Wins!")
else:
    print("Draw!")
