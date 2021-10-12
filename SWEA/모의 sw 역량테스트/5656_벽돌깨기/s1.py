import sys
sys.stdin = open('input.txt')
from itertools import product
from collections import deque
import copy


def crush(a, b):
    q = deque()
    q.append([a, b, brick[a][b]])
    brick[a][b] = 0

    while q:
        y, x, z = q.popleft()
        for m in range(1, z):
            for k in range(4):
                i = y + m*dy[k]
                j = x + m*dx[k]
                if 0 <= i < h and 0 <= j < w and brick[i][j] != 0:
                    if brick[i][j] != 1:
                        q.append([i, j, brick[i][j]])
                    brick[i][j] = 0


T = int(input())

for tc in range(T):
    n, w, h = map(int, input().split())
    brick_input = [list(map(int, input().split())) for _ in range(h)]
    result = []

    # 떨어뜨릴 라인을 선택하는 모든 경우의 수 구하기(중복순열)
    line = []
    for i in product(range(w), repeat=n):
        line.append(list(i))

    # 상,하,좌,우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 벽돌 깨기
    for l in line:
        brick = copy.deepcopy(brick_input)

        for j in l:
            f = 0
            for i in range(h):
                if brick[i][j]:
                    f = i
                    break
            crush(f, j)

            # 깨고 난 후 0 자리 메꿔주기
            for b in range(w):
                check = []
                for a in range(h-1, -1, -1):
                    if brick[a][b]:
                        check.append(brick[a][b])
                        brick[a][b] = 0
                for p in range(len(check)):
                    brick[h-1-p][b] = check[p]

        # 남는 벽돌 개수 저장
        total = 0
        for i in range(h):
            for j in range(w):
                if brick[i][j] != 0:
                    total += 1

        result.append(total)

    print('#{} {}'.format(tc+1, min(result)))