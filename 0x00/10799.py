arr = input()
stack = []
raser = []
bar = []
for idx in range(len(arr)):
    if len(stack) == 0:
        stack.append((arr[idx],idx))
    else:
        stack_value,stack_idx = stack[-1]
        if stack_value == '(' and arr[idx] == ')':
            stack.pop()
            if idx-stack_idx == 1:
                raser.append((idx+stack_idx)/2)
            else:
                bar.append((stack_idx,idx))
        else:
            stack.append((arr[idx],idx))

result_sum = 0
for bar_value in bar:
    first,second = bar_value[0],bar_value[1]
    result = 1
    for raser_val in raser:
        if raser_val < second and raser_val > first:
            result+=1
    result_sum += result

print(result_sum)
