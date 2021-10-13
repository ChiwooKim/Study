import sys
sys.stdin = open('input.txt')

p, k = map(int, input().split())

print(p-k+1)

#for문을 이용해 하나씩 카운트해가며 나타내는 방법도 있음