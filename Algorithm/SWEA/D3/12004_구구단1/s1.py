import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    result = 'No'
    for i in range(1, 10):
        a = N // i
        if a < 10 and a * i == N:
            result = 'Yes'
            break

    print('#{} {}'.format(tc+1, result))
