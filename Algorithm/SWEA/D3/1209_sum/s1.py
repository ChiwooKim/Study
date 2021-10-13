import sys
sys.stdin = open('input.txt')

for _1 in range(10): # 10개의 테스트 케이스
    case_num = int(input()) # 케이스 번호
    test_list = [list(map(int, input().split())) for _2 in range(100)]
    result_list = []
    total1 = [] # 행의 합 리스트
    total2 = [] # 열의 합 리스트
    c_cnt = 0 # 대각선의 합 (좌상단에서 우하단 방향의 대각선)
    c_cnt2 = 0 # 위와 반대대는 대각선

    # 각 열들의 합의 최댓값
    for j in range(len(test_list[0])):
        total1.append(sum(test_list[j]))  # test_list 안의 리스트가 각 행이고 sum을 통해 바로 합을 구함
        c_cnt += test_list[j][j]  # 대각선의 좌표는 열과 행의 인덱스가 같음
        c_cnt2 += test_list[j][len(test_list[j]) - 1 - j] # 우상단에서 좌하단으로 가는 대각선
        cnt = 0 # 열의 합 초기화
        for i in range(len(test_list)):
            cnt += test_list[i][j] # 열의 합
        total2. append(cnt)

    result_list = [max(total1), max(total2), c_cnt, c_cnt2]

    print('#{} {}'.format(_1 + 1, max(result_list)))

