#42. 상근이의 친구들
# t =1
# while t==1:
#     a, b = map(int, input().split())
#     if a==0 and b==0:
#         break
#     print(a+b)

#44. ox퀴즈
# t = int(input())

# for _ in range(t):
#     bonus = 0
#     input_list = list(input())
#     result = input_list.count('O')
#     for i in range(1,len(input_list)):
#         if input_list[i]=='O' and input_list[i] == input_list[i-1]:
#             bonus += 1
#             result += bonus
#         else:
#             bonus = 0
#     print(result)
    
#46. 전자레인지
# t = int(input())
# a = 0
# b = 0
# c = 0
# if t>=300:
#     a = t//300
#     t = t%300
# if t>=60:
#     b = t//60
#     t = t%60
# if t>=10:
#     c = t//10
#     t = t%10
# if t:
#     print(-1)
# else:
#     print(a,b,c)

#48. Baseball
# t = int(input())
# a_count = 0
# b_count = 0
# for _ in range(t):
#     for __ in range(9):
#         a, b=map(int, input().split())
#         a_count += a
#         b_count += b
#     if a_count > b_count:
#         print('Yonsei')
#     elif a_count < b_count:
#         print('Korea')
#     else:
#         print('Draw')

#50. 큰 수 A + B
a, b = map(int, input().split())
print(a+b)