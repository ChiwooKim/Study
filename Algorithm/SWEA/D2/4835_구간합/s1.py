import sys
sys.stdin = open('input.txt')

T = int(input())
for k in range(T):
    N, num = map(int, input().split())
    num_list = list(map(int, input().split()))
    result_list = []
    for i in range(N - (num-1)):
        result_list.append(sum(num_list[i:i+num]))
    for i in range(len(result_list)-1, 0, -1):
        for j in range(i):
            if result_list[j] > result_list[j+1]:
                result_list[j], result_list[j+1] = result_list[j+1], result_list[j]

    result = result_list[len(result_list) - 1] - result_list[0]

    print('#{0} {1}'.format(k + 1, result))

