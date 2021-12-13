import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    S = set(input())
    result = ''

    if len(S) == 2:
        result = 'Yes'
    else:
        result = 'No'

    print('#{} {}'.format(tc+1, result))