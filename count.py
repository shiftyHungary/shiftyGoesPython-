print ("""
Számolás!
""")

userAge = int(input("Hány éves vagy?: "))

if userAge < 18:
    print("Akkor még ne számoljunk...")
elif userAge >= 18 and userAge < 100:
    print("")
    print("Akkor számolunk!")
    print("")
    pi = float(input("Mi a Pi 2 értéke 2 tizedesjegyre?: "))
    if pi == 3.14:
        print("Helyes válasz!")
    else:
        print("")
        print("Nem... a helyes érték 3.14!")
        print("")
else:
    print("Számoltál már eleget.")