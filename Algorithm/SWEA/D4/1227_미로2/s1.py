import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def find_goal(start, goal):
    res = 0
    q = deque()
    q.append(start)
    visited = [[0]*100 for _ in range(100)]   # 방문지 체크
    visited[start[0]][start[1]] = 1   # 출발점 방문 체크

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        temp = q.popleft()

        if temp == goal:
            res = 1
            return res

        for k in range(4):
            y = temp[0] + dy[k]
            x = temp[1] + dx[k]
            if 0 <= y < 100 and 0 <= x < 100 and maze[y][x] != 1 and visited[y][x] == 0:
                q.append([y, x])
                visited[y][x] = 1
    return res



ans = []
for tc in range(10):
    n = int(input())
    # 0: 길, 1: 벽, 2: 출발점, 3: 도착점
    maze = [list(map(int, input())) for _ in range(100)]
    start = []
    goal = []

    # 출발지점과 도착지점 찾기
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                goal = [i, j]
            if start and goal:
                break
        if start and goal:
            break

    # 출발지점으로부터 목적지까지 가는 경우를 찾기
    result = find_goal(start, goal)

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))
