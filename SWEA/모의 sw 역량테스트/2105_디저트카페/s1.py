import sys
sys.stdin = open('input.txt')

def safe(dy, dx): # 탐색 범위 & 중복 디저트 체크
    if -1 < dy < n and -1 < dx < n:
        if cafe[dy][dx] in stack:
            return 0
        if visited[dy][dx] == 0:
            return 1
    return 0

def search(y, x, prev):
    global result
    # 사각형 경로 종료조건(디저트종류가 최소 4개 이상이며, 시작지점으로 되돌아 와야함)
    if [y, x] == start and 3 < len(stack):
        result = max(result, len(stack)) # 최대경로 저장
        return

    # 방향 전환시 이전에 진행했던 방향으로는 갈수 없음(이동경로가 사각형이 되기 위함)
    for i, j in directions:
        if (i, j) not in check: # 진행했던 방향인지 확인
            dy = y + i
            dx = x + j
            if safe(dy, dx):
                visited[dy][dx] = 1 # 방문지 체크
                stack.append(cafe[dy][dx]) # 디저트 저장
                if prev != (i, j): # 방향전환
                    check.add(prev)
                    search(dy, dx, (i, j))
                    check.remove(prev)
                else: # 방향전환을 하지 않는다면 같은 방향 진행
                    search(dy, dx, prev)
                visited[dy][dx] = 0
                stack.pop()



T = int(input())

for tc in range(T):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    stack = [] # 디저트 종류 체크
    check = set()
    result = 0

    # 대각선 탐색(dy,dx)
    directions = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

    # 시작지점 찾기
    for i in range(1, n):
        for j in range(n):
            start = [i, j]
            search(i, j, (1, 1))

    if result == 0:
        result = -1

    print('#{} {}'.format(tc+1, result))