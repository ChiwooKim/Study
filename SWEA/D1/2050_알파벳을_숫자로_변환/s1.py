import sys
sys.stdin = open('input.txt')

al = input()
result = []

for i in al:
    result.append(ord(i)-64)

print(*result)