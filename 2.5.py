import math

leiviska = float(input("Anna leiviskät: \n"))
naula = float(input("Anna naulat: \n"))
luoti = float(input("Anna luodit: \n"))

luotinyt = 13.3 * luoti
naulanyt = (13.3 * 32) * naula
leiviskanyt = (13.3 * 32 * 20) * leiviska
massa = luotinyt + naulanyt + leiviskanyt
# print(f"Massa nykymittojen mukaan:\n{massa:2.0f} grammaa.")

kilot = (massa / 1000)
grammat = ((kilot/1) - (kilot//1)) * 1000
print(f"Massa nykymittojen mukaan:")
print(math.floor(kilot), end = ' ')
print("kilogrammaa ja", end = ' ')
print(f"{grammat:.2f} grammaa.")