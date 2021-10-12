import sys
sys.stdin = open('input.txt')
'''
NxN의 모든 좌표에서 1씩 증가하는 곳을 찾아가기엔 N이 커지면 중복된곳도 여러번 탐색해야한다.
예를들어 1부터 시작해서 2, 3, 4, 5 순으로 찾았다면 2,3,4,5의 좌표에서는 어차피 찾아도 5가 종착지 이기 때문에 굳이 다시 체크할 필요가 없다.
따라서 최대 길이를 체크했다면 그 과정에서 거쳐간 수들은 스킵 할 수 있도록 함. 
'''
T = int(input())

for tc in range(T):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*(N**2 + 1) # 지나치는 구간 체크

    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if check[numbers[i][j]]:
                continue
            else:
                while True:
                    for k in range(4):
                        y = i + dy[k]
                        x = j + dx[k]
                        if 0 <= y < N and 0 <= x < N and numbers[y][x] == numbers[i][j] + 1:
                            check[numbers[i][j]] = 1
                            break
                    if check[numbers[i][j]] == 1:
                        i = y
                        j = x
                    else:
                        break


    # 연속된 1의 개수 카운트하기(=방 이동 횟수)
    result = 0
    cnt = 0
    room = 0
    for i in range(1, N**2+1):
        if check[i]:
            cnt += 1
        else:
            if cnt > result:
                result = cnt
                room = i - cnt
            cnt = 0
    # 방의 개수는 이동횟수보다 1개 더 많기 때문에 result+1을 해줘야한다.
    print('#{} {} {}'.format(tc+1, room, result+1))



