n = int(input())

arr = list(map(int,input().split()))

sosu=0
for num in arr:
    if num == 1 :
        continue
    count = 0
    for i in range(2,num):
        if num%i != 0 :
            count += 1
    if count == num-2 :
        sosu += 1
print(sosu)

