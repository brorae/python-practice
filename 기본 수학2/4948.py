def sosu(a) :
    if a == 1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            return False
    return True


import sys

while True :
    n = int(sys.stdin.readline())
    if n==0 : 
        break
    count = 0
    for i in range(n+1,2*n+1):
        if sosu(i) :
            count +=1
    print(count)