import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    # A리스트가 길이가 더 짧은 것으로 고정
    if N > M:
        A_list, B_list = B_list, A_list
    result = []
    # A리스트르 B리스트 인덱스 순서에 따라 한번씩 대응했을 때 마주보는 값들을 곱의 합을 구해서 result 리스트 생성
    # 그 중 max 값 반환
    for i in range(len(B_list)-len(A_list)+1):
        result_sum = 0
        for j in range(len(A_list)):
            result_sum += A_list[j] * B_list[i+j]
        result.append(result_sum)

    print('#{} {}'.format(_+1, max(result)))
