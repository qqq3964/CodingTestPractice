from collections import deque
from copy import deepcopy
N,L,R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]
day = 0

while True:
    cnt = 1
    visited = [[0]*N for _ in range(N)]
    temp = deepcopy(board)
    temp_list = [(-1,-1)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                queue = deque()
                queue.append((i,j))
                visited[i][j] = cnt
                value = board[i][j]
                count = 1
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        rx = x + dx[k]
                        ry = y + dy[k]
                        if rx < 0 or ry < 0 or rx >= N or ry >= N:
                            continue
                        if visited[rx][ry] == 0 and L <= abs(board[x][y] - board[rx][ry]) <= R:
                            visited[rx][ry] = cnt
                            queue.append((rx,ry))
                            value += board[rx][ry]
                            count += 1
                if count > 1:
                    value = int(value/count)
                    temp_list.append((value,cnt))
                cnt += 1

    for value,idx in temp_list:
        for i in range(N):
            for j in range(N):
                if visited[i][j] == idx:
                    board[i][j] = value
                    
    if temp == board:
        break
    else:
        day += 1
print(day)