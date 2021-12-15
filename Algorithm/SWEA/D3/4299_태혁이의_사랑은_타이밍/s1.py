import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # 깨닳음을 얻은 시간 - 약속시간
    D, H, M = map(lambda x: int(x)-11, input().split())
    result = D * 24 * 60 + H * 60 + M
    print('#{}'.format(tc + 1), end=' ')
    if result >= 0:
        print(result)
    else:
        print(-1)



