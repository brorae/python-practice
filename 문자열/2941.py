s = input()

croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']

count=0

for a in croa:    
    if a in s:
        count += s.count(a)

print(len(s)-count)