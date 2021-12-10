import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    # 월(0), 화(1), 수(2), 목(3), 금(4), 토(5), 일(6)
    # 1월 1일은 금요일(4)
    month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
             7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    m, d = map(int, input().split())

    day = 0
    # 2월부터 전 달까지 일 수 체크
    # 1월이면 바로 d = day
    if m == 1:
        day = d - 1
    else:
        for i in range(1, m):
            day += month[i]
        day += (d-1)

    result = (day + 4) % 7

    print('#{} {}'.format(tc+1, result))
