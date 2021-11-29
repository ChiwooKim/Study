import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    words = input()
    check = ['a', 'e', 'i', 'o', 'u']   #모음
    result = ''

    for i in words:
        if i not in check:
            result += i

    print('#{} {}'.format(tc+1, result))