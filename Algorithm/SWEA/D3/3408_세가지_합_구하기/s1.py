import sys
sys.stdin = open('input.txt')

'''
for문을 이용했더니 시간초과가 발생했다.
for문도 사치인듯.... 그냥 N까지의 합, 홀수합, 짝수합을 수학적으로 풀어내어 바로 N을 대입하여 값이 나오게 하니
pass가 나왔다.
'''

ans = []
for tc in range(int(input())):
    N = int(input())

    s1 = N*(N+1)//2
    s2 = N**2
    s3 = N**2 + N

    # for i in range(1, N+1):
    #     s1 += i
    #     s2 += 2*(i-1)+1
    #     s3 += 2*i


    ans.append('#{} {} {} {}\n'.format(tc+1, s1, s2, s3))
print(''.join(ans))