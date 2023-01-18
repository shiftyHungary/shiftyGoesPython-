""" exit = ""
while exit != "igen":
    print("Akkor maradunk...")
    exit = input("Kilépés?: ") """
    
""" while True:
    tovabb = input("A program fusson tovább?: ")
    if tovabb == "ne" or tovabb == "Ne":
        break
    else:
        print("A program fut tovább...")
print("A program nem fut tovább.")  """

print("Motörhead-time! Fill the gap in the lyrics of 'Ace of Spades'!")
missed = 0
while True:
    missing = input("If you like to ______, I tell you, I'm your man! ")
    if missing == "gamble":
        break
    else:
        missed +=1
        print("False! Try again!")
print("Great job! You only fucked up", missed, "time(s)!")