import sys
sys.stdin = open('input.txt')

ans = []
for _ in range(10):
    num = int(input())
    numbers = input()

    stack = [int(numbers[0])]
    for i in range(1,num):
        try:
            if 0 < int(numbers[i]):
                if numbers[i-1] == '*':
                    stack.append(stack.pop() * int(numbers[i]))
                else:
                    stack.append(int(numbers[i]))
        except:
            pass

    ans.append('#{} {}\n'.format(_+1, sum(stack)))
print(''.join(ans))