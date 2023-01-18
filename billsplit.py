#Welcome
print("Számla-szétdobó")
print("")

#Input
total = int(input("Mennyi volt a teljes számla?: "))
tipPercent = int(input("Hány százalék borravalót számoljak?: ")) / 100
people = int(input("Hányan fogyasztottatok?: "))

#Calculate
tipAmount = total * tipPercent
tippedTotal = total + tipAmount
final = tippedTotal / people

#Output
print("")
print("A borravaló ", tipAmount , "forint!")
print("")
print("Fejenként" , final , "forint a számla!")