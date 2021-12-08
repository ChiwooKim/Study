import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    number = int(input())
    result = ''
    # 2로 나누었을 때 나머지가 있으면 홀수 없으면 짝수
    if number % 2:
        result = 'Odd'
    else:
        result = 'Even'

    print('#{} {}'.format(tc+1, result))