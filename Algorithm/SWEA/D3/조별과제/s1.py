import sys
sys. stdin = open('input.txt')

'''
N명의 학생, 최소 3명이상으로 구성 => 3으로 나누고 나머지를 다른 조에 배분
'''

T = int(input())

for tc in range(T):
    N = int(input())   # 학생 수

    print('#{} {}'.format(tc+1, N//3))