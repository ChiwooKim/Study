'''
pop 과 슬라이스를 사용할 경우 시간 복잡도 때문에시간초과 오류가 발생하게 된다.
deque 모듈을 사용
'''

from collections import deque
import sys

n = int(input())
q = deque()
for _ in range(n):
    x = sys.stdin.readline().split()
    if x[0] == 'push':
        q.append(x[1])
    elif x[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(q))
    elif x[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif x[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif x[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)


