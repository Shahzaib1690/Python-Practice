import random
from time import sleep
print("\nWelcome to Dice Rolling game\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
sleep(1)
print("The game is about to start!\n Let's play Hangman!")
sleep(1)

def play_loop():
    global ch
    ch = input("Wanna Play Again , Y = yes  and N = No")
    while ch not in ["Y","y","N","n"]:
        print("Press Y to play again and N to quit ")
    if ch=="Y" or ch == "y":
        play()

    elif ch == "N" or ch == "n":
        print("Thanks for playing")
        exit()
def play():
    global num
    print("DICE ROLLING..............")
    sleep(3)
    num = random.randint(1,6)
    print(f"You got {num}")
    play_loop()

play()