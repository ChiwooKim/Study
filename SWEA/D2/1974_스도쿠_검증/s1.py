import sys
sys.stdin = open('input.txt')

def check(sudoku):
    for i in range(9):
        row_check = [0] * 10
        col_check = [0] * 10
        for j in range(9):
            if row_check[sudoku[i][j]]:
                return 0
            if col_check[sudoku[j][i]]:
                return 0
            row_check[sudoku[i][j]] = 1
            col_check[sudoku[j][i]] = 1

            if i % 3 == 0 and j % 3 == 0:
                by_check = [0] * 10
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if by_check[sudoku[k][l]]:
                            return 0
                        by_check[sudoku[k][l]] = 1
    return 1

T = int(input())

for _ in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(_+1, check(sudoku)))




