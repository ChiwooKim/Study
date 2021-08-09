# 합
# result = sum(range(int(input())+1))
# print(result)

# 피보나치 수 2 (재귀사용하면 에러발생)
# def fib(num):
#     if num < 2:
#         return num
#     else:
#         return fib(num-1) + fib(num-2)

# def fib(number):
#     a, b = 0, 1
#     i = 0
#     while i < number-1:
#         a, b = b, a + b
#         i += 1
#     return b
# n = int(input())
# print(fib(n))

# A+B-3
# T = int(input())
# for _ in range(T):
#     a, b = map(int, input().split())
#     print(a+b)

# 내 학점을 구해줘
T = int(input())

for _ in range(T):
    sub = 0
    score = 0
    n = int(input())
    for i in range(n):
        a, b = map(float, input().split())
        sub += a
        score += b*a
    print('{0} {1:.1f}'.format(int(sub), score/sub ))


