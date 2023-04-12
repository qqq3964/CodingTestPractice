from copy import deepcopy

cctv = [1,2,3,4,5]

# mode를 정해줘서 back tracking 해주는게 핵심이다. 여기서 모드별로 방향을 dx,dy로 지정해서 확인가능
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

# 남 동 북 서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

# cctv 위치 찾기
cctv_pos = []
for i in range(N):
    for j in range(M):
        if board[i][j] in cctv:
            cctv_pos.append((board[i][j],i,j))

# fill함수를 이용하는데 특이한점은 while문을 이용해 적절히 break를 걸어줌 이제 채우는 문제는 이런식으로 풀어야겠다는걸 알겠음
def fill(board,mode,x,y):
    for mod in mode:
        rx = x
        ry = y
        while True:
            rx += dx[mod]
            ry += dy[mod]

            if rx<0 or ry<0 or rx>=N or ry>=M:
                break
            if board[rx][ry] == 6:
                break
            elif board[rx][ry] == 0:
                board[rx][ry] = '#'

result = []
def backtracking(board,depth):
    if depth == len(cctv_pos) :
        check = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    check += 1
        result.append(check)
        return check
    
    cctv_num,x,y = cctv_pos[depth]
    # 이제 여기다가 채워야함
    temp = deepcopy(board)
    for i in mode[cctv_num]:
        '''
        backtracking시 이부분이 특이함 temp값을 넘겨줬는데 알아서 temp값이 갱신이됨
        여기서 헷갈리면 안되는게 함수는 c언어처럼 reference 리스트에 주소값만 날림 
        그래서 안에 값이 다 바뀌게 됨 외부 함수에서 적용해도 결국 리스트의 주소값을 날린다가 핵심이다.
        '''
        fill(temp,i,x,y)
        backtracking(temp,depth+1)
        temp = deepcopy(board)

         
backtracking(board,0)
print(min(result))