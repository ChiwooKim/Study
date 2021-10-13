import sys
sys.stdin = open('input.txt')

n = input()
result = 0

# 입력받은 문자열을 for문으로 하나씩 받아 int변환 후 누적 합
for i in n:
    result += int(i)

print(result)
