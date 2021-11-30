import sys
sys.stdin = open('input.txt')

'''
다같이 최대한 많이 마시기 위해서는 N분의 1 씩 마시는 것!!!
'''

T = int(input())

for tc in range(T):
    n = int(input())

    print('#{}'.format(tc+1), end=' ')
    for i in range(n):
        print('1/{}'.format(n), end=' ')
    print()