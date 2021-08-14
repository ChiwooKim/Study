import sys
sys.stdin = open('input.txt')

num = int(input())

for _ in range(num):
    a, b = map(int, input().split())

    print('#{} {} {}'.format(_+1, a//b, a%b))


