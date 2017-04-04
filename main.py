class Paper:
    name = "paper"

    def attack(self, action):
        action.got_attacked_by_paper(self)

    def got_attacked_by_paper(self, action):
        print("You chose " + action.name + ", your opponent chose paper. It's a tie!\n")
    def got_attacked_by_rock(self, action):
        print("You chose " + action.name + ", your opponent chose paper. You win!\n")
    def got_attacked_by_scissors(self, action):
        print("You chose " + action.name + ", your opponent chose paper. Your opponent wins!\n")


class Rock:
    name = "rock"

    def attack(self, action):
        action.got_attacked_by_rock(self)

    def got_attacked_by_paper(self, action):
        print("You chose " + action.name + ", your opponent chose rock. You win!\n")
    def got_attacked_by_rock(self, action):
        print("You chose " + action.name + ", your opponent chose rock. It's a tie!\n")
    def got_attacked_by_scissors(self, action):
        print("You chose " + action.name + ", your opponent chose rock. Your opponent wins!\n")

class Scissors:
    name = "scissors"

    def attack(self, action):
        action.got_attacked_by_sissors(self)

    def got_attacked_by_paper(self, action):
        print("You chose " + action.name + ", your opponent chose scissors. Your opponent wins!\n")
    def got_attacked_by_rock(self, action):
        print("You chose " + action.name + ", your opponent chose scissors. You win!\n")
    def got_attacked_by_scissors(self, action):
        print("You chose " + action.name + ", your opponent chose scissors. It's a tie!\n")


'''var = input("Rounds :")

try:
    print(int(var) + 3)
except ValueError:
    print('nto')'''
action = Rock()

action.attack(Rock())