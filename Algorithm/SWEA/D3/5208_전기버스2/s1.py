import sys
sys.stdin = open('input.txt')

def bus_stop(idx, now, cnt): # now: 현재 충전된 양, idx:정류장
    global result
    if result < cnt:
        return

    if idx >= n:
        result = cnt
        return

    now = input_list[idx]
    cnt += 1
    for i in range(now, 0, -1):
        bus_stop(idx+i, now, cnt)



T = int(input())

ans = []
for tc in range(T):
    input_list = list(map(int, input().split()))
    n = input_list[0]
    input_list += [0]
    result = n
    cnt = -1
    charge = input_list[1]
    bus_stop(1, 0, cnt)

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))