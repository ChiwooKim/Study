import sys
sys.stdin = open('input.txt')

T = int(input())

for k in range(T):
    num, Q = map(int, input().split())
    result = [0]*num
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            result[j] = i+1

    print('#{}'.format(k + 1), end=' ')
    print(*result)
