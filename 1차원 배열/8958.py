import sys

n = int(input())

for _ in range(n):
    arr = list(sys.stdin.readline().strip())
    a = 0
    while(arr[a]=='O'):
        

        if(arr[a]=='X'):
            break