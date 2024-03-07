import random
import time


class OctagonGame:
    def __init__(self):
        self.alphabet = [chr(ord('A') + i) for i in range(26)]
        self.suits = {ch: random.randint(0, 10) for ch in self.alphabet}
        self.vis = {}
        self.match_round = 0

    def fill_values(self):
        pass  # No need to fill values in Python; it's done during initialization

    def show_octagons(self):
        print("=============================")
        for ch in self.alphabet:
            color_code = random.randint(31, 37)  # ANSI color codes for red to white
            print(f"\033[1;{color_code}m  [{ch}]  \033[0m", end="")
        print("\n=============================")

    def show_value(self, ch, name):
        print(f"{name} has revealed [{ch}] with a value of {self.suits[ch]}")

    def check_if_already_chosen(self, ch):
        return ch in self.vis

    def menu(self):
        print(
            "\033[1;36m  W   W  EEEEE  L      CCCC   OOO   M   M  EEEEE\n"
            "  W   W  E      L     C      O   O  MM MM  E    \n"
            "  W W W  EEEE   L     C      O   O  M M M  EEEE \n"
            "  W W W  E      L     C      O   O  M   M  E    \n"
            "   W W   EEEEE  LLLLL  CCCC   OOO   M   M  EEEEE\n\033[0m"
        )
        print("\n\t1)  Player Vs. AI"
              "\n\t2)  Multiplayer"
              "\n\t0)  EXIT"
              "\n\nSelect a game mode: ")

    def check_winner(self, name, score, other_name, other_score):
        if score > other_score:
            print(f"\nCONGRATULATIONS {name} you have won!")
        elif score < other_score:
            print(f"\nCONGRATULATIONS {other_name} you have won!")
        else:
            print("It's a draw!")

    def player_vs_ai(self):
        self.fill_values()

        player_name = input("\nWhat's your name? ")
        ai_name = "AI"
        player_score = 0
        ai_score = 0
        self.vis.clear()

        while self.match_round < 26:
            self.show_octagons()
            print(f"\n\n{player_name} it's your turn...")

            ch = input("Please enter the letter of your choice: ").upper()
            while ch not in self.alphabet:
                print("Enter a valid move: ")
                ch = input("Please enter the letter of your choice: ").upper()

            yo = self.check_if_already_chosen(ch)
            if yo:
                print("This character was already chosen.")
                print(f"Your score is decreased by {self.suits[ch]}")
                player_score -= self.suits[ch]
                player_score = max(0, player_score)
            else:
                self.vis[ch] = True
                player_score += self.suits[ch]

            self.show_value(ch, player_name)
            print(f"{player_name} your score is: {player_score}")
            self.match_round += 1
            time.sleep(1)  # Pause for 1 second

            self.show_octagons()
            print("\n\nIt's the AI's turn...")

            ch = random.choice(self.alphabet)
            while self.check_if_already_chosen(ch):
                ch = random.choice(self.alphabet)
            self.vis[ch] = True
            ai_score += self.suits[ch]
            self.show_value(ch, ai_name)
            print(f"AI your score is: {ai_score}")

            self.match_round += 1
            time.sleep(1)  # Pause for 1 second

        self.show_octagons()
        print("\nFinal Score: "
              f"\n{player_name}: {player_score}"
              f"\nAI: {ai_score}")

        self.check_winner(player_name, player_score, ai_name, ai_score)

    def multiplayer(self):
        self.fill_values()

        player1_name = input("\nName of Player 1: ")
        player2_name = input("\nName of Player 2: ")
        player1_score = 0
        player2_score = 0
        self.vis.clear()

        while self.match_round < 26:
            self.show_octagons()
            print(f"\n\n{player1_name} it's your turn...")

            ch = input("Please enter the letter of your choice: ").upper()
            while ch not in self.alphabet:
                print("Enter a valid move: ")
                ch = input("Please enter the letter of your choice: ").upper()

            if ch in self.vis:
                print("This character was already chosen.")
                player1_score -= self.suits[ch]
                player1_score = max(0, player1_score)
            else:
                self.vis[ch] = True
                player1_score += self.suits[ch]

            self.show_value(ch, player1_name)
            print(f"{player1_name} your score is: {player1_score}")

            self.match_round += 1
            time.sleep(1)  # Pause for 1 second

            self.show_octagons()
            print(f"\n\n{player2_name} it's your turn...")

            ch = input("Please enter the letter of your octagon: ").upper()
            while ch not in self.alphabet:
                print("Enter a valid move: ")
                ch = input("Please enter the letter of your octagon: ").upper()

            if ch in self.vis:
                print("This character was already chosen.")
                player2_score = max(0, player2_score)
            else:
                self.vis[ch] = True
                player2_score += self.suits[ch]

            self.show_value(ch, player2_name)
            print(f"{player2_name} your score is: {player2_score}")

            self.match_round += 1
            time.sleep(1)  # Pause for 1 second

        self.show_octagons()
        print("\nFinal Score: "
              f"\n{player1_name}: {player1_score}"
              f"\n{player2_name}: {player2_score}")

        self.check_winner(player1_name, player1_score, player2_name, player2_score)


if __name__ == "__main__":
    game = OctagonGame()

    while True:
        game.menu()
        option = input()
        if option == "1":
            print("\n\n[  P L A Y E R    V S.   C P U  ]")
            game.player_vs_ai()
        elif option == "2":
            print("\n\n[  M U L T I P L A Y E R  ]")
            game.multiplayer()
        elif option == "0":
            break
