import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    num_list = [''.join(input().split()) for _ in range(N)]

    third = list(map(''.join, zip(*num_list)))[::-1]

    second = []
    for i in range(N-1,-1,-1):
        second.append(num_list[i][::-1])

    first = []
    for i in range(N-1,-1,-1):
        first.append(third[i][::-1])

    result = []
    cnt = 0
    while cnt < N:
        result.append(first[cnt]+' '+second[cnt]+' '+third[cnt])
        cnt += 1
    print('#{}'.format(_+1))
    for i in result:
        print(i)