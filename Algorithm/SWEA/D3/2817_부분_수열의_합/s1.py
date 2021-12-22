import sys
sys.stdin = open('input.txt')

'''
1. 비트연산을 이용하여 부분집합을 구하면서 합을 구한 후 K값과 비교
2. 재귀(dfs)를 이용하여 풀이
재귀로 풀었을 경우가 2배 빠른속도로 결과가 나왔다.
'''

# ans = []
# for tc in range(int(input())):
#     N, K = map(int, input().split())
#     numbers = list(map(int, input().split()))
#
#     result = 0
#     for i in range(1<<N):
#         temp = 0
#         for j in range(N):
#             if i & (1<<j):
#                 temp += numbers[j]
#         if temp == K:
#             result += 1
#
#     ans.append('#{} {}\n'.format(tc+1, result))
# print(''.join(ans))

def check(idx, total):
    global result
    visited[idx] = 1
    total += numbers[idx]

    if total == K:
        result += 1

    for i in range(idx, N):
        if not visited[i]:
            check(i, total)
            visited[i] = 0
ans = []
for tc in range(int(input())):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = 0
    visited = [0] * N
    for i in range(N):
        check(i, 0)
    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))