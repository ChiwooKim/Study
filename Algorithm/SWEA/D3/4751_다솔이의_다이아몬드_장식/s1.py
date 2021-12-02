import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    words = input()
    n = len(words)
    line1 = '..#.' * n + '.'
    line2 = '.#.#' * n + '.'
    line3 = ''
    for word in words:
        line3 += ('#.' + word + '.')
    line3 += '#'

    print(line1)
    print(line2)
    print(line3)
    print(line2)
    print(line1)

