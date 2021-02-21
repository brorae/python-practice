import sys
t = int(input())

for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().strip().split())
    d = ((x2-x1)**2+(y2-y1)**2)**0.5

    if d==0 and r1==r2:
        print(-1)
    elif d==r1+r2 or d==abs(r1-r2):
        print(1)
    elif d<abs(r1-r2) or d>r1+r2:
        print(0)
    else:
        print(2) 
