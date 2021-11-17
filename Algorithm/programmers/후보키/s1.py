import sys
sys.stdin = open('input.txt')
'''
순열을 통해 모든 경우를 다 구한다
구한 순열의 인덱스에 대응하는 튜플을 구성한 후 중복이 있는지 비교
없다면 후보키 +1
'''
# from itertools import combinations
#
#
# unique = []
# def check(per, relation, N):
#     result = set()
#
#     for i in relation:
#         temp = tuple()
#         for j in per:
#             temp += tuple([i[j]])
#         result.add(temp)
#
#     if len(result) == N:
#         for i in per:
#             if i in unique:
#                 return 0
#         unique.extend(per)
#         return 1
#     else:
#         return 0
#
#
# def solution(relation):
#     answer = 0
#     n = len(relation[0])
#     N = len(relation)
#     cnt = 1
#
#     while cnt <= n:
#         for i in combinations(range(n), cnt):
#             answer += check(list(i), relation, N)
#         cnt += 1
#
#     return answer



def solution(relations):
    answer = []
    targets = [[i for i in range(len(relations[0]))]]
    while targets:
        check = 0
        tmp = targets.pop(0)
        for i in range(len(tmp)):
            lst = []
            for leng in range(len(relations)):
                a = tmp.copy()
                a.remove(tmp[i])
                b = ''
                for x in a:
                    b += relations[leng][x]
                lst.append(b)
            if (len(set(lst)) == len(lst)) and (a not in targets):
                targets.append(a)
            elif (len(set(lst)) != len(lst)):
                check +=1
        if check ==len(tmp):
            answer.append(tmp)
    return len(answer)


relation = []
for i in range(6):
    temp = input().split(',')
    relation.append(temp)

print(solution(relation))