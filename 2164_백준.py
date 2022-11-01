from collections import deque

n = int(input())
que = [i+1 for i in range(n)]

dq = deque(que)

while len(dq) != 1 :
  dq.popleft()
  dq.append(dq.popleft())

print(dq.pop())