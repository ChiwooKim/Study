import sys
sys.stdin = open('input.txt')

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def make_set(x):
    p[x] = x
    rank[x] = 0

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


T = int(input())

ans = []
for tc in range(T):
    n, m = map(int, input().split())
    p = [0] * (n+1)
    rank = [0] * (n+1)

    for i in range(n+1):
        make_set(i)

    for i in range(m):
        x, y = map(int, input().split())
        union(x,y)

    result = 0

    for i in range(1, n+1):
        if i == p[i]:
            result += 1

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))