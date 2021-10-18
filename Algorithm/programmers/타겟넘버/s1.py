import sys
sys.stdin = open('input.txt')

def solution(numbers, target, temp=0, cnt=0):
    global result

    if cnt == len(numbers) and temp == target:
        result += 1
        return

    if cnt == len(numbers):
        return

    solution(numbers, target, temp+numbers[cnt], cnt+1)
    solution(numbers, target, temp-numbers[cnt], cnt+1)



target = int(input())
numbers = list(map(int, input().split()))
result = 0
solution(numbers, target)
print(result)

'''
프로그래머스 제출용 코드
answer = 0
def dfs(numbers, target, temp=0, cnt=0):
    global answer

    if cnt == len(numbers) and temp == target:
        answer += 1
        return

    if cnt == len(numbers):
        return

    dfs(numbers, target, temp+numbers[cnt], cnt+1)
    dfs(numbers, target, temp-numbers[cnt], cnt+1)


def solution(numbers, target):
    global answer
    dfs(numbers, target)
    return answer
'''



