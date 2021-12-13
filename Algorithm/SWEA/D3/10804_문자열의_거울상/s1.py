import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    words = input()[::-1]
    mirror = {
        'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'
    }

    result = ''
    for word in words:
        result += mirror[word]

    print('#{} {}'.format(tc+1, result))