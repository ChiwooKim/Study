import sys
sys.stdin = open('input.txt')

n = int(input())
result = []
for i in range(n+1):
    result.append(2**i)
print(*result)