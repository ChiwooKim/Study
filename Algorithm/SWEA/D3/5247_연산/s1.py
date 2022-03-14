import sys
sys.stdin = open('input.txt')

from collections import deque

def calculate(n):
    cnt = 0
    q = deque()
    q.append((n, cnt))
    visited = [0]*1000001
    visited[n] = 1

    while q:
        now, cnt = q.popleft()
        if now == m:
            return cnt

        for i in range(4):
            if i == 0:
                if 0 < now + 1 <= 1000000 and visited[now+1] == 0:
                    visited[now+1] = 1
                    q.append((now+1, cnt+1))

            elif i == 1:
                if 0 < now - 1 <= 1000000 and visited[now-1] == 0:
                    visited[now-1] = 1
                    q.append((now-1, cnt+1))

            elif i == 2:
                if 0 < now * 2 <= 1000000 and visited[now*2] == 0:
                    visited[now*2] = 1
                    q.append((now*2, cnt+1))

            elif i == 3:
                if 0 < now - 10  <= 1000000 and visited[now-10] == 0:
                    visited[now-10] = 1
                    q.append((now-10, cnt+1))

T = int(input())

ans = []
for tc in range(T):
    n, m = map(int, input().split())
    ans.append('#{} {}\n'.format(tc+1, calculate(n)))
print(''.join(ans))