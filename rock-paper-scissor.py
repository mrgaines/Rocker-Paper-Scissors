# Rock, Paper, Scissor Game

from random import randint

# Game options for playing
x = ["Rock", "Paper", "Scissor"]
computer = x[randint(0, 2)]
# Set player to False for game
player = False
while not player:
    player = input("Rock, Paper, Scissor?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Rock":
            print("You Lose ...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That is not a valid play. Check your entry!")
    player = False
    computer = x[randint(0, 2)]
