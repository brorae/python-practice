def d(n):
    
    a = n//1000
    b = (n%1000)//100
    c = (n%100)//10
    d = n%10
    self_num = n+a+b+c+d
    return self_num

arr = list()
for i in range(1,10001):
    arr.append(d(i))

arr.sort()

for i in range(1,10001):
    if i in arr: continue
    else : print(i)
