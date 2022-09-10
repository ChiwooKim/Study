import sys
sys.stdin = open('input.txt')

T = int(input())
ans = []
for t in range(T):
    weed = input()
    res = 0

    for i in range(len(weed)):
        if weed[i] == '(':
            res += 1
        elif weed[i] == ')':
            if weed[i-1] == '(':
                continue
            res += 1


    ans.append('#{} {}\n'.format(t+1, res))

print(''.join(ans))