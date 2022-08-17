def pa(a):
    vin=[]
    for i in range(1, a+1):
        vin.append([0]*i)
    for i in range(a):
        for j in range(i+1):
            if j==0 or j==i:
                vin[i][j]=1
            else:
                vin[i][j]=vin[i-1][j-1]+vin[i-1][j]
    return vin
   
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    ans=pa(N)
    for i in range(N):
        for j in range(i+1):
            print(ans[i][j], end=' ')
        print()
   