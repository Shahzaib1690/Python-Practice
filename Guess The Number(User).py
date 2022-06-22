import random

def play(x):
    ran = random.randint(0,x)
    guess =-1
    while guess != ran:
        guess = int(input("Enter Your Guess :"))
        if guess < ran:
            print("Sorry! its low")
        elif guess > ran:
            print("Sorry! its high")
    print(f"Congratulations, You guess then number {ran} correctly")
    play_loop()
def play_loop():
    global ch
    global a
    ch = input("Wanna Play Again , Y = yes  and N = No")
    while ch not in ["Y","y","N","n"]:
        print("Press Y to play again and N to quit ")
    if ch=="Y" or ch == "y":
        main()

    elif ch == "N" or ch == "n":
        print("Thanks for playing")
        exit()
def main():
    a = int(input("Enter the maximum number you want as random number :"))
    play(a)
main()