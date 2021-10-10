'''
왼 - 중 - 오(중위순회)
'''
def inorder(x):
    global idx
    if x < 2**k:
        inorder(x*2)
        tree[x] = num[idx]
        idx += 1
        inorder(x*2+1)

k = int(input())
num = [0]+list(map(int, input().split()))
idx = 1
tree = [0] * (2**k)
inorder(1)
cnt = 1

# 트리 구성 후 제출양식에 따라 print하기
while True:
    if cnt > k:
        break
    for i in range(2**(cnt-1), 2 ** cnt):
        try:
            print(tree[i], end = ' ')
        except:
            break
    print()
    cnt += 1


