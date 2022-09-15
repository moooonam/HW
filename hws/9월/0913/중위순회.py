def inorder(n):
    if n:
        inorder(ch1[n])
        order_list.append(n)
        inorder(ch2[n])
for tc in range(1, 11):
    N = int(input())
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    word_list =['start']
    arr=[]
    order_list=[]
    ans=[]
    for i in range(1,N+1):
        arr= list(input().split())
        word_list.append(arr[1])
        if len(arr)==3:
            p, c = int(arr[0]), int(arr[2])
            ch1[p] = c
           
        if len(arr)==4:
            p, c1, c2 = int(arr[0]), int(arr[2]), int(arr[3])
            ch1[p] = c1
            ch2[p] = c2    
    
    inorder(1)
    for j in range(N):
        ans.append(word_list[order_list[j]])
    print(f'#{tc}', end=' ')
    for k in range(N):
        print(ans[k], end='')
    print()


        
