import sys
sys.stdin = open('input.txt')

def bfs():
    # 방문지 체크
    visited = [[0]*16 for _ in range(16)]
    q = [] # 큐 생성
    q.append(me)
    visited[me[0]][me[1]] = 1
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        st = q.pop(0)
        for k in range(4):
            i, j = st[0]+dy[k], st[1]+dx[k]
            if 0 <= i <= 15 and 0 <= j <= 15 and maze[i][j] != 1 and visited[i][j] == 0:
                q.append([i,j])
                visited[i][j] += 1
                if maze[i][j] == 3:
                    return 1
    return 0

ans = []
for _ in range(10):
    num = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # 출발점 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                me = [i, j]

    ans.append('#{} {}\n'.format(num, bfs()))
print(''.join(ans))
