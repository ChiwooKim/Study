import sys
sys.stdin = open('input.txt')

def tree(x):
    if x > n:
        return 0
    if tr[x]:
        return tr[x]
    tr[x] = tree(x*2) + tree(x*2+1)
    return tr[x]

T = int(input())

ans = []
for tc in range(T):
    n, m, l = map(int, input().split())
    tr = [0]*(n+1)

    for _ in range(m):
        x = list(map(int, input().split()))
        tr[x[0]] = x[1]
    result = tree(l)
    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))
