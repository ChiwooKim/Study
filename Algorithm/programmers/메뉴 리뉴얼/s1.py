import sys
sys.stdin = open('input.txt')
from itertools import combinations
from collections import Counter

'''
Counter 클래스는 dict구조의 확장.
ex) Counter('hello world')
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
'''

def solution(orders, course):
    answer = []

    for i in course:  # 메뉴 개수에 맞게 모든 경우의 수를 조합으로 check()
        check = []
        for j in orders:
            temp = combinations(sorted(j), i)  # 메뉴를 먼저 오름차순으로 정렬 후 조합
            check += temp
        menu = Counter(check)  # 메뉴 조합의 수를 셈

        if menu and max(list(menu.values())) >= 2:  # 메뉴 조합이 가장 많이 나온 값을 찾고 2이상이면 코스요리로 추가
            for key, value in menu.items():
                if menu[key] == max(list(menu.values())):
                    answer.append(''.join(key))

    return sorted(answer)

T = int(input())
for tc in range(T):
    orders = input().split()
    course = list(map(int, input().split()))
    print(solution(orders, course))


