import sys
sys.stdin = open('input.txt')

def solution(record):
    # 명령어(Enter, Leave, Change)를 구분하기 위해 이중리스트로 분리
    records = []
    for rec in record:
        records += [list(rec.split())]

    # 유저아이디로 닉네임 관리(dict로 관리)
    user_dict = {}
    for i in records:
        if i[0] == 'Enter':
            user_dict[i[1]] = i[2]
        elif i[0] == 'Change': # 어차피 최종 출력은 바뀐 것으로 모두 출력하기 때문에 바로 변경
            user_dict[i[1]] = i[2]

    # 출력문 answer 리스트에 담기
    answer = []
    for i in records:
        if i[0] == 'Enter':
            ans = '{}님이 들어왔습니다.'.format(user_dict[i[1]])
            answer.append(ans)
        elif i[0] == 'Leave':
            ans = '{}님이 나갔습니다.'.format(user_dict[i[1]])
            answer.append(ans)

    return answer


record = []
for _ in range(5):
    record.append(input())

print(solution(record))