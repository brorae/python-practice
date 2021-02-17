s = input()

str1 = ""
time = 0

for i in s:
    if 0<=ord(i)-ord('A')<=2 : str1 += '2'
    if 3<=ord(i)-ord('A')<=5 : str1 += '3' 
    if 6<=ord(i)-ord('A')<=8 : str1 += '4' 
    if 9<=ord(i)-ord('A')<=11 : str1 += '5' 
    if 12<=ord(i)-ord('A')<=14 : str1 += '6' 
    if 15<=ord(i)-ord('A')<=18 : str1 += '7' 
    if 19<=ord(i)-ord('A')<=21 : str1 += '8'
    if 22<=ord(i)-ord('A')<=25 : str1 += '9'

for i in str1:
    time += int(i)
time = time+len(str1)

print(time)