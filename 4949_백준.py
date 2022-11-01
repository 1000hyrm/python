n = int(input())
que = [i+1 for i in range(n)]
card = []

while len(que) != 1 :
  card.append(que.pop(0))
  que.append(que.pop(0))

for i in card :
  print(i, end=' ')
print(que[0])