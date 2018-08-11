from itertools import product


def main():
    a = [int(x) for x in input().rstrip().split()]
    b = [int(y) for y in input().rstrip().split()]
    if (len(a) > 0 and len(a) < 30) and (len(b) > 0 and len(b) < 30):
        a.sort()
        b.sort()
        print(' '.join(map(str, list(product(a, b)))))


if __name__ == '__main__':
    main()
