from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(board,R,C,map):
    j_queue = deque()
    f_queue = deque()
    # queue 에 다들어감 위치들
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'J':
                j_queue.append((board[i][j],(i,j)))
                map[i][j] = 1
                if i == 0 or j == 0 or i == R-1 or j == C-1:
                    return 1
            elif board[i][j] == 'F':
                f_queue.append((board[i][j],(i,j)))
                map[i][j] = 'F'

    result = []
    while j_queue:
                # 그다음으로 불이 이동
        for _ in range(len(f_queue)):
            value,pos = f_queue.popleft()
            x,y = pos[0],pos[1]
            for i in range(4):
                rx = x + dx[i]
                ry = y + dy[i]
                if rx<0 or ry<0 or rx>R-1 or ry>C-1:
                    continue
                if map[rx][ry] == 0 and board[rx][ry] == '.':
                    map[rx][ry] = 'F'
                    f_queue.append((value,(rx,ry)))
        # 지훈이 먼저 이동
        for _ in range(len(j_queue)):
            value,pos = j_queue.popleft()
            x,y = pos[0],pos[1]
            for i in range(4):
                rx = x + dx[i]
                ry = y + dy[i]
                if rx<0 or ry<0 or rx>R-1 or ry>C-1:
                    continue
                if map[rx][ry] == 0 and board[rx][ry] == '.':
                    map[rx][ry] = map[x][y] + 1
                    j_queue.append((value,(rx,ry)))
                    if rx == 0 or ry == 0 or rx == R-1 or ry == C-1:
                        result.append(map[rx][ry])

    if result:
        return min(result)
    else:
        return 'IMPOSSIBLE'

# main문
if __name__ == '__main__':
    R,C = map(int,input().split(' '))
    board = [list(map(str,input())) for _ in range(R)]
    map = [[0]*C for _ in range(R)]

    print(solution(board,R,C,map))

