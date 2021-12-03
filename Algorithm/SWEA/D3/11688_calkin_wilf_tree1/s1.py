import sys
sys.stdin = open('input.txt')

import math

'''
Calkin-Wilf tree는 모든 양의 유리수를 정확히 하나씩 포함하고 있는 트리다. 이 트리는 다음과 같이 정의된다
 트리의 루트는 1/1 을 나타낸다.
 트리의 각 노드는 왼쪽 자식과 오른쪽 자식을 가지는데 어떤 노드가 a/b 를 나타내고 있다면, 
왼쪽 자식은 a/a+b 를 오른쪽 자식은 a+b/b 를 나타낸다.
'''

T = int(input())

for tc in range(T):
    words = input()
    temp = [1, 1]
    'L: [a,a+b], R: [a+b, b]'

    for word in words:
        if word == 'L':
            temp[1] = temp[0] + temp[1]
        else:
            temp[0] = temp[0] + temp[1]

    k = math.gcd(temp[0], temp[1])

    print('#{} {} {}'.format(tc+1, temp[0]//k, temp[1]//k))