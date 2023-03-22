import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())    # 동전의 가지수
    coins = list(map(int, input().split()))    # 동전
    m = int(input())    # 금액

    dp = [1] + [0] * m    # dp

    for coin in coins:
        for i in range(m+1):
            if i >= coin:    # 현재 경우의 수(dp[i])에 이전 경우의 수(dp[i-coin])를 더한다.
                dp[i] += dp[i-coin]

    print(dp[m])