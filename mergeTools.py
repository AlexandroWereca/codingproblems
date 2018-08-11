def merge_the_tools(string, k):
    if len(string) >=1 and len(string) <= 10**4 and k>=1 and k <= len(string):
        t = [string[k*x:k*(x+1)] for x in range(len(string)//k)]
        u = []
        for s in t:
            u.clear()
            for p in s:
                if p not in u:
                    u.append(p)
            print(''.join(u))
if __name__=='__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)