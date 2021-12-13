import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    cards = list(input().split())

    group1 = cards[:(N+1)//2]
    group2 = cards[(N+1)//2:]

    result = []
    for i in range(len(group1)):
        try:
            result.append(group1[i])
            result.append(group2[i])
        except:
            continue

    print('#{}'.format(tc+1), *result)

