n = int(input())

price = []
for _ in range(n):
    price += [int(input())]

price.sort(reverse=True)

total = sum(price)
# free = sum(price[2::3])
# print(total-free)
# 위 코드를 for로 해결 가능
for i in range(2, len(price), 3):
    total -= price[i]

print(total)
