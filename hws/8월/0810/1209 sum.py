
for T in range(1, 11):
    num=int(input())
    N=100
    arr = [list(map(int,input().split())) for _ in range(N)]
    max1 = 0 #최대 행의합
    max2 = 0
    max3 = 0
    max4 = 0
    for i in range(N):
        s1 = 0 #행의 합
        s2 = 0 #열의 합
        max3 += arr[i][i] #대각선1의 합
        max4 += arr[i][99-i] #대각선2의 합
        for j in range(N):
            s1 += arr[i][j]
            s2 += arr[j][i]
        if max1 <s1:
            max1 =s1
        if max2 <s2:
            max2 =s2
    result1=0
    result2=0
    if max1 <=max2:
        result1=max2
    else:
        result1=max1
    if max3 <=max4:
        result2=max4
    else:
        result2=max3
    if result1<=result2:
        print(f'#{num} {result2}')
    else:
        print(f'#{num} {result1}')


    