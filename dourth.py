import string


def convert(x, i):
    converted = ""
    while x >= i:
        ost = x % i
        x = x // i
        converted = string.hexdigits[ost] + converted
    return string.hexdigits[x] + converted


ch = int(input("введите число"))
print(str(convert(ch, 2)))
print(str(convert(ch, 8)))
print(str(convert(ch, 16)))



