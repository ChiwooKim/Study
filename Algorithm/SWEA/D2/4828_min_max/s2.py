import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    num = int(input())
    numbers = list(map(int, input().split()))

    # 선택 정렬
    for i in range(num-1):
        min_idx = i
        for j in range(i+1, num):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    result = numbers[num - 1] - numbers[0]

    print('#{0} {1}'.format(_ + 1, result))

