def print_rangolin(size):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    if size > 0 and size < 27:
        row_len = 4*n - 3
        subset = alphabet[:size]
        subset.reverse()
        dash = "-"
        stng = subset[:]
        stngnormal = stng[:]
        stngnormal.sort()
        format_str = '{:-^' + str(row_len) + '}'
        for x in range(size):
            if x == 0:
                print(format_str.format(dash.join(stng[x])))
            else:
                newstng = stng[:x+1] + stngnormal[-x:]
                print(format_str.format(dash.join(newstng)))

        for y in range(size-1, 0, -1):
            if y == 1:
                print(format_str.format(dash.join(stng[y-1])))
            else:
                newstng = stng[:y] + stngnormal[-y+1:]
                print(format_str.format(dash.join(newstng)))

if __name__ == '__main__':
    n = int(input())
    print_rangolin(n)

