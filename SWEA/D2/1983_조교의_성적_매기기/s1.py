import sys
sys.stdin = open('input.txt')

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for _ in range(T):
    n, k = map(int, input().split())
    result = []
    for i in range(n):
        m, f, h = map(int, input().split())
        result += [m * 0.35 + f * 0.45 + h * 0.2]
    k = result[k-1]
    result = sorted(result)

    if k in result[0:n//10]:
        kg = grade[9]
    elif k in result[n//10:n//10*2]:
        kg = grade[8]
    elif k in result[n//10*2:n//10*3]:
        kg = grade[7]
    elif k in result[n//10*3:n//10*4]:
        kg = grade[6]
    elif k in result[n//10*4:n//10*5]:
        kg = grade[5]
    elif k in result[n//10*5:n//10*6]:
        kg = grade[4]
    elif k in result[n//10*6:n//10*7]:
        kg = grade[3]
    elif k in result[n//10*7:n//10*8]:
        kg = grade[2]
    elif k in result[n//10*8:n//10*9]:
        kg = grade[1]
    else:
        kg = grade[0]
    print('#{} {}'.format(_+1, kg))



