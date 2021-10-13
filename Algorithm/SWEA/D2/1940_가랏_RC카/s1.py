import  sys
sys.stdin = open('input.txt')

T = int(input())
# 일반적인 물리법칙을 기반으로 한게 아님
# 그냥 제자리에서 가속을 완료한 다음에 움직인다고 생각
for _ in range(T):
    num = int(input())
    distance = 0
    velocity = 0

    for i in range(num):
        command_list = list(input())
        if command_list[0] == '0':
            distance += velocity

        elif command_list[0] == '1':
            velocity += int(command_list[2])
            distance += velocity

        # 감속할 때 감속할 속도보다 현재 속도가 작으면 속도는 0
        elif command_list[0] == '2':
            if velocity < int(command_list[2]):
                velocity =0
            else:
                velocity -= int(command_list[2])
                distance += velocity
    print('#{} {}'.format(_+1, distance))


