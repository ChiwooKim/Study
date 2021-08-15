import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    result = 0
    num = int(input())
    for i in range(1,num+1):
        if i % 2:
            result += i
        else:
            result -= i
    print('#{} {}'.format(_+1, result))