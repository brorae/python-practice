import sys

n = int(input())

comp = n
count = 0

while True:
    a = n//10
    b = n%10
    n = (a+b)%10+b*10
    count += 1
    if (n==comp):
        break
print (count)
