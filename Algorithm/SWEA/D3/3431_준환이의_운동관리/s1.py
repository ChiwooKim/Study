import sys
sys.stdin = open('input.txt')

'''
1주일 => L분 <= X분 <= U분
입력값 L U X(0≤ L ≤ U ≤ 10**7, 0 ≤ X ≤ 10**7)
'''

T = int(input())

for tc in range(T):
    l, u, x = map(int, input().split())

    if u < x:
        print('#{} {}'.format(tc+1, -1))
    elif l > x:
        print('#{} {}'.format(tc+1, l-x))
    else:
        print('#{} {}'.format(tc + 1, 0))