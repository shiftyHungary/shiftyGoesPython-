import random

score = 0

print("Matek teszt!")

for i in range (1,11):
    a = random.randint(1,13)
    b = random.randint(1,13)

    print(i,". kérdés:", a, " x ", b, "= ")
    solution = int(input(""))
    if solution == a*b:
        score += 1
        print("Helyes válasz!")
    else:
        print("Rossz válasz...")

print("Teszt vége!", score, "helyes válaszod volt!")