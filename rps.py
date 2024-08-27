import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def play_RPS():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerChoice = input(
        "\nLet's Play Rock, Paper and Scissors!\n\nEnter... \n1 for Rock\n2 for Paper\n3 for Scissors:\n"
    )

    if playerChoice not in (["1", "2", "3"]):
        print("Not a valid choice, game reboots...")
        return play_RPS()

    playerChoiceInt = int(playerChoice)
    computerChoice = random.choice("123")
    computerChoiceInt = int(computerChoice)

    print("\nYour choice was: " + playerChoice)
    print("Computer choice was " + computerChoice)

    if (
        (playerChoiceInt == 1 and computerChoiceInt == 3)
        or (playerChoiceInt == 2 and computerChoiceInt == 1)
        or (playerChoiceInt == 3 and computerChoiceInt == 2)
    ):
        print("Yey!, You've won! 🥳🎉")
    elif playerChoiceInt == computerChoiceInt:
        print("It is a tie! 😮")
    else:
        print("Python, Wins! 🐍")

    print("Play Again?")
    playAgain = True

    while True:
        playAgain = input("\nY for Yes\nQ for Quit\n")
        if playAgain.upper() not in ["Y", "Q"]:
            print(
                "Not a valid response. Please enter either you want to play again or not!"
            )
            continue
        else:
            break

    if playAgain.upper() == "Y":
        return play_RPS()
    else:
        print("thank you for playing")
        sys.exit("Bye!")


play_RPS()


# if playerChoiceInt < 1 or playerChoiceInt > 3:
#     sys.exit(
#         "You've entered an invalid value. Next time, it should only be 1, 2 or 3."
#     )

# print("")
# print("Your choice was: " + playerChoice)
# print("Computer choice was " + computerChoice)

# if (
#     (playerChoiceInt == 1 and computerChoiceInt == 3)
#     or (playerChoiceInt == 2 and computerChoiceInt == 1)
#     or (playerChoiceInt == 3 and computerChoiceInt == 2)
# ):
#     print("Yey!, You've won! 🥳🎉")
# elif playerChoiceInt == computerChoiceInt:
#     print("It is a tie! 😮")
# else:
#     print("Python, Wins! 🐍")
# play_again_input = (
#     input("\nPlay Again? \nY for Yes or \nQ to Quit: ").strip().upper()
# )
# if play_again_input == "Q":
#     playAgain = False
# elif play_again_input == "Y":
#     playAgain = True
