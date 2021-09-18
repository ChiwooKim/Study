import sys
sys.stdin = open('input.txt')

def omok_check(omok,n):
    res = 0
    # 아래, 우측, 대각(좌하, 우하) 확인
    for i in range(n-4):
        check1 = []
        check2 = []
        for j in range(5):
            check1.append(omok[i+j][i+j])
            check2.append(omok[i+j][i+4-j])
        if ('.' not in check1) or ('.' not in check2):
            res = 1
            return res

    for i in range(n):
        for j in range(n-4):
            check3 = []
            check4 = []
            for k in range(5):
                check3.append(omok[i][j+k])
                check4.append(omok[j+k][i])
            if ('.' not in check3) or ('.' not in check4):
                res = 1
                return res
    return res

T = int(input())

for tc in range(T):
    n = int(input())
    omok = [list(input()) for _ in range(n)]
    result = omok_check(omok, n)
    if result == 0:
        print('#{} NO'.format(tc + 1))
    else:
        print('#{} YES'.format(tc + 1))