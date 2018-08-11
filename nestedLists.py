if __name__ == '__main__':
    n = int(input())
    if n >= 2 and n <= 5:
        sheet = []
        for _ in range(n):
            name = input()
            score = float(input())
            student = [name, score]
            sheet.append(student)
        low = sorted(list(set([sheet[x][1] for x in range(n)])))[1]
        print('\n'.join(sorted([a for a,b in sheet if b == low])))


# 5
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21