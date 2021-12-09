import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, A, B = map(int, input().split())
    # P채널 구독자 수: A
    # T채널 구독자 수: B

    if N < (A+B):
        min_sub = A + B - N
        if A > B:
            max_sub = B
        else:
            max_sub = A
    else:
        min_sub = 0
        if A > B:
            max_sub = B
        else:
            max_sub = A

    print('#{} {} {}'.format(tc+1, max_sub, min_sub))



