# 검증수
# num = list(map(int, input().split()))
# total = 0
# for i in num:
#     total += i**2
# result = total % 10
# print(result)

# 홀수
# num = []
# for _ in range(7):
#     a= int(input())
#     if a%2:
#         num.append(a)
# if len(num)==0:
#     print(-1)
# else:
#     print(sum(num))
#     print(min(num))

# 윷놀이
# for _ in range(3):
#     in_list = list(map(int, input().split()))
#     if in_list.count(0) == 1:
#         print('A')
#     elif in_list.count(0) == 2:
#         print('B')
#     elif in_list.count(0) == 3:
#         print('C')
#     elif in_list.count(0) == 4:
#         print('D')
#     else:
#         print('E')
    
#  점수계산
# t = int(input())
# cnt = 1
# in_list = list(map(int, input().split()))
# if in_list[0]:
#     result = 1
# else:
#     result = 0
# for i in range(1,t):
#     if in_list[i]:
#         if in_list[i-1]:
#             result += (1+cnt)
#             cnt += 1
#         else:
#             result +=1
#     else:
#         cnt = 1
# print(result)
            
# 지능형 기차
result = []
a = 0
for _ in range(4):
    op, ip = map(int, input().split())
    a = a+ip-op
    result.append(a)
print(max(result))
