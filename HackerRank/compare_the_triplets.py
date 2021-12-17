a = [5, 6, 7]
b = [3, 6, 10]

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif b[i] > a[i]:
            bob += 1
    result = [alice, bob]
    return result

c = compareTriplets(a, b)
print(c)