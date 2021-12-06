import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    numbers = input() * 2
    start = 0
    rot = N//4
    temp = []   # 임시저장

    # 16진수로 만들어지는 모든 수 찾기
    while start < rot:
        for i in range(1, 5):
            hex = numbers[(start+rot*(i-1)):(start+rot*i)]
            if hex not in temp:   # 중복제거
                temp.append(hex)
        start += 1

    # 16진수 10진수로 변환
    hex_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }
    result = []
    for i in temp:
        num = 0
        cnt = 0
        while cnt < rot:
            num += hex_dict[i[cnt]] * 16**(rot-1-cnt)
            cnt += 1
        result.append(num)

    # 정렬 후, K번째 수 출력
    result.sort(reverse=True)

    print('#{} {}'.format(tc+1, result[K-1]))

