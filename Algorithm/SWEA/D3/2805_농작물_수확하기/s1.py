import sys
sys.stdin = open('input.txt')

'''
수익 = n**2(마름모 범위)
'''

T = int(input())

for tc in range(T):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    result = 0
    line = 0
    center = N//2
    plus = 0

    while True:
        for k in range(center-plus, center+1+plus):
            result += farm[line][k]

        line += 1
        if line <= center:
            plus += 1
        elif line == N:
            break
        else:
            plus -= 1


    print('#{} {}'.format(tc+1, result))

