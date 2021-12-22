import sys
sys.stdin = open('input.txt')

ans = []
for tc in range(int(input())):
    day = input()

    if day == 'SUN':
        result = 7
    elif day == 'MON':
        result = 6
    elif day == 'TUE':
        result = 5
    elif day == 'WED':
        result = 4
    elif day == 'THU':
        result = 3
    elif day == 'FRI':
        result = 2
    elif day == 'SAT':
        result = 1

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))