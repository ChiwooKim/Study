import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    result = [0,0,0,0,0]
    num = int(input())
    num_list = [2,3,5,7,11]
    count = 0
    for j in num_list:
        while True:
            if num%j == 0:
                result[count] += 1
                num = num//j
            else:
                break
        count += 1


    print('#{}'.format(i + 1), end=' ')
    print(*result)



