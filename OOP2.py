import random
import time
import os

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

suits = {}
vis = {}
match_round = 0

def fill_values():
    global suits
    ch = "A"
    for _ in range(26):
        suits[ch] = random.randint(0, 10)
        ch = chr(ord(ch) + 1)

def show_octagons(a,b,c,d):
    os.system("cls" if os.name == "nt" else "clear")
    print("=============================")

    for pair in suits.items():
        color_code = random.randint(1, 7)
        print(f"\033[{color_code}m  [{pair[0]}]  \033[0m", end="")

    print("\n=============================")
    print(f"Score of {a} : {b} ",end="")
    print(f"Score of {c} : {d}")

def show_value(ch, name):
    print(f"{name} has revealed [{ch}] with a value of {suits[ch]}")

def check_if_already_chosen(ch):
    return vis.get(ch, False)

def set_color(color_code):
    print(f"\033[{color_code}m", end="")

def reset_color():
    print("\033[0m", end="")

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    set_color(36)

    print("  W   W  EEEEE  L      CCCC   OOO   M   M  EEEEE\n"
          "  W   W  E      L     C      O   O  MM MM  E    \n"
          "  W W W  EEEE   L     C      O   O  M M M  EEEE \n"
          "  W W W  E      L     C      O   O  M   M  E    \n"
          "   W W   EEEEE  LLLLL  CCCC   OOO   M   M  EEEEE\n")
    reset_color()

    print("\n\t1)  Player Vs. AI"
          "\n\t2)  Multiplayer"
          "\n\t0)  EXIT"
          "\n\nSelect a game mode: ")

def check_winner(name, score, other_name, other_score):
    if score > other_score:
        print(f"\nCONGRATULATIONS {name} you have won!")
    elif score < other_score:
        print(f"\nCONGRATULATIONS {other_name} you have won!")
    else:
        print("It's a draw!")

def player_vs_ai():
    global match_round
    fill_values()

    player_name = input("\nWhat's your name? ")
    ai_name = "AI"
    player_score = 0
    ai_score = 0
    vis.clear()

    while match_round < 26:
        show_octagons(player_name,player_score,ai_name,ai_score)
        print(f"\n\n{player_name} it's your turn...")

        ch = input("Please enter the letter of your choice: ").upper()
        while ch not in alphabet:
            ch = input("Enter a valid move: ").upper()

        yo = check_if_already_chosen(ch)
        if yo:
            print("This character was already chosen.")
            print(f"Your score is decreased by {suits[ch]}")
            player_score -= suits[ch]
            player_score = max(0, player_score)
        else:
            vis[ch] = True
            player_score += suits[ch]

        show_value(ch, player_name)
        print(f"{player_name} your score is: {player_score}")
        match_round += 1
        time.sleep(1.5)

        show_octagons(player_name,player_score,ai_name,ai_score)
        print("\n\nIt's the AI's turn...")

        ch = random.choice(alphabet)
        yo = check_if_already_chosen(ch)
        while yo:
            ch = random.choice(alphabet)
            yo = check_if_already_chosen(ch)

        vis[ch] = True
        ai_score += suits[ch]
        show_value(ch, ai_name)
        print(f"AI your score is: {ai_score}")
        match_round += 1
        time.sleep(1.5)

    show_octagons(player_name,player_score,ai_name,ai_score)
    print("\nFinal Score: "
          f"\n{player_name}: {player_score}"
          f"\nAI: {ai_score}")

    check_winner(player_name, player_score, ai_name, ai_score)

def multiplayer():
    global match_round
    fill_values()

    player1_name = input("\nName of Player 1: ")
    player2_name = input("\nName of Player 2: ")
    player1_score = 0
    player2_score = 0
    vis.clear()

    while match_round < 26:
        os.system("cls" if os.name == "nt" else "clear")
        show_octagons(player1_name,player1_score,player2_name,player2_score)
        print(f"\n\n{player1_name} it's your turn...")

        ch = input("Please enter the letter of your choice: ").upper()
        while ch not in alphabet:
            ch = input("Enter a valid move: ").upper()

        if ch in vis:
            print("This character was already chosen.")
            player1_score -= suits[ch]
            player1_score = max(0, player1_score)
        else:
            vis[ch] = True
            player1_score += suits[ch]

        show_value(ch, player1_name)
        print(f"{player1_name} your score is: {player1_score}")
        match_round += 1
        time.sleep(1.5)

        show_octagons(player1_name,player1_score,player2_name,player2_score)
        print(f"\n\n{player2_name} it's your turn...")

        ch = input("Please enter the letter of your choice: ").upper()
        while ch not in alphabet:
            ch = input("Enter a valid move: ").upper()

        if ch in vis:
            print("This character was already chosen.")
            player2_score -= suits[ch]
            player2_score = max(0, player2_score)
        else:
            vis[ch] = True
            player2_score += suits[ch]

        show_value(ch, player2_name)
        print(f"{player2_name} your score is: {player2_score}")
        match_round += 1
        time.sleep(1.5)

    show_octagons(player1_name,player1_score,player2_name,player2_score)
    print("\nFinal Score: "
          f"\n{player1_name}: {player1_score}"
          f"\n{player2_name}: {player2_score}")

    check_winner(player1_name, player1_score, player2_name, player2_score)

if __name__ == "__main__":
    opt = ""
    while opt != "0":
        menu()
        opt = input()
        if opt == "1":
            print("\n\n[  P L A Y E R    V S.   C P U  ]")
            player_vs_ai()
        elif opt == "2":
            print("\n\n[  M U L T I P L A Y E R  ]")
            multiplayer()
