'''
처음에 노드 번호에 맞게 트리를 구성하려다가 미리 리스트를 생성해야했고,
항상 최대치를 만들어서 대입해서 트리를 완성해야 해서 메모리 초과가 발생!!!
트리를 dict형식으로 만드는 것 까지는 같고, 이후 트리를 구성한 후 찾아가는 것이 아닌
그냥 dict를 따라가면서 바로바로 print하면 되었다!!
'''
# 전위순회
def preorder(x):
    if x != '.':
        print(x, end='')
        preorder(tree[x][0])
        preorder(tree[x][1])

# 중위순회
def inorder(x):
    if x != '.':
        inorder(tree[x][0])
        print(x, end='')
        inorder(tree[x][1])

# 후위순회
def postorder(x):
    if x != '.':
        postorder(tree[x][0])
        postorder(tree[x][1])
        print(x, end='')

N = int(input())
tree = {}
for _ in range(N):
    v, l, r = input().strip().split()
    tree[v] = [l, r]
preorder('A')
print()
inorder('A')
print()
postorder('A')

# 메모리 초과
# from collections import deque
#
# def maketree(start):
#     q = deque()
#     q.append(start)
#     cnt = 0
#     visited = []
#     while q:
#         try:
#             t = q.popleft()
#             cnt += 1
#             if t == '.':
#                 tree[cnt] = t
#                 q.extend(['.', '.'])
#             else:
#                 visited.append(t)
#                 tree[cnt] = t
#                 q.extend(node_dict[t])
#             if len(visited) == N:
#                 break
#         except:
#             break
# # 전위순회
# def preorder(a):
#     try:
#         if tree[a] != '.' and tree[a] != 0 and a < 2**N:
#             print(tree[a], end='')
#             preorder(a*2)
#             preorder(a*2+1)
#     except:
#         pass
#
# # 중위순회
# def inorder(b):
#     try:
#         if tree[b] != '.' and tree[b] != 0 and b < 2 ** N:
#             inorder(b * 2)
#             print(tree[b], end='')
#             inorder(b * 2 + 1)
#     except:
#         pass
#
#
# # 후위순회
# def postorder(c):
#     try:
#         if tree[c] != '.' and tree[c] != 0 and c < 2 ** N:
#             postorder(c * 2)
#             postorder(c * 2 + 1)
#             print(tree[c], end='')
#     except:
#         pass
#
# N = int(input())
# node_list = []
# for _ in range(N):
#     node_list.append(input().split())
# tree = [0] * 2**N # 최대 번호
# node_dict = {}
# for i in node_list:
#     node_dict[i[0]] = i[1:3]
#
# maketree('A')
# preorder(1)
# print()
# inorder(1)
# print()
# postorder(1)




