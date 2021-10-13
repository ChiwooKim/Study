import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(T):
    n, m = map(int, input().split()) # 세로크기: n, 가로크기: m
    secret = [list(input()) for _ in range(n)]
    result = 0
    check = ''

    # 암호코드의 각 숫자
    password_code = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    # 암호코드 스캔
    cnt = 0
    for i in range(n):
        for j in range(m-1, m-57, -1):
            if secret[i][j] == '1':
                while cnt < 56:
                    check += secret[i][j]
                    cnt += 1
                    j -= 1
            if cnt:
                break
        if cnt:
            break

    check = check[::-1]
    # 암호코드 숫자로 만들기
    code = []
    for i in range(0, 56, 7):
        code.append(password_code[check[i:i+7]])


    # 올바른 암호인지 확인
    for i in range(8):
        if i % 2:
            result += code[i]
        else:
            result += (code[i] * 3)

    if result % 10:
        print('#{} {}'.format(tc+1, 0))
    else:
        print('#{} {}'.format(tc + 1, sum(code)))




