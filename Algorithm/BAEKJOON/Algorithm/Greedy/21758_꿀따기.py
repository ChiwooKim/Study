'''
벌-벌-통
벌-통-벌
통-벌-벌
'''

n = int(input())
honey = list(map(int, input().split()))

max_honey = 0
# 벌-벌-통(통이 가장 끝이 있어야함)
for i in range(len(honey)):
    for j in range(i+1, len(honey)):
        cnt = sum(honey[i+1:len(honey)])+sum(honey[j+1:len(honey)])-honey[j]
        if cnt > max_honey:
            max_honey = cnt

# 통-벌-벌
for i in range(len(honey)-1, -1, -1):
    for j in range(i-1, -1, -1):
        cnt = sum(honey[i-1:-1:-1])+sum(honey[j-1:-1:-1])-honey[j]
        if cnt > max_honey:
            max_honey = cnt

# 벌-통-벌
for i in range(1, len(honey)-1):
    cnt = sum(honey[1:len(honey)-1])+honey[i]
    if cnt > max_honey:
        max_honey = cnt

print(max_honey)