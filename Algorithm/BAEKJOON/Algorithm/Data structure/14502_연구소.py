import copy
# 조합으로 벽 설치할 좌표 지정
def combination(wall):
    if wall == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                combination(wall+1)
                lab[i][j] = 0


# bfs로 바이러스 퍼트리기
def virus():
    global result
    q = []
    virus_lab = copy.deepcopy(lab)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 바이러스 시발점 찾기
    for i in range(n):
        for j in range(m):
            if virus_lab[i][j] == 2:
                q.append([i, j])
    # 바이러스 퍼트리기
    while q:
        start = q.pop(0)
        for k in range(4):
            i, j = start[0]+dy[k], start[1]+dx[k]
            if 0 <= i <= n-1 and 0 <= j <= m-1 and virus_lab[i][j] == 0:
                q.append([i, j])
                virus_lab[i][j] = 2
    # 퍼지지 않은 지역 세기
    cnt = 0
    for i in virus_lab:
        cnt += i.count(0)

    # 안전지역이 많은 곳을 result로 대체
    if cnt > result:
        result = cnt


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
result = 0
combination(0)
print(result)


