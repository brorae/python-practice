t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    apt = [[] for i in range(15)]
    apt[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    for i in range(1,15):
        for j in range(14):
            apt[i].append(sum(apt[i-1][0:j+1]))
    print(apt[k][n-1])


        


