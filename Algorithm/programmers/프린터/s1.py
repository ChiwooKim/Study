import sys
sys.stdin = open('input.txt')
'''
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.(큐)
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
'''

from collections import deque

def solution(priorities, location):
    answer = 0
    check = deque()
    # check라는 deque에 리스트를 넣어 주는데
    # priorities의 요소랑 location와 대응하는 idx 값은 true로 넣어준다.
    for i in range(len(priorities)):
        if i == location:
            check.append([priorities[i], True])
        else:
            check.append([priorities[i], False])

    # 큐에서 pop하여 자기보다 우선순위가 높은 것이 있는지 확인
    # 있으면 push, 없으면 출력되는 순서 번호 +1 카운트한다.
    # try except를 통해 deque의 요소가 변화하고 continue 되면 에러 문구가 뜨는데 이를 스킵하기 위함.
    while check:
        temp = check.popleft()
        try:
            for i in check:
                if temp[0] < i[0]:
                    check.append(temp)
                    continue
            answer += 1
        except:
            continue

        # 위 조건을 통과 했다면 출력되는 요소다.
        # 출력되는 요소가 location에 대응하는 수 였다면 True값을 가지고 있기 때문에 if문으로 확인한다.
        # True면 return한다
        if temp[1]:
            return answer


T = int(input())
for tc in range(T):
    priorities = list(map(int, input().split()))
    location = int(input())
    print(solution(priorities, location))
