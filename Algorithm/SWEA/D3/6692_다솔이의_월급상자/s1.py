import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    result = 0

    for i in range(N):
        p, x = map(float, input().split())
        result += p * x

    print('#{} {:.6f}'.format(tc+1, result))
