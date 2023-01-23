""" loan = 1000
rate = 1.05
payback = 0

for years in range(10):
    years +=1
    payback = loan * rate**years
    print("Year ", years," :", round(payback, 2)) """

loan2 = 1000
rate2 = 0.05

for years2 in range(10):
    years2 +=1
    loan2 += loan2*rate2
    print("Year ", years2, ": ", round(loan2,2))