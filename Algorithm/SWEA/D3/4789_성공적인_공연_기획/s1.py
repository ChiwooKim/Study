import sys
sys.stdin = open('input.txt')

ans = []
for tc in range(int(input())):
    people = list(map(int, input()))
    total = 0
    result = 0

    for i in range(1, len(people)+1):
        if i > total + people[i-1]:
            result += 1
            total = i
        else:
            total += people[i-1]


    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))
