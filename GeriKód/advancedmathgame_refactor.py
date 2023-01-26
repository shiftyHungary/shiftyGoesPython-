import random
from context import Context
import strategy

scoreAdd = 0
scoreSub = 0
scoreMul = 0
scoreDiv = 0
rounds = 0


print("Matek teszt!")
while True:
    gameMode = int(input(
        "VĂˇlassz tesztet! Ă–sszeadĂˇs(1), kivonĂˇs(2), szorzĂˇs(3) vagy osztĂˇs(4)?: "))

    if gameMode not in [1, 2, 3, 4]:
        print("Nem vĂˇlasztottĂˇl jĂˇtĂ©kmĂłdot!")
        continue

    roundScore = 0
    rounds += 1
    print(rounds, ". teszt!")

    for i in range(1, 11):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        match gameMode:
            case 1:
                context = Context(strategy.Ă–sszeadĂˇs())
                if context.do_test(a, b, i):
                    scoreAdd += 1
                    roundScore += 1
            case 2:
                context = Context(strategy.KivonĂˇs())
                if context.do_test(a, b, i):
                    scoreDiv += 1
                    roundScore += 1
            case 3:
                context = Context(strategy.SzorzĂˇs())
                if context.do_test(a, b, i):
                    scoreMul += 1
                    roundScore += 1
            case 4:
                context = Context(strategy.OsztĂˇs())
                if context.do_test(a, b, i):
                    scoreSub += 1
                    roundScore += 1

    print("Teszt vĂ©ge!", roundScore, "helyes vĂˇlaszod volt!")

    sumScore = scoreAdd+scoreDiv+scoreMul+scoreSub

    continueGame = input("JĂˇtsszunk Ăşjra? Igen / Nem: ")
    if continueGame == "Igen" or continueGame == "igen":
        continue
    else:
        print("\n", "JĂˇtĂ©k vĂ©ge! Ă–sszesen ", sumScore,
              "jĂł vĂˇlaszod volt, ", rounds*10, " feladatbĂłl!")
        break
