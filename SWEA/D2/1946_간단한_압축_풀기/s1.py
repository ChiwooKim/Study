import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    n = int(input())
    result = ''
    for i in range(n):
        word, num = input().split()
        result += word * int(num)

    print('#{}'.format(_+1))
    while True:
        cut = result[:10]
        result = result[10:]
        print(cut)
        if len(result) == 0:
            break







