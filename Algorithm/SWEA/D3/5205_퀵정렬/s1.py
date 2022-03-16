import sys
sys.stdin = open('input.txt')

def partition(arr, l, r):
    p = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quick_sort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quick_sort(arr, l, s-1)
        quick_sort(arr, s+1, r)


T = int(input())

ans = []
for tc in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, n-1)
    result = numbers[n//2]

    ans.append('#{} {}\n'.format(tc+1, result))
print(''.join(ans))