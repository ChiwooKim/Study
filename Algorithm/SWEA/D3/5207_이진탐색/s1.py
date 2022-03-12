import sys
sys.stdin = open('input.txt')

def bi_search(arr, start, end):
    global check
    if i < arr[start] or i > arr[end]:
        return 0

    mid = (start+end) // 2
    if i == arr[mid]:
        return 1
    elif i < arr[mid]:
        if check == -1:
            return 0
        check = -1
        return bi_search(arr, start, mid-1)
    elif i > arr[mid]:
        if check == 1:
            return 0
        check = 1
        return bi_search(arr, mid+1, end)
    return 0

T = int(input())

ans = []
for tc in range(T):
    n, m = map(int, input().split())
    n_list = sorted(list(map(int, input().split())))
    m_list = list(map(int, input().split()))
    result = 0

    for i in m_list:
        check = 0
        if bi_search(n_list, 0, n-1):
            result += 1

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))