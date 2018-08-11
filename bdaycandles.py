from itertools import count
def birthdayCakeCandles(ar_count, ar):
    max_val = max(ar)
    counter = ar.count(max_val)
    return counter

if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar_count, ar)

    print(str(result))