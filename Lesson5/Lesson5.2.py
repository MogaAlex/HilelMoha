answer = ""
while answer == "Yes" or "yes" or "y":

    x = int(input("Vedite 1-oe chislo: "))
    y = str(input("Vedite znak +,-,*,/: "))
    z = int(input("Vedite 2-oe chislo: "))
    if y == "+":
        print(x + z)
    elif y == "/" and z != 0:
        print(x / z)
    elif y == "*":
        print(x * z)
    elif y == "-":
        print(x - z)
    elif y == "/" and z == 0:
        print("Na nol ne delitsa")
    else:
        print("Vedite pravilniy znak")

    print("Hotite prodoljit?")
    answer = input()
    if answer == "Yes" or answer == "yes" or answer == "y":
        continue
    else:
        break
