for tc in range(1,11):
    T=int(input())
    expend_list=[[0]*(102)for _ in range(100)] # 양 옆에 0을 추가하겠음
    arr=[list(map(int, input().split()))for _ in range(100)]
    for i in range(100):
        for j in range(100):
            expend_list[i][j+1]=arr[i][j]
    for q in range(101):
        if expend_list[99][q]==2:
            x=q
    y=99
    while y!=0: # 2부터 1을 따라서 올라와서 0열에 도착하면 멈추게
        if expend_list[y-1][x]==1 and expend_list[y][x-1]==0 and expend_list[y][x+1]==0: #위에가 1 이고 양옆이 0이면 위로 이동
            y-=1   
        elif expend_list[y][x-1]==1 and expend_list[y-1][x]==1: #왼쪽 이동
            while expend_list[y][x-1]==1:
                x-=1
            y-=1
        elif expend_list[y][x+1]==1 and expend_list[y-1][x]==1: #오른쪽 이동
            while expend_list[y][x+1]==1:
                x+=1
            y-=1
    print(f'#{tc} {x-1}')