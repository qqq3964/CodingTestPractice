N,M,K = map(int,input().split())
s2d2 = [list(map(int,input().split())) for _ in range(N)]
ground = [[5]*N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

for i in range(M):
    x,y,z = map(int,input().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    # spring and summer
    for i in range(N):
        for j in range(N):
            if trees[i][j] != []:
                trees[i][j].sort()
                
                for idx in range(len(trees[i][j])):
                    if trees[i][j][idx] <= ground[i][j]:
                        ground[i][j] -= trees[i][j][idx]
                        trees[i][j][idx] += 1
                    else:
                        die = trees[i][j][idx:]
                        for now in die: # 죽은 나무
                            ground[i][j] += now//2
                        trees[i][j] = trees[i][j][:idx]
                        break
    # autom
    for i in range(N):
        for j in range(N):
            for idx in range(len(trees[i][j])):
                if trees[i][j][idx]%5 == 0:
                    for k in range(8):
                        rx = i + dx[k]
                        ry = j + dy[k]
                        if rx<0 or ry<0 or rx>=N or ry>=N:
                            continue
                        trees[rx][ry].append(1)

    # winter
    for i in range(N):
        for j in range(N):
            ground[i][j] += s2d2[i][j]
ans=0
for i in range(N):
    for j in range(N):
        ans+=len(trees[i][j])
print(ans)
    
                            
                            
