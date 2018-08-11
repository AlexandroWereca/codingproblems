def leftRotation(a, d):
    rotatedlst = a[:]
    for x in range(d):
        elem = rotatedlst[0]
        rotatedlst.pop(0)
        rotatedlst.append(elem)
    return ' '.join(rotatedlst)
if __name__=="__main__":
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    #a = list(map(int, input().rstrip().split()))
    result = leftRotation([5, 4, 7, 2, 3], d)
    print(result)