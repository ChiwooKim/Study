def bfs():
    # 좌표를 체크 해야하기 때문에 visited도 행렬로 표기
    visited = [[0]*m for _ in range(n)]
    q = [] # 큐 생성
    q.append(start)
    visited[start[0]][start[1]] = 1
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        st = q.pop(0)
        for k in range(4):
            i, j = st[0]+dy[k], st[1]+dx[k]
            if 0 <= i <= n-1 and 0 <= j <= m-1 and maze[i][j] == 1 and visited[i][j] == 0:
                q.append([i, j])
                visited[i][j] = visited[st[0]][st[1]] + 1
                if [i, j] == [n-1, m-1]:
                    return visited[i][j]




n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]

start = [0, 0]

print(bfs())
