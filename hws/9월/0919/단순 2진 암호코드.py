T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    x = 0
    y = 0
    for i in range(N):
        for j in range(M-1,50,-1):#50인 이유는 대충 줄인거임
            if arr[i][j]=='1':
                x=i
                y=j
                break
        if y!=0:
            break
    code=arr[x][y-55:y+1]
    num=[]
    # print(code)
    for i in range(0,50,7):
        if code[i:i+7] == '0001101':
            num.append(0)
 
        elif code[i:i+7] == '0011001':
            num.append(1)
 
        elif code[i:i+7] == '0010011':
            num.append(2)
 
        elif code[i:i+7] == '0111101':
            num.append(3)
 
        elif code[i:i+7] == '0100011':
            num.append(4)
 
        elif code[i:i+7] == '0110001':
            num.append(5)
 
        elif code[i:i+7] == '0101111':
            num.append(6)
 
        elif code[i:i+7] == '0111011':
            num.append(7)
 
        elif code[i:i+7] == '0110111':
            num.append(8)
 
        elif code[i:i+7] == '0001011':
            num.append(9)
    hol=0
    jjack=0
    for i in range(0,7,2):
        hol+=num[i]
    for i in range(1,8,2):
        jjack+=num[i]
    ans=0
    if (hol*3 +jjack)%10 ==0:
        ans =hol+jjack
    print(f'#{tc} {ans}')