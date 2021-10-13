def dfs():
    visited = [[0]*(n+1) for _ in range(n+1)]
    stack = []
    stack.append(v)
    visited[v][v] = 1
    result = []
    while stack:
        st = stack.pop()
        if st not in result:
            result.append(st)
        for i in range(n, 0, -1):
            if node_ch[st][i] != 0 and visited[st][i] == 0:
                visited[st][i] = 1
                stack.append(i)
    return result


def bfs():
    visited = [0] * (n + 1)
    q = []
    q.append(v)
    visited[v] = 1
    result = []

    while q:
        st = q.pop(0)
        result.append(st)
        for i in range(1, n+1):
            if node_ch[st][i] != 0 and visited[i] == 0:
                q.append(i)
                visited[i] = 1
    return result


n, m, v = map(int, input().split())
number = []
for _ in range(m):
    number.append(list(map(int, input().split())))
node_ch = [[0]*(n+1) for _ in range(n+1)]
for i in number:
    node_ch[i[0]][i[1]] = 1
    node_ch[i[1]][i[0]] = 1

print(*dfs())
print(*bfs())
