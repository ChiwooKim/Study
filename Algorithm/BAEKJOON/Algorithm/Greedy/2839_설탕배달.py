N = int(input())

result = 0
while True:
    # 5의 배수일 경우 나누고 몫을 더하고 반복문 out!
    if N % 5 == 0:
        result += (N // 5)
        break
    # 5읠 배수가 아닐 경우 3을 빼고 봉지수 +1 후 다시 5의 배수인지 확인 할 수 있도록 한다.
    N -= 3
    result += 1

    # 3kg, 5kg 봉지로 분배를 할 수 없다면 result값을 -1로 하고 반복문 out
    if N < 0:
        result = -1
        break
print(result)