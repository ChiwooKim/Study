import sys
sys.stdin = open('input.txt')

'''
어렵진 않았는데 너무 복잡하게 생각한 것 같다.
첫 번째 시도에서 실패한 경우는 너무 for문에 집착했던 것 같다. 2중 for문 안에서 모든 것들을 i와 j의 좌표로 관계를 만들어
해결하는데 집착한 나머지 제대로 된 답도 나오지 않았고 시간만 낭비했다.
두 번째 시도에서는 어차피 5개 이상만 확인하면 되기 때문에 조건 코드가 길어지더라도 +1, +2 이런식으로 해결하는게 이해도 쉬웠고 좋았다.
하지만 가로확인 할 때 count 메서드를 이용하는 바람에 왜 틀린지도 모르고 있었다... 카운트는 연속적인게 아닌 그냥 세기만 하는건데.......
이런 실수를 하지 않도록 하자.
그리고 내가 omok 배열을 이중리스트가 아닌 리스트안에 문자열로 받아왔다면 'ooooo' 가 포함된 것만 체크하는 것을 된다는 것을 다른 사람코드를 보고 알게되었다.
이러한 문제가 나오면 무조건 imput 받을 때 2중 리스트로 받고본다... 앞으로는 생각을 좀 더 하여 무조건 이중리스트가 아닌 한줄을 문자열로 하여 단일 리스트로 받도록 해보자.
'''

def omok_check(omok, n):
    global result

    for i in range(n):
        for j in range(n):
            # 가로, 세로, 좌상우하, 좌하우상 방향으로 'o'rk 5개 있는지 체크
            if omok[i][j] == 'o':
                if j+4 < n and omok[i][j+1] == 'o' and omok[i][j+2] == 'o' and omok[i][j+3] == 'o' and omok[i][j+4] == 'o':
                    result = 'YES'
                    break
                if i+4 < n and omok[i+1][j] == 'o' and omok[i+2][j] == 'o' and omok[i+3][j] == 'o' and omok[i+4][j] == 'o':
                    result = 'YES'
                    break
                if i+4 < n and j+4 < n and omok[i+1][j+1] == 'o' and omok[i+2][j+2] == 'o' and omok[i+3][j+3] == 'o' and omok[i+4][j+4] == 'o':
                    result = 'YES'
                    break
                if 0 <= i-4 < n and j+4 < n and omok[i-1][j+1] == 'o' and omok[i-2][j+2] == 'o' and omok[i-3][j+3] == 'o' and omok[i-4][j+4] == 'o':
                    result = 'YES'
                    break

        if result == 'YES':
            break


ans = []
for tc in range(int(input())):
    n = int(input())
    omok = [list(input()) for _ in range(n)]
    result = 'NO'
    omok_check(omok, n)
    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))

