from random import randrange

count = int(input("введите длину 1 списка"))

list = [randrange(20) for i1 in range(count)]

print(list)

for i in range(count):
    print(list[count - i - 1])