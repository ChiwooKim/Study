import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    words = input()
    result = []

    for i in words:
        if i in result:
            result.remove(i)
        else:
            result.append(i)
    if result:
        result.sort()
        print('#{} {}'.format(tc+1, ''.join(result)))
    else:
        print('#{} Good'.format(tc + 1))
