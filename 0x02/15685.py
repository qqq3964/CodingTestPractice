

N = int(input())
board = [[0]*101 for _ in range(101)]
# 동,북,서,남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 오른쪽,오른쪽 대각아래,아래
c_dx = [0,1,1]
c_dy = [1,1,0]

def check():
    answer = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
                answer += 1
    print(answer)
for _ in range(N):
    y,x,d,g = map(int,input().split())
    stack = [d]
    for _ in range(g):
        now_gen = [(i+1)%4 for i in reversed(stack)]
        stack = stack + now_gen

    board[x][y] = 1
    for idx in stack:
        x = dx[idx] + x
        y = dy[idx] + y
        board[x][y] = 1
check()
