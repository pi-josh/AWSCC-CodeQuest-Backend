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
print(f"Player 1: {player1}")
print(f"Player 2: {player2}")

# Evaluating who wins
if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
    print("Player 1 Wins!")
elif player1 == player2:
    print("Draw!")
else:
    print("Player 2 Wins!")
