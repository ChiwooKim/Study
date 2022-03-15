import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = float(input())
    a = n
    check = 0
    cnt = 1
    result = ''

    while cnt < 13:
        x = 1*2**(-cnt)
        if a >= x:
            check += x
            a -= x
            result += '1'
        else:
            result += '0'

        if a == 0:
            break

        cnt += 1

    if check == n:
        print('#{} {}'.format(tc+1, result))
    else:
        print('#{} {}'.format(tc+1, 'overflow'))