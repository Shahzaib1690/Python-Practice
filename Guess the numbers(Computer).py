import random

def play(x):
    global guess
    low = 0
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # it could be high also
        feedback = input(f"Please tell if the Number {guess} is too Low (L), too high (H) or its correct (C)").lower()[0]
        if feedback == "l":
            print("Its too low")
            low = guess +1
        elif feedback == "h":
            print("Its too high")
            high = high - 1
    print(f"Congratulations, You guess then number {guess} correctly")
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