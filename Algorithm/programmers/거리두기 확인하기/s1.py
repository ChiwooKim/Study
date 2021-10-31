import sys
sys.stdin = open('input.txt')

'''
응시자: p, 테이블: o, 파티션: x
거리두기를 지켰다면 1, 아니면 0을 return 
행렬 (r1, c1), (r2, c2)
맨해튼 거리 =  |r1 - r2| + |c1 - c2| <= 2는 거리두기를 지키지 않은 것
'''
from itertools import combinations


def check_distance(place):
    result = 1
    check = []
    # 배열로 만들기
    for i in place:
        check.append(list(i))

    # 사람위치 찾기
    now = []
    for i in range(5):
        for j in range(5):
            if check[i][j] == 'P':
                now.append([i, j])

    # 사람 사이의 맨해튼 거리를 찾는다(combination으로 경우의 수를 모두 확인)
    # 만족하면 pass 만족하지 않으면 그 사이에 파티션이 있는지 확인
    # 있다면 pass 아니면 return 0
    for com in combinations(range(len(now)), 2):
        # 거리조건 체크
        a, b = com[0], com[1]
        c = now[a][0] - now[b][0]  # X좌표 거리
        d = now[a][1] - now[b][1]  # Y좌표 거리

        if abs(c) + abs(d) <= 2:
            # 파티션 있는지 확인
            if abs(c) == 2:
                if now[a][0] - now[b][0] > 0:
                    if check[now[b][0] + 1][now[a][1]] != 'X':
                        return 0
                elif now[a][0] - now[b][0] < 0:
                    if check[now[a][0] + 1][now[a][1]] != 'X':
                        return 0
            elif abs(d) == 2:
                if now[a][1] - now[b][1] > 0:
                    if check[now[a][0]][now[b][1] + 1] != 'X':
                        return 0
                elif now[a][1] - now[b][1] < 0:
                    if check[now[a][0]][now[a][1] + 1] != 'X':
                        return 0
            elif abs(c) + abs(d) == 1:
                return 0

            else:
                if c < 0 and d < 0:
                    if check[now[a][0] + 1][now[a][1]] != 'X' or check[now[a][0]][now[a][1] + 1] != 'X':
                        return 0
                elif c < 0 and d > 0:
                    if check[now[a][0] + 1][now[a][1]] != 'X' or check[now[a][0]][now[a][1] - 1] != 'X':
                        return 0
                elif c > 0 and d < 0:
                    if check[now[a][0] - 1][now[a][1]] != 'X' or check[now[a][0]][now[a][1] + 1] != 'X':
                        return 0
                elif c > 0 and d > 0:
                    if check[now[a][0] - 1][now[a][1]] != 'X' or check[now[a][0]][now[a][1] - 1] != 'X':
                        return 0

    return result


def solution(places):
    answer = []
    for i in places:
        answer.append(check_distance(i))

    return answer

places = []
for _ in range(5):
    places.append(list(input().split()))
print(solution(places))

