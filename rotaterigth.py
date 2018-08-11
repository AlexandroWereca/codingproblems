if __name__=="__main__":
    lst = [1, 2, 3, 4, 5, 6]
    n = 4
    newlst = lst[-n:] + lst[:n]
    print(newlst)