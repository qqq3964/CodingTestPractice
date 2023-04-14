N,M = map(int,input().split())
INF = 1000000
board = [list(map(int,input().split())) for _ in range(N)]
chickens = []
home = []
answer = 100000
result = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chickens.append((i,j))
        if board[i][j] == 1:
            home.append((i,j))


def solution(idx,depth):
    global answer
    if depth == M:
        sum_distance = 0
        for p_home in home:
            x,y = p_home
            distance = INF
            for res in result:
                rx,ry = res[0],res[1]
                distance = min(distance,abs(rx-x) + abs(ry-y))
            sum_distance += distance
        answer = min(answer,sum_distance)
        return
    
    # 일단 치킨집 세개 고르기
    for i in range(idx,len(chickens)):
        # combination 을 구하는거기에 방문했던거는 체크해서 빼야해서 continue문을 만들어줬다.
        if chickens[i] in result:
            continue
        # 어떤 치킨집인지, 위치
        result.append(chickens[i])
        solution(i+1,depth+1)
        result.pop()
        

solution(0,0)
print(answer)

