import sys
sys.stdin = open('input.txt')

'''
단순하게 정방향, 역방향으로만하는 코드를 짰더니 test11을 통과하지 못함
AABAAAAAAAAAABB 와 같은 경우 단방향 보다 중간에 역방향으로 다시 진행하는 것이 더 거리가 짧기 때문이다.
좌우 방향을 체크할 때 파이썬에서 인덱스가 음수가 되는 경우도 가능하기 때문에 아래와 같은 코드가 가능함.
'''

def solution(name):
    # 각 알파벳에서 정방향, 역방향 중 가까운 방향을 찾아서 그 횟수를 리스트로 만든다.
    idx = 0
    answer = 0
    updown_stick = []
    for i in name:
        updown_stick.append(min(ord(i) - ord('A'), 26-(ord(i) - ord('A'))))
    idx = 0
    answer = 0

    while True:
        # 스틱으로 원하는 알파벳을 맞춰준 후 그 자리는 0으로 대체
        answer += updown_stick[idx]
        updown_stick[idx] = 0

        # 원하는 name이 완성 되었을 때 반복문 빠져나가기
        if sum(updown_stick) == 0:
            break

        # 좌, 우로 이동시 'A'거나 0이면 이동하는 스틱횟수만 count
        left, right = 1, 1
        while updown_stick[idx - left] == 0:
            left += 1
        while updown_stick[idx + right] == 0:
            right += 1

        # 위에서 카운트한 좌우이동 횟수를 이용해 카운트가 더 적은 쪽으로 이동
        if left >= right:
            idx += right
            answer += right

        else:
            idx -= left
            answer += left

    return answer


T = int(input())

for tc in range(T):
    name = input()
    print(solution(name))