import sys
sys.stdin = open("input.txt")

ans = []
for tc in range(int(input())):
    n = input()

    # 한 자리 수가 될 때까지 반복
    while True:
        result = 0

        # 각 자리수 더하기
        for i in n:
            result += int(i)

        # 각 자리 수가 더한 값이 한 자리 수인지 확인 하기
        if result < 10:
            break
        else:
            n = str(result)

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))