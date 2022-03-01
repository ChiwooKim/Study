import sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for tc in range(T):
    # n: 심사대 수, m: 사람 수
    n, m = map(int, input().split())
    immigration = []

    for i in range(n):
        immigration.append(int(input()))
    result = 0
    # 가장 오래 걸리는 심사대에서 모두 입국 심사 할 때 걸리는 시간
    # 가장 오래 걸리는 시간을 구하기 위함
    end = max(immigration) * m
    start = 0

    # Binary Search
    # 중앙값(시간: mid)을 구한 후 각 심사대에서 해당 시간동안 심사대에서 처리하는 사람의 수를 구한 후 더한다.
    # 더한 값을 m(사람수)과 비교 후 Binary Search 반복 진행
    # 최종적으로 check(각 심사대에서 처리하는 사람수의 합)와 m이 같아진다면 while문 out(start>end가 되기 때문)
    while start <= end:
        mid = (start + end) // 2
        check = 0
        for i in immigration:
            check += mid // i  # mid만큼의 시간동안 심사대에서 처리하는 사람의 수

        if check >= m:
            result = mid
            end = mid - 1

        elif check < m:
            start = mid + 1

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))