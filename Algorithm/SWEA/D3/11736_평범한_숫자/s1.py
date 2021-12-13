import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0
    # 리스트내의 값이 최소값, 최대값이 아닌 i-1, i, i+1 중 최대, 최소가 아닌 값이 되면 되는 것이다.
    for i in range(1, N-1):
        if numbers[i-1] < numbers[i] < numbers[i+1] or numbers[i-1] > numbers[i] > numbers[i+1]:
            result += 1

    print('#{} {}'.format(tc+1, result))