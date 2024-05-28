import random
number = random.randint(1,10)
while True:
    guessed_num = int(input("Enter a number to guess :"))
    if guessed_num == number:
        print("Well gussed")
    else:
        print("Try again")
