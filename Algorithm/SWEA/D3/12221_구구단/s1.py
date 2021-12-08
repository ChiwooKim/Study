import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    result = 0

    if A > 9 or B > 9:
        result = -1
    else:
        result = A * B

    print('#{} {}'.format(tc+1, result))