import sys
from player import *
from insulte import *

sujet = Sujet("m", 5, "m")
print(sujet)
print(getPhrase)

def terminate():
    sys.exit()


def show_go_screen():
    print("\t\tOh sir ! (not) an insult simulator")
    print("\t\tThis game plays with the numpad")
    print("\t\tPress ENTER to begin")
    input()

def ChooseAPlayer(P):
    if not P:
        P = Player1
    elif P == Player1:
        P = Player2
    else:
        P == Player1
    return P

game_over = True
while True:
    if game_over:
        show_go_screen()
        print("Player 1 : Choose your character ! (Write is name) ")
        print(player("test", 0).classe)
        Player1 = player(input(), 1)
        print("Player 2 : Choose your character ! (Write is name) ")
        print(player("test", 0).classe)
        Player2 = player(input(), 2)
        print()
        print("!!! The match will now begin !!!")
        print("\t" + Player1.name + " vs " + Player2.name)
        P = ""
        game_over = False

    P = ChooseAPlayer(P)
    print(P.name)
    print("Player " + str(P.P) + " it's your turn")
    print("here are your word for this turn : ")
    word = list(getPhrase())
    for i in range(len(word)):
        print(word[i])
    P = ChooseAPlayer(P)
    print(P.name)
    score = 0
    
    #process input (events)
    break