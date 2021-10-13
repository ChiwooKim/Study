import sys
sys.stdin = open('input.txt')

T = int(input())
for k in range(T):
    num = int(input())
    num_list = list(map(int, input()))
    result_list = [0]*10
    for i in num_list:
        result_list[i] += 1
    max_val = 0
    max_idx = 0
    for idx, val in enumerate(result_list):
        if val >= max_val:
            max_val = val
            max_idx = idx

    print('#{0} {1} {2}'.format(k+1, max_idx, max_val ))



