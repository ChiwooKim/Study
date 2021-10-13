#52. 첼시를 도와줘!
t = int(input())

for q in range(t):
    n = int(input())
    max_price = 0
    max_name = ''
    pr = 0
    for _ in range(n):
        price, name = input().split()
        pr = int(price)
        if max_price < pr:
            max_price = pr
            max_name = name
        else:
            continue
    print(max_name)
    


# 54. 24
# hour1, min1, sec1 = map(int, input().split(':'))
# hour2, min2, sec2 = map(int, input().split(':'))
# hh = hour2 - hour1
# mm = min2 - min1
# ss = sec2 - sec1
# if ss<0:
#     ss +=60
#     mm -= 1
# if mm < 0:
#     mm += 60
#     hh -= 1
# if hh <0:
#     hh += 24

# print(f'{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}')

#56. 기찍N
# t = int(input())
# while t>0:
#     print(t)
#     t-=1

#58. 별 찍기 - 1
# t = int(input())
# count = 1
# for _ in range(t):
#     print(count*'*')
#     count+=1

#60. 별 찍기 - 3
# t = int(input())
# for i in list(range(t))[::-1]:
#     print((i+1)*'*')