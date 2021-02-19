x = int(input())

count = 1
while True :
    if (x-count)<=0 :
        break
    x -= count
    count += 1
if count%2 == 0:
    a=x
    b=count+1-x
else:
    a=count+1-x
    b=x
print(a,'/',b, sep='')

# x = int(input())

# sum = 0
# a = 0
# for i in range(1,5000):
#     sum += int(i)
#     if sum>=x : 
#         a=int(i)
#         break

# sum -= a
# count = x-sum
# if a%2 == 1 : 
#     print('%d/%d'% ((a+1)-count,count))
# else :
#     print('%d/%d'% (count,(a+1)-count))