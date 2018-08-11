if __name__=="__main__":
    n = int(input())
    input_list =list(map(int, input().split()))
    if len(input_list) == n and (n >=2 and n <=10):
        fixedlst = list(set(input_list))
        fixedlst.sort()
        print(fixedlst[-2])
