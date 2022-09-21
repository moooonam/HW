def swap(num,s):
    if s==0:
        return
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            num[i],num[j]=num[j],num[i]
            new_num=int("".join(num))
            num[i],num[j]=num[j],num[i]
            if (new_num,s) not in num_list:
                num_list.append((new_num,s))
                # print(new_num, s)
                swap(list(str(new_num)),s-1)
            if s==1:
                ans_list.append(new_num)
            
                           
T = int(input())
for tc in range(1, T+1):
    my_num, N = input().split()
    N = int(N)
    max_num=0
    my_num = list(my_num)
    num_list=[]
    new_num=0
    ans_list=[]
    # for _ in range(N):
    #     for i in range(len(num)-1):
    #         for j in range(i+1,len(num)):
    #             num[i],num[j]=num[j],num[i]
    #             new_num=int("".join(num))
    #             if new_num not in num_list:
    #                 num_list.append(new_num)
    swap(my_num, N)
    max_num = max(ans_list)

    print(f"#{tc} {max_num}")
            
            



    
    