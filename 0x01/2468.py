from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def solution(N,board):
    # 최대값 찾기
    temp = []
    for i in board:
        temp.append(max(i))
    MAX = max(temp)
    
    queue = deque()
    result = -1
    for max_height in range(MAX+1):
        visited = [[0]*N for _ in range(N)]
        area_num = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] > max_height and visited[i][j] == 0:
                    queue.append((i,j))
                    visited[i][j] = 1
                    while queue:
                        # 행,열
                        x,y = queue.popleft()
                        for idx in range(4):
                            rx = dx[idx]+x
                            ry = dy[idx]+y
                            if rx<0 or ry<0 or rx>=N or ry>=N:
                                continue
                            if board[rx][ry] > max_height and visited[rx][ry] == 0:
                                queue.append((rx,ry))
                                visited[rx][ry] = 1
                    area_num += 1
        result = max(result,area_num)
    
    return result

if __name__ == '__main__':
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    print(solution(N,board))