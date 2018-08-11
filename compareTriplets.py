def compareTriplets(a, b):
    alice = 0
    bob = 0
    for x in range(3):
        if a[x] > b[x]:
            alice += 1
        elif a[x] < b[x]:
            bob += 1
    return list([alice, bob])

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))
