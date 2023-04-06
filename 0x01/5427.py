from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(board,w,h):
    visited = [[0]*w for _ in range(h)]

    s_queue = deque()
    f_queue = deque()

    # check 불의 위치와 사람의 위치
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                s_queue.append((i,j))
                if i == 0 or j == 0 or i == h-1 or j == w-1:
                    return 1
                visited[i][j] = 1
            elif board[i][j] == '*':
                f_queue.append((i,j))
                visited[i][j] = 'F'

    result = []

    while s_queue:
        # 불이 먼저 붙는다. queue 를 두개로 해줘야 돌면서 움직일수있음
        for _ in range(len(f_queue)):
            pos = f_queue.popleft()
            x,y = pos[0],pos[1]
            for i in range(4):
                rx = x + dx[i]
                ry = y + dy[i]
                if rx<0 or ry<0 or rx>h-1 or ry>w-1:
                    continue
                if board[rx][ry] == '.' and visited[rx][ry] == 0:
                    visited[rx][ry] = 'F'
                    f_queue.append((rx,ry))
        
        for _ in range(len(s_queue)):
            pos = s_queue.popleft()
            x,y = pos[0],pos[1]
            for i in range(4):
                rx = x + dx[i]
                ry = y + dy[i]
                if rx<0 or ry<0 or rx>h-1 or ry>w-1:
                    continue
                if board[rx][ry] == '.' and visited[rx][ry] == 0:
                    visited[rx][ry] = visited[x][y] + 1
                    s_queue.append((rx,ry))
                    # 가장자리에 닿았을 때 조건식
                    if rx == 0 or ry == 0 or rx == h-1 or ry == w-1:
                        result.append(visited[rx][ry])

    if result:
        return min(result)
    else:
        return 'IMPOSSIBLE'

 

if __name__ == '__main__':
    for _ in range(int(input())):
        w,h = map(int,input().split())
        board = [list(map(str,input())) for _ in range(h)]
        print(solution(board,w,h))
