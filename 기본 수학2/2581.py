m = int(input())
n = int(input())

arr = []
for num in range(m,n+1):
    count = 0
    for i in range(1,num):
        if num%i != 0:
            count += 1
    if count == num-2:
        arr.append(num)
if len(arr)==0 : print(-1)
else :
    print(sum(arr),min(arr))
    