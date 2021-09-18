'''
binary search
'''

n, c = map(int, input().split())
home = []

for _ in range(n):
    home += [int(input())]
home.sort()
sp = 1
ep = home[-1] - home[0]
# binary search
while sp <= ep:
    mid = (sp+ep) // 2
    now = home[0]
    cnt = 1

    for i in range(1, len(home)):
        if home[i] >= now + mid:
            cnt += 1
            now = home[i]

    if cnt >= c:
        sp = mid + 1
        result = mid
    else:
        ep = mid - 1

print(result)
