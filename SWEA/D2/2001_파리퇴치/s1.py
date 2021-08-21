import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    kill_list = []
    # 좌표마다 파리수가 있는 배열
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            #죽이는 범위 안에서 각 좌표의 죽인 파리수 합
            for k in range(M):
                for l in range(M):
                    kill += fly_list[i+k][j+l]
            kill_list.append(kill)
    # 1타에 가장 많이 죽였을 때 킬값 반환
    print('#{} {}'.format(_+1, max(kill_list)))


