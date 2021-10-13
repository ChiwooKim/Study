import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    if a < b:
        print('#{} <'.format(_+1))
    elif a == b:
        print('#{} ='.format(_ + 1))
    else:
        print('#{} >'.format(_ + 1))