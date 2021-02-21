n = int(input())

arr=[]
num = 2
while n>1 :
    if n%num == 0:
        n //= num
        arr.append(num)
    else :
        num += 1
for i in arr:
    print(i)
