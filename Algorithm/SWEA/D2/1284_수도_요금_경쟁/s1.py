import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    p, q, r, s, w = map(int, input().split())
    # A사 요금
    a = p * w
    # R리터 기준으로 이하면 기본요금 초과면 추가요금
    if w > r:
        b = q + (w-r) * s
    else:
        b = q
    # 적은 요금 출력
    if a > b:
        result = b
    else:
        result = a
    print('#{} {}'.format(_+1, result))