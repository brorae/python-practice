a,b = input().split()

str1 = ""
str2 = ""

for i in range(2,-1,-1):
    str1 += a[i]
    str2 += b[i]
if (int(str1)>=int(str2)): print(str1)
else : print(str2)
