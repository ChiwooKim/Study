import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    result = 0

    for i in range(K):
        result += score[i]

    print('#{} {}'.format(tc+1, result))
