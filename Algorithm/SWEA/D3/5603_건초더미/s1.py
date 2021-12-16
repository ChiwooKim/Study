import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    hay = list(int(input()) for _ in range(N))
    avg = sum(hay) // N

    result = 0
    for i in hay:
        if i < avg:
            result += (avg - i)

    print('#{} {}'.format(tc+1, result))