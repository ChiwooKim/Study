import sys
sys.stdin = open('input.txt')
'''
S: 직진, L: 좌회전, R: 우회전
어렵다... 
'''
# 범위 체크(범위 밖으로 좌표가 되었을 경우 다시 돌아와 방향을 순환하게 하기 위함)
def check(y, x, d, grid, dir):
    dy = y + dir[d][0]
    dx = x + dir[d][1]

    if dy >= len(grid):
        dy = 0
    elif dy < 0:
        dy = len(grid) - 1

    if dx >= len(grid[0]):
        dx = 0
    elif dx < 0:
        dx = len(grid[0]) - 1

    return dy, dx


def dfs(state, org, route, grid):
    direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    y = state[0]
    x = state[1]
    d = state[2]

    # 시작지점 방문지 체크
    visited[d][y][x] = 1

    # 이동경로가 idx 이내의 범위인지 확인
    dy, dx = check(y, x, d, grid, direction)
    now = grid[dy][dx]

    #방향 전환
    if now == 'R':
        d = (d + 5) % 4

    elif now == 'L':
        d = (d + 7) % 4

    # 하나의 사이클이 완성됬을 경우 경로의 길이를 answer 리스트에 추가
    if org[0] == dy and org[1] == dx and org[2] == d:
        answer.append(route)
        return

    # 아직 방문지가 남았을경우 남은 사이클을 확인
    if not visited[d][dy][dx]:
        dfs([dy, dx, d], org, route + 1, grid)


def solution(grid):
    global answer, visited
    answer = []

    # 가로 세로 방향으로 방문체크 하기 위한 visited
    visited = [[[0] * len(grid[0]) for _ in range(len(grid))] for _ in range(4)]

    # 모든 경우의 수 확인
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                dfs([i, j, d], [i, j, d], 1, grid)

    # 조건대로 결과값을 오름차순 정렬하여 return
    return sorted(answer)




T = int(input())

for tc in range(T):
    grid = list(input().split())
    print(solution(grid))