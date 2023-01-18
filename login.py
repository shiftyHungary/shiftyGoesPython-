#Elkezdünk tanulni
print ("""Belépés!
""")
userName = input("> felhasználónév: ")
userPw = input("> jelszó: ")

if userName == "Bence" and userPw =="bence":
    userFav = input("> kedvenc karaktered: ")
    if userFav == "Obi-wan" or userFav == "Obi-Wan":
        print("")
        print("Zsír, " + userFav +  " a legjobb!")
        print("")
    elif userFav == "Anakin":
        print("")
        print("Érthető..." + "A sötét oldal veszélyes, " + userFav + "!")
        print("")
    elif userFav == "Palpatine":
        print("")
        print("No Jedi-archives for you!")
        print("")
    else:
        print("")
        print("Ha nem tudod, akkor te nem " + userName + " vagy!")
        print("")
elif userName == "Petra" and userPw =="Lolita":
    print("""
    Szia """ + userName + "!" + """
    """)
elif userName == "Vendég" or userName == "vendég":
    print("Üdv vendég!")
else:
    print("Ismeretlen felhasználó!")