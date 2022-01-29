import sys
sys.stdin = open('input.txt')

'''
페르마의 소정리... 잘 이해가 되질 않는다;;
'''

MOD = 1234567891
fac = [1, 1] + [0] * 1000000
for i in range(2, 1000001):
    fac[i] = fac[i-1]*i % MOD

def double_count(num, mod):
    if mod == 0:
        return 1
    temp = double_count(num, mod//2)
    count = temp ** 2 % MOD
    if mod % 2 == 0:
        return count
    return (num * count) % MOD

ans = []
for tc in range(int(input())):
    n, r = map(int, input().split())
    a = double_count(fac[r] * fac[n-r] % MOD, MOD - 2)
    result = (fac[n] * a) % MOD
    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))