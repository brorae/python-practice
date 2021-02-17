s = input()

arr = [0 for i in range(26)]

s =s.lower()

for i in s:
    arr[ord(i)-ord('a')] += 1

if arr.count(max(arr))!=1 : print("?")
else : print(chr(arr.index(max(arr))+ord('A')))