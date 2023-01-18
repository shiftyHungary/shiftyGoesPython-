print ("Számolás!" "\n")
exit = ""

while exit != "igen" or exit != "Igen":
    userAge = int(input("Hány éves vagy?: "))
    if userAge < 10:
        print("Akkor még ne tippelj...")
    elif userAge >= 10 and userAge < 80:
        print("\n" "Akkor kérdezek!" "\n")
        pi = float(input("Mi a Pi 2 értéke 2 tizedesjegyre?: "))
        if pi == 3.14:
            print("Helyes válasz!")
        else:
            print("")
            print("Nem... a helyes érték 3.14!")
            print("")
    else:
        print("Akkor te tippeltél már eleget.")
    exit = input("Kilépjünk a programból?: ")