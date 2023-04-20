from copy import deepcopy

# row 이어져있는 개수 col
N,M,H = map(int,input().split())
board = [[0]*N for _ in range(H)]
# 오른쪽 왼쪽 확인
dy = [1,-1]
dx = [0,0]

for _ in range(M):
    a,b = map(int,input().split())
    board[a-1][b-1],board[a-1][b] = 1,1

def check(map):
    row,col = len(map),len(map[0])
    for i in range(col):
        idx = i
        for j in range(row):
            if map[j][idx] == 1:
                if idx+1 < col and map[j][idx+1] == 1:
                    idx += 1
                elif idx-1 >= 0 and map[j][idx-1] == 1:
                    idx -= 1
        if idx == i:
            continue
        else:
            return False
    return True
                
result = -1

def solution(num,map,depth):
    global result
    if depth == num:
        if check(map):
            result = num
        return
    for i in range(H):
        for j in range(N):
            if map[i][j] == 0 and j+1 < N and map[i][j+1] != 1:
                map[i][j],map[i][j+1] = 1,1
                solution(num,map,depth+1)
                map[i][j],map[i][j+1] = 0,0
            elif map[i][j] == 0 and j-1 >= 0 and map[i][j-1] != 1:
                map[i][j],map[i][j-1] = 1,1
                solution(num,map,depth+1)
                map[i][j],map[i][j-1] = 0,0


for num in range(1,4):
    map = deepcopy(board)
    solution(num,map,0)

print(result)

'''
[1, 1, 0, 0, 0], 
[0, 0, 1, 1, 0], 
[0, 1, 1, 0, 0], 
[0, 0, 0, 0, 0], 
[1, 1, 0, 1, 1], 
[0, 0, 0, 0, 0]
'''