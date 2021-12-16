import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    A, B = map(int, input().split())
    result = 0

    for i in range(A//B):
        result += 2*i + 1

    print('#{} {}'.format(tc+1, result))