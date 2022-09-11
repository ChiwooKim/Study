import sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for t in range(T):
    result = list(input())
    now = len(result)
    win = result.count('o')

    if win + 15 - now >= 8:
        ans.append('#{} {}\n'.format(t+1, 'YES'))
    else:
        ans.append('#{} {}\n'.format(t+1, 'NO'))

print(''.join(ans))