N,M,x,y,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
move = list(map(int,input().split()))

# 바닥 서 위 동
right_left = [0,0,0,0]
# 바닥 뒤 위 앞
front_back = [0,0,0,0]

def rotation(direction,now_x,now_y):
    global front_back,right_left,board
    # 남쪽,오른쪽으로
    if direction == 4:
        front_back = [front_back[-1]]+front_back[:-1]
        right_left[0],right_left[2] = front_back[0],front_back[2]
    # 북쪽,왼쪽으로
    elif direction == 3:
        front_back = front_back[1:]+[front_back[0]]
        right_left[0],right_left[2] = front_back[0],front_back[2]
    # 동쪽,오른쪽으로
    elif direction == 1:
        right_left = [right_left[-1]]+right_left[:-1]
        front_back[0],front_back[2] = right_left[0],right_left[2]
    # 서쪽,왼쪽으로
    else:
        right_left = right_left[1:]+[right_left[0]]
        front_back[0],front_back[2] = right_left[0],right_left[2]  
    if board[now_x][now_y] == 0:
        board[now_x][now_y] = front_back[0]
    else:
        front_back[0],right_left[0] = board[now_x][now_y],board[now_x][now_y]
        board[now_x][now_y] = 0

now_x,now_y = x,y
# 동 서 남 북 으로 움직임
for direction in move:
    # 동쪽이면
    if direction == 1 and now_y+1 < M:
        now_y += 1
        rotation(direction,now_x,now_y)
        print(front_back[2])
    # 서쪽
    elif direction == 2 and now_y-1 >= 0:
        now_y -= 1
        rotation(direction,now_x,now_y)
        print(front_back[2])
    # 북쪽
    elif direction == 3 and now_x-1 >= 0:
        now_x -= 1
        rotation(direction,now_x,now_y)
        print(front_back[2])
    # 남쪽
    elif direction == 4 and now_x+1 < N:
        now_x += 1
        rotation(direction,now_x,now_y)
        print(front_back[2])
