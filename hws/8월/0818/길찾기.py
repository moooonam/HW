for tc in range(1, 11):
    m, n = map(int, input().split())
    node_list = [list([0]*100) for _ in range(100)]
    in_list = list(map(int, input().split()))
    for i in range(n):
        x, y = in_list[2*i], in_list[2*i+1]
        node_list[x][y] = 1
    visited = [0] * (100)
    stack = []
    now = 0
    visited[now] = 1
    ans = 0
    me =True
    while me:
        for w in range(1, 100):
            if node_list[now][w] == 1 and visited[w] == 0:
                stack.append(now)
                visited[w] = 1
                now = w
                if now == 99:
                    ans = 1
                    me = False
                break
        else:
            if stack:
                now= stack.pop()
            else:
                break
    print(f"#{tc} {ans}")
