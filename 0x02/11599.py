from collections import deque
from copy import deepcopy

N,M = 12,6
board = [list(map(str,input())) for _ in range(N)]

# 남 동 북 서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

combo = 0

# 중력 코드인데 아래로 당기는점을 제대로 구현못함
def gravity():
    global board
    for c in range(6):
        q = deque()
        for r in range(11, -1, -1):
            if board[r][c] != '.':
                q.append(board[r][c])

        # 다모아서 그냥 끌어내리고 끌어내리고 남은 공간 다 '.'으로 대체하면 되는거지
        for r in range(len(q)):
            board[11-r][c] = q[r]
        # 남은공간 다 '.'으로 대체한코드
        for r in range(12-len(q)):
            board[r][c] = '.'

# 일반적인 bfs코드이다.
def bfs():
    global combo
    queue = deque()
    visited = [[0]*M for _ in range(N)]
    temp_combo = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and board[i][j] in ['R','G','B','P','Y']:
                queue.append((board[i][j],i,j))
                value = 0
                temp = []
                while queue:
                    color,x,y = queue.popleft()
                    for k in range(4):
                        rx = dx[k]+x
                        ry = dy[k]+y
                        if rx<0 or ry<0 or rx>=N or ry>=M:
                            continue
                        if board[rx][ry] == color and visited[rx][ry] == 0:
                            visited[rx][ry] = 1
                            temp.append((rx,ry))
                            value += 1
                            queue.append((color,rx,ry))
                if value >=4 :            
                    temp_combo += 1
                    for temp_list in temp:
                        tp_x,tp_y = temp_list
                        board[tp_x][tp_y] = '.'
    if temp_combo >= 1:
        combo += 1
        gravity()
    
                    
s = 0
while True:
    pre_board = deepcopy(board)
    bfs()
    if pre_board == board:
        break
    s += 1

print(combo)

