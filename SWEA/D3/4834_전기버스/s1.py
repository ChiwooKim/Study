import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    K, N, M = map(int,input().split())
    charge_list = list(map(int, input().split())) #충전이 가능한 정류장
    bus_stop = list(range(N+1)) # 정류장

    now = 0 #현위치
    c_cnt = 0 #충전횟수
    result = 0

    while True:
        if now + K >= N:#현재 위치가 정류장일때 종료
            result = c_cnt # 도착시 카운트 된 충전 횟수
            break

        if bus_stop[now + K] in charge_list: #이동한 거리에 충전소가 있으면 카운트
            now += K
            c_cnt +=1
        else: #이동거리 만큼 이동시 없으면 이동거리 이내에 있는 충전소 탐색
            for i in range(K, 0, -1):
                if bus_stop[now+i] in charge_list:
                    now += i
                    c_cnt += 1
                    break
            else: # 도착하지 못했기 때문에 결과값 0을 출력
                result = 0
                break

    print('#{0} {1}'.format(_ + 1, result))










