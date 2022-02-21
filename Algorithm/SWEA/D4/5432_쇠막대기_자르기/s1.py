import sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for _ in range(T):
    stick_list = list(input())
    stick = []
    cnt = 0
    for i in range(len(stick_list)):
        if stick_list[i] == '(':
            stick.append(stick_list[i])
        else:
            if stick_list[i] == ')' and stick_list[i-1] == '(':
                stick.pop()
                cnt += (len(stick))
            else:
                stick.pop()
                cnt += 1
    ans.append('#{} {}\n'.format(_+1, cnt))
print(''.join(ans))