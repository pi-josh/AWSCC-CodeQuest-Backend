# Simple rock-paper-scissor game

# Starting the game
print("Welcome to the rock-paper-scissor game!")
print("Instruction: Choose one of the choices (Rock/Paper/Scissors) to you feel would defeat your opponent. Good luck!")

# Prompting the user for their choices
player1 = input("Player 1: ")
player2 = input("Player 2: ")

# Evaluating who wins
if player1 == "Rock" and player2 == "Scissors":
    print("Player 1 Wins!")
elif player1 == "Scissors" and player2 == "Paper":
    print("Player 1 Wins!")
elif player1 == "Paper" and player2 == "Rock":
    print("Player 1 Wins!")
elif player2 == "Rock" and player1 == "Scissors":
    print("Player 2 Wins!")
elif player2 == "Scissors" and player1 == "Paper":
    print("Player 2 Wins!")
elif player2 == "Paper" and player1 == "Rock":
    print("Player 2 Wins!")
else:
    print("Draw!")
