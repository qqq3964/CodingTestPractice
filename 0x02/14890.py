
N,L = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]


def check(temp):
    global L,N
    idx = 0
    check = [0 for _ in range(N)]
    while idx < N:
        if idx+1 >= N:
            break
        # 이제 경사로를 둘 수 있는 조건 높은곳에서 낮은곳으로
        if (temp[idx] - temp[idx+1]) == 1:
            for slope_idx in range(L):
                if idx+1+slope_idx >= N:
                    return False
                if temp[idx+1+slope_idx] != temp[idx+1]:
                    return False
                if check[idx+1+slope_idx] == 1:
                    return False
                else:
                    check[idx+1+slope_idx] = 1
            idx = idx+L
        # 경사로가 낮은곳에서 높은곳
        elif (temp[idx] - temp[idx+1]) == -1:
            if idx-L+1 < 0:
                return False
            for slope_idx in range(idx,idx-L,-1):
                if temp[slope_idx] != temp[slope_idx-1] and slope_idx != idx-L+1:
                    return False
                if check[slope_idx] == 1:
                    return False
                else :
                    check[slope_idx] = 1
            idx += 1
        # 경사로가 없고 같다면
        elif temp[idx] == temp[idx+1]:
            idx += 1
        # 경사로를 두지 못함
        else:
            return False
    # 조건을 다통과하면
    return True

def rotation():
    global board
    N,M = len(board),len(board[1])
    result = [[0]*N for _ in range(M)]

    for i in range(N):
        for j in range(M):
            result[j][N-i-1] = board[i][j]
    return result

result = 0
# row 검사
for row in range(N):
    if check(board[row]):
        result += 1

board_rot = rotation()
for col in range(N):
    if check(board_rot[col]):
        result += 1

print(result)