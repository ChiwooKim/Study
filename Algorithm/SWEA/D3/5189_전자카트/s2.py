import sys
sys.stdin = open('input.txt')

from itertools import permutations

T = int(input())

ans = []
for tc in range(T):
    n = int(input())
    battery = [[0]*(n+1)] + [([0]+list(map(int, input().split()))) for _ in range(n)]
    numbers = []
    result = []

    for i in range(2, n+1):
        numbers.append(i)

    for i in permutations(numbers, n-1):
        temp = [1] + list(i) + [1]
        total = 0
        for j in range(1, n+1):
            total += battery[temp[j-1]][temp[j]]
        result.append(total)

    ans('#{} {}\n'.format(tc+1, min(result)))
print(''.join(ans))