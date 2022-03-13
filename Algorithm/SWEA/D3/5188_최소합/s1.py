import sys
sys.stdin = open('input.txt')

def search():
    global result

    # 델타 탐색(하,우)
    dy = [1, 0]
    dx = [0, 1]
    stack = [[0, 0, numbers[0][0]]] # [y,x,now]

    while stack:
        s = stack.pop()
        for k in range(2):
            i = s[0] + dy[k]
            j = s[1] + dx[k]
            if i < n and j < n:
                now = s[2] + numbers[i][j]
                if i == n-1 and j == n-1:
                    if now < result:
                        result = now
                else:
                    stack.append([i, j, now])


T = int(input())

ans = []
for tc in range(T):
    n = int(input())
    numbers = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in numbers:
        result += sum(i)
    search()

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))