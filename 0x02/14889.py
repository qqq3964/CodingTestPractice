N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [0]*N
res = 1e9

def dfs(depth,idx):
    global res,N
    if depth == N//2:
        start_team = 0
        link_team = 0

        for i in range(N):
            for j in range(N):
                if visited[i] == 1 and visited[j] == 1:
                    start_team += board[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    link_team += board[i][j]
        res = min(abs(start_team-link_team),res)
        return
    
    for i in range(idx,N):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(depth+1,i+1)
        visited[i] = 0    
    

dfs(0,0)

print(res)