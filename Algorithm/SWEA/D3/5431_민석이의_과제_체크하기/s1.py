import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    result = []   # 제출하지 않은 사람

    for i in range(1, N+1):
        if i not in submit:
            result.append(i)

    print('#{}'.format(tc+1), end=' ')
    print(*result)