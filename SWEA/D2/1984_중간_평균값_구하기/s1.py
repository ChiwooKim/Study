import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    numbers = list(map(int, input().split()))
    # 버블소트
    for i in range(len(numbers),0,-1):
        for j in range(i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    # 앞뒤 자르고 평균값ㄴ
    numbers = numbers[1:len(numbers)-1]

    print('#{} {}'.format(_+1, round(sum(numbers)/len(numbers))))
