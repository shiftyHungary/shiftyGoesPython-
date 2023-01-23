import random

scoreAdd = 0
scoreSub = 0
scoreMul = 0
scoreDiv = 0
rounds = 0

print("Matek teszt!")
while True: 
    gameMode = int(input("Válassz feladatot! Összeadás (1), kivonás(2), szorzás(3) vagy osztás(4)?: "))

    if gameMode == 1:
        #összeadás
        rounds += 1
        print(rounds, ". feladat!")
        for i in range (1,11):
            a = random.randint(1,100)
            b = random.randint(1,100)
            print(i,". kérdés:", a, " + ", b, "= ")
            solution = int(input(""))
            if solution == a + b:
                scoreAdd += 1
                print("Helyes válasz!")
            else:
                print("Rossz válasz!")
        print("Teszt vége!", scoreAdd, "helyes válaszod volt!")
    elif gameMode == 2:
        #kivonás
        rounds += 1
        print(rounds, ". feladat!")
        for j in range (1,11):
            c = random.randint(1,100)
            d = random.randint(1,100)
            print(j,". kérdés:", c, " - ", d, "= ")
            solution = int(input(""))
            if solution == c - d:
                scoreSub += 1
                print("Helyes válasz!")
            else:
                print("Rossz válasz!")
        print("Teszt vége!", scoreSub, "helyes válaszod volt!")
    elif gameMode == 3:
        #szorzás
        rounds += 1
        print(rounds, ". feladat!")
        for k in range (1,11):
            e = random.randint(1,12)
            f = random.randint(1,12)
            print(k,". kérdés:", e, " x ", f, "= ")
            solution = int(input(""))
            if solution == e * f:
                scoreMul += 1
                print("Helyes válasz!")
            else:
                print("Rossz válasz!")
        print("Teszt vége!", scoreMul, "helyes válaszod volt!")
    elif gameMode == 4:
        #osztás
        rounds += 1
        print(rounds, ". feladat!")
        for l in range (1,11):
            g = random.randint(1,100)
            h = random.randint(1,100)
            print(l,". kérdés:", g, " / ", h, "= ")
            solution = int(input(""))
            if solution == g // h:
                scoreDiv += 1
                print("Helyes válasz!")
            else:
                print("Rossz válasz!")
        print("Teszt vége!", scoreDiv, "helyes válaszod volt!")
    else:
        print("Nem választottál játékmódot!")
        
    sumScore = scoreAdd+scoreDiv+scoreMul+scoreSub
    
    continueGame = input("\n","Játsszunk újra? Igen / Nem: ")
    if continueGame == "Igen" or continueGame == "igen":
        continue
    else:
        print("\n","Játék vége! Összesen ", sumScore, " / ", rounds*10, "jó válaszod volt!")
        break