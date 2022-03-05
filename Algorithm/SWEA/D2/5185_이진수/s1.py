import sys
sys.stdin = open('input.txt')

T = int(input())

ans = []
for tc in range(T):
    n, sixteen = input().split()

    sixteen_dict = {'0': '0000',
                    '1': '0001',
                    '2': '0010',
                    '3': '0011',
                    '4': '0100',
                    '5': '0101',
                    '6': '0110',
                    '7': '0111',
                    '8': '1000',
                    '9': '1001',
                    'A': '1010',
                    'B': '1011',
                    'C': '1100',
                    'D': '1101',
                    'E': '1110',
                    'F': '1111',
                    }

    result = ''

    for i in sixteen:
        result += sixteen_dict[i]

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))