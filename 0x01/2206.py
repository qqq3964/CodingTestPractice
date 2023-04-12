from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def solution(board,N,M):
    start = (0,0,0)
    dst = (N-1,M-1,0)
    # index 0번은 벽파괴 안한거고 1번은 벽파괴했을경우
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append(start)
    visited[0][0][0] = 1
    while queue:
        x,y,break_wall = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][break_wall]
        for i in range(4):
            rx = dx[i]+x
            ry = dy[i]+y

            if rx<0 or ry<0 or rx>=N or ry>=M:
                continue
            # 다음 이동할곳이 벽이고 파괴기회 사용안했으면
            if board[rx][ry] == 1 and break_wall == 0:
                visited[rx][ry][1] = visited[x][y][0] + 1
                queue.append((rx,ry,1))
            # 다음 이동할곳이 벽이 아니면서 한번도 방문 안하면
            elif board[rx][ry] == 0 and visited[rx][ry][break_wall] == 0:
                visited[rx][ry][break_wall] = visited[x][y][break_wall] + 1
                queue.append((rx,ry,break_wall))
    return -1


if __name__ == '__main__':
    N,M = map(int,input().split())
    board = [list(map(int,input())) for _ in range(N)]
    print(solution(board,N,M))