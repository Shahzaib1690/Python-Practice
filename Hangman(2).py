import random
from time import sleep

print("Welcome to Hangman Game")
sleep(1)
name = input("Enter Your Name :")
sleep(1)
print(f"Hello {name}! Best of Luck")

def main():
    global word
    global display
    global length
    global WTH    # Word to Guess
    global count
    global display
    global AG       # Already Guessed
    WTH = ["january","feburary","march","april", "may","june","july","august","september","october","november","december"]
    word = random.choice(WTH)
    count = 5
    length = len(word)
    display = "_" * length
    AG = []
def play_loop():
    global ch
    ch = input("Wanna Play Again , Y = yes  and N = No")
    while ch not in ["Y","y","N","n"]:
        print("Press Y to play again and N to quit ")
    if ch=="Y" or ch == "y":
        main()
        hangman()
    elif ch == "N" or ch == "n":
        print("Thanks for playing")
        exit()

def hangman():
    global word
    global display
    global count
    global AG
    global ch
    guess = input("This is the Hangman word  " + display + "\nEnter Your Guess :")
    guess = guess.strip()
    if len(guess) == 0 or len(guess) >=2:
        print("Invalid input,Try a letter")
        hangman()
    elif guess in word:
        AG.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        display = display[:index]+ guess + display[index+1:]
        print(display)
    elif guess in AG:
        print("try another letter")
    else:
        while count >=-1:
            if count == 0:
                print('Wrong Guessed, You are hanged')
                play_loop()
            print(f"Invalid Guess, Guesses remaining  {count}")
    if word == "_" * length:
        print("Congrats! you have guessed the word corrctly")
        play_loop()
    elif count!=0:
        hangman()
main()
hangman()

