import random

myNumber = random.randint(0,100)
rounds = 0
print("Gondoltam egy számra 1 és 100 között!")
while True:
    rounds += 1
    playerNumber = int(input("Tippelj!: "))    
    if playerNumber > myNumber:
        print("Kisebb számra gondoltam!")
    elif playerNumber < myNumber:
        print("Nagyobb számra gondoltam!")
    elif playerNumber < 0:
        exit()
    else:
        print("Valamit nem jól írtál be.")
    
    if playerNumber != myNumber:
        continue
    else:
        print("Szép munka! A szám amire gondoltam: ", myNumber,"\n",
              "Ugyan kellett hozzá ", rounds, "esély, de kitaláltad!")
        break