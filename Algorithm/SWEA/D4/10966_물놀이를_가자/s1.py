import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    waterpark = [list(input()) for _ in range(n)]
    result = 0

    # bfs를 통해 탐색
    # 델타탐색(상하좌우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[0]*m for _ in range(n)] # 방문지 체크
    q = deque()

    # 물인 지점 찾기
    for i in range(n):
        for j in range(m):
            if waterpark[i][j] == 'W':
                q.append([i, j])

    # bfs
    while q:
        start = q.popleft()
        for k in range(4):
            i = start[0] + dy[k]
            j = start[1] + dx[k]
            if 0 <= i <= n-1 and 0 <= j <= m-1 and visited[i][j] == 0 and waterpark[i][j] == 'L':
                q.append([i, j])
                visited[i][j] = visited[start[0]][start[1]] + 1
                result += visited[i][j]

    print('#{} {}'.format(tc+1, result))
