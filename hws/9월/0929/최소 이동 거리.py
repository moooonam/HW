def di(s, V):
    global E
    U = [0] *(N+1) # 비용이 결정된 정점을 표시
    U[s] =1 # 출발지점 비용 결정
    for i in range(N+1):
        D[i] = hap[s][i]
    for _ in range(N+1):
        u = 0
        minV = 100*E
        for i in range(N+1):
            if U[i] == 0 and minV>D[i]:
                minV = D[i]
                u = i   # 출발점 이동
        U[u]=1
        for v in range(N+1):
            if 0 < hap[u][v] < 100*E:
                D[v] = min(D[v], D[u] + hap[u][v])
T = int(input())
for tc in range(1, T+1):
    N , E = map(int, input().split()) #N은 구간 끝지점 # E는 도로 갯수
    hap = [[100*E]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        hap[i][i] = 0
    for _ in range(E):
        x, y, w = map(int, input().split())
        hap[x][y] = w
    D = [0] * (N+1)
    di(0,N)
    print(D)
    print(f'#{tc} {D[N]}')