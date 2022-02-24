import sys
sys.stdin = open('input.txt')

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    p[find_set(x)] = find_set(y)

T = int(input())

ans = []
for tc in range(T):
    n = int(input()) # 섬의 개수
    x = list(map(int, input().split())) # x좌표
    y = list(map(int, input().split())) # y좌표
    tax = float(input()) # 세율

    # 섬 사이의 거리 저장 (섬 번호 사이 거리의 제곱의 값을 저장)
    island = []

    for i in range(n):
        for j in range(i+1, n):
            if i == j:
                continue
            length = (x[i]-x[j])**2 + (y[i]-y[j])**2
            island.append([i, j, length])

    island.sort(key=lambda x: x[2])

    p = list(range(n)) # make-set

    cnt = 0  # 섬 사이 연결한 회수
    result = 0  # 환경부담금
    idx = 0

    while cnt < n-1:
        n1 = island[idx][0]
        n2 = island[idx][1]

        if find_set(n1) != find_set(n2):
            union(n1, n2)
            cnt += 1
            result += island[idx][2] * tax
        idx += 1

    ans.append('#{} {}\n'.format(tc+1, round(result)))
print(''.join(ans))
