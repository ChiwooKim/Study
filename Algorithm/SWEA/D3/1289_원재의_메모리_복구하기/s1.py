import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    num = input()
    result = 0
    check = 0

    for i in num:
        if i != str(check):
            result += 1
            check = abs(check-1)

    print('#{} {}'.format(tc+1, result))
