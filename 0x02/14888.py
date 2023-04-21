N = int(input())
digits = list(map(int,input().split()))
# + - * %
add,sub,mul,div = map(int,input().split())

# 최대 최소
MAX = -1e9
MIN = 1e9

# dfs 정의

def dfs(i,arr):
    global add,sub,mul,div,MAX,MIN

    if i==N:
        MAX = max(MAX,arr)
        MIN = min(MIN,arr)
        return
    
    if add > 0:
        add -= 1
        dfs(i+1,arr + digits[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i+1,arr - digits[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i+1,arr * digits[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i+1,int(arr / digits[i]))
        div += 1

dfs