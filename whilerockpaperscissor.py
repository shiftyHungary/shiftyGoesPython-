#imports
from getpass import getpass as input

#welcome
print("Kő 💎, papír 📄, olló ✂!" "\n" "Kő : k ; Papír : p ; Olló : o")

#input
p1WinStr = str("Első játékos nyert!")
p2WinStr = str("Második játékos nyert!")
p1WinCount = 0
p2WinCount = 0
rounds = 0

#looplogic
while True:
    rounds += 1
    print("\n",rounds, ". menet!", "\n")
    p1input = input("Első játékos: ")
    p2input = input("Második játékos: ")
    
# ide lehetne egyszer egy errort betenni, ha valamelyik játékos nem megengedett karaktert
# használ, akkor dobja a while elejére, ne keljen minden feltétel ellenőrzésnél 
# else ágat írni, a játékos javíthasson egyből.

    if p1input == "k":
        if p2input == "k":
            print("Mindketten követ mondtatok, döntetlen!")
        elif p2input == "o":
            print(p1WinStr,"A kő veri az ollót!")
            p1WinCount += 1
        elif p2input == "p":
            print(p2WinStr," A papír veri a követ!")
            p2WinCount += 1
        else:
            print("A második játékos nem jól írt be valamit, sajnálom.")
    elif p1input == "o":
        if p2input == "o":
            print("Mindketten ollót mondtatok, döntetlen!")
        elif p2input == "p":
            print(p1WinStr,"Az olló veri a papírt!")
            p1WinCount += 1
        elif p2input == "k":
            print(p2WinStr, "A kő veri az ollót!")
            p2WinCount += 1
        else:
            print("A második játékos nem jól írt be valamit, sajnálom.")
    elif p1input == "p":
        if p2input == "p":
            print("Mindketten papírt mondtatok, döntetlen!")
        elif p2input == "k":
            print(p1WinStr, "A papír veri a követ!")
            p1WinCount += 1
        elif p2input == "o":
            print(p2WinStr, "Az olló veri a papírt!")
            p2WinCount += 1
        else:
            print("A második játékos nem jól írt be valamit, sajnálom.")
    else:
        print("Az első játékos nem jól írt be valamit, sajnálom.")
   
    print("\n", "Az állás: ", p1WinCount, " - ", p2WinCount)
    
    if p1WinCount == 3 or p2WinCount == 3:
        break
    else:
        continue
    
print("\n", "Játék vége! A végeredmény: ", p1WinCount, " - ", p2WinCount)
exit()