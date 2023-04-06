def solution(arr):
    stack = []
    check = []
    for idx,val in enumerate(arr):
        if len(stack) == 0:
            stack.append((val,idx))
        else:
            pre_val,pre_idx = stack[-1]
            if pre_val == '(' and val == ')':
                if check:
                    temp = []
                    rm_temp = []
                    for i in check:
                        check_val,check_idx = i[0],i[1]
                        if check_idx < idx and check_idx > pre_idx:
                            temp.append(check_val)
                            rm_temp.append(i)
                    for i in rm_temp:
                        check.remove(i)
                    sum_result = sum(temp)*2

                    if sum_result != 0:
                        check.append((sum_result,idx))
                    else:
                        check.append((2,idx))
                else:
                    check.append((2,idx))
                stack.pop()
            elif pre_val == '[' and val == ']':
                if check:
                    temp = []
                    rm_temp = []
                    for i in check:
                        check_val,check_idx = i[0],i[1]
                        if check_idx < idx and check_idx > pre_idx:
                            temp.append(check_val)
                            rm_temp.append(i)
                    for i in rm_temp:
                        check.remove(i)
                    sum_result = sum(temp)*3
                    if sum_result != 0:
                        check.append((sum_result,idx))
                    else:
                        check.append((3,idx))
                else:
                    check.append((3,idx))
                stack.pop()
            else:
                stack.append((val,idx))
    result = 0
    for i in check:
        result+=i[0]
    if stack:
        print(0)
    else:
        print(result)
if __name__ == '__main__':
    arr = input()
    solution(arr)
