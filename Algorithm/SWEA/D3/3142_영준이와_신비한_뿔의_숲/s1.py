import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    # n: 뿔의수, m: 짐승의 수
    # 유니콘(1개), 트윈혼(2개) 구하기
    # 연립방정식
    n, m = map(int, input().split())
    x = 2*m - n
    print('#{} {} {}'.format(tc + 1, x, m - x))



