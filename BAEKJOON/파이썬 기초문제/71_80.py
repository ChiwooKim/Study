# 별 찍기 - 5
# t = int(input())
# for i in range(1, t+1):
#     print(' '*(t-i)+'*'*(2*i-1))

# 별 찍기 - 7
# t = int(input())

# for i in range(1, t+1):
#     print(' '*(t-i) + '*'*(2*i-1))
# for j in range(t-1,0,-1):
#     print(' '*(t-j) + '*'*(2*j-1))

# 별 찍기 - 13
# t = int(input())

# for i in range(1,t+1):
#     print('*'*i)
# for j in range(t-1,0,-1):
#     print('*'*j)

# 별 찍기 -8
# t = int(input())

# for i in range(1,t+1):
#     print('*'*i + ' '*((t-i)*2) + '*'*i)
# for j in range(t-1,0,-1):
#     print('*'*j + ' '*((t-j)*2) + '*'*j)

# 플러그
import sys
input =  sys.stdin.readline

T = int(input())

cnt = 0
for _ in range(T):
    cnt += int(input())
          
print(cnt-(T-1))