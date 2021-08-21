import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    cnt_list = [0] * 101
    num = int(input())
    scores = list(map(int, input().split()))
    # 각 점수가 몇 번인지 카운트
    for i in scores:
        cnt_list[i] += 1

    max_cnt = 0

    # 가장 큰 카운트 찾기
    for i in range(101):
        if cnt_list[i] > max_cnt:
            max_cnt = cnt_list[i]

    # 카운트된 수가 가장 큰것 중 점수가 높은 것을 찾기 위해 뒤에서 부터 조사
    for i in range(100, -1, -1):
        if cnt_list[i] == max_cnt:
            print('#{} {}'.format(_+1, i))
            break
