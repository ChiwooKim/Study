import sys
sys.stdin = open('input.txt')

N = int(input())
num = list(map(str, range(1, N+1)))
clap = ['3', '6', '9']
result = []
for i in num:
    cnt = 0
    for j in i: # 3,6,9가 있는지 확인
        if j in clap: # 3, 6, 9가 있다면 카운트
            cnt += 1
    if cnt != 0: # 카운트가 없다는건 3,6,9가 없다는 의미기 때문에 원래 값 반환
        i = cnt*'-' # 카운트가 있다면 카운트 개수 만큼 - 반환
    result += [i]
print(*result)


