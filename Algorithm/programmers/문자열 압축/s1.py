import sys
sys.stdin = open('input.txt')
'''
처음에 결과와 같은 유사한 코드를 작성했으나 케이스 3가지만 통과했었다.
압축되는 길이는 같은데 다른 문자가 압축되는 경우를 해결하지 못하여 결국 다른 사람코드를 보게되었다....
비록 카피했지만 내것으로 만들고 이해하고 유사한 문제가 나오면 내가 혼자서 풀 수 있도록 하자!!!
'''
def solution(s):
    str_len = len(s) # 문자열 길이
    min_len = str_len # 압축 문자열의 최소 길이

    # 반복이 되는 것을 압축하기 때문에 문자열 길이의 절반이 최대!
    for i in range(1, int(str_len/2)+1):
        check = s[0:i] # 반복되는 것을 확인하기 위함
        cnt = 1 # 반복 문자열 반복 횟수
        temp = '' # 압축할 문자열

        for j in range(i, str_len+1-i, i):
            # 이전 문자와 같은 문자인지 체크
            if check == s[j:j+i]:
                cnt += 1 # 반복 카운트
            else:
                # 중복이 끝난 후 압축 (반복횟수 + 압축문자)
                if cnt != 1:
                    temp += str(cnt)
                temp += check
                check = s[j:j+i]
                cnt = 1

        # 마지막 문자열 추가
        if cnt != 1:
            temp += str(cnt)
        temp += check

        if j != (str_len - i):
            temp += s[j+i:str_len]

        # 최소 길이
        if len(temp) < min_len:
            min_len = len(temp)
    return min_len

for tc in range(5):
    string = input()

    print(solution(string))
