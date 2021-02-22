import sys

t = int(input())

for _ in range(t):
    x,y=map(int,sys.stdin.readline().split())
    d = y-x
    if d<=3 :
        print(d)
    else:
        n = int(d**0.5)
        if n**2 == d :
            print(2*n-1)
        elif n**2 < d <= n*(n+1) :
            print(2*n)
        elif n*(n+1) < d <= n*(n+2) :
            print(2*n+1)
