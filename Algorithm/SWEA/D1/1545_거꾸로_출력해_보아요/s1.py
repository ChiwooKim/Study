import sys
sys.stdin = open('input.txt')

num = int(input())

result = list(range(num, -1, -1))

print(*result)