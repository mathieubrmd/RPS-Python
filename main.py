class Paper:
    pass
class Rock:
    pass
class Scissors:
    pass

class Action:
    @property
    def name(self):
        return self.__class__

    def failed_attack(action1, action2):
        print('You should use rock, paper or scissors. Try again.')

    def attack_rock_paper(paper, rock):
        print('Rock x Paper')

    def attack_paper_rock(paper, rock):
        print('Paper x Rock')

    def attack_paper_scissors(paper, scissors):
        print('Paper x Scissors')

    def attack_rock_scissors(rock, scissors):
        print('Rock x Scissors')

    _map = {
        (Rock, Paper): attack_rock_paper,
        (Paper, Rock): attack_rock_paper,
        (Paper, Scissors): attack_paper_scissors,
        (Scissors, Paper): attack_paper_scissors,
        (Rock, Scissors): attack_rock_scissors,
        (Scissors, Rock): attack_rock_scissors,
    }


class Paper(Action):
    def attack(self, action):

        if (self == action):
            print("Draw")

        to = Action._map.get((type(self), type(action)), Action.failed_attack)
        to(self, action)
    pass

class Rock(Action):
    def attack(self, action):

        if (self == action):
            print("Draw")

        to = Action._map.get((type(self), type(action)), Action.failed_attack)
        to(self, action)
    pass

class Scissors(Action):
    def attack(self, action):

        if (self == action):
            print("Draw")

        to = Action._map.get((type(self), type(action)), Action.failed_attack)
        to(self, action)
    pass

scissors = Scissors()
rock = Rock()
paper = Paper()

paper.attack(paper)
