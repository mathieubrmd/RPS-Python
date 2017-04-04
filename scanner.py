'''
scanner.py - Read the user input in the console
Mathieu Bourmaud - 19941124-P335
Martin Porrès -
'''

import sys

class Scanner:
    def readRoundNumber(self):
        rounds = input("How many rounds? ")

        try:
            int(rounds)

            if int(rounds) < 0 or int(rounds) > sys.maxsize:
                print("The number of round should be a valid number. "
                      "It cannot be more than the integer type can support.")
                return False

            return rounds
        except ValueError:
            print("It musts be a number")
            return False


    def readActionName(self):
        action = input("")

        if action != "scissors" and action != "rock" and action != "paper":
            print("\nThe action that you choose should be rock, scissors or paper.")
            return False

        return action

