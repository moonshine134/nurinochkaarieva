
x = int(input("введите тип перевода 1 - дюймы, 2 - футы"))
if x == 1:
    print(str(float(input("введите число")) / 2.54))
else:
    print(str(float(input("введите число")) / 30.48))