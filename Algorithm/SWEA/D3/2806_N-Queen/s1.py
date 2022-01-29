import sys
sys.stdin = open('input.txt', 'r')

def check(x, y):
    for i in range(x):
        if x - i == abs(y-position[i]):
            return False
    return True

def n_queen(cnt = 0):
    global result
    # 퀸이 모두 올려졌을 경우 경우의 수 +1
    if cnt == N:
        result += 1
        return

    for i in range(N):
        if visited[i] == 0 and check(cnt, i):
            visited[i] = 1
            position[cnt] = i
            n_queen(cnt + 1)
            visited[i] = 0

ans = []
for tc in range(int(input())):
    N = int(input())
    position = [0] * N # 인덱스는 행, 숫자는 열의 위치좌표를 나타낸다.
    visited = [0] * N
    result = 0
    n_queen()
    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))
