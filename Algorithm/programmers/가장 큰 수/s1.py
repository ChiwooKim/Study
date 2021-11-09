import sys
sys.stdin = open('input.txt')

'''
1. 시간초과 해결 못함....
from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    result = []
    for i in permutations(range(len(numbers))):
        temp = ''
        for j in i:
            temp += numbers[j]
        result.append(temp)
    result.sort()
    answer = result[-1]
    return answer
'''



T = int(input())

for tc in range(T):
    numbers = list(map(int, input().split()))
    print(solution(numbers))