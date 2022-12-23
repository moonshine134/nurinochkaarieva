count = int(input("введите диапазон"))

for i in range(2, count):
    i1 = True
    for n in range(2, i // 2 + 1):
        if i % n == 0:
            i1 = False
    if i1:
        print(i)
