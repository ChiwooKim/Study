import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())

    temp = str(bin(M))[-1:-N-1:-1]
    if temp == '1'*N:
        print('#{} {}'.format(tc+1, 'ON'))
    else:
        print('#{} {}'.format(tc + 1, 'OFF'))

'''
1초 빠른 코드(swea 기준)
비트연산으로 마지막 부분 비트만 체크
비트연산에 대한 이해부족으로 위와 같이 풀었다.
비트연산 정리하자!!!!

cases = []
for _ in range(int(input())):
    N, M = map(int, input().split())
    cases.append((N, M))
ans_list = []
for case in cases:
    mask = int('1' * case[0], 2)
    if (case[1] & mask) == mask:
        ans_list.append('ON')
    else:
        ans_list.append('OFF')
for i, ans in enumerate(ans_list):
    print(f"#{i + 1} {ans_list[i]}")
'''


