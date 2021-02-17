import sys

n = int(input())

for _ in range(n):
    r, s = sys.stdin.readline().strip().split()
    r = int(r)
    s = str(s)
    str1 = ""
    for i in s:
        str1 += i*r
    print (str1)
