import sys
sys.stdin = open('input.txt')

from itertools import combinations, permutations

def search(pick):
    total = 0
    # 맛 조합 찾기
    for i in permutations(pick, 2):
        print(i)
        total += flavor[i[0]][i[1]]
    return total

T = int(input())

for tc in range(2):
    n = int(input())
    flavor = [list(map(int, input().split())) for _ in range(n)]
    result = []

    # 식재료 경우의 수 찾기
    for i in combinations(range(n), n//2):
        A = list(i)
        B = []
        for j in range(n):
            if j not in A:
                B.append(j)
        result.append(abs(search(A) - search(B)))
    print('#{} {}'.format(tc+1, min(result)))
