# run_list=[
#     [0,1,2],
#     [1,2,3],
#     [2,3,4],
#     [3,4,5],
#     [4,5,6],
#     [5,6,7],
#     [6,7,8],
#     [7,8,9]
#     ]
        # for i in range(len(player_1)-2):
        #     check_list1=[player_1[i],player_1[i+1],player_1[i+2]]
        #     if check_list1 in run_list:
        #         winner=1
        #         break
        # for i in range(len(player_2)-2):
        #     check_list2=[player_2[i],player_2[i+1],player_2[i+2]]
        #     if check_list2 in run_list:
        #         winner=2
        #         break

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    player_1=[]
    player_2=[]
    for i in range(6):
        if i%2==0:
            player_1.append(card[i])
        else:
            player_2.append(card[i])
    
    winner=0
    for j in range(6,13):
        check_list1=[]
        check_list2=[]
        for k in player_1:
            if winner!=0:
                break
            check=k
            cnt=0
            for p in range(len(player_1)):
                if player_1[p]==check:
                    cnt+=1
            if cnt==3:
                winner=1
                break
        for k in player_2:
            if winner!=0:
                break
            check=k
            cnt=0
            for p in range(len(player_2)):
                if player_2[p]==check:
                    cnt+=1
            if cnt==3:
                winner=2
                break
        
        # 연속된거 확인
        player_1.sort()
        player_2.sort()
        for k in player_1:
            if winner!=0:
                break
            check=k
            cnt=0
            for p in range(len(player_1)):
                if player_1[p]==check+1:
                    cnt+=1
                    check+=1
            if cnt==2:
                winner=1
                break
        for k in player_2:
            if winner!=0:
                break
            check=k
            cnt=0
            for p in range(len(player_2)):
                if player_2[p]==check+1:
                    cnt+=1
                    check+=1
            if cnt==2:
                winner=2
        if winner!=0:
            break
        if j==12:
            break
        if j%2==0:
            player_1.append(card[j])
        else:
            player_2.append(card[j])   
    print(f'#{tc} {winner}')

            