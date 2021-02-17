import sys

n = int(input())

for _ in range(n):
    arr = list(sys.stdin.readline().strip())
    sum = 0
    c = 1
    for i in arr:
        if (i=='O'):
            sum += c
            c += 1
        if (i=='X'):
            c = 1
    print(sum)