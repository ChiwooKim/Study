import sys
sys.stdin = open('input.txt')

def calendar(num):
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    #입력된 값에서 년도 확인은 불필요하기 때문에 월부터 확인
    if not num[4:6] in month:
        return -1

    #각 달마다 일수가 다르기 때문에 일수가 같은 월을 묶어서 확인
    if num[4:6] == '02':
        if not num[6:8] in day[:28]:
            return -1

    if num[4:6] in ['01', '03', '05', '07', '08', '10', '12']:
        if not  num[6:8] in day:
            return -1

    if num[4:6] in ['04', '06', '09', '11']:
        if not num[6:8] in day[:30]:
            return -1

    return num[:4]+'/'+num[4:6]+'/'+num[6:8]


T = int(input())

for _ in range(T):
    num = input()
    print('#{} {}'.format(_+1, calendar(num)))


