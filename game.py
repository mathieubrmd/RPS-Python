'''
game.py - Basically, this file is the main file and this code runs the game
Mathieu Bourmaud - 19941124-P335
Martin Porrès - 19940926-P170
'''

from actions import Rock
from actions import Paper
from actions import Scissors
from actions import Action
from actions import ActionFactory
from scanner import Scanner

class Player:
    score = 0
    currentAction = Action()

class Game:
    player = Player()
    computer = Player()
    scanner = Scanner()
    rounds = 0
    actionFactory = ActionFactory()

    def run(self):
        self.rounds = self.scanner.readRoundNumber()

        if self.rounds == False:
            self.run()
            return False

        i = 0
        while i < int(self.rounds):
            print("Make your choice for round " + str(i) + ": ")

            action = self.scanner.readActionName()

            if action != False:
                self.player.currentAction = self.actionFactory.createAction(action)

                self.computer.currentAction = self.actionFactory.getRandomAction()

                result = self.player.currentAction.attack(self.player.currentAction, self.computer.currentAction)

                if result == True:
                    self.player.score += 1;
                if result == False:
                    self.computer.score += 1;
                i += 1

        self.showResults()

    def showResults(self):
        if self.player.score > self.computer.score:
            print("Result: You won " + str(self.player.score) + " time(s), your opponent won " + str(self.computer.score) + " time(s). You win!");
        if self.player.score < self.computer.score:
            print("Result: You won " + str(self.player.score) + " time(s), your opponent won " + str(self.computer.score) + " time(s). Your oponnent wins!");
        if self.player.score == self.computer.score:
            print("Result: You won " + str(self.player.score) + " time(s), your opponent won " + str(self.computer.score) + " time(s). It's a tie!");


game = Game().run()