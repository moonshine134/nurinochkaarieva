from random import randrange

count = int(input("введите длину 1 и 2 списка"))

first_list = [randrange(20) for i in range(count)]
second_list = [randrange(20) for i1 in range(count)]

print(first_list)
print(second_list)

last_list = []

for i in range(count):
    if first_list[i] % 2 != 0:
        last_list.append(first_list[i])
    if second_list[i] % 2 == 0:
        last_list.append(second_list[i])

print(last_list)