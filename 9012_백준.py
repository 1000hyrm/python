num = int(input())
stack = []
for i in range(num) :
    stack.append(input())

print(stack)

for p in stack :
    if p == "(" :
        stack.push(p)
    elif p == ")" :
        if stack.top() == "(" :
            stack.pop()
        else :
            exit(0)

    if(len(stack) == 0) :
        print("True")
    else :
        print("False")
