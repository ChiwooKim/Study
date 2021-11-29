import sys
sys.stdin = open('input.txt')

'''
I(삽입)x,y,s : 앞에서 부터 x의 위치 바로 다음에 y새의 숫자를 삽입한다. s는 덧붙일 숫자들
D(삭제)x,y : 앞에서부터 x의 위치 바로 다음부터 y개의 숫자를 삭제한다.
A(추가)y,s : 암호문의 맨 뒤에 y개의 숫자를 덧붙인다. s는 덧붙일 숫자들이다.
'''

for tc in range(10):
    N = int(input())
    password = list(input().split())
    command = int(input())
    temp_order = list(input().split())
    order = []
    temp = []

    # 명령어 분류
    for i in temp_order:
        if not i.isdigit():
            order.append(temp)
            temp = []
            temp.append(i)
        else:
            temp.append(i)
    order.remove([])
    order.append(temp)

    # 명령어 수행
    for i in order:
        if i[0] == 'I':
            password = password[:int(i[1])] + i[3:] + password[int(i[1]):]
        elif i[0] == 'D':
            password = password[:int(i[1])] + password[int(i[1])+int(i[2])+1:]
        else:
            password += i[3:]

    print('#{} {} {} {} {} {} {} {} {} {} {}'.format(tc+1, *password[:10]))