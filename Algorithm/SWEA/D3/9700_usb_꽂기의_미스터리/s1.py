import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    p, q = map(float, input().split())


    # 뒤집어진면*(올바른면*정상적 꽂힘)
    s1 = (1-p) * q
    # 2번 뒤집었을 때 꽂힘
    # 시작이 올바른면일 때
    s2 = p * (1-q) * q

    if s1 < s2:
        print('#{} {}'.format(tc+1, 'YES'))
    else:
        print('#{} {}'.format(tc+1, 'NO'))