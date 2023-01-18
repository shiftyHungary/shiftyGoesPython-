#welcome
print("Osztályozó program")
print("")

#input
maxPoints = int(input("Maximális pontszám: "))
userPoints = int(input("Dolgozat pontszáma: "))

#calculate
userPerc = round(float((userPoints / maxPoints) * 100), 1)

#statements
if userPerc == 100:
    userGrade = "Kiváló, 5*"
elif userPerc < 100 and userPerc >= 85:
    userGrade = "Jeles, 5"
elif userPerc < 85 and userPerc >= 70:
    userGrade = "Jó, 4"
elif userPerc < 70 and userPerc >= 60:
    userGrade = "Közepes, 3"
elif userPerc < 60 and userPerc >=50:
    userGrade = "Elégséges, 2"
else:
    userGrade = "Elégtelen, 1"

#output
print("")
print("A dolgozat ", userPerc," százalékos lett, az értékelése:" , userGrade, ".")