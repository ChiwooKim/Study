import sys
sys.stdin = open('input.txt')
'''
첫번째, while문 안에 for문을 써서 삭제되면 다시 처음부터 찾는 방식 - 시간초과
두번째, 길이가 홀수인 문자열 제거하고 탐색 - 시간초과
세번째, stack을 이용하여 처음부터 시작하는 다시 탐색하는 과정을 삭제 - pass
'''
def solution(s):
    answer = 1       # 1로 기본값을 두어 문자열을 모두 제거한다는 결과로 가정
    check = list(s)

    if len(check) % 2:  # 문자열 길이가 홀수이면 어차피 나머지가 남기때문에 검사 전 제거
        answer = 0
        return answer

    stack = [check[0]]  # stack에 첫 문자 저장

    for i in range(1, len(check)):  # for문을 통해 stack을 pop하여 그 해당문자와 비교
        if stack:  # stack이 비어있으면 무조건 push 아니면 pop하며 비교
            temp = stack.pop()  # 짝지어 지면 다음 과정으로 넘어가는 것으로 삭제
            if check[i] == temp:
                continue
            else:  # 삭제하지 못할 경우 pop한 값을 다시 넣어주고 그 다음에 비교했던 문자를 push함
                stack.append(temp)
                stack.append(check[i])
        else:
            stack.append(check[i])

    if stack:
        answer = 0
        return answer
    else:
        return answer



T = int(input())
for tc in range(T):
    s = input()
    print(solution(s))