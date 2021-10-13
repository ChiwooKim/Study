import sys
sys.stdin = open('input.txt')

test_case = int(input()) #test case

for k in range(test_case):
    num = int(input()) # 수의 개수
    num_list = list(map(int, input().split())) # num개의 양수
#버블소트 방식으로 입력받은 수의 리스트를 정렬
    for i in range(num-1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
#정렬한 리스트에서 양 끝의 값들이 최대 최소이기 때문에 그들의 차를 구함
    result = num_list[len(num_list)-1] - num_list[0]
    print('#{0} {1}'.format(k+1, result))





