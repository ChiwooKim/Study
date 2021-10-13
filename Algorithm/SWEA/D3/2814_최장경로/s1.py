import sys
sys.stdin = open('input.txt')
'''
무방향 그래프
정점의 번호 : 1 ~ n번 
정점 번호 2번 이상 x
인접한 점 사이에 간선 존재
'''

def search(start,cnt):
    global result
    visited[start] = 1
    if result < cnt:
        result = cnt
    for i in range(1, n+1):
        if node[start][i] and visited[i] == 0:
            search(i, cnt+1)
    visited[start] = 0

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    node = [[0]*(n+1) for _ in range(n+1)]
    visited = [0] * (n + 1)
    for _ in range(m):
        x, y = map(int, input().split())
        node[x][y] = 1
        node[y][x] = 1

    result = 0
    cnt = 1
    for i in range(1, n+1):
        search(i, cnt)


    print('#{} {}'.format(tc+1, result))



