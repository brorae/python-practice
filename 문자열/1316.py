import sys

n = int(input())
count = 0
for _ in range(n):
    s = sys.stdin.readline().strip()
    error = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i] in s[i+1:]: error += 1
        
    if error == 0 : count+=1 
print (count)

