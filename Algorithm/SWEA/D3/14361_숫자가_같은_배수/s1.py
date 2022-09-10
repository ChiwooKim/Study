from itertools import permutations
import sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for t in range(T):
    N = input()
    number = list(N)
    N = int(N)
    number.sort(reverse=True)

    flag = True
    for num in permutations(number, len(number)):
        n = int(''.join(num))
        if n <= N:
            break
        if n % N == 0:
            ans.append('#{} {}\n'.format(t+1, 'possible'))
            flag = False
            break

    if flag:
        ans.append('#{} {}\n'.format(t+1, 'impossible'))

print(''.join(ans))