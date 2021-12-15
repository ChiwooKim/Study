import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())

    print('#{} {}'.format(tc+1, A+B))