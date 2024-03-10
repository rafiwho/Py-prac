from random import randint
import time

class Octagon(object):
    suits = ["", "", "", "", "", "", "", ""]
    values = [0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        self.endgame_points = 0

    def fill_suits(self):
        su = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(8):
            self.suits[i] = su[i]

    def fill_values(self):
        for i in range(8):
            self.values[i] = randint(1, 10)

    def show_octagons(self):
        for i in range(8):
            print(f"[{self.suits[i]}]", end="")

    def show_value(self, i, name):
        print(f"{name} has revealed octagon [{self.suits[i]}] with a value of {self.values[i]}")
        self.suits[i] = str(self.values[i])

    def update_endgame_points(self):
        self.endgame_points = self.endgame_points + 1

    def check_if_already_chosen(self, octagon):
        chosen = True
        for i in range(8):
            if octagon == self.suits[i] and octagon != str(self.values[i]):
                chosen = False
                break
            elif octagon == self.suits[i] and octagon == str(self.values[i]):
                chosen = True
                break
            else:
                chosen = True

        return chosen

class User(object):
    def __init__(self):
        self.name = "CPU"
        self.score = 0

    def update_score(self, i):
        self.score = self.score + Octagon.values[i]

    def show_score(self):
        print(f"{self.name} your score is: {self.score} ")

    def choose_octagon(self):
        print("Please enter the letter of your octagon: ")
        octagon = input().upper()
        chosen = Octagon.check_if_already_chosen(Octagon(), octagon)
        while chosen is True:
            print("This octagon was already chosen. Please select another one: ")
            octagon = input().upper()
            chosen = Octagon.check_if_already_chosen(Octagon(), octagon)
        for i in range(8):
            if octagon == Octagon().suits[i]:
                self.update_score(i)
                Octagon.show_value(Octagon(), i, self.name)
                self.show_score()

    def check_winner(self, other_score):
        if self.score > other_score:
            print(f"\nCONGRATULATIONS {self.name} you have won!")
        elif self.score < other_score:
            print(f"\nSorry, {self.name} you have lost. Good luck next time!")
        else:
            print(f"\nThere's a tie. Both of you won!")

class Cpu(User):
    def __init__(self):
        super(User).__init__()
        self.name = "CPU"
        self.score = 0

    def show_score(self):
        print(f"CPU's score is: {self.score}")

    def choose_octagon(self):
        octagon = Octagon().suits[randint(0, 7)]
        chosen = Octagon.check_if_already_chosen(Octagon(), octagon)
        while chosen is True:
            octagon = Octagon.suits[randint(0, 7)]
            chosen = Octagon.check_if_already_chosen(Octagon(), octagon)
        for i in range(8):
            if octagon == Octagon().suits[i]:
                self.update_score(i)
                Octagon.show_value(Octagon(), i, self.name)
                self.show_score()

class Player(User):
    def __init__(self):
        super(User).__init__()
        self.set_name()
        self.score = 0

    def set_name(self):
        print("\nWhat's your name? ")
        self.name = input()

def menu():
    print("\n---------WELCOME TO THE [OCTAGON] GAME----------"
          "\n\t1) Player Vs. CPU"
          "\n\t2) Multiplayer"
          "\n\t0) EXIT")
    print("\n\nSelect a game mode: ")
    option = input()
    return option

if __name__ == "__main__":
    opt = ""
    while opt != "0":
        octagons = Octagon()
        opt = menu()
        if opt == "1":
            print("\n\n[  P L A Y E R    V S.   C P U  ]")
            octagons.fill_suits()
            octagons.fill_values()
            player = Player()
            cpu = Cpu()
            while octagons.endgame_points < 8:
                time.sleep(2)
                octagons.show_octagons()
                print(f"\n\n{player.name} it's your turn...")
                player.choose_octagon()
                octagons.update_endgame_points()

                time.sleep(4)
                octagons.show_octagons()
                print("\n\nIt's the CPU'S turn...")
                cpu.choose_octagon()
                octagons.update_endgame_points()

            print("\nFinal Score: "
                  f"\n{player.name}: {player.score}"
                  f"\n{cpu.name}: {cpu.score}")
            player.check_winner(cpu.score)
            input()
        elif opt == "2":
            print("\n\n[  M U L T I P L A Y E R  ]")
            octagons.fill_suits()
            octagons.fill_values()
            player1 = Player()
            player2 = Player()
            while octagons.endgame_points < 8:
                time.sleep(2)
                octagons.show_octagons()
                print(f"\n\n{player1.name} it's your turn...")
                player1.choose_octagon()
                octagons.update_endgame_points()

                time.sleep(2)
                octagons.show_octagons()
                print(f"\n\n{player2.name} it's your turn...")
                player2.choose_octagon()
                octagons.update_endgame_points()

            print("\nFinal Score: "
                  f"\n{player1.name}: {player1.score}"
                  f"\n{player2.name}: {player2.score}")
            player1.check_winner(player2.score)
            player2.check_winner(player1.score)
            input()
