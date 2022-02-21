import sys
sys.stdin = open('input.txt')

def dfs (node_dict):
    visited_list = [] # 방문했던 곳들을 표시
    stack = [] # 스택 쌓는 곳
    stack.append(0) # 시작점을 첫 스택으로 줌

    # 스택이 있을 때 반복문
    while stack:
    # 스택에서 마지막을 꺼내서 노드로 하여 경로를 다음 경로를 찾음
        node = stack.pop()
    # 노드가 목표 노드(도착점)와 같다면 경로가 있다는 것이기 때문에 1출력
        if node == 99:
            return 1
    # 노드가 dict에 존재하는지 확인
    # 노드가 없다면 경로가 없다는 뜻이기 때문에 다음 스택에서 pop
        if node in node_dict:
    # 존재한다면 방문리스트 확인 후 없으면 방문 리스트에 노드 추가
    # 스택에는 노드가 갈수 있는 다음 지점을 dict에서 꺼내옴
            if node not in visited_list:
                visited_list.append(node)
                stack.extend(node_dict[node])
    # 목표 노드에 도달하지 못했기 때문에 0 출력
    return 0

ans = []
for _ in range(10):
    t, n = map(int, input().split())
    # 각 노드에서 갈라지는 곳 확인을 위해 딕셔너리 만들기
    node_dict = {}
    num = list(map(int, input().split()))
    for i in range(n*2):
        if i % 2 == 0:
            if not num[i] in node_dict:
                node_dict[num[i]] = [num[i+1]]
            else:
                node_dict[num[i]] += [num[i+1]]

    result = dfs(node_dict)

    ans.append('#{} {}\n'.format(t, result))
print(''.join(ans))
