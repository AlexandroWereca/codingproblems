from math import pow
from collections import OrderedDict

if __name__=='__main__':
    n = int(input())
    if n >= 1 and n <= pow(10, 5):
        wordslst = OrderedDict()
        for _ in range(n):
            word = str(input()).rstrip().lower()
            if word not in wordslst.keys():
                wordslst.update({word: 1})
                continue
            wordslst[word] += 1
        print(len(wordslst.keys()))
        print(*wordslst.values())

