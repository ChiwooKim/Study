import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    sound = list(input()) + ['']
    H = int(input())
    place = list(map(int, input().split()))

    for i in place:
        sound[i] = '-' + sound[i]

    print('#{} {}'.format(tc+1, ''.join(sound)))