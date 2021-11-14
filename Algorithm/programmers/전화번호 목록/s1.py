import sys
sys.stdin = open('input.txt')

'''
for문을 통해 순서대로 확인
1.
길이순으로 정렬한다.
정렬하는 이유는 체크하는 숫자보다 접두어가 길면 당연히 포함이 불가능하며,
또한 for문을 통해 차례대로 체크 할 경우 길이가 짧은 것이 앞에 있다면 
굳이 길이 체크를 할 필요없이 접두어 자신 이후의 요소들만 확인하면 되기 때문이다.
2중 for문 => 효율성 3,4 fail

2.
for문을 한줄로 사용하기 위해선난 현재의 나 자신이 다음에 오늘 수에 포함 되는지 확인을 한다.
이렇게 하기 위해서 sort를 할때 첫번쨰 때 시도했던 방법과 달리 그냥 정렬을 하면 자연스럽게 숫자 순으로 정렬이 되며,
길이가 긴거이 뒤로가게 된다.
이 경우 바로 다음 것만 비교해주는 이유는 예를 들어 12 123 1235로 정렬되었다면 12가 만약 다음수에 접두어가 아니라면
정렬이 되었을때 앞에 숫자에 따라 오름차순으로 정렬하기 때문에 그 이후의 수에도 당연히 접두어가 불가능 하기 때문이다.
그래서 starswith라는 메서드를 이용하면 find와 달리 자연스럽게 앞에서 부터 찾으려는 문자를 찾는다.
'''

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return answer


T = int(input())
for tc in range(T):
    st = input().split()
    print(solution(st))