from copy import deepcopy

N,M,K = map(int,input().split())
board = [[0]*M for _ in range(N)]

# 90도 만큼 돌림
def rotation(temp):
    x,y = len(temp),len(temp[0])
    result = [[0]*x for _ in range(y)]
    for i in range(x):
        for j in range(y):
            result[j][x-i-1] = temp[i][j]
    return result

def attach(temp,i,j):
    global board
    # checking
    flag = 0
    for x in range(len(temp)):
        for y in range(len(temp[0])):
            if board[x+i][y+j] == 1 and temp[x][y] == 1:
                flag = 1
    if flag == 1:
        return False
    else:
        for x in range(len(temp)):
            for y in range(len(temp[0])):
                if board[x+i][y+j] == 0:
                    board[x+i][y+j] = temp[x][y]
    return True

def solution(temp):
    x,y = len(temp),len(temp[0])
    for i in range(N):
        for j in range(M):
            if x-1+i>=N or y-1+j>=M:
                continue
            if attach(temp,i,j):
                return True
    return False

for _ in range(K):
    R,C = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(R)]
    cnt = 0
    while cnt<4:
        if not solution(sticker):
            sticker = rotation(sticker)
        else:
            break
        cnt += 1

# 마지막으로 최종적으로 몇개의 1이있는지 세기
result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            result += 1

print(result)
