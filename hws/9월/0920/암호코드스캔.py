# 구글 검색해서 참고하였음!!
my_dict_16={
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
    }
code= {
    (2,1,1):0,
    (2,2,1):1,
    (1,2,2):2,
    (4,1,1):3,
    (1,3,2):4,
    (2,3,1):5,
    (1,1,4):6,
    (3,1,2):7,
    (2,1,3):8,
    (1,1,2):9

}
T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    arr = sorted(list(set([input().strip() for _ in range(N)]))) # 중복제거
    arr.pop(0)#0만 있는거 제거
    visited=[]
    ans=0
    for i in range(len(arr)):
        arr_2 = '' #2진수로 바꿀거
        for n in range(len(arr[i])):
            arr_2 += my_dict_16[arr[i][n]]
        arr_2 =arr_2.rstrip('0')

        num_list=[]
        n1=n2=n3=n4=0
        for j in range(len(arr_2)-1,-1,-1):
            if arr_2[j] =='1' and n3 ==0:
                n4+=1
            elif arr_2[j] == '0' and n2==0:
                n3+=1
            elif arr_2[j] == '1' and n1==0:
                n2+=1
            elif arr_2[j]=='0':
                if arr_2[j-1]=='1':
                    n= min(n2,n3,n4)
                    num_list.append((code[n2//n, n3//n, n4//n]))
                    n2 = n3 = n4=0
                    if len(num_list)==8:
                        if ((num_list[7]+num_list[5]+num_list[3]+num_list[1])*3 +(num_list[6]+num_list[4]+num_list[2])+num_list[0])%10 == 0 and num_list not in visited:
                            ans += sum(num_list)
                            visited.append(num_list)
                        # print(num_list)
                        num_list=[]

    print(f'#{tc} {ans}')                        


