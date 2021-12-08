import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    length = list(map(int, input().split()))

    if len(set(length)) == 1:
        print('#{} {}'.format(tc+1, length[0]))
    else:
        check = dict()
        for i in length:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1

        for i in length:
            if check[i] == 1:
                print('#{} {}'.format(tc+1, i))

# 다른사람 풀이
# results = []
# T = int(input())
# for t in range(1, T+1):
#     a, b, c = input().split()
#     if a == b:
#         r = c
#     else:
#         if a == c:
#             r = b
#         else:
#             r = a
#     results.append('#{} {}'.format(t, r))
# print('\n'.join(results))