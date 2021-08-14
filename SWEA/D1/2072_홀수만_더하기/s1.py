import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    result = 0
    num = list(map(int, input().split()))
    for i in num:
        if i%2:
            result += i
    print('#{} {}'.format(_+1, result))