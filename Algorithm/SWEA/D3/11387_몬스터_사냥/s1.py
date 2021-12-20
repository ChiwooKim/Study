import sys
sys.stdin = open('input.txt')

'''
damage = D(1+0*L/100)+D(1+1*L/100)+D(1+2*L/100)+...+D(1+(N-1)*L/100)
       = D(N+N*(N-1)/2*L/100)
매번 프린트를 바로 출력하는 것보다 리스트에 담은 후 한번에 출력하니 시간이 대폭 줄었다.
'''
answer = []
for tc in range(int(input())):
    D, L, N = map(int, input().split())
    result = 0
    for i in range(N):
        result += D*(1+(i*L*0.01))
    answer.append('#{} {}\n'.format(tc+1, int(result)))
print(''.join(answer))