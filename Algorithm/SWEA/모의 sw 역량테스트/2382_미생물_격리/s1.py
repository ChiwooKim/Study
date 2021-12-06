import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())
    microbe = []   # 미생물 군집 정보 저장
    # [y, x, 개체수, 방향]
    for i in range(K):
        a, b, m, p = map(int, input().split())
        microbe.append([a, b, m, p-1])

    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # M시간 동안 이동 후 결과찾기
    time = 1
    while time <= M:
        # 이동하기
        for micro in microbe:
            micro[0] = micro[0] + dy[micro[3]]
            micro[1] = micro[1] + dx[micro[3]]
            # 이동한 좌표들이 약품좌표에 있는지 확인하기
            # 약품위에 있다면 개체수 절반(나머지는 버림)
            if micro[0] == 0 or micro[1] == 0 or micro[0] == N-1 or micro[1] == N-1:
                # 개체수 줄이기
                micro[2] = micro[2] // 2
                # 방향 전환
                if micro[3] == 0 or micro[3] == 1:
                    micro[3] = 1 - micro[3]
                else:
                    micro[3] = 5 - micro[3]
        # 개체수가 많은 순으로 내림차순으로 정렬
        microbe.sort(key=lambda x: x[2], reverse=True)

        # 위치에 대한 자료를 dict로 변환
        # dict로 변환시 좌표를 key로 지정하여 동일한 좌표의 개체는 모두 더한다.
        # 개체수 기준으로 내림차순으로 정렬 했기 때문에 합쳐질 때 방향 고려없이
        # for문을 실행할 때 첫 key,value 생성때 방향을 넣어 주면 된다.

        position = {}
        for temp in microbe:
            if (temp[0], temp[1]) not in position:
                position[(temp[0], temp[1])] = temp
            else:
                position[(temp[0], temp[1])][2] += temp[2]

        # 다시 리스트로 전환
        temp_microbe = []
        for temp in position.values():
            temp_microbe.append(temp)

        microbe = temp_microbe
        time += 1

    # 개체수 총합
    result = 0
    for i in microbe:
        result += i[2]

    print('#{} {}'.format(tc+1, result))










