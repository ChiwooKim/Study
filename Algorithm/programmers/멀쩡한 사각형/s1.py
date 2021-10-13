import sys
sys.stdin = open('input.txt')
import math
'''
모서리 끝에서 끝으로 가는 최소 사각형을 확인해보면 
가로, 세로 길이가 최대공약수로 나눈 것이라는 것을 알 수 있다.
그 작은 사각형을 가로 세로 길이를 a, b 라고 한다면 대각선이 지나가는 사각형의 수는
a+b-1 개라는 규칙을 알 수 있다. 그래서 최종적으로 (a+b-1)*최대공약수
즉, w+h-최대공약수 만큼 제거하면 사용할 수 있는 사각형을 수를 구할 수 있다.   
'''

def solution(w,h):
    # 최대공약수 구하기
    num = math.gcd(w, h)

    # 사용할 수 있는 사각형
    answer = (w*h) - (w+h-num)

    return answer


for _ in range(1):
    w = int(input())
    h = int(input())
    print(solution(w,h))