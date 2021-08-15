import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    num = int(input())
    result = set()
    n = 1
    cnt = 0
    # 0~9 까지 모든 수가 result 리스트에 들어 가면 반복문 종료
    while len(result) < 10:
        result_number = num * n
        for i in list(str(result_number)):
            result.add(i)
        n += 1
        cnt += 1

    print('#{} {}'.format(_+1, result_number))



