import sys
sys.stdin = open('input.txt')

n = int(input())
result = 0
for i in range(1,n+1):
    result += i
print(result)