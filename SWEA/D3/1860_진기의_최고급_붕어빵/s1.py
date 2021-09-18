import sys
sys.stdin = open('input.txt')



T = int(input())

for _ in range(T):
    n, m, k = map(int, input().split())
    # m초 동안 k 개의 붕어빵 제작
    # n개의 정수
    waiting = list(map(int, input().split()))
    result = 'Possible'
    waiting.sort()
    cnt = 0
    for i in waiting:

        if i < m:
            result = 'Impossible'

    print('#{} {}'.format(_+1, result))