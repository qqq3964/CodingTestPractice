n = int(input())
for i in range(n):
    arr = input()
    stack = []
    for idx in range(len(arr)):
        if len(stack) == 0:
            stack.append(arr[idx])
        else:
            if stack[-1] == '(' and arr[idx] == ')':
                stack.pop()
            else:
                stack.append(arr[idx])
    if stack:
        print('NO')
    else:
        print('YES')
