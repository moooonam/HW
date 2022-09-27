def work(x,percent):
    global max_percent
    if x==N:
        if percent>max_percent:
            max_percent=percent
        return
    if percent<= max_percent:
        return
    for i in range(N):
        if visited[i]==0 and arr[x][i]!=0:
            visited[i]=1
            work(x+1,percent*arr[x][i]/100)
            visited[i]=0
           
        

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_percent =0
    visited=[0]*N
    work(0,1)
    max_percent=format(round(max_percent*100,6),".6f")
    print(f'#{tc} {max_percent}')
