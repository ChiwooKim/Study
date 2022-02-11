import sys
sys.stdin = open('input.txt')

def in_order(n):
    global result
    if n:
        in_order(left[n])
        result += parent[n]
        in_order(right[n])

ans = []
for tc in range(1,11):
    n = int(input())
    tree = [list(input().split()) for _ in range(n)]
    parent = [0]*(n+1)
    left = [0]*(n+1)
    right = [0]*(n+1)
    for baby in tree:
        parent[int(baby[0])] = baby[1]
        if len(baby) > 2:
            left[int(baby[0])] = int(baby[2])
        if len(baby) > 3:
            right[int(baby[0])] = int(baby[3])
    result = ''
    in_order(1)
    ans.append('#{} {}\n'.format(tc, result))
print(''.join(ans))