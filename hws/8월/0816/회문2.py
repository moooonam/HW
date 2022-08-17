def check(a):
    leng=len(a)
    for h in range(leng//2):
        if a[h] != a[leng-h-1]:
            return False
    return True


for tc in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    arr1=[]   # 행과 열 바꾸기
    for i in range(100):   
        str1=""
        for j in range(100):
            str1+=arr[j][i]
        arr1.append(str1)

    result=0
    for t in range(100, 0, -1):
        if result >=t:
            break
        for i in range(100):
            if result==t:
                break
            for j in range(100-t+1):
                if check(arr[i][j:j+t]) or check(arr1[i][j:j+t]):
                    result=t
                    break

    print(f'#{tc} {result}') 
             