#imports
from getpass import getpass as input

#welcome
print("Kő 💎, papír 📄, olló ✂!" "\n" "Kő : k ; Papír : p ; Olló : o" "\n")

print("Emlékeztető:" "\n"
"A kő veri az ollót, de a papír veri a követ." "\n" 
"Az olló veri a papírt, de veszít a kő ellen" "\n"
"A papír veri a követ, de veszít a kő ellen" "\n"
)

#input
player1Input = input("Első játékos: ")
player2Input = input("Második játékos: ")
player1win = str("Első játékos nyert!")
player2win = str("Második játékos nyert!")

#logic
if player1Input == "k":
    if player2Input == "k":
        print("Mindketten követ mondtatok, döntetlen!")
    elif player2Input == "o":
        print(player2win,"A kő veri az ollót!")
    elif player2Input == "p":
        print(player1win," A papír veri a követ!")
    else:
        print("A második játékos nem jól írt be valamit, sajnálom.")
elif player1Input == "o":
    if player2Input == "o":
        print("Mindketten ollót mondtatok, döntetlen!")
    elif player2Input == "k":
        print(player2win, "A kő veri az ollót!")
    elif player2Input == "p":
        print(player1win,"Az olló veri a papírt!")
    else:
        print("A második játékos nem jól írt be valamit, sajnálom.")
elif player1Input == "p":
    if player2Input == "p":
        print("Mindketten papírt mondtatok, döntetlen!")
    elif player2Input == "o":
        print(player2win, "Az olló veri a papírt!")
    elif player2Input == "k":
        print(player1win, "A papír veri a követ!")
    else:
        print("A második játékos nem jól írt be valamit, sajnálom.")
else:
    print("Az első játékos nem jól írt be valamit, sajnálom.")