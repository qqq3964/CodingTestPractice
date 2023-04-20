from collections import deque

# 입출력 휠 방향은 왼쪽이 반시계 오른쪽이 시계
# 2번과 6번이 맡다아있음
wheel = [[]]
wheel.extend([list(map(int,input())) for _ in range(4)])

# 회전횟수 1 시계 -1 반시계
K = int(input())

def rotation(num,direction):
    global wheel
    # 시계방향
    if direction == 1:
        temp = []
        for i in range(0,7):
            temp.append(wheel[num][i])
        wheel[num] = [wheel[num][7]] + temp
    else:
        temp = []
        for i in range(1,8):
            temp.append(wheel[num][i])
        wheel[num] = temp + [wheel[num][0]]


for _ in range(K):
    num,direction = map(int,input().split())
    check = [0 for _ in range(5)]
    check_list = []
    # num 번호에서 회전시킴
    check_list.append((num,direction))
    check[num] = 1

    while check_list:
        num,direction = check_list.pop()
        if num == 2 or num == 3:
            # 다른 극
            if wheel[num][2] != wheel[num+1][6] and check[num] == 1 and check[num+1] == 0:
                check[num+1] = 1
                check_list.append((num+1,-direction))
            if wheel[num][6] != wheel[num-1][2] and check[num] == 1 and check[num-1] == 0:
                check[num-1] = 1
                check_list.append((num-1,-direction))
        elif num == 1 or num == 4:
            if num == 1:
                if wheel[num][2] != wheel[num+1][6] and check[num] == 1 and check[num+1] == 0:
                    check[num+1] = 1
                    check_list.append((num+1,-direction))
            else:
                if wheel[num][6] != wheel[num-1][2] and check[num] == 1 and check[num-1] == 0:
                    check[num-1] = 1
                    check_list.append((num-1,-direction))
        if check[num] == 1:
            rotation(num,direction)


result = 0
a = [0,1,2,4,8]
for i in range(1,5):
    if wheel[i][0] == 1:
        result += a[i]
        
print(result)