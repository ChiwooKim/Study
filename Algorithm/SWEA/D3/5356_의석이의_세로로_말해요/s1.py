import sys
sys.stdin = open('input.txt')

T = int(input())
# 문자열 => 리스트, 2중 for문 이용해 모두 탐색, 에러(out of range) 무시후 다음 수가 있는지 확인
for tc in range(T):
    words = [list(input()) for _ in range(5)]
    result = ''

    for i in range(15):
        for j in range(5):
            try:
                result += words[j][i]
            except:
                continue

    print('#{} {}'.format(tc+1, result))

'''
다른 사람의 코드(내가 짠 코드보다 40ms 빠름)
문자열을 그대로 이용(list로 변환하는 시간을 낭비를 줄였다.)
2중 for문에서 모든 15*5를 모두 탐색해야 했지만, 이 경우 필요한 부분만 빠르게 가져간 후 남은 부분을 새로 저장하여 불필요한 탐색을 줄임
범위가 커졌다면 더 큰 시간차가 나거나 혹은 내 코드에서 시간 초과가 났을 것 같다.
result = []
for tc in range(int(input())):
    words = [input() for _ in range(5)]
    temp = ''
    while True:
        for i in range(5):
            if words[i]:
                temp += words[i][0]
                words[i] = words[i][1:]
        if words == ['','','','','']:
            break
    result.append("#{} {}".format(tc+1,temp))
print("\n".join(result))
'''
