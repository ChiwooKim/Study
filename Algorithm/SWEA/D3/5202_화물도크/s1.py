import sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for tc in range(T):
    n = int(input())
    time_list = []
    for _ in range(n):
        s, e = map(int, input().split())
        time_list.append([s, e])

    # 시작시간에 따라 정렬, 같은 시간 시작이 여러개라면 끝나는 시간이 중복되거나 긴 것은 지워줌
    time_list = sorted(time_list)
    check = []

    for i in range(n):
        if time_list[i] not in check:
            for j in range(i+1, n):
                if time_list[i][0] == time_list[j][0]:
                    check.append(time_list[j])
                elif time_list[i][0] <= time_list[j][0] and time_list[i][1] >= time_list[j][1]:
                    check.append(time_list[i])

    for i in check:
        try:
            time_list.remove(i)
        except:
            continue

    for i in range(1, len(time_list)):
        try:
            if time_list[i-1][1] > time_list[i][0]:
                time_list.remove(time_list[i])
        except:
            break
    ans.append('#{} {}\n'.format(tc+1, len(time_list)))
print(''.join(ans))