import sys

n,x = map(int,sys.stdin.readline().strip().split())
a = []
num = list(map(int,sys.stdin.readline().strip().split()))
for i in range(n):
    if (num[i]<x):
        a.append(num[i])
for i in a:
    print(i,end=" ")