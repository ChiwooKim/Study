import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
parent = [0] * (n+1)
q = deque()
q.append(1)
while q:
    t = q.popleft()
    for i in tree[t]:
        if parent[i] == 0:
            parent[i] = t
            q.append(i)
for i in range(2, n+1):
    print(parent[i])


# 시간초과
# input_list = []
# for _ in range(n-1):
#     input_list.append(list(map(int, input().split())))
# tree = [0] * (n+1)
# q = deque()
# q.append(1)
# while q:
#     t = q.popleft()
#     for i in input_list:
#         if i[0] == t and tree[i[1]] == 0:
#             tree[i[1]] = t
#             q.append(i[1])
#         if i[1] == t and tree[i[0]] == 0:
#             tree[i[0]] = t
#             q.append(i[0])
#
# for i in range(2, n+1):
#     print(tree[i])