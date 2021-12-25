import sys
sys.stdin = open('input.txt')


T = int(input())
ans = []
for tc in range(T):
    N = int(input())
    numbers = ''

    # 입력받은 수를 하나의 정수열로 만들기(str)
    while len(numbers) != N:
        numbers += input().replace(' ', '')

    # 0부터 차례대로 1씩 더해가며 그 숫자가 정수열의 한 부분인지 찾고 아니면 result로 출력
    result = 0
    while True:
        if str(result) not in numbers:
            break
        result += 1

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))