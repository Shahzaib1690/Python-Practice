import random

def play():
    player = input("Choose 'r' for rock, 'p' for paper and 's' for scissor :" ).lower()[0]
    while player not in ['s','p','r']:
        print("Invalid input! kindly choose from given options")
        player = input("Choose 'r' for rock, 'p' for paper and 's' for scissor :").lower()[0]
    computer = random.choice(['r', 'p' , 's'])

    if player == computer:
        print("Draw!!!!!!!")
    elif winner(player,computer):
        print("You won")
    else:
        print('You lost')
    play_loop()
def winner(a,b):
    if (a == 'r' and b == 's') or (a == 'p' or b == 'r') or (a == 's' and b == 'p'):
        return True
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y" or play_game == "Y":
        play()
    elif play_game == "n" or play_game == "N":
        print("Thanks For Playing! We expect you back again!")
        exit()
play()