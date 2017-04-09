'''
action.py - Define the different types of actions - Paper/Rock/Scissors
Mathieu Bourmaud - 19941124-P335
Martin Porrès - 19940926-P170
'''

import random

class Action:
    name = ""

class Paper(Action):
    name = "paper"

    def attack(self, action):
        return action.got_attacked_by_paper(self, self)

    def got_attacked_by_paper(self, action):
        print("You chose " + action.name + ", your opponent choose paper. It's a tie!\n")
        return None
    def got_attacked_by_rock(self, action):
        print("You chose " + action.name + ", your opponent choose paper. Your opponent wins!\n")
        return False
    def got_attacked_by_scissors(self, action):
        print("You chose " + action.name + ", your opponent choose paper. You win!\n")
        return True
    pass

class Rock(Action):
    name = "rock"

    def attack(self, action):
        return action.got_attacked_by_rock(self, self)

    def got_attacked_by_paper(self, action):
        print("You chose " + action.name + ", your opponent chose rock. You win!\n")
        return True
    def got_attacked_by_rock(self, action):
        print("You chose " + action.name + ", your opponent chose rock. It's a tie!\n")
        return None
    def got_attacked_by_scissors(self, action):
        print("You chose " + action.name + ", your opponent chose rock. Your opponent wins!\n")
        return False
    pass

class Scissors(Action):
    name = "scissors"

    def attack(self, action):
        return action.got_attacked_by_scissors(self, self)

    def got_attacked_by_paper(self, action):
        print("You chose " + action.name + ", your opponent chose scissors. Your opponent wins!\n")
        return False
    def got_attacked_by_rock(self, action):
        print("You chose " + action.name + ", your opponent chose scissors. You win!\n")
        return True
    def got_attacked_by_scissors(self, action):
        print("You chose " + action.name + ", your opponent chose scissors. It's a tie!\n")
        return None
    pass

class ActionFactory:
    def createAction(self, name):
        if (name == "rock"):
            return Rock
        if (name == "paper"):
            return Paper
        if (name == "scissors"):
            return Scissors

    def getRandomAction(self):
        val = random.randint(0, 2)

        if val == 0:
            return Rock
        if val == 1:
            return Paper
        if val == 2:
            return Scissors
