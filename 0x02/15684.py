N,M,H = map(int,input().split())
ans = 4
def check():
    for i in range(N):
        temp = i
        for j in range(H):
            # 오른쪽이 1인경우
            if bridge[j][temp] == 1:
                temp += 1
            # 왼쪽인 1인경우
            elif temp-1 >= 0 and bridge[j][temp-1] == 1:
                temp -= 1
        if temp != i:
            return False
    return True

def dfs(depth,x,y):
    global ans
    if ans <= depth:
        return
    if check():
        ans = min(ans,depth)
        return
    if depth == 3:
        return
    
    for i in range(x,H):
        # 왼쪽 오른쪽 자기자신 확인해야하는 코드를 작성하고 완탐을 해야한다.
        for j in range(0,N-1):
            if bridge[i][j] == 1 or bridge[i][j+1] == 1 or (j-1 >=0 and bridge[i][j-1] == 1):
                continue
            bridge[i][j] = 1
            dfs(depth+1,i,j+1)
            bridge[i][j] = 0
    
    
# 사다리 그어줌
bridge = [[0]*N for _ in range(H)]
for _ in range(M):
    # 자기자신이면 오른쪽, 왼쪽은 좌표에 -1 만큼을 확인하면된다.
    a, b = map(int, input().split())
    bridge[a-1][b-1] = 1

dfs(0,0,0)

if ans > 3:
    print(-1)
else:
    print(ans)