import sys

n = int(input())

for i in range(n):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    avg = sum(arr[1:])/arr[0]
    count = 0
    for i in arr[1:]:
        if(i>avg):
            count += 1
    rate = round(count/arr[0]*100,3)
    print(str('%.3f'% rate)+"%")