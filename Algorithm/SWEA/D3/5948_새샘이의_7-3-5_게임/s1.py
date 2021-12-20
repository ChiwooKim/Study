import sys
sys.stdin = open('input.txt')

from itertools import combinations

for tc in range(int(input())):
    numbers = list(map(int, input().split()))
    result = set()
    # 모든 경우의 수를 구한 후 합한 값들을 결과에 담는다(set으로 중복제거)
    for i in combinations(numbers, 3):
        result.add(sum(i))
    # 큰 수 에서 5번째를 뽑기 위해 set을 list로 바꾼 후 정렬
    result = sorted(list(result))

    print('#{} {}'.format(tc+1, result[-5]))