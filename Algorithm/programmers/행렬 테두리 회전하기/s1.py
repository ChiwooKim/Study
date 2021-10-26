import sys
sys.stdin = open('input.txt')

def rotation(q, temp):
    a, b, c, d = q
    check = 0              # while문 check
    row = b - 2            # 행표
    col = a - 1            # 열좌표
    moving = 1             # 방향전환
    fst = temp[a][b - 1]   # 현 좌표에서 바로 전 좌표의 값
    num1 = d - b + 1       # 움직여야할 가로길이
    num2 = c - a           # 움직여야할 세로길이
    ans = []               # 시계 방향 돌면서 지나간 곳들의 숫자 저장
    while check < 2:
        # 가로방향
        for i in range(num1):
            row += moving
            snd = temp[col][row]  # 다음에 새겨야 할 자리의 숫자가 현재 위치기 때문에 현위치 숫자 변환 전 저장
            temp[col][row] = fst  # 현위치 숫자 이전 좌표의 숫자로 저장
            ans.append(fst)       # 지나간 곳 숫자 담기
            fst = snd             # 다음 지점을 위해 현좌표였던 숫자 다시 바꿔주기
        num1 -= 1
        # 세로방향
        for j in range(num2):
            col += moving
            snd = temp[col][row]
            temp[col][row] = fst
            ans.append(fst)
            fst = snd
        num2 -= 1
        moving *= -1             # 방향전환
        check += 1
    return min(ans), temp


def solution(rows, columns, queries):
    answer = []
    temp = [[0] * columns for _ in range(rows)]
    cnt = 1

    for i in range(rows):
        for j in range(columns):
            temp[i][j] = cnt
            cnt += 1

    for i in queries:
        ans, temp = rotation(i, temp)
        answer.append(ans)
    return answer


T = int(input())

for tc in range(1):
    rows, columns = map(int, input().split())
    queries = []
    for _ in range(3):
        queries.append(list(map(int, input().split())))

    print(solution(rows, columns, queries))