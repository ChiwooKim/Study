import sys
sys.stdin = open('input.txt')

def work(worker, total):
    global result
    # 가지치기(현재 찾고 있는 경우가 이미 결과값보다 확률이 낮을경우)
    if total <= result:
        return

    # 모든 직원이 다 성공했을 때 확률을 result에 저장
    if visited == [1] * n:
        result = total

    # 직원들을 순회하며 재귀를 통해 최대 확률일 때를 찾아간다.
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            work(worker+1, total * (success[worker][i]/100))
            visited[i] = 0


T = int(input())

for tc in range(T):
    n = int(input())
    success = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    result = 0
    work(0, 1)
    result = result*100
    # 소수점 6번째까지 출력
    print('#{} {:.6f}'.format(tc + 1, result))