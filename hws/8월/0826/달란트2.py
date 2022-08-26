T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    arr =[0]*b
    ans =1
    for i in range(a):
        arr[i%b] +=1
    for i in range(b):
        ans = ans*arr[i]
    print(f"#{tc} {ans}")