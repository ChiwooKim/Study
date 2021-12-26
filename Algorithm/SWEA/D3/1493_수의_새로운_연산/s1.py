import sys
sys.stdin = open('input.txt')
'''
처음에 그냥 수학적으로 힘들게 규칙을 찾아내어 2중 for문을 이용해 x,y를 찾다보니 시간초과가 발생
그래서 도저히 방법이 생각나지 않아 다른사람들의 풀이를 참고하여 또 다른 방식으로 x,y를 찾는 방법을 알게 되었다.
    temp = [0, 0]   # [y, x]
    # p,q에 해당하는 좌표들 찾기
    cnt = 0
    for i in range(1, 10001):
        for j in range(1, 10001):
            k = (j**2 + j + (2*j + i - 2) * (i - 1)) // 2
            if k == p or k == q:
                temp[0] += i
                temp[1] += j
                cnt += 1

            if cnt == 2:
                break
        if cnt == 2:
            break

    # 공식을 이용해 다시 좌표로 최종 값 찾기
    result = (temp[1]**2 + temp[1] + (2*temp[1] + temp[0] - 2) * (temp[0] - 1)) // 2
'''


# x, y 좌표를 찾은 후 temp에 각 좌표에 더해주기
def find(k):
    line = 1
    # k가 몇 번째 라인 위에 존재하는 수 인지 찾기
    while True:
        if sum(range(line)) < k < (sum(range(line + 1))+1):
            break
        line += 1

    x = line - (sum(range(1, line + 1)) - k)
    y = line + 1 - x

    temp[1] += x
    temp[0] += y

ans = []
for tc in range(int(input())):
    p, q = map(int, input().split())

    #  temp = [y, x] 좌표 저장
    temp = [0, 0]

    find(p)
    find(q)

    result = (temp[1]**2 + temp[1] + (2*temp[1] + temp[0] - 2) * (temp[0] - 1)) // 2

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))