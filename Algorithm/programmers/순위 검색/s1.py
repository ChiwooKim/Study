import sys
sys.stdin = open('input.txt')

info = list(input().split(','))
query = list(input().split(','))
'''
1. 정확성 실패
'''
# def solution(info, query):
#     answer = []
#     info = [list(_.split()) for _ in info]
#     query = [list(_.split()) for _ in query]
#     print(query)
#     for j in query:
#         cnt = 0
#         for i in info:
#             temp = 0
#             for k in j:
#                 if k == 'and':
#                     continue
#
#                 elif temp != 4 and k != '-' and i[temp] != k:
#                     break
#                 else:
#                     if temp == 4:
#                         if int(i[temp]) >= int(k):
#                             cnt += 1
#                     else:
#                         temp += 1
#         answer.append(cnt)
#     return answer

print(solution(info, query))