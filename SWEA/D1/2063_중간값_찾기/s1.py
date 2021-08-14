import sys
sys.stdin = open('input.txt')

T = int(input())

result = sorted(list(map(int, input().split())))

print(result[int((T-1)/2)])