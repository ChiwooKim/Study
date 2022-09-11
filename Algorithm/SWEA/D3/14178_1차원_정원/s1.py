import math, sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for t in range(T):
    N, D = map(int, input().split())
    x = 2 * D + 1
    ans.append('#{} {}\n'.format(t+1, math.ceil(N/x)))

print(''.join(ans))