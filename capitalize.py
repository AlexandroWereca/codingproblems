def capital(s):
    result = ' '
    if len(s) > 0 and len(s) < 1000:
        lst = s.split(' ')
        for x in range(len(lst)):
            if lst[x].isalpha():
                lst[x] = lst[x][0].upper() + lst[x][1:]
        return result.join(lst)

if __name__ == '__main__':
    s = input()
    result = capital(s)
    print(result)