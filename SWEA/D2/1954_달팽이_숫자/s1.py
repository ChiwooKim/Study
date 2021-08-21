import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    num = int(input())
    arr = [[0 for i in range(num)] for j in range(num)] # n*n 배열 생성
    row = -1
    col = 0
    cnt = 1
    moving = 1

    while num > 0:
        for i in range(num): #가로
            row += moving
            arr[col][row] = cnt
            cnt += 1
        num -= 1

        for j in range(num): #세로
            col += moving
            arr[col][row] = cnt
            cnt += 1
        moving *= -1

    print('#{}'.format(_+1))
    for i in arr:
        for j in i:
            print('{} '.format(j), end='')
        print()
