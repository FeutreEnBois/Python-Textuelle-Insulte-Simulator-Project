import sys
import player
import insulte

print(insulte.getPhrase)

def terminate():
    sys.exit()


def show_go_screen():
    print("\t\tOh sir ! (not) an insult simulator")
    print("\t\tThis game plays with the numpad")
    print("\t\tPress ENTER to begin")
    input()


game_over = True
while True:
    if game_over:
        show_go_screen()
        game_over = False

        score = 0
    #process input (events)
    break