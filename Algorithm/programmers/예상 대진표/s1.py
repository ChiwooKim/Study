import sys, math
sys.stdin = open('input.txt')
'''
      4               7
  1       4       5       7
1   2   3   4   5   6   7   8
'''
def solution(n, a, b, start=1):
    answer = 0
    temp = list(range(start, n+1))
    check_a = [False, False]
    check_b = [False, False]


    if a in temp[:(n//2+1)]:
        check_a[0] = True
    else:
        check_a[1] = True

    if b in temp[:(n//2+1)]:
        check_b[0] = True
    else:
        check_b[1] = True

    if check_a[0] == True and check_b[0] == True:
        solution(n//2, a, b)
    elif check_a[1] == True and check_b[1] == True:
        solution(n, a, b, n//2+1)
    else:
        answer = int(math.log2(n))

    return answer

n, a, b = map(int, input().split())
print(solution(n, a, b))