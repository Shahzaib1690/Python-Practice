import random
import time
xstate = [0,0,0,0,0,0,0,0,0]
zstate = [0,0,0,0,0,0,0,0,0]
valx = -1
valz = -1
turn = 1
def sum(a,b,c):
    return a+b+c
def printboard():
    zero = 'X' if xstate[0] else 'O' if zstate[0]  else 0
    one = 'X' if xstate[1] else 'O' if zstate[1] else 1
    two = 'X' if xstate[2] else 'O' if zstate[2] else 2
    three = 'X' if xstate[3] else 'O' if zstate[3] else 3
    four = 'X' if xstate[4] else 'O' if zstate[4] else 4
    five = 'X' if xstate[5] else 'O' if zstate[5] else 5
    six = 'X' if xstate[6] else 'O' if zstate[6] else 6
    seven = 'X' if xstate[7] else 'O' if zstate[7] else 7
    eight = 'X' if xstate[8] else 'O' if zstate[8] else 8
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
def winner(xstate,zstate):
    wins = [[0,1,2],[3,4,5],[6,7,8,],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if sum(xstate[win[0]],xstate[win[1]],xstate[win[2]]) == 3:
            print("X won The Game")
            return 1
        elif sum(zstate[win[0]],zstate[win[1]],zstate[win[2]]) == 3:
            print("O won")
            return 0
    return -1
used_ch = []
def play():
    left = 9
    turn = 1
    print("Welcome To Tic Toe Game")
    while(True):
        global valx, valz
        printboard()
        if turn == 1:
            print("X Turn")
            valx = int(input("Enter A value from 0-8 :"))
            print("X Chose ", valx)
            while valx in used_ch:
                print(valx, "Number already taken")
                valx = int(input("Enter A value from 0-8 :"))
            used_ch.append(valx)
            if valx >8:
                print("Invalid Input.")
                valx = int(input("Kindly chose from 0-8 :"))


            xstate[valx] = 1
            time.sleep(0.8)
        elif turn == 0:
            print("O Turn")
            valz = random.randint(0,8)
            while valz in used_ch:
                print(valz, "Number already taken")
                valz = random.randint(0, 8)
            print("O Chose ", valz)
            used_ch.append(valz)
            zstate[valz] = 1
            time.sleep(0.8)
        player_win = winner(xstate,zstate)
        if player_win != -1:
            print("Match Over")
            break
        turn = 1 - turn
        left = left -1
        if left <=0:
            print("Match Draw")

play()