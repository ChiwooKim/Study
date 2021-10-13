#22. 시험성적
# score = int(input())
# if 90 <= score <= 100:
#     print('A')
# elif 80 <= score <= 89:
#     print('B')
# elif 70 <= score <= 79:
#     print('C')
# elif 60 <= score <= 69:
#     print('D')
# else:
#     print('F')

#24. 소인수분해
# score = int(input())
# n = 2
# while score > 1:
#     if score % n:
#         n +=1
#     else:
#         score = score/n
#         print(n) 

#26. 윤년
# year = int(input())
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(1)
#         else:
#             print(0)
#     else:
#         print(1)
# else:
#     print(0)

#28. 최소공배수 - 유클리드 호제법 학습
# t = int(input())
# count = 0
# input_list = []


# while count < t:
#     a, b = map(int, input().split( ))
#     sample = [a,b]
#     input_list.append(sample)
#     count +=1
    

# for i in input_list:
#     x = i[0]
#     y = i[1]
#     while y:
#         x, y = y, x%y
    
#     result = i[0]*i[1]//x

#     print(result)

#30. 크냐 - sys
# import sys
# t=1
# def size(a,b):
#     if a>b:
#         return 'Yes'
#     else:
#         return 'No'
# while t==1:
#     a, b = map(int, sys.stdin.readline().split())
#     if a==0 and b==0:
#         break
#     else:
#         print(size(a,b))

#32. 네번째 점
# t = 3
# count = 0
# x_list = []
# y_list = []
# result1 = ''
# result2 = ''
# while count<t:
#     a,b = map(int, input().split())
#     x_list.append(a)
#     y_list.append(b)
#     count += 1

# for i in x_list:
#     if x_list.count(i) == 2:
#         continue
#     else:
#         result1 += str(i)
# for j in y_list:
#     if y_list.count(j) == 2:
#         continue
#     else:
#         result2 += str(j)

# print(result1, result2)

#34. 학점계산
# grade_dict ={'A+': 4.3, 'A0': 4.0, 'A-': 3.7,'B+': 3.3, 'B0': 3.0, 'B-': 2.7,'C+': 2.3, 'C0': 2.0, 'C-': 1.7,'D+': 1.3, 'D0': 1.0, 'D-': 0.7,'F': 0.0}
# a = input()
# print(grade_dict.get(a))

#36. 그릇
# input_list= list(input())
# result = 10
# for i in range(1,len(input_list)):
#     if input_list[i] == input_list[i-1]:
#         result += 5
#     else:
#         result += 10
# print(result)

#38. 개표
# t = map(int, input())
# input_list = list(input())
# if input_list.count('A') > input_list.count('B'):
#     print('A')
# elif input_list.count('A') < input_list.count('B'):
#     print('B')
# else:
#     print('Tie') 

#40. 팰린드롬인지 확인하기
def is_pal_while(word):
    result=''
    i = len(word) - 1
    while i >= 0:
        result += word[i]
        i -= 1
    if word == result:
        return 1
    else:
        return 0

print(is_pal_while(input()))