import sys
sys.stdin = open('input.txt')

def make_group():
    visited = [0] * (n+1)
    for i in range(m):
        stack = [numbers[i*2]]
        while stack:
            t = stack.pop()
            if visited[t] == 0:
                check[i].append(t)
                visited[t] = 1
                if t in num_dict:
                    stack.extend(num_dict[t])

T = int(input())

ans = []
for tc in range(T):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    num_dict = {}

    for i in range(0, m*2, 2):
        if numbers[i] not in num_dict:
            num_dict[numbers[i]] = [numbers[i+1]]
        else:
            num_dict[numbers[i]] += [numbers[i + 1]]
        if numbers[i+1] not in num_dict:
            num_dict[numbers[i+1]] = [numbers[i]]
        else:
            num_dict[numbers[i+1]] += [numbers[i]]

    check = [[] for _ in range(m)]
    make_group()
    cnt = 0
    used = []
    for i in check:
        if i:
            cnt += 1
            used.extend(i)

    for i in range(1, n+1):
        if not i in used:
            cnt += 1

    ans.append('#{} {}\n'.format(tc+1, cnt))
print(''.join(ans))