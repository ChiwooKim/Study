import sys
sys.stdin = open('input.txt')

# 후위 순회
def traversal(x):
    if x:
        traversal(child1[x])
        traversal(child2[x])

    if tree[x] in ['+', '-', '*', '/']:
        tree[x] = cal(tree[x], child1[x], child2[x])

# 사칙연산
def cal(x, a, b):
    if x == '+':
        return tree[a]+tree[b]
    elif x == '-':
        return tree[a]-tree[b]
    elif x == '*':
        return tree[a]*tree[b]
    elif x == '/':
        return tree[a]/tree[b]

ans = []
for tc in range(10):
    n = int(input())
    child1 = [0]*(n+1) # 좌측 자식 노드의 값을 저장
    child2 = [0]*(n+1) # 우측 자식 노드의 값을 저장
    tree = [0]*(n+1) # 트리 구성

    for i in range(n):
        input_list = input().split()
        if len(input_list) == 4:
            tree[int(input_list[0])] = input_list[1]
            child1[int(input_list[0])] = int(input_list[2])
            child2[int(input_list[0])] = int(input_list[3])
        else:
            tree[int(input_list[0])] = int(input_list[1])

    traversal(1)

    ans.append('#{} {}\n'.format(tc+1, int(tree[1])))
print(''.join(ans))
