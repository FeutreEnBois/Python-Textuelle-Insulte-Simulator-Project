from player import *
from insulte import *

# ne fait rien jusqu'a ce que l'utilisateur appuie sur enter
def show_go_screen():
    print("\t\tOh sir ! (not) an insult simulator")
    print("\t\tThis game plays with the numpad")
    print("\t\tPress ENTER to begin")
    input()

# change le joueur actuel
def ChooseAPlayer(P):
    if not P:
        P = Player1
    elif P == Player1:
        P = Player2
    else:
        P = Player1
    return P

# boucle du jeu
game_over = True
while game_over:
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

        print()
        print("*************************************************************************************")
        print("*                           !!! The match will now begin !!!                        *")
        print("*                        \t"+Player1.name+" vs "+Player2.name+"                     *")
        print("*************************************************************************************")
        P = ""
        game_over = False


        while (Player1.pv > 0 and Player2.pv > 0):
            score = 0
            P = ChooseAPlayer(P)
            E = ChooseAPlayer(P)
            print(P.name)
            print("pv adversaire : ", E.pv)
            print("Player " + str(P.P) + " c'est à votre tour")
            print("Voici vos mots pour ce : ")
            word = list(getPhrase())
            for i in range(len(word)):
                print(word[i] , "[" + str(i) + "]")
            insulte = []*10
            print("Choisissez un mot avec son index[0 - x]")
            print("Et placez le à l'endroit voulu dans la phrase [0 -x]")
            print("Quand votre insulte est prête, tapez 'PUNCH'")
            enter = ""

            # tour tu joueur
            while (enter != "PUNCH" or enter != "punch"):
                r = ""
                for i in insulte:
                    r += i.name
                    r+=" "
                print(r)
                enter = input("Quels mot choisissez vous? : ")
                if (enter == "PUNCH" or enter == "punch"):
                    break
                else :
                    enter = int(enter)

                print("Vous vez choisi ", word[enter])
                place = int(input(" Où le placez-vous ? [0 - x]"))
                insulte.insert(place, word[enter])

                # compte des points :
                # applique des malus / bonus en fonction des résistance / faiblesse adverse
                if type(word[enter]) == type(Principal("",0,"")) or type(word[enter]) == type(Sujet("",0,"")):
                    if word[enter].type in E.weakness:
                        score += word[enter].point * 2
                    elif word[enter].type in E.resistance:
                        score += word[enter].point / 2
                    else :
                        score += word[enter].point
                else:
                    score += word[enter].point


            

            # vérification des erreurs d'orthographe du joueur
            # application de malus en conséquence
            for i in range(len(insulte)-1):
                if type(insulte[i]) == type(insulte[i+1]):
                    print("point divisé par 2, vous avez utilisé deux fois le meme type de mot d'affilez !")
                    score /= 24
                if len(insulte) > 5 :
                    print("phrase longue, pti malus : 0 score")
                    score = 0
            E.pv -= score
            print(score)

    if Player1.pv <=0:
        print("!!! Le joueur 2 l'emporte !!!")
    else:
        print("!!! Le joueur 1 l'emporte !!!")

    print("recommencé a jouer ?")
    loop = input("(y / n) : ")
    if loop == "y":
        game_over = True
    