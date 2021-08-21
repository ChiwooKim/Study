import sys
sys.stdin = open('input.txt')

def pattern(words):
    length = 2
    while length <= 10:
        total = []
        result = words[0:length]
        for i in range(len(result),len(result)*2):
            if result[i-len(result)] == words[i]:
                total.append(words[i])
        if total == result:
            return len(total)
        length += 1

T = int(input())

for _ in range(T):
    words = list(input())
    a = pattern(words)
    print('#{} {}'.format(_+1, a))

