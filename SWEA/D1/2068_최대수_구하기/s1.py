import sys
sys.stdin = open('input.txt')

T =int(input())

for _ in range(T):
    num_list = list(map(int, input().split()))
    # 입력받은 수 중 큰수 찾기
    max_number = 0
    for i in num_list:
        if max_number < i:
            max_number = i

    print('#{} {}'.format(_+1, max_number))