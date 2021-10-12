import sys
sys.stdin = open('input.txt')

def search(i, j, temp):
    temp += numbers[i][j]
    if len(temp) == 7:
        result.add(temp)
        return
    for k in range(4):
        y = dy[k] + i
        x = dx[k] + j
        if 0 <= x < 4 and 0 <= y < 4:
            search(y, x, temp)



T = int(input())

for tc in range(T):
    numbers = [list(input().split()) for i in range(4)]
    result = set()

    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(4):
        for j in range(4):
            temp = ''
            search(i, j, temp)

    print('#{} {}'.format(tc+1, len(result)))