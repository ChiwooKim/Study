import sys
sys.stdin = open('input.txt')

def perm(temp, k):
    global result

    if k == len(numbers):
        temp = [1]+temp+[1]
        total = 0

        for j in range(1, k+2):
            total += battery[temp[j - 1]][temp[j]]

        if result > total:
            result = total
        return

    for i in range(len(numbers)):
        if not used[i]:
            used[i] = 1
            temp.append(numbers[i])
            perm(temp, k+1)
            temp.pop()
            used[i] = 0

T = int(input())

ans = []
for tc in range(T):
    n = int(input())
    battery = [[0]*(n+1)] + [([0]+list(map(int, input().split()))) for _ in range(n)]
    numbers = []
    result = 0
    for i in battery:
        result += sum(i)
    for i in range(2, n+1):
        numbers.append(i)
    used = [0] * len(numbers)

    perm([], 0)
    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))