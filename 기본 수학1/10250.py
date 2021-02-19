import sys

t = int(input())

for _ in range(t):
    h,w,n = map(int, sys.stdin.readline().strip().split())
    if n%h == 0 :
        floor=h
        hosu = n//h
    else :
        floor = n%h
        hosu = n//h + 1
    if hosu<10 :
        hosu = '0'+str(hosu)
    print(floor,hosu, sep='')