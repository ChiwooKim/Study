import sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for tc in range(T):
    n, m = map(int, input().split())
    c_weight = sorted(list(map(int, input().split())), reverse=True)
    t_weight = sorted(list(map(int, input().split())), reverse=True)
    result = 0
    cnt = 0

    for i in range(len(t_weight)):
        for j in range(cnt, len(c_weight)):
            if t_weight[i] >= c_weight[j]:
                result += c_weight[j]
                cnt = j+1
                break

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))
