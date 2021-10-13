import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    a_h, a_m, b_h, b_m = map(int, input().split())
    hour = a_h + b_h
    min = a_m + b_m

    if hour > 12:
        hour -= 12

    if min >= 60:
         min -= 60
         hour += 1

    print('#{} {} {}'.format(_+1, hour, min))