'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
import _random
import random
UI = 0
U_Win=0
C_Win=0
U_lost = 0
C_lost = 0
Tie_Cnt=0

print("4 to quit.")
while UI != 4:
    UI = 0
    while UI < 1 or UI > 4:
        UI_Str = input("1 for rock, 2 for paper,3 for scissor:")
        if UI_Str == "":
            UI = 0
        else:
            UI = int(UI_Str)

    if UI == 4:
        break
    elif UI == 1:
        UI2 = "rock"
    elif UI == 2:
        UI2 = "paper"
    elif UI == 3:
        UI2 = "scissors"

    CI = random.randint(1,3)
    if CI == 1:
        CI2 = ("rock")
    elif CI == 2:
        CI2 = ("paper")
    elif CI == 3:
        CI2 = ("scissors")


    if UI2 == CI2:
        Winner = "Tie"
    elif UI2 == "rock" and CI2 == "scissors":
        Winner = "User"
    elif UI2 == "paper" and CI2 == "rock":
        Winner = "User"
    elif UI2 == "scissors" and CI2 == "paper":
        Winner = "User"
    elif CI2 == "rock" and UI2 == "scissors":
        Winner = "computer"
    elif CI2 == "paper" and UI2 == "rock":
        Winner = "computer"
    elif CI2 == "scissors" and UI2 == "paper":
        Winner = "computer"
    else:
        Winner = ""

    if Winner == "User":
        U_Win = U_Win + 1
        C_lost = C_lost + 1
    elif Winner == "Tie":
        Tie_Cnt = Tie_Cnt + 1
    else:
        C_Win = C_Win + 1
        U_lost = U_lost + 1

    if Winner == "User":
        result = "won"
    elif Winner == "Tie":
        result = "tied"
    else:
        result = "lost"
    print("computer picked",CI2,"You Choose",UI2,"you",result)
print("your record is,",C_Win,"Wins,",C_lost,"Lost,",Tie_Cnt,"Tie")





















