import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    price = int(input())
    cnt50000, price = divmod(price, 50000)
    cnt10000, price = divmod(price, 10000)
    cnt5000, price = divmod(price, 5000)
    cnt1000, price = divmod(price, 1000)
    cnt500, price = divmod(price, 500)
    cnt100, price = divmod(price, 100)
    cnt50, price = divmod(price, 50)
    cnt10 = price // 10

    print('#{}'.format(_+1))
    print('{} {} {} {} {} {} {} {}'.format(cnt50000, cnt10000, cnt5000, cnt1000, cnt500, cnt100, cnt50, cnt10))