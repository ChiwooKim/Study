n = int(input())
guest = []
for _ in range(n):
    guest += [int(input())]
# 돈이 많은 사람을 앞배치 해야 팁을 많이 받을 수 있음
# 보유금액에 따른 내림차순 정렬
guest.sort()
guest_line = guest[::-1]

# 강호 = tip - (받은등수 - 1)
total = 0
for i in range(len(guest_line)):
    tip = guest_line[i] - ((i+1) - 1)
    if tip >= 0: # tip이 음수일 경우 제거
        total += tip
print(total)