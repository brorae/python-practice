arr=[]
count=0

for i in range(42):
    arr.append(0)

for i in range (10):
    arr[int(input())%42] += 1

for i in arr:
    if (i>=1):
        count += 1
print(count)



