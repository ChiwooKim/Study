import sys
sys.stdin = open('input.txt')

# 균형잡힌 괄호 문자열
def balance(p):
    cnt = 0   # '('의 개수
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

# 올바른 괄호 문자열인지 확인
# 쌍이 맞으면 True 안맞으면 False 반환
def check(p):
    cnt = 0   # '('의 개수
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True


def solution(p):
    answer = ''

    # 빈문자열인 경우 빈문자열 반환
    if p == '':
        return answer

    # p안에서 균형잡힌 문자열이 될 때 idx를 구함
    idx = balance(p)
    u = p[:idx+1]   # 균형잡힌 곳 까지 리스트
    v = p[idx+1:]   # 나머지

    # 균형잡힌 부분이 올바른 문자열인지 확인
    # 올바른 문자열이면 그래도 두고 나머지 부분인 v를 다쉬 solution으로 재귀
    # 아니라면 교정해주기
    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer

T = int(input())
for tc in range(T):
    p = input()
    print(solution(p))