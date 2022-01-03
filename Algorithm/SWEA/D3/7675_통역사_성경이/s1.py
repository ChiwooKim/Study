import sys
sys.stdin = open('input.txt')

ans = []
for tc in range(int(input())):
    N = int(input())
    input_list = list(input().split())

    # 문장 분류하기
    sentence = []
    temp = []
    for word in input_list:
        # 구두점 확인 후 구두점 제거하고 추가한다.
        if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
            temp.append(word[:len(word)-1])
            sentence.append(temp)
            temp = []
            continue
        temp.append(word)

    # 대문자로 시작해서 소문자로 끝나는 단어들 찾고 카운트 하기
    result = ''   # 카운트한 값들 넣기
    for words in sentence:
        cnt = 0
        for word in words:
            # 글자의 길이가 1글자인 경우도 확인한다
            if len(word) == 1:
                if word.isupper():
                    cnt += 1
            else:
                if word.isalpha() and word[0].isupper() and word[1:].islower():
                    cnt += 1
        result += ' {}'.format(cnt)

    ans.append('#{}{}\n'.format(tc+1, result))
print(''.join(ans))

