class Paper:
    def attack(self, action):
        action.got_attack_by_paper(self)

    def got_attacked_by_paper(self, action):
        print("You chose paper, your opponent chose paper. It’s a tie!\n")
    def got_attacked_by_rock(self, action):
        print("You chose paper, your opponent chose rock. You win!\n")
    def got_attacked_by_scissors(self, action):
        print("You chose paper, your opponent chose scissors. Your opponent wins!\n")


class Rock:
    def attack(self, action):
        if (self == action):
            print("Draw")
        action.attack(self)

class Scissors:
    def attack(self, action):
        if (self == action):
            print("Draw")
        action.attack(self)


'''var = input("Rounds :")

try:
    print(int(var) + 3)
except ValueError:
    print('nto')'''
