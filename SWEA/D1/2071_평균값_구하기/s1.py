import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    num_list = list(map(int, input().split()))
    print('#{} {}'.format(_+1, round(sum(num_list)/len(num_list))))