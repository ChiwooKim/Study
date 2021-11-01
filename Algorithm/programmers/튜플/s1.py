import sys
sys.stdin = open('input.txt')

def remake(s):
    temp = []
    res = []
    word = ''
    # 숫자면 word에 추가
    # ,가 나타나면 숫자가 완성되기 때문에 숫자로 변형하고 temp에 임시저장
    # {가 시작되면 튜플이 새로 다시 생기는 것이기 때문에 temp를 res에 추가 후 temp는 초기화
    # 처음에 {{로 시작하는 부분을 제거하기위해 temp가 빈 리스트는 추가하지 않는다.
    # for문이 완료되면 word와 temp에 남은 수들을 마무리하여 결과 리스트에 추가한다.
    for i in s:
        if i.isdigit():
            word += i
        elif i == ',':
            temp.append(int(word))
            word = ''
        elif i == '{':
            if temp:
                res.append(temp)
            temp = []
    temp.append(int(word))
    res.append(temp)
    return res


def solution(s):
    answer = []
    # 입력된 문자열을 리스트로 변환
    s = remake(s)
    # remove를 이용하기 위해 원본 카피
    st = s.copy()
    cnt = 1   # while문 조건용
    temp = []    # 임시 저장 리스트
    # while 문을 통해 cnt 개수와 같은 원소를 가진 리스트를 temp에 추가
    # 1부터 진행하기 때문에 자연스럽게 조건에 나타나는 튜플 순서대로 배열이 된다.
    while cnt <= len(s):
        for i in st:
            if cnt == len(i):
                temp.append(i)
                st.remove(i)
                break
        cnt += 1

    # 리스트가 적은 수부터 결과 리스트에 없는 값을 추가하면 조건에 맞게 원소가 배열 된다.
    for i in temp:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer


T = int(input())
for tc in range(T):
    s = input()
    print(solution(s))