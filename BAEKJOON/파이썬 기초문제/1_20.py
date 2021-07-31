#2. A+B
# A, B = map(int,input().split())
# print(A+B)

#4. A-B
# A, B = map(int,input().split())
# print(A-B)

#6. 사칙연산
# A, B = map(int,input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)

#8. A+B -2
# a = int(input())
# b = int(input())
# print(a+b)

#10. R2
# r1,s = map(int,input().split())
# r2 = 2*s - r1
# print(r2)

#12 A+B -7
# t = int(input())
# n = 0
# ab_list=[]
# while n < t:
#     a, b = map(int,input().split())
#     ab_list.append(a+b)
#     n += 1

# for i in range(t):
#     print('Case #{0}: {1}'.format(i+1,ab_list[i]))

#14 오늘날짜
# from datetime import date

# print(date.isoformat(date.today()))

#16. 오븐시계
# hour, min = map(int, input().split())
# cook_min = int(input())

# if (min+cook_min) >= 60:
#     hour += (cook_min+min)//60
#     min = (cook_min+min)%60
#     if hour >= 24:
#         hour -= 24
#     print(hour, min)
# else:
#     if hour >= 24:
#         hour -= 24
#     print(hour, min+cook_min)

#18. 저작권
# a, b = map(int, input().split())
# auth_list = list(range((b-1)*a+1,b*a+1))
# print(min(auth_list))

#20. 문자열 반복
# t = int(input())
# count = 0
# result = ''
# result_list = []
# while count < t:
#     a, b = input().split()
#     a = int(a)
#     count += 1
#     for i in b:
#         result += i*a
#     result_list.append(result)
#     result = ''
# for j in result_list:
#     print(j)   
