from collections import deque
if __name__=="__main__":
    n = int(input())
    d = deque()
    if n > 0 and n <= 100:
        for _ in range(n):
            cmd = input().split()
            print(cmd)
            print(d)
            if cmd[0] == "append":
                d.append(cmd[1])
                print(d)
            elif cmd[0] == "pop":
                d.pop()
                print(d)
            elif cmd[0] == "popleft":
                d.popleft()
                print(d)
            elif cmd[0] == "appendleft":
                d.appendleft(cmd[1])
                print(d)
        print(' '.join(d))