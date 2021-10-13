import  sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    # 편의를 위해 좌우 [0]추가해 줌
    n_list = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    # k만큼의 1이 나오고 좌우 0으로 하여 쉽게 찾기 위함
    k_list = [0] + [1]*k + [0]
    cnt = 0
    # 열 방향을 행으로 전환하여 계산을 쉽게하기 위함
    col_list = list(map(list, zip(*n_list)))
    cp = []
    for i in col_list:
        cp.append([0] + i + [0])

    # 가로줄 확인, 원하는게 있다면 카운트
    for i in range(len(n_list)):
        for j in range(len(n_list[i])-len(k_list)+1):
            if n_list[i][j:j+len(k_list)] == k_list:
                cnt += 1

    # 세로줄 확인
    for i in range(len(cp)):
        for j in range(len(cp[i])-len(k_list)+1):
            if cp[i][j:j+len(k_list)] == k_list:
                cnt += 1

    print('#{} {}'.format(_+1, cnt))


