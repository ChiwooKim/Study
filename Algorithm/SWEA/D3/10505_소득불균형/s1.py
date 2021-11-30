import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    money = list(map(int, input().split()))

    # 평균 소득 계산
    avg = sum(money) / n

    result = []

    for i in money:
        if i <= avg:
            result.append(i)

    print('#{} {}'.format(tc+1, len(result)))