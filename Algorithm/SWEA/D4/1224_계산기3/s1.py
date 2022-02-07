import sys
sys.stdin = open('input.txt')

for _ in range(10):
    n = int(input())
    data = input()
    stack = []
    numbers = []

    icp = {'*': 2, '+': 1, '(': 3}
    isp = {'*': 2, '+': 1, '(': 0}

    # 중위표기법을 후위 표기법으로 변경
    for str in data:
        # 피연산자인 경우 숫자를 리스트 넣기
        if str.isdigit():
            numbers.append(str)
        # 연산자인 경우
        else:
            # stack이 빈 경우
            if not stack:
                stack.append(str)
                continue

            # stack이 비지 않은 경우
            elif stack:
                # 여는 괄호가 나올 때까지 연산자들의 pop을 수행
                if str == ')':
                    while stack[-1] != '(':
                        numbers.append(stack.pop())
                    stack.pop()

                # 연산자 우선순위 비교
                elif icp[str] > isp[stack[-1]]:
                    stack.append(str)

                else:
                    # icp가 isp 보다 작으면 스택에 있는 연산자를 피연산자 리스트에 추가 후 연산자는 스택에 쌓기
                    while icp[str] <= isp[stack[-1]]:
                        numbers.append(stack.pop())
                    stack.append(str)

    # 연산
    for i in numbers:
        if i.isdigit():
            stack.append(i)
        elif i == '*':
            st2 = stack.pop()
            st1 = stack.pop()
            stack.append(int(st1) * int(st2))
        elif i == '+':
            st2 = stack.pop()
            st1 = stack.pop()
            stack.append(int(st1) + int(st2))
        else:
            stack.append(str)
    print('#{} {}'.format(_+1, *stack))
