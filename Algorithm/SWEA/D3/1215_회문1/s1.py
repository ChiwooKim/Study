import sys
sys.stdin = open('input.txt')

# 회문찾는 함수
def palindrome(words_list, length):
    count = 0
    for i in range(8):
        for j in range(8 - length + 1):
            word = words_list[i][j:j + length]
            if word == word[::-1]:
                count += 1
    return count

for _ in range(10):
    num = int(input()) # 회문길이
    row_list = [input() for _ in range(8)] # 평판
    col_list = list(map(''.join, zip(*row_list))) # 90도 회전 평판(열을 쉽게 찾기 위함)
    row_cnt = palindrome(row_list, num)
    col_cnt = palindrome(col_list, num)

    print('#{} {}'.format(_+1, row_cnt+col_cnt))