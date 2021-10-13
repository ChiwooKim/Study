import sys
sys.stdin = open('input.txt')

# 비길 때가 없음
A, B = map(int, input().split())

if A+B == 4:
    if A < B:
        print('A')
    else:
        print('B')

if A<B:
    print('B')
else:
    print('A')