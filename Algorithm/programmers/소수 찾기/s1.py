import sys
sys.stdin = open('input.txt')

from itertools import permutations

def check(numbers):
    temp = ''
    for i in numbers:
        temp += i
    temp = int(temp)

    if temp == 1:
        return 0

    for i in range(2, temp):
        if temp % i == 0:
            return 0
    return temp

def solution(numbers):
    result = set()
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            k = check(j)
            if k != 0:
                result.add(k)

    answer = len(result)
    return answer

T = int(input())

for tc in range(T):
    numbers = input()
    print(solution(numbers))