import sys
sys.stdin = open('input.txt')

def make(idx, score, total):
    global result
    selected[idx] = 1
    score += ingredients[idx][0]
    total += ingredients[idx][1]

    # 총칼로리 <= 제한칼로리
    if total > L:
        return
    # 누적인기 합이 크면 result가 인기합으로 대체
    if score > result:
        result = score

    # 다음재료 찾기(재귀)
    for i in range(idx, N):
        if not selected[i]:
            make(i, score, total)
            selected[i] = 0


ans = []
for tc in range(int(input())):
    # N: 재료의 수, L: 제한 칼로리
    N, L = map(int, input().split())
    # [점수, 칼로리]
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    selected = [0] * N
    for i in range(N):
        make(i, 0, 0)

    ans.append('#{} {}\n'.format(tc + 1, result))
print(''.join(ans))