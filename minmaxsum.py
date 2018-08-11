import math
import os
import random
import re
import sys
from functools import reduce


def miniMaxSum(arr):
    arr.sort()
    max_val = reduce(lambda x,y: x+y, arr[1:])
    min_val = reduce(lambda x,y: x+y, arr[:-1])
    print(min_val, max_val)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)