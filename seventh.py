li = [10, 14, 15, 235, 1235, 1235, 10]

for i in range(len(li)):
    isS = True
    for i1 in range(len(li)):
        if li[i] == li[i1] and i != i1:
            isS = False
            break
    if isS:
        print(li[i])