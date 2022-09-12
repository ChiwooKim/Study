import sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for t in range(T):
    log_length = int(input())

    if log_length % 2:
        ans.append('#{} {}\n'.format(t+1, 'Bob'))
    else:
        ans.append('#{} {}\n'.format(t+1, 'Alice'))

print(''.join(ans))