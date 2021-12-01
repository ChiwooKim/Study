import sys
sys.stdin= open('input.txt')

T = int(input())

for tc in range(T):
    score = list(map(int, input().split()))
    total = 0

    # 40점 이상은 더하고 미만인 경우 40점으로 통일하여 합산
    for i in score:
        if i >= 40:
           total += i
        else:
            total += 40

    avg = total // len(score)

    print('#{} {}'.format(tc+1, avg))
