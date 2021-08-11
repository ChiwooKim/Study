# 할로윈의 사탕
# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     print('You get {0} piece(s) and your dad gets {1} piece(s).'.format(a//b,a%b))


# 다면체
# t = int(input())
# for _ in range(t):
#     a, b =map(int,input().split())
#     c = 2+b-a
#     print(c)

# 별 찍기 - 20
# t = int(input())

# for i in range(1,t+1):
#     if i%2:
#         print('* '*t)
#     else:
#         print(' *'*t)


# x보다 작은수
# n, x = map(int, input().split())
# num_list = list(map(int,input().split()))
# result = []
# for i in num_list:
#     if i < x:
#         result.append(i)
# print(*result)


# 소수찾기
# t = int(input())
# ab = list(map(int, input().split()))
# cnt = 0
# for i in ab:
#     result = []
#     for j in range(1,i+1):
#         if  i% j == 0:
#             result.append(i)
#     if len(result) == 2:
#         cnt +=1
# print(cnt)

# 약수구하기
a, b = map(int,input().split())
result=[]
for i in range(1,a+1):
    if a%i==0:
        result.append(i)
if len(result)>=b:
    print(result[b-1])
else:
    print(0)