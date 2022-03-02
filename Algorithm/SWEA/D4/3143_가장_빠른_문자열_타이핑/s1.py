import sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for _ in range(T):
    A, B = input().split()
    cnt = len(A) - A.count(B)*(len(B)-1)

    ans.append('#{} {}\n'.format(_+1, cnt))
print(''.join(ans))