s = input()

for i in range (26):
    print(s.find(chr(ord('a')+i)), end=' ')

# find : 찾으려는 인자가 없으면 -1 반환
# index : 찾으려는 인자가 없으면 오류 발생