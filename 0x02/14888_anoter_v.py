N = int(input())
digits = list(map(int,input().split()))
# + - * %
operator = list(map(int,input().split()))
operators = []
for idx,op in enumerate(operator):
    if idx == 0:
        operators += ['+']*op
    elif idx == 1:
        operators += ['-']*op
    elif idx == 2:
        operators += ['*']*op
    else:
        operators += ['%']*op

# 백트래킹이용
result = []
MAX = -1e9
MIN = 1e9
def backtracking(n):
    global MAX,MIN,result
    if len(result) == n:
        res = 0
        result = [(-1,-1)] + result
        for op,digit in zip(result,digits):

            if op[1] == -1:
                res = digit
                continue
            if op[1] == '+':
                res = res + digit
            elif op[1] == '-':
                res = res - digit
            elif op[1] == '*':
                res = res * digit
            else:
                res = int(res / digit)
                
        MAX = max(res,MAX)
        MIN = min(res,MIN)
        result = result[1:]
        return
    for i in range(len(operators)):
        res = (i,operators[i])
        if res in result:
            continue
        result.append(res)
        backtracking(n)
        result.pop()

backtracking(len(operators))

print(MAX)
print(MIN)