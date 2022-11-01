import sys

n  = int(sys.stdin.readline())
stack = []

for i in range(n) :
  s = sys.stdin.readline().split()
  for j in s :
    if j == "push" :
      stack.append(int(s[1]))
      #print(stack)
    elif j == "pop" :
      if len(stack) == 0 :
        print(-1)
      else :
        print(stack[-1])
        del stack[-1]
    elif j == "size" :
      print(len(stack))
    elif j == "empty" :
      if len(stack) == 0 :
        print(1)
      else :
        print(0)
    elif j == "top" :
      if len(stack) == 0 :
        print(-1)
      else :
        print(stack[-1])