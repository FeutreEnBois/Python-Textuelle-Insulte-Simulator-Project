import sys
from player import *
from insulte import *

sujet = Sujet("m", 5, "m")
print(sujet)
print(getPhrase())

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
        print("*************************************************************************************")
        print("*                                                                                   *")
        print("*                                                                                   *")
        print("*                      Bienvenue dans le jeu de l'insulte                           *")
        print("*                                                                                   *")
        print("*                                                                                   *")
        print("*************************************************************************************")
        print("")
        print("")
        print("")
        print("")
        print("*************************************************************************************")
        print("*                           Player 1 choisie un combatant                           *")
        print("*                        1. Mage 2. Vieille 3. Étudiant                             *")
        print("*************************************************************************************")

        Player1 = player(1, int(input("Entrer le numero correspondant au combatant choisi.")))

        print("")
        print("Vous avez choisi:",Player1.name)
        print("")
        print("")
        print("")
        print("*************************************************************************************")
        print("*                           Player 2 choisie un combatant                           *")
        print("*                        1. Mage 2. Vieille 3. Étudiant                             *")
        print("*************************************************************************************")

        Player2 = player(2,int(input("Entrer le numero correspondant au combatant choisi.")))
        print("")
        print("Vous avez choisi:",Player2.name)
        # print("Player 1 : Choose your character ! (Write is name) ")
        # classe = player(0, "test").classe
        # Player1 = player(input(), 1)
        # print("Player 2 : Choose your character ! (Write is name) ")
        # # print(player("test", 0).classe)
        # Player2 = player(input(), 2)
        print()
        print("*************************************************************************************")
        print("*                           !!! The match will now begin !!!                        *")
        print("*                        \t"+Player1.name+" vs "+Player2.name+"                     *")
        print("*************************************************************************************")
        P = ""
        game_over = False

    P = ChooseAPlayer(P)
    print(P.name)
    print("Player " + str(P.P) + " it's your turn")
    print("here are your word for this turn : ")
    word = list(getPhrase())
    for i in range(len(word)):
        print(word[i] , "[" + str(i) + "]")
    insulte = [""]*10
    print("Choose a word with it's index [0 - x]")
    print("And place it in you insulte with the number of it's place [0 -x]")
    print("When you insult is ready enter 'PUNCH'")
    print("your insult : ", " ".join(insulte))
    enter = int(input("which word do you choose : "))
    while enter != "PUNCH":
        print("you choose ", word[enter])
        place = int(input(" where do you place it ? [0 - x]"))

    P = ChooseAPlayer(P)
    print(P.name)
    score = 0
    
    #process input (events)
    break