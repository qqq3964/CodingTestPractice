from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def solution(L,R,C,board):
    # S,E찾기
    S = 0
    E = 0
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]

    for k in range(L):
        temp_board = board[k]
        for i in range(R):
            for j in range(C):
                if temp_board[i][j] == 'S':
                    # 층수,위치
                    S = (k,i,j)
                elif temp_board[i][j] == 'E':
                    # 층수,위치
                    E = (k,i,j)
    
    queue = deque()
    queue.append(S)
    visited[S[0]][S[1]][S[2]] = 1
    while queue:
        height,x,y = queue.popleft()
        for idx in range(4):
            rx = dx[idx]+x
            ry = dy[idx]+y
            north_h = height+1
            south_h = height-1
            if rx<0 or ry<0 or rx>=R or ry>=C:
                continue

            if (board[height][rx][ry] == '.' or board[height][rx][ry] == 'E') and visited[height][rx][ry] == 0:
                queue.append((height,rx,ry))
                visited[height][rx][ry] = visited[height][x][y] + 1

            if north_h < L and (board[north_h][x][y] == '.' or board[north_h][x][y] == 'E') and visited[north_h][x][y] == 0:
                queue.append((north_h,x,y))
                visited[north_h][x][y] = visited[height][x][y] + 1

            if south_h >= 0 and (board[south_h][x][y] == '.' or board[south_h][x][y] == 'E') and visited[south_h][x][y] == 0:
                queue.append((south_h,x,y))
                visited[south_h][x][y] = visited[height][x][y] + 1
            
    result = visited[E[0]][E[1]][E[2]] - 1 
    if result == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")
    

    

if __name__ == '__main__':
    while True:
        L,R,C = map(int,input().split())
        if L == 0 and R == 0 and C == 0:
            break
        board = []
        for _ in range(L):
            board_temp = [list(map(str,input())) for _ in range(R)]
            not_input = input()
            board.append(board_temp)
        solution(L,R,C,board)
        
