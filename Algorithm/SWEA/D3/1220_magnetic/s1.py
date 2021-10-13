import sys
sys.stdin = open('input.txt')

for tc in range(10):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    # n극이 내려오면서 파란색을 만나면 교착, 아니면 out!
    for j in range(n):
        for i in range(n):
            if table[j][i] == 1:
                cnt = 1
                while j + cnt <= 99:
                    if table[j+cnt][i] == 1:
                        break
                    if table[j+cnt][i] == 2:
                        result +=1
                        break
                    cnt +=1
    print('#{} {}'.format(tc+1, result))



