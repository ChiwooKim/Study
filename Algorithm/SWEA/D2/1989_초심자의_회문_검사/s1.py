import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    word = input()
    if word[:] == word[::-1]:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(_+1, result))