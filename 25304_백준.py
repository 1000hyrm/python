sum = int(input())
n = int(input())
total = 0

for i in range(n) :
  p, num = map(int, input().split())
  total = total + (p * num)

if sum == total :
  print('Yes')
else :
  print('No')