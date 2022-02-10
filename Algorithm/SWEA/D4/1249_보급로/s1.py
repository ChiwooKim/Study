import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

ans = []
for tc in range(T):
    n = int(input())
    road = [list(map(int, input())) for _ in range(n)]

    start = (0, 0) # 출발지

    # 최소 복구 시간 저장하기 위한 visited 생성(복수시간 최대보다 항상 커야 비교했을 때 저장할 수 있으므로 초기값을 크게 설정하여 생성 )
    visited = [[999999999]*n for _ in range(n)]

    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    q = deque()
    q.append(start)
    visited[0][0] = 0

    # 최소시간 찾기
    while q:
        y, x = q.popleft()

        for k in range(4):
            i = y + dy[k]
            j = x + dx[k]

            if 0 <= i < n and 0 <= j < n and visited[i][j] > visited[y][x] + road[i][j]:
                visited[i][j] = visited[y][x] + road[i][j]
                q.append((i, j))

    ans.append('#{} {}\n'.format(tc+1, visited[n-1][n-1]))
print(''.join(ans))