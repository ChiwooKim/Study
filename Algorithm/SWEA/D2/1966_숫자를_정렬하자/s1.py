import sys
sys.stdin = open('input.txt')

T = int(input())
#버블소트
for _ in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))
    for i in range(n-1,-0,-1):
        for j in range(n-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    print('#{} '.format(_+1), end='')
    print(*num_list)