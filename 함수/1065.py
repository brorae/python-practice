def hansu():
    count = 99
    n = int(input())
    if n < 99 : return n
    if 99<=n<=110 : return count
    else:
        for i in range(111,n+1):
            a = i//100
            b = (i%100)//10
            c = (i%10)
            if 2*b == a+c : count += 1
        return count

print(hansu())