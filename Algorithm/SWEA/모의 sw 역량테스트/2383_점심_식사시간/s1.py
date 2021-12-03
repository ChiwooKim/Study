import sys
sys.stdin = open('input.txt')

from itertools import product

def check(temp0, temp1):
    temp0 = temp0
    temp1 = temp1
    stairs0_last = 0
    stairs1_last = 0

    if len(temp0) > 3:
        for i in range(3, len(temp0)):
            if temp0[i-3]+stairs0[1] > temp0[i]:
                temp0[i] = temp0[i-3]+stairs0[1]
    if len(temp1) > 3:
        for i in range(3, len(temp1)):
            if temp1[i-3]+stairs1[1] > temp1[i]:
                temp1[i] = temp1[i-3]+stairs1[1]

    if temp0:
        stairs0_last = temp0[-1] + stairs0[1]
    if temp1:
        stairs1_last = temp1[-1] + stairs1[1]

    if stairs0_last == 0:
        return stairs1_last
    elif stairs1_last == 0:
        return stairs0_last
    else:
        if stairs0_last >= stairs1_last:
            return stairs0_last
        else:
            return stairs1_last


def down_stairs(now, case):
    global result
    temp0 = []   # stairs0로 간 사람들 데이터 저장
    temp1 = []   # stairs1로 간 사람들 데이터 저장

    # 계단도착 => 대기까지의 시간을 계단 별로 정리
    for i in range(len(case)):
        if case[i] == 0:
            temp0.append(abs(now[i][0][0]-stairs0[0][0])+abs(now[i][0][1]-stairs0[0][1]) + 1)
        else:
            temp1.append(abs(now[i][0][0] - stairs1[0][0]) + abs(now[i][0][1] - stairs1[0][1]) + 1)


    # 계단 내려가기(계단은 최대 3명 내려갈 수 있음)
    # ex) 첫번째가 도착 후 시간이 네번째가 대기하는 시간보다 크면 네번째는 출발하지 못한다.
    temp0.sort()
    temp1.sort()
    t = check(temp0, temp1)
    if result > t:
        result = t


T = int(input())

for tc in range(T):
    N = int(input())   # N*N
    room = [list(map(int, input().split())) for _ in range(N)]
    now = []  # [시작위치, 시간]
    stairs0 = []   # [계단위치, 계단길이]
    stairs1 = []
    result = 987654321

    # 계단 및 사람들 좌표 찾기
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                now.append([(i, j), 0])
            elif room[i][j] not in [0, 1]:
                if not stairs0:
                    stairs0 = [(i, j), room[i][j]]
                else:
                    stairs1 = [(i, j), room[i][j]]

    # 완전탐색하여 계단 선택하기
    for i in product(range(2), repeat=len(now)):
        down_stairs(now, i)

    print('#{} {}'.format(tc+1, result))
