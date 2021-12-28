import sys
sys.stdin = open('input.txt')

ans = []
for tc in range(int(input())):
    a, b, c, d = map(int, input().split())

    result = 'DRAW'

    if a/b > c/d:
        result = 'ALICE'
    elif a/b < c/d:
        result = 'BOB'

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))