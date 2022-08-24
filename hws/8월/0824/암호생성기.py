for tc in range(1, 11):
    N= int(input())
    arr = list(map(int, input().split()))
    q =[]
    k = 1
    while True:
        h = arr.pop(0)
        a = h-k
        if a <= 0:
            arr.append(0)
            break
        else:
            arr.append(a)
        if k == 5:
            k = 1
        else:
            k+=1
        
    print(f"#{tc}",end=" ")
    for i in range(8):
        print(arr[i], end=" ")
    print()
    
        
