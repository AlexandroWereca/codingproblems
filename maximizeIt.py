from math import pow
import random

if __name__=='__main__':
    k, m = input().split()
    if (int(k) >= 1 and int(k)<= 7) and (int(m) >=1 and int(m) <= 1000):
        a = []
        # for _ in range(int(k)):
        N = (list(map(int, input().split()))[1:] for _ in range(int(k)))
        print(N)
            # n, *l = [int(x) for x in input().rstrip().split()]
            # if n >= 1 and n <= 7:
            #     if len(l) == n:
            #         a.append(l)
        # results = map(lambda x: sum(i ** 2 for i in x) % int(m), a)
        # print(max(results))
        #print(max(list(map(lambda x: sum(pow(x, 2)) % int(m), a))))