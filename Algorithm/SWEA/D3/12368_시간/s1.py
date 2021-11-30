import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    a, b = map(int, input().split())

    result = (a+b) % 24  # 24시가 0시가 되어야함

    print('#{} {}'.format(tc+1, result))
