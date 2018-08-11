def minimumSwaps(arr):
    p = 0
    swap = 0
    while p < len(arr):
        minimun = min(arr[p:len(arr)])
        index = arr.index(minimun)
        if arr[p] > minimun:
            arr[index] = arr[p]
            arr[p] = minimun
            swap += 1
        p += 1
    return swap

if __name__=='__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print(str(res))