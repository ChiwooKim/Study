import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    order = list(input().split())
    N = int(order.pop(0))

    # [시간, 위치]
    B = [0, 1]
    O = [0, 1]

    # 결과값이 되는 시간
    result = 0
    for i in range(0, 2*N, 2):
        if order[i] == 'B':
            # 이동거리
            d = abs(B[1] - int(order[i+1]))

            if d <= result - B[0]:
                B[1] = int(order[i+1])
                result += 1
                B[0] = result
            else:
                result += d - (result - B[0]) + 1
                B[1] = int(order[i+1])
                B[0] = result

        if order[i] == 'O':
            d = abs(O[1] - int(order[i+1]))
            if d <= result - O[0]:
                O[1] = int(order[i+1])
                result += 1
                O[0] = result
            else:
                result += d - (result - O[0]) + 1
                O[1] = int(order[i+1])
                O[0] = result

    print('#{} {}'.format(tc+1, result))






