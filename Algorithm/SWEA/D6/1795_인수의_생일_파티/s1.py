import sys
sys.stdin = open('input.txt')

def time(start, graph):
    check = [999999999] * (n + 1)
    check[0] = 0 # 0번집은 없으니 0
    check[start] = 0 # 출발지는 시간 0
    visited = [0] * (n+1) # 방문지 확인

    for _ in range(n):
        st = 0
        min_v = 999999999 # 최소 시간 비교하기 위함

        for i in range(1, n+1):  # 최소 시간 찾기
            if visited[i] == 0:
                if check[i] < min_v:
                    st = i
                    min_v = check[i]
        visited[st] = 1  # 방문지 체크

        for j in range(1, n+1):
            if visited[j] == 0 and graph[st][j] != 0 and check[j] > check[st] + graph[st][j]:
                check[j] = check[st] + graph[st][j]

    return check

T = int(input())

ans = []
for tc in range(T):
    n, m, home = map(int, input().split())

    go = [[0]*(n+1) for _ in range(n+1)] # 갈 때
    back = [[0]*(n+1) for _ in range(n+1)] # 올 때

    for _ in range(m):
        a, b, c = map(int, input().split())
        go[a][b] = c
        back[b][a] = c

    go_time = time(home, go) # 갈 때 시간 저장
    back_time = time(home, back) # 올 때 시간 저장

    result = 0

    for i in range(1, n+1): # 갔다 오는데 가장 오래 걸린 시간 찾기
        if go_time[i] + back_time[i] > result:
            result = go_time[i] + back_time[i]

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))