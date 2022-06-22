from time import sleep
import random
print("Welcome to Rock Paper Scissor Game")
sleep(1)
a = input("Enter name of 1st Player :")
sleep(1)
print(f"Hello {a}, Best Of Luck")
b = "Computer"


def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y" or play_game == "Y":
        main()
        hangman()
    elif play_game == "n" or play_game == "N":
        print("Thanks For Playing! We expect you back again!")
        exit()
def main():
    dis = ["R","P","S","r","p","s"]
    player1 = input(f"waiting for '{a}' to choose from Rock, Paper or Scissor :")[0]
    while player1 not in dis:
        print("Invalid Input")
        player1 = input(f"waiting for '{a}' to choose from r, p or s")
        break
    player2 = random.choice(dis)
    if (player1 == "r" or player1 == "R") and (player2 == "r" or player2 == "R"):
        print("its draw")
        play_loop()
    elif (player1 == "p" or player1 == "P") and (player2 == "p" or player2 == "P"):
        print("its draw")
        play_loop()
    elif (player1 == "s" or player1 == "S") and (player2 == "s" or player2 == "S"):
        print("its draw")
        play_loop()
    else:
        if (player1 == "r" or player1 == "R") and (player2 == "P" or player2 == "p"):
            print(f"Congratulations '{b}' for winning the Game")
            print(f"Better Luck Next time '{a}'")
            play_loop()
        elif (player1 == "r" or player1 == "R") and (player2 == "S" or player2 == "s"):
            print(f"Congratulations '{a}' for winning the Game")
            print(f"Better Luck Next time '{b}'")
            play_loop()
        elif (player1 == "p" or player1 == "P") and (player2 == "r" or player2 == "R"):
            print(f"Congratulations '{a}' for winning the Game")
            print(f"Better Luck Next time '{b}'")
            play_loop()
        elif (player1 == "p" or player1 == "P") and (player2 == "s" or player2 =="S"):
            print(f"Congratulations '{b}'for winning the Game")
            print(f"Better Luck Next time '{a}'")
            play_loop()
        elif (player1 == "s" or player1 == "S") and (player2 == "R" or player2 == "r"):
            print(f"Congratulations '{b}' for winning the Game")
            print(f"Better Luck Next time '{a}'")
            play_loop()
        elif (player1 == "s" or player1 == "S") and (player2 == "p" or player2 == "P"):
            print(f"Congratulations '{a}' for winning the Game")
            print(f"Better Luck Next time '{b}'")
            play_loop()
main()