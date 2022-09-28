from collections import deque 

def find(n):
    q =deque([(n,0)]) # 카운트와 숫자를 저장하고 앞에서 하나씩 꺼내서 연산
    visited = set([n]) # 지금까지 나온 숫자를 저장
    while q:
        num, count = q.popleft() # 이부분을 pop(0)으로 했는데 시간초과가 나와서 검색해보니 디큐 쓰면 된다해서 이걸로 했습니다.
        if num==M:
            return count
        count+=1
        if num*2 not in visited and  num*2<=1000000:
            q.append((num*2, count))
            visited.add(num*2)
        if num+1 not in visited and  num+1<=1000000:
            q.append((num+1, count))
            visited.add(num+1)
        if num-1 not in visited and 0< num-1<=1000000:
            q.append((num-1, count))
            visited.add(num-1)
        if num-10 not in visited and 0< num-10<=1000000:
            q.append((num-10, count))
            visited.add(num-10)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {find(N)}')