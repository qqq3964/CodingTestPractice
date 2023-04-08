from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def solution(M,N,board):
    queue = deque()
    visited = [[0]*N for _ in range(M)]
    result = []
    num = 0
    for i in range(M):
        for j in range(N):
            if board[i][j] == 0 and visited[i][j] == 0:
                queue.append((i,j))
                visited[i][j] = 1
                area = 1
                num += 1
                while queue:
                    x,y = queue.popleft()
                    for idx in range(4):
                        rx = dx[idx] + x
                        ry = dy[idx] + y
                        if rx<0 or ry<0 or rx>=M or ry>=N:
                            continue
                        if board[rx][ry] == 0 and visited[rx][ry] == 0:
                            queue.append((rx,ry))
                            visited[rx][ry] = 1
                            area += 1
                result.append(area)
    print(num)
    return sorted(result)

if __name__ == '__main__':
    # 행,열,개수
    M,N,K = map(int,input().split())
    # 열,행
    board = [[0]*N for _ in range(M)]
    for _ in range(K):
        '''
        이 부분이 핵심이다. 이번에 풀때 이 부분에서 시간을 많이썼다.
        아래 부분은 결국 지평좌표계로 값을 준것이기에 이를 행과 열로 바꿔주는 작업이 필요했다.
        이를 통해 블럭을 다채우고 이를 함수로보내 bfs돌리면 그대로 영역 붙이기 문제와 같아진다.
        '''
        y1,x1,y2,x2 = map(int,input().split())
        y1,x1,y2,x2 = y1,M-1-x1,y2-1,M-x2
        for x in range(x2,x1+1):
            for y in range(y1,y2+1):
                board[x][y] = 1
    for res in solution(M,N,board):
        print(res,end = ' ')                