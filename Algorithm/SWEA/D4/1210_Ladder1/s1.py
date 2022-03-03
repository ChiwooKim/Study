import sys
sys.stdin = open('input.txt')

ans = []
for _ in range(10):
    num = int(input())
    ladder_list = []
    # 사다리 생성
    for _ in range(100):
        ladder_list.append(list(map(int, input().split())))
    result = 0
    # 사다리 시작점 찾기
    for i in range(100):
        # 좌표 할당값이 0이면 pass 1이면 사다리 start!
        if ladder_list[0][i] == 0:
            continue
        else:
            p = [0, i]  # (y,x)
            start_p = [0, i]

            #가장 아래로 내려왔을때 2가 아니면 while문 종료 후 새 출발
            #마지막이 좌표의 수가 2로 할당 되어있다면 break
            while p[0] < 100:
                #마지막에 2를 찾지 못했기 때문에 새 출발하기위해 반복문 break
                if p[0] == 99:
                    break
                #오른쪽으로 이동
                if p[1] != 99 and ladder_list[p[0]][p[1]+1]:
                    p = [p[0], p[1]+1]
                    while p[1] != 99 and ladder_list[p[0]][p[1]+1]:
                        p = [p[0],p[1]+1]

                #왼쪽으로 이동
                elif p[1] != 0 and ladder_list[p[0]][p[1]-1]:
                    p = [p[0], p[1] - 1]
                    while p[1] != 0 and ladder_list[p[0]][p[1]-1]:
                        p = [p[0],p[1]-1]

                #아래로 이동
                if ladder_list[p[0]+1][p[1]]:
                    p = [p[0] + 1, p[1]]
                    if ladder_list[p[0]][p[1]] == 2:
                        result = start_p[1]
                        break
    ans.append('#{} {}\n'.format(num, result))
print(''.join(ans))