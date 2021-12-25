import sys
sys.stdin = open('input.txt')

ans = []
for tc in range(int(input())):
    D, A, B, F = map(int, input().split())

    result = D * F / (B + A)

    ans.append('#{} {:.6f}\n'.format(tc+1, result))
print(''.join(ans))