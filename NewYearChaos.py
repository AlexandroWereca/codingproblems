def minimumBribes(q):
    swaps = 0
    fail = False
    for i, v in enumerate(q):
        if q[i] - (i + 1) > 2:
            fail = True
            break
        elif q[i] - (i + 1) >= 0:
            swaps += q[i] - (i + 1)
    if fail:
        print('Too chaotic')
    else:
        print(str(swaps))

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)


        1 2 3 4 5 6 7 8
        1 2 5 3 4 6 7 8 2
        1 2 5 3 7 4 6 8 2
        1 2 5 3 7 8 4 6 2
        1 2 5 3 7 8 6 4 1