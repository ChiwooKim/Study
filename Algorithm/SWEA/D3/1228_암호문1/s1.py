import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())   # 원본 암호문의 길이
    password = list(input().split())   # 원본 암호문
    command = int(input())   # 명령어의 개수
    order = list(input().split())   # 명령어

    for i in range(len(order)):
        if order[i] == 'I':
            idx = int(order[i+1])
            password = password[:idx] + order[i+3:i+3+int(order[i+2])] + password[idx:]

    print('#{}'.format(tc+1), *password[:10])
