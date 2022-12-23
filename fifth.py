from random import randrange

count = int(input("введите длину 1 и 2 списка"))

first_list = [randrange(20) for i in range(count)]
second_list = [randrange(20) for i1 in range(count)]

print(first_list)
print(second_list)


for i in first_list:
    if i not in second_list:
        print(i)