import sys

def sosu(a):
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            return False
    return True


n = int(input())


for _ in range(n):
    g = int(sys.stdin.readline())

    for i in range(g//2,1,-1):
        if sosu(i) and sosu(g-i):
             print(i,g-i,sep=' ')
             break
  
        
