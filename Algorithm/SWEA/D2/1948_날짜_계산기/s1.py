import sys
sys.stdin = open('input.txt')

T = int(input())
calender = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30,'12': 31}
for _ in range(T):
    mon1, day1, mon2, day2 = map(int, input().split())
    # 몇 일째이니까 첫날도 포함되어서 +1
    result = day2 - day1+1

    for i in range(mon1, mon2):
        result += calender.get(str(i))

    print('#{} {}'.format(_+1, result))
