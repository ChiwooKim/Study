import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def postorder(s,e):
    if s > e:
        return
    root = input_list[s]
    x = s + 1
    while x <= e:
        if input_list[x] > root:
            break
        x += 1
    postorder(s+1, x-1)
    postorder(x, e)
    print(root)

input_list = []
# input 값을 몇 개 받는지 알수 없기 때문에 오류가 날 때 까지 받은 후 오류 발생 시 break
while True:
    try:
        input_list.append(int(input()))
    except:
        break

postorder(0, len(input_list)-1)

