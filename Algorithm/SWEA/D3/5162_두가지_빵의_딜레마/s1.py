import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    A, B, C = map(int, input().split())

    result = []

    for i in range(C//A + 1):
        temp = i
        temp += (C-(A * i)) // B
        result.append(temp)

    print('#{} {}'.format(tc+1, max(result)))

