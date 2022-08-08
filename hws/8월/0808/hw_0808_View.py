for i in range(10):
    count=0
    T =int(input())
    case=list(map(int, input().split()))
    for j in range(2,len(case)-2):
        l1 =case[j-1]
        l2 =case[j-2]
        r1 =case[j+1]
        r2 =case[j+2]
        if l1<=case[j] and l2<=case[j] and r1<=case[j] and r2<=case[j]:
            max1=max(l1,l2,r1,r2)
            count+=case[j]-max1 
    print(f'#{i+1} {count}')
         
