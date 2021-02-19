import sys
arr_x=[]
arr_y=[]
for _ in range(3):
    x, y= map(int,sys.stdin.readline().split())
    arr_x.append(x)
    arr_y.append(y)

arr_x.sort()
arr_y.sort()
if (arr_x[0]==arr_x[1]):
    print(arr_x[2],end=' ')
else:
    print(arr_x[0],end=' ')

if (arr_y[0]==arr_y[1]):
    print(arr_y[2])
else:
    print(arr_y[0])


    
