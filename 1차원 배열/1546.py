import sys

n = int(input())

arr = list(map(int,sys.stdin.readline().strip().split()))
sum = 0

max = max(arr)

for i in range(n):
    arr[i] = arr[i]/max*100

for i in arr:
    sum += i
print(sum/n)