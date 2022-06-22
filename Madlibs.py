from time import sleep
print("\nWelcome to Madlib game\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
sleep(1)
print("The game is about to start!\n Let's play Madlib")
sleep(1)
def main():
    print("Player Unknown Battlerground(PUBG) is such a ____ game that it will make u feel ____.I ____ to play it everyday but it take\n"
        "lot of ____ and u need a lot of ____ to become a __.There is a __ version of PUBG also but i love __ version ")
    global madlibs
    global a,b,c,d,e,f,g,h
    a = input("Fill the Blank NO.1")
    b = input("Fill the Blank NO.2")
    c = input("Fill the Blank NO.3")
    d = input("Fill the Blank NO.4")
    e = input("Fill the Blank NO.5")
    f = input("Fill the Blank NO.6")
    g = input("Fill the Blank NO.7")
    h = input("Fill the Blank NO.8")
    madlibs = f"Player Unknown Battlerground(PUBG) is such a {a} game that it will make u feel {b}.I {c} to play it everyday but it take\n" \
              f"lot of {d} and u need a lot of {e} to become a {f}.There is a {g} version of PUBG also but i love {h} version"
    print(madlibs)
    play_loop()
def play_loop():
    global ch
    ch = input("Wanna Play Again , Y = yes  and N = No")
    while ch not in ["Y","y","N","n"]:
        print("Press Y to play again and N to quit ")
    if ch=="Y" or ch == "y":
        main()

    elif ch == "N" or ch == "n":
        print("Thanks for playing")
        exit()
main()