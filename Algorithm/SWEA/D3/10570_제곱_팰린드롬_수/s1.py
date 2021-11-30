import sys
sys.stdin = open('input.txt')

import math # math.sqrt() => 루트

T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    result = 0

    for i in range(a, b+1):
        # 팰린드롬 체크
        if str(i) == str(i)[::-1]:

            # 제곱수 체크
            k =math.sqrt(i)
            if k.is_integer():
                check = str(int(math.sqrt(i)))

                # 팰린드롬 체크
                if check == check[::-1]:
                    result += 1

    print('#{} {}'.format(tc+1, result))
