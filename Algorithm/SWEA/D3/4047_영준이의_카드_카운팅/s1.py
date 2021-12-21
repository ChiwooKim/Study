import sys
sys.stdin = open('input.txt', 'r')

ans = []
for tc in range(int(input())):
    cards = input()

    # 카드분류
    temp = []
    for i in range(0, len(cards), 3):
        if cards[i:i+3] in temp:
            temp = []
            break
        else:
            temp.append(cards[i:i+3])

    if temp:
        S, D, H, C = 13, 13, 13, 13
        for i in temp:
            if i[0] == 'S':
                S -= 1
            elif i[0] == 'H':
                H -= 1
            elif i[0] == 'D':
                D -= 1
            else:
                C -= 1
        ans.append('#{} {} {} {} {}\n'.format(tc+1, S, D, H, C))
    else:
        ans.append('#{} ERROR\n'.format(tc+1))

print(''.join(ans))

