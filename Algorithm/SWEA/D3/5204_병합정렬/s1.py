import sys
sys.stdin = open('input.txt')

def merge_sort(mini):
    global cnt
    if len(mini) == 1:
        return mini

    # 분할과정
    mid = len(mini) // 2
    left_list = merge_sort(mini[:mid])
    right_list = merge_sort(mini[mid:])

    # 병합과정
    merge_list = []
    left = right = 0
    while left < len(left_list) and right < len(right_list):
        if left_list[left] < right_list[right]:
            merge_list.append(left_list[left])
            left += 1
        else:
            merge_list.append(right_list[right])
            right += 1
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 카운트
    if left_list[-1] > right_list[-1]:
        cnt += 1
    merge_list += left_list[left:]
    merge_list += right_list[right:]
    return merge_list


T = int(input())

ans = []
for tc in range(T):
    n = int(input())
    numbers =list(map(int, input().split()))
    cnt = 0
    merge = merge_sort(numbers)
    ans.append('#{} {} {}\n'.format(tc+1, merge[n//2], cnt))
print(''.join(ans))