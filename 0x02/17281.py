from itertools import permutations
from copy import deepcopy
N = int(input())

MAX = 0

def soultion(result):
    global MAX
    idx = 0
    score = 0
    for i in range(N):
        out = 0
        b1,b2,b3 = 0,0,0
        while out != 3:
            runner = result[idx%9]
            mod = game[i][runner]
            if mod == 0:
                out += 1
            # shift 해줘야함
            elif mod == 1:
                score += b3
                b1,b2,b3 = 1,b1,b2
            elif mod == 2:
                score += b2+b3
                b1,b2,b3 = 0,1,b1
            elif mod == 3:
                score += b1+b2+b3
                b1,b2,b3 = 0,0,1
            else:
                score += b1+b2+b3+1
                b1,b2,b3 = 0,0,0
                
            idx += 1
    return score


game = [list(map(int,input().split())) for _ in range(N)]

# 1~9번 순서 정해야함
for i in set(permutations(range(1,9),8)):
    a = list(i)[:3] + [0] + list(i)[3:]
    MAX = max(MAX,soultion(a))
print(MAX)
